import shutil
import csv
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  CSV file paths
# ─────────────────────────────────────────────
PRICES_CSV   = "product_prices.csv"
ORDERS_CSV   = "order_history.csv"
BILL_CSV     = "final_bill.csv"

# ─────────────────────────────────────────────
#  Utility helpers
# ─────────────────────────────────────────────

def get_terminal_width():
    return shutil.get_terminal_size().columns

def print_centered(text):
    w = get_terminal_width()
    print(text.center(w))

def print_divider(char="=", width=60):
    print(char * width)

def yn(prompt):
    """Ask a yes/no question; return True for yes."""
    while True:
        ans = input(prompt + " (yes/no): ").strip().lower()
        if ans in ("yes", "y"):
            return True
        if ans in ("no", "n"):
            return False
        print("  Please enter yes or no.")

# ─────────────────────────────────────────────
#  CSV: prices
# ─────────────────────────────────────────────

DEFAULT_PRICES = {
    "phone": 15000,
    "laptop": 50000,
    "desktop": 40000,
    "printer": 5000,
    "wearable": 8000,
    "tv": 10000,
    "audio_device": 7000,
    "gaming_console": 15000,
}

def ensure_prices_csv():
    """Create prices CSV if it doesn't exist."""
    if not os.path.exists(PRICES_CSV):
        with open(PRICES_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["product", "base_price"])
            for product, price in DEFAULT_PRICES.items():
                writer.writerow([product, price])
        print(f"  [INFO] Created '{PRICES_CSV}' with default prices.")

def load_prices():
    """Load base prices from CSV into a dict."""
    ensure_prices_csv()
    prices = {}
    with open(PRICES_CSV, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prices[row["product"]] = int(row["base_price"])
    return prices

# ─────────────────────────────────────────────
#  CSV: order history
# ─────────────────────────────────────────────

def save_order_to_csv(order_data: dict):
    """Append a single order dict to order_history.csv."""
    file_exists = os.path.exists(ORDERS_CSV)
    with open(ORDERS_CSV, "a", newline="") as f:
        fieldnames = ["timestamp", "session_id", "order_no", "category",
                      "specifications", "total_cost"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(order_data)

def save_bill_to_csv(order_summary: dict, amount_stored: list):
    """Export the final bill to final_bill.csv."""
    with open(BILL_CSV, "w", newline="") as f:
        fieldnames = ["s_no", "category", "specification", "value", "total_cost"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for idx, (key, item) in enumerate(order_summary.items(), start=1):
            first = True
            for spec_key, spec_val in item.items():
                if spec_key == "category":
                    continue
                writer.writerow({
                    "s_no": idx if first else "",
                    "category": item["category"] if first else "",
                    "specification": spec_key,
                    "value": spec_val,
                    "total_cost": item["Total Cost (Rs)"] if spec_key == "Total Cost (Rs)" else "",
                })
                first = False
        writer.writerow({})
        writer.writerow({
            "s_no": "", "category": "", "specification": "",
            "value": "GRAND TOTAL (Rs)",
            "total_cost": sum(amount_stored),
        })
    print(f"  [INFO] Final bill saved to '{BILL_CSV}'.")

# ─────────────────────────────────────────────
#  Accessories helper
# ─────────────────────────────────────────────

def select_accessories(accessory_map: dict):
    """
    accessory_map = { "accessory name": price, ... }
    Returns (selected_label, extra_cost).
    """
    print_divider()
    print("Available accessories:")
    for name, price in accessory_map.items():
        print(f"  {name:<30}  Rs. {price}")
    print_divider()

    keys_lower = {k.lower(): (k, v) for k, v in accessory_map.items()}
    choice = input("Enter accessories (or 'all'): ").strip().lower()

    selected = []
    extra_cost = 0

    if "all" in choice or "everything" in choice:
        selected = list(accessory_map.keys())
        extra_cost = sum(accessory_map.values())
    else:
        for keyword, (name, price) in keys_lower.items():
            if keyword in choice:
                selected.append(name)
                extra_cost += price

    if selected:
        label = ", ".join(selected)
        print(f"  Added: {label}  (+Rs. {extra_cost})")
    else:
        label = "None"
        print("  No matching accessories found.")

    return label, extra_cost

# ─────────────────────────────────────────────
#  Order confirmation helper
# ─────────────────────────────────────────────

def confirm_and_add(specs: dict, cost: int,
                    order_summary: dict, amount_stored: list,
                    session_id: str) -> bool:
    """
    Show specs, ask for confirmation, add to cart.
    Returns True if user wants to add another item.
    """
    print_divider("-")
    print(f"  Order specifications:")
    for k, v in specs.items():
        print(f"    {k:<28}: {v}")
    print(f"    {'Total Cost (Rs)':<28}: {cost}")
    print_divider("-")

    if yn("Confirm and add to cart?"):
        order_no = len(order_summary) + 1
        order_summary[order_no] = {**specs, "Total Cost (Rs)": cost}
        amount_stored.append(cost)
        print(f"  ✔ Order #{order_no} added to cart!")

        # persist to history CSV immediately
        save_order_to_csv({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "session_id": session_id,
            "order_no": order_no,
            "category": specs.get("category", ""),
            "specifications": str({k: v for k, v in specs.items() if k != "category"}),
            "total_cost": cost,
        })
    else:
        print("  Order cancelled.")

    return yn("Add another item to cart?")

# ─────────────────────────────────────────────
#  Product order functions
# ─────────────────────────────────────────────

def order_phone(prices, order_summary, amount_stored, session_id):
    print_centered("── Phones & Accessories ──")
    cost = prices["phone"]

    ram      = input("RAM (4GB / 6GB / 8GB / 12GB): ")
    storage  = input("Storage (64GB / 128GB / 256GB / 512GB): ")
    display  = input("Display (LCD / AMOLED): ")
    color    = input("Color (Black / White / Blue / Red): ")
    sim      = input("SIM type (Single SIM / Dual SIM): ")
    print(f"  Base phone cost: Rs. {cost}")

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Charger": 500, "Earphones": 1000,
            "Case": 700,    "Screen Protector": 300,
        })
        cost += extra

    specs = {"category": "Phone", "RAM": ram, "Storage": storage,
             "Display": display, "Color": color, "SIM": sim,
             "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_laptop(prices, order_summary, amount_stored, session_id):
    print_centered("── Laptops & Accessories ──")
    cost = prices["laptop"]

    size      = input("Size (13 / 14 / 15 / 16 / 17 inch): ")
    ram       = input("RAM (8GB / 16GB / 32GB / 64GB): ")
    storage   = input("Storage (256GB / 512GB / 1TB / 2TB): ")
    processor = input("Processor (i3/i5/i7/i9 / Ryzen 3/5/7/9): ")
    graphics_choice = input("Graphics (Integrated / Dedicated): ").lower()
    graphics_name = "Not specified"

    if "integrated" in graphics_choice:
        if "ryzen" in processor.lower():
            graphics_name = "AMD Radeon Graphics"
        else:
            ig = input("  Intel UHD Graphics / Intel Iris Xe Graphics: ").lower()
            if "iris xe" in ig:
                cost += 3000
                graphics_name = "Intel Iris Xe Graphics"
            else:
                graphics_name = "Intel UHD Graphics"
    elif "dedicated" in graphics_choice:
        dg = input("  GTX 1650 / RTX 3060 / RX 6600M: ").lower()
        if "gtx 1650" in dg:
            cost += 5000;  graphics_name = "NVIDIA GeForce GTX 1650"
        elif "rtx 3060" in dg:
            cost += 15000; graphics_name = "NVIDIA GeForce RTX 3060"
        elif "rx 6600m" in dg:
            cost += 12000; graphics_name = "AMD Radeon RX 6600M"

    os_choice = input("OS (Windows / MacOS / Linux): ").lower()
    if "macos"   in os_choice: cost += 10000
    elif "linux" in os_choice: cost += 5000
    color = input("Color (Silver / Black / Grey / Blue): ")
    print(f"  Laptop cost so far: Rs. {cost}")

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Charger": 1000, "Laptop Bag": 1500,
            "Mouse": 800,    "Keyboard": 1200,
        })
        cost += extra

    specs = {"category": "Laptop", "Size": size, "Processor": processor,
             "RAM": ram, "Storage": storage, "Graphics": graphics_name,
             "OS": os_choice.title(), "Color": color,
             "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_desktop(prices, order_summary, amount_stored, session_id):
    print_centered("── Desktops & Accessories ──")
    cost = prices["desktop"]

    processor = input("Processor (i3/i5/i7/i9 / Ryzen 3/5/7/9): ")
    ram       = input("RAM (8GB / 16GB / 32GB / 64GB): ")
    storage   = input("Storage (256GB / 512GB / 1TB / 2TB): ")

    graphics_choice = input("Graphics (Integrated / Dedicated): ").lower()
    graphics_name = "Not specified"
    if "integrated" in graphics_choice:
        if "ryzen" in processor.lower():
            graphics_name = "AMD Radeon Graphics"
        else:
            ig = input("  Intel UHD Graphics / Intel Iris Xe Graphics: ").lower()
            if "iris xe" in ig:
                cost += 3000; graphics_name = "Intel Iris Xe Graphics"
            else:
                graphics_name = "Intel UHD Graphics"
    elif "dedicated" in graphics_choice:
        dg = input("  GTX 1650 / RTX 3060 / RX 6600M: ").lower()
        if "gtx 1650" in dg:
            cost += 5000;  graphics_name = "NVIDIA GeForce GTX 1650"
        elif "rtx 3060" in dg:
            cost += 15000; graphics_name = "NVIDIA GeForce RTX 3060"
        elif "rx 6600m" in dg:
            cost += 12000; graphics_name = "AMD Radeon RX 6600M"

    os_choice = input("OS (Windows / Linux / MacOS): ").lower()
    if "windows" in os_choice: cost += 2000
    elif "linux" in os_choice: cost += 5000
    elif "macos" in os_choice: cost += 10000

    monitor_label = "None"
    if yn("Add a monitor?"):
        monitor_choice = input("  Monitor size (24 inch / 27 inch / 32 inch): ")
        monitor_label = monitor_choice + " Monitor"
        cost += 8000

    km_label = "None"
    if yn("Add keyboard & mouse combo? (+Rs.1500)"):
        km_label = "Keyboard & Mouse Combo"
        cost += 1500

    print(f"  Desktop cost so far: Rs. {cost}")
    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Speakers": 2000, "Webcam": 2500, "Printer": 3000,
        })
        cost += extra

    specs = {"category": "Desktop", "Processor": processor, "RAM": ram,
             "Storage": storage, "Graphics": graphics_name,
             "OS": os_choice.title(), "Monitor": monitor_label,
             "Keyboard & Mouse": km_label, "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_printer(prices, order_summary, amount_stored, session_id):
    print_centered("── Printers & Scanners ──")
    cost = prices["printer"]

    ptype        = input("Type (Inkjet / Laser / All-in-one): ")
    color        = input("Color (Black-White / Colour): ")
    connectivity = input("Connectivity (USB / Wi-Fi / Ethernet): ")
    resolution   = input("Resolution (600x600 / 1200x1200 / 2400x1200 dpi): ")

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Extra Ink Cartridges": 1500, "Paper Ream": 800,
        })
        cost += extra

    specs = {"category": "Printer", "Type": ptype, "Color": color,
             "Connectivity": connectivity, "Resolution": resolution,
             "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_wearable(prices, order_summary, amount_stored, session_id):
    print_centered("── Wearable Accessories ──")
    cost = prices["wearable"]

    wtype        = input("Type (Smartwatch / Fitness Tracker / Smart Glasses): ")
    connectivity = input("Connectivity (Bluetooth / Wi-Fi / Cellular): ")
    battery      = input("Battery life (1 day / 3 days / 7 days): ")
    color        = input("Color (Black / White / Blue / Red / Green): ")

    features_raw = input("Special features (Heart Rate Monitor, GPS, Sleep Tracking, "
                         "Music Playback, SPO2 Monitor — or 'all'): ")
    feature_map = {
        "heart rate monitor": 3000, "gps": 2000,
        "sleep tracking": 1500, "music playback": 1000, "spo2 monitor": 2500,
    }
    fl = features_raw.lower()
    selected_features = []
    if "all" in fl or "everything" in fl:
        selected_features = list(feature_map.keys())
        cost += sum(feature_map.values())
    else:
        for feat, price in feature_map.items():
            if feat in fl:
                selected_features.append(feat)
                cost += price
    features_label = ", ".join(selected_features) if selected_features else "None"

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Charging Dock": 2000, "Extra Straps": 1000,
            "Earbuds": 1500,       "Screen Protector": 500,
        })
        cost += extra

    specs = {"category": "Wearable", "Type": wtype, "Connectivity": connectivity,
             "Battery Life": battery, "Color": color,
             "Special Features": features_label, "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_tv(prices, order_summary, amount_stored, session_id):
    print_centered("── TV & Accessories ──")
    cost = prices["tv"]

    size         = input("Size (32 / 40 / 50 / 60 / 70 inch): ")
    resolution   = input("Resolution (HD / Full HD / 4K / 8K): ")
    display_type = input("Display (LED / OLED / QLED / 4K UHD / Smart): ").lower()
    if "oled"    in display_type: cost += 10000
    elif "qled"  in display_type: cost += 8000
    elif "4k uhd" in display_type: cost += 6000

    special  = input("Special features (HDR, Voice Control, Screen Mirroring, Built-in Apps): ")
    smart    = input("Smart platform (Google TV / Android TV / Fire TV / Roku): ")
    sound    = input("Sound (Standard / Surround Sound / Dolby Atmos): ").lower()
    if "surround" in sound: cost += 5000
    elif "dolby"  in sound: cost += 8000
    connectivity = input("Connectivity (HDMI / USB / Wi-Fi / Bluetooth): ")

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Wall Mount": 2000, "Soundbar": 5000,    "Remote Control": 1500,
            "TV Stand": 3000,   "HDMI Cable": 800,
            "Surge Protector": 1200, "Stabilizer": 2500,
        })
        cost += extra

    specs = {"category": "TV", "Size": size, "Resolution": resolution,
             "Display": display_type.upper(), "Special Features": special,
             "Smart Platform": smart, "Sound": sound.title(),
             "Connectivity": connectivity, "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_audio(prices, order_summary, amount_stored, session_id):
    print_centered("── Audio Devices & Accessories ──")
    cost = prices["audio_device"]

    atype        = input("Type (Headphones / Speakers / Soundbar / Earbuds): ")
    connectivity = input("Connectivity (Wired / Wireless / Bluetooth / Wi-Fi): ")
    color        = input("Color (Black / White / Blue / Red / Green): ")

    features_raw = input("Special features (Noise Cancellation, Waterproof, Voice Assistant, "
                         "Surround Sound, Long Battery Life — or 'all'): ")
    feature_map = {
        "noise cancellation": 3000, "waterproof": 2000,
        "voice assistant": 1500,    "surround sound": 2500, "long battery life": 1800,
    }
    fl = features_raw.lower()
    selected_features = []
    if "all" in fl or "everything" in fl:
        selected_features = list(feature_map.keys())
        cost += sum(feature_map.values())
    else:
        for feat, price in feature_map.items():
            if feat in fl:
                selected_features.append(feat)
                cost += price
    features_label = ", ".join(selected_features) if selected_features else "None"

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Carrying Case": 1000, "Extra Ear Tips": 500,
            "Charging Cable": 800, "Wireless Adapter": 1500,
        })
        cost += extra

    specs = {"category": "Audio Device", "Type": atype, "Connectivity": connectivity,
             "Color": color, "Special Features": features_label,
             "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)


def order_gaming(prices, order_summary, amount_stored, session_id):
    print_centered("── Gaming Consoles & Accessories ──")
    cost = prices["gaming_console"]

    gtype   = input("Console (PlayStation / Xbox / Nintendo Switch): ")
    storage = input("Storage (256GB / 512GB / 1TB / 2TB): ")
    color   = input("Color (Black / White / Blue / Red): ")

    accessories = "None"
    if yn("Add accessories?"):
        accessories, extra = select_accessories({
            "Extra Controller": 3000, "Charging Dock": 2000, "Headset": 2500,
        })
        cost += extra

    specs = {"category": "Gaming Console", "Type": gtype,
             "Storage": storage, "Color": color, "Accessories": accessories}
    return confirm_and_add(specs, cost, order_summary, amount_stored, session_id)

# ─────────────────────────────────────────────
#  Checkout
# ─────────────────────────────────────────────

def show_cart(order_summary):
    print_divider()
    print("  🛒  YOUR CART")
    print_divider()
    for idx, item in order_summary.items():
        print(f"\n  Order #{idx} — {item['category']}")
        for k, v in item.items():
            if k != "category":
                print(f"    {k:<28}: {v}")
    print_divider()

def checkout(order_summary, amount_stored):
    if not order_summary:
        print("  Cart is empty. Nothing to checkout.")
        return

    if yn("View cart before checkout?"):
        show_cart(order_summary)

    address = input("Delivery address: ")
    print(f"  Delivering to: {address}")

    total = sum(amount_stored)
    print(f"\n  Total payable: Rs. {total}")
    method = input("Payment method (Credit Card / Debit Card / UPI / Net Banking / Cash on Delivery): ")

    if method.lower() in ("credit card", "debit card", "upi", "net banking"):
        print(f"  Redirecting to {method} gateway…")
        print("  Payment link: https://chetan-go.github.io/tech-gazer/payment%20link1.html")
        done = input("  Type 'done' after completing payment: ").strip().lower()
        if done == "done":
            print("  ✔ Payment received!")
        else:
            print("  Payment incomplete. Try again later.")
            return
    else:
        print("  Cash on Delivery selected. Keep exact amount ready.")

    print("  🎉 Order placed! Estimated delivery: 7 days.")

    if yn("Save final bill to CSV?"):
        save_bill_to_csv(order_summary, amount_stored)

    if yn("View final bill on screen?"):
        show_cart(order_summary)
        print(f"\n  GRAND TOTAL: Rs. {total}")

# ─────────────────────────────────────────────
#  Menu & main loop
# ─────────────────────────────────────────────

MENU = {
    "1": ("Phones and accessories",          order_phone),
    "2": ("Laptops and accessories",         order_laptop),
    "3": ("Desktops and accessories",        order_desktop),
    "4": ("Printers and scanners",           order_printer),
    "5": ("Wearable accessories",            order_wearable),
    "6": ("TV and accessories",              order_tv),
    "7": ("Audio devices and accessories",   order_audio),
    "8": ("Gaming consoles and accessories", order_gaming),
    "9": ("Exit",                            None),
}

def print_menu():
    print_divider()
    print("  Select a product:")
    print_divider()
    for key, (label, _) in MENU.items():
        print(f"  {key}. {label}")
    print_divider()

def main():
    # Session ID for CSV tracking
    session_id = datetime.now().strftime("%Y%m%d%H%M%S")

    # Load prices from CSV
    prices = load_prices()

    # Welcome banner
    print_divider()
    print_centered("Welcome to Tech Gazer!")
    print_centered("Your one-stop tech shop")
    print_divider()

    order_summary  = {}
    amount_stored  = []

    while True:
        print_menu()
        choice = input("  Enter choice (1-9): ").strip()

        if choice not in MENU:
            print("  Invalid choice. Please enter 1-9.")
            continue

        label, handler = MENU[choice]

        if choice == "9":
            break

        print_divider()
        print_centered(f"You selected: {label}")
        print_divider()

        # Each handler returns True = add another, False = go to checkout
        continue_shopping = handler(prices, order_summary, amount_stored, session_id)
        if not continue_shopping:
            break

    # ── Checkout or exit ──────────────────────────────
    if order_summary:
        if yn("\nProceed to checkout?"):
            checkout(order_summary, amount_stored)
        else:
            print("  Orders saved in session but not placed.")
    else:
        print("  No orders placed this session.")

    print_divider()
    print_centered("Thank you for visiting Tech Gazer. Have a great day!")
    print_divider()


if __name__ == "__main__":
    main()
