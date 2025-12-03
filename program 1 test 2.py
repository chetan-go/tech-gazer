import shutil
width = shutil.get_terminal_size().columns
print_centered =width // 2
order_summary={}
order_quantity=0
amount_stored=[]
print(' '*print_centered,"=======================")
print(' '*print_centered,"Welcome to Tech gazer!")
print(' '*print_centered,"=======================")
print("We offer a wide range of tech products to fulfill to your needs.")
print("====================================================")
print("Here are all the products available in our stores:")
print("====================================================")
print("Product 1: \t Phones and accessories")
print("Product 2: \t Laptops and accessories")
print("Product 3: \t Desktops and accessories")
print("Product 4: \t Printers and scanners")
print('Product 5: \t wearable accessories')
print("Product 6: \t Tv and accessories")
print("Product 7: \t Audio devices and accessories")
print("Product 8: \t Gaming consoles and accessories")
print('9 to exit')
while True:
    print("=======================================")
    print("Proceeding to order selection...")
    print("=======================================")
    print("======================================================")
    print("Please select your order from the following options:")
    print("======================================================")
    print("1. Phones and accessories")
    print("2. Laptops and accessories")
    print("3. Desktops and accessories")
    print("4. Printers and scanners")
    print("5. Wearable accessories")
    print("6. Tv and accessories")
    print("7. Audio devices and accessories")
    print("8. Gaming consoles and accessories")
    print("9. Exit")
    phone_cost=15000
    laptop_cost=50000
    desktop_cost=40000
    printer_cost=5000
    wearable_cost=8000
    tv_cost=10000
    audio_devices_cost=7000
    gaming_console_cost=15000
    graphics_name = "Not specified"
    order = input("Enter the product number you wish to order (1-9): ")
    if order == '1':
        print("===============================================")
        print("You have selected Phones and accessories.")
        print("===============================================")
        phone_ram=input("Enter the RAM size you want (4GB, 6GB, 8GB, 12GB): ")
        phone_storage=input("Enter the storage size you want (64GB, 128GB, 256GB, 512GB): ")
        phone_display=input("Enter the display type you want (LCD, AMOLED): ")
        phone_color=input("Enter the color you want (Black, White, Blue, Red): ")
        phone_sim=input("Enter the SIM type you want (Single SIM / Dual SIM): ")
        print('cost of phone is Rs.15000')
        phone_accessories_request=input("would you like to add accessories? (yes/no): ")
        if phone_accessories_request.lower()=='yes':
            phone_accessories_menu=input("would you like to see the accessories available? (yes/no): ")
            if phone_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your phone:")
                print("=============================================================")
                print("accessories available:")
                print("1.Charger","price: Rs.500")
                print("2.Earphones","price: Rs.1000")
                print("3.Case","price: Rs.700")
                print("4.Screen Protector","price: Rs.300")
                phone_accessories=input("Enter the accessories you want (charger, earphones, case, screen protector, Enter all if all accessories needed): ").lower()
                if "all" in phone_accessories or "everything" in phone_accessories:
                    print("Your selected accessories are added to cart")
                    phone_cost += 500 + 1000 + 700 + 300
                    print("total phone cost after adding accessories is Rs.",phone_cost)
                else:
                    if "charger" in phone_accessories:
                         print("Added charger to your cart.")
                         phone_cost += 500
                         print("total phone cost after adding accessories is Rs.",phone_cost)
                    if "earphones" in phone_accessories:
                        print("Added earphones to your cart.")
                        phone_cost += 1000
                        print("total phone cost after adding accessories is Rs.",phone_cost)
                    if "case" in phone_accessories:
                        print("Added case to your cart.")
                        phone_cost += 700
                        print("total phone cost after adding accessories is Rs.",phone_cost)
                    if "screen" in phone_accessories:
                        print("Added screen protector to your cart.")
                        phone_cost += 300
                        print("total phone cost after adding accessories is Rs.",phone_cost)
            elif phone_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                phone_accessories=input("Enter the accessories you want (Charger, Earphones, Case, Screen Protector, Enter all if all accessories needed): ").lower()
                if "all" in phone_accessories or "everything" in phone_accessories:
                    print("Your selected accessories are added to cart")
                    phone_cost += 500 + 1000 + 700 + 300
                    print("total phone cost after adding accessories is Rs.",phone_cost)
                else:
                    if "charger" in phone_accessories:
                         print("Added charger to your cart.")
                         phone_cost += 500
                         print("total phone cost after adding accessories is Rs.",phone_cost)
                    if "earphones" in phone_accessories:
                        print("Added earphones to your cart.")
                        phone_cost += 1000
                        print("total phone cost after adding accessories is Rs.",phone_cost)
                    if "case" in phone_accessories:
                        print("Added case to your cart.")
                        phone_cost += 700
                        print("total phone cost after adding accessories is Rs.",phone_cost)
                    if "screen" in phone_accessories:
                        print("Added screen protector to your cart.")
                        phone_cost += 300
                        print("total phone cost after adding accessories is Rs.",phone_cost)
        elif phone_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            phone_accessories='No accessories added' 
        print("-------------------------------------------------------------")
        print("You have ordered a Phone with the following specifications:")
        print('-------------------------------------------------------------')
        print("RAM Size:", phone_ram)
        print("Storage Size:",phone_storage)
        print("Display Type:",phone_display)
        print("Color:",phone_color)
        print("SIM Type:",phone_sim)
        print("Accessories:",phone_accessories)
        print("your total phone cost is Rs.",phone_cost)
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Phone", "RAM":phone_ram, "Storage":phone_storage, "Display":phone_display, "Color":phone_color, "SIM":phone_sim, "Accessories":phone_accessories, "Total Cost (Rs)":phone_cost}
            amount_stored.append(phone_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
    elif order == '2':
        print("================================================")
        print("You have selected Laptops and accessories.")
        print("================================================")
        laptop_size=input("Enter the laptop size you want (13 inch, 14 inch, 15 inch, 16 inch, 17 inch): ")
        laptop_ram=input("Enter the RAM size you want (8GB, 16GB, 32GB, 64GB): ")
        laptop_storage=input("Enter the storage size you want (256GB, 512GB, 1TB, 2TB): ")
        laptop_processor=input("Enter the processor type you want (i3, i5, i7, i9, Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9): ")
        laptop_graphics=input("Enter the graphics card you want (Integrated, Dedicated): ")
        if laptop_graphics.lower()=='integrated':
            if "ryzen" in laptop_processor.lower():
                print("Integrated graphics comes free with Ryzen processors.")
                graphics_name="AMD Radeon Graphics"
            elif laptop_processor.lower() in ['i3','i5','i7','i9']:
                intel_graphics_choice=input("which integrated graphics do you want? (Intel UHD Graphics / Intel Iris Xe Graphics): ").lower()
                if 'uhd' in intel_graphics_choice:
                    print("Intel UHD Graphics comes free with Intel processors.")
                    graphics_name="Intel UHD Graphics"
                elif 'iris xe' in intel_graphics_choice:
                    laptop_cost += 3000
                    graphics_name="Intel Iris Xe Graphics"
        elif laptop_graphics.lower()=='dedicated':
            dedicated_graphics_choice=input("which dedicated graphics card do you want? (NVIDIA GeForce GTX 1650 / NVIDIA GeForce RTX 3060 / AMD Radeon RX 6600M): ").lower()
            if 'gtx 1650' in dedicated_graphics_choice:
                laptop_cost += 5000
                graphics_name="NVIDIA GeForce GTX 1650"
            elif 'rtx 3060' in dedicated_graphics_choice:
                laptop_cost += 15000
                graphics_name="NVIDIA GeForce RTX 3060"
            elif 'rx 6600m' in dedicated_graphics_choice:
                laptop_cost += 12000
                graphics_name="AMD Radeon RX 6600M"
        laptop_color=input("Enter the color you want (Silver, Black, Grey, Blue): ")
        laptop_operating_system=input("Enter the operating system you want (Windows, MacOS, Linux): ")
        if laptop_operating_system.lower()=='windows':
            laptop_cost += 0
        elif laptop_operating_system.lower()=='macos':
            laptop_cost += 10000
        elif laptop_operating_system.lower()=='linux':
            laptop_cost += 5000
        print("your total laptop cost is Rs.",laptop_cost)
        laptop_accessories_request=input("would you like to add accessories? (yes/no): ").lower()
        if laptop_accessories_request.lower()=='yes':
            laptop_accessories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if laptop_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your laptop:")
                print("=============================================================")
                print("accessories available:")
                print("1.Charger","price: Rs.1000")
                print("2.Laptop Bag","price: Rs.1500")
                print("3.Mouse","price: Rs.800")
                print("4.Keyboard","price: Rs.1200")
                laptop_accessories=input("Enter the accessories you want (Charger, Laptop Bag, Mouse, Keyboard, Enter all if all accessories needed): ").lower()
                if "all" in laptop_accessories or "everything" in laptop_accessories:
                    print("Your selected accessories are added to cart")
                    laptop_cost += 1000 + 1500 + 800 + 1200
                    print("total laptop cost after adding accessories is Rs.",laptop_cost)
                else:
                    if "charger" in laptop_accessories:
                         print("Added charger to your cart.")
                         laptop_cost += 1000
                         print("total laptop cost after adding accessories is Rs.",laptop_cost)
                    if "laptop bag" in laptop_accessories:
                        print("Added laptop bag to your cart.")
                        laptop_cost += 1500
                        print("total laptop cost after adding accessories is Rs.",laptop_cost)
                    if "mouse" in laptop_accessories:
                        print("Added mouse to your cart.")
                        laptop_cost += 800
                        print("total laptop cost after adding accessories is Rs.",laptop_cost)
                    if "keyboard" in laptop_accessories:
                        print("Added keyboard to your cart.")
                        laptop_cost += 1200
                        print("total laptop cost after adding accessories is Rs.",laptop_cost)
            elif laptop_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                laptop_accessories=input("Enter the accessories you want (Charger, Laptop Bag, Mouse, Keyboard, Enter all if all accessories needed): ").lower()
                if "all" in laptop_accessories or "everything" in laptop_accessories:
                    print("Your selected accessories are added to cart")
                    laptop_cost += 1000 + 1500 + 800 + 1200
                else:
                    if "charger" in laptop_accessories:
                         print("Added charger to your cart.")
                         laptop_cost += 1000
                    if "laptop bag" in laptop_accessories:
                        print("Added laptop bag to your cart.")
                        laptop_cost += 1500
                    if "mouse" in laptop_accessories:
                        print("Added mouse to your cart.")
                        laptop_cost += 800
                    if "keyboard" in laptop_accessories:
                        print("Added keyboard to your cart.")
                        laptop_cost += 1200
        elif laptop_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            laptop_accessories='No accessories added'
        print("-------------------------------------------------------------")
        print("You have ordered a Laptop with the following specifications:")
        print("-------------------------------------------------------------")
        print("Size:", laptop_size)
        print("Processor:", laptop_processor)
        print("RAM:", laptop_ram)
        print("Storage:", laptop_storage)
        print("Graphics Card:", graphics_name)
        print("Operating System:", laptop_operating_system)
        print("Accessories:", laptop_accessories)
        print("Total Cost (Rs):", laptop_cost)
        print("-------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Laptop", "Size":laptop_size, "Processor":laptop_processor, "RAM":laptop_ram, "Storage":laptop_storage, "Graphics":graphics_name, "Operating System":laptop_operating_system, "Accessories":laptop_accessories, "Total Cost (Rs)":laptop_cost}
            amount_stored.append(laptop_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
    elif order == '3':
        print("===========================================")
        print("You have selected Desktops and accessories.")
        print("===========================================")
        desktop_processor=input("Enter the processor type you want (i3, i5, i7, i9, Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9): ")
        desktop_ram=input("Enter the RAM size you want (8GB, 16GB, 32GB, 64GB): ")
        desktop_storage=input("Enter the storage size you want (256GB, 512GB, 1TB, 2TB): ")
        desktop_graphics=input("Enter the graphics card you want (Integrated, Dedicated): ")
        if desktop_graphics.lower()=='integrated':
            if "ryzen" in desktop_processor.lower():
                print("Integrated graphics comes free with Ryzen processors.")
                graphics_name="AMD Radeon Graphics"
            elif desktop_processor.lower() in ['i3','i5','i7','i9']:
                intel_graphics_choice=input("which integrated graphics do you want? (Intel UHD Graphics / Intel Iris Xe Graphics): ").lower()
                if 'uhd' in intel_graphics_choice:
                    print("Intel UHD Graphics comes free with Intel processors.")
                    graphics_name="Intel UHD Graphics"
                elif 'iris xe' in intel_graphics_choice:
                    desktop_cost += 3000
                    graphics_name="Intel Iris Xe Graphics"
        elif desktop_graphics.lower()=='dedicated':
            dedicated_graphics_choice=input("which dedicated graphics card do you want? (NVIDIA GeForce GTX 1650 / NVIDIA GeForce RTX 3060 / AMD Radeon RX 6600M): ").lower()
            if 'gtx 1650' in dedicated_graphics_choice:
                desktop_cost += 5000
                graphics_name="NVIDIA GeForce GTX 1650"
            elif 'rtx 3060' in dedicated_graphics_choice:
                desktop_cost += 15000
                graphics_name="NVIDIA GeForce RTX 3060"
            elif 'rx 6600m' in dedicated_graphics_choice:
                desktop_cost += 12000
                graphics_name="AMD Radeon RX 6600M"
        desktop_operating_system=input("Enter the operating system you want (Windows, Linux, MacOS): ")
        if desktop_operating_system.lower()=='windows':
            desktop_cost += 2000
        elif desktop_operating_system.lower()=='linux':
            desktop_cost += 5000
        elif desktop_operating_system.lower()=='macos':
            desktop_cost += 10000
        desktop_monitor=input("Would you like to add a monitor? (yes/no): ")
        monitor_choice1="No monitor added"
        if desktop_monitor.lower()=='yes':
            desktop_cost += 8000
            monitor_choice=input("Which monitor would you like to add? (24 inch / 27 inch / 32 inch): ")
            print("Added",monitor_choice,"monitor to your cart.")
            monitor_choice1=monitor_choice + " monitor"
        elif desktop_monitor.lower()=='no':
            print("No monitor added to your cart.")
        keyboard_mouse_combo=input("Would you like to add a keyboard and mouse combo? (yes/no): ")
        keyboard_mouse_choice1="No keyboard and mouse combo added"
        if keyboard_mouse_combo.lower()=='yes':
            desktop_cost += 1500
            print("Added keyboard and mouse combo to your cart.")
            keyboard_mouse_choice1="Keyboard and Mouse Combo"
        elif keyboard_mouse_combo.lower()=='no':
            print("No keyboard and mouse combo added to your cart.")
        desktop_accessories_request=input("would you like to add accessories in your desktop? (yes/no): ").lower()
        if desktop_accessories_request.lower()=='yes':
            desktop_accessories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if desktop_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your desktop:")
                print("=============================================================")
                print("accessories available:")
                print("1.Speakers","price: Rs.2000")
                print("2.Webcam","price: Rs.2500")
                print("3.Printer","price: Rs.3000")
                desktop_accessories=input("Enter the accessories you want (Speakers, Webcam, Printer, Enter all if all accessories needed): ").lower()
                if "all" in desktop_accessories or "everything" in desktop_accessories:
                    print("Your selected accessories are added to cart")
                    desktop_cost += 2000 + 2500 + 3000
                    print("total desktop cost after adding accessories is Rs.",desktop_cost)
                else:
                    if "speakers" in desktop_accessories:
                         print("Added speakers to your cart.")
                         desktop_cost += 2000
                         print("total desktop cost after adding accessories is Rs.",desktop_cost)
                    if "webcam" in desktop_accessories:
                        print("Added webcam to your cart.")
                        desktop_cost += 2500
                        print("total desktop cost after adding accessories is Rs.",desktop_cost)
                    if "printer" in desktop_accessories:
                        print("Added printer to your cart.")
                        desktop_cost += 3000
                        print("total desktop cost after adding accessories is Rs.",desktop_cost)
            elif desktop_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                desktop_accessories=input("Enter the accessories you want (Speakers, Webcam, Printer, Enter all if all accessories needed): ").lower()
                if "all" in desktop_accessories or "everything" in desktop_accessories:
                    print("Your selected accessories are added to cart")
                    desktop_cost += 2000 + 2500 + 3000
                    print("total desktop cost after adding accessories is Rs.",desktop_cost)
                else:
                    if "speakers" in desktop_accessories:
                         print("Added speakers to your cart.")
                         desktop_cost += 2000
                         print("total desktop cost after adding accessories is Rs.",desktop_cost)
                    if "webcam" in desktop_accessories:
                        print("Added webcam to your cart.")
                        desktop_cost += 2500
                        print("total desktop cost after adding accessories is Rs.",desktop_cost)
                    if "printer" in desktop_accessories:
                        print("Added printer to your cart.")
                        desktop_cost += 3000
                        print("total desktop cost after adding accessories is Rs.",desktop_cost)
        elif desktop_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            desktop_accessories='No accessories added'
        print("-------------------------------------------------------------")
        print("You have ordered a Desktop with the following specifications:")
        print("-------------------------------------------------------------")
        print("Processor:", desktop_processor)
        print("RAM:", desktop_ram)
        print("Storage:", desktop_storage)
        print("Graphics Card:", graphics_name)
        print("Operating System:", desktop_operating_system)
        print("Monitor:", monitor_choice1)
        print("Keyboard and Mouse Combo:", keyboard_mouse_choice1)
        print("Accessories:",desktop_accessories)
        print("Total Cost (Rs):", desktop_cost)
        print("-------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Desktop", "Processor":desktop_processor, "RAM":desktop_ram, "Storage":desktop_storage, "Graphics":graphics_name, "Operating System":desktop_operating_system, "Monitor":monitor_choice1, "Keyboard and Mouse Combo":keyboard_mouse_choice1, "Accessories":desktop_accessories, "Total Cost (Rs)":desktop_cost}
            amount_stored.append(desktop_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
    elif order=='4':
        print("=======================================")
        print("You have selected Printers and scanners.")
        print("=======================================")
        printer_type=input("Enter the type of printer you want (Inkjet, Laser, All-in-one-printers and scanners): ")
        printer_color=input("Enter the color you want (Black-White, colour): ")
        printer_connectivity=input("Enter the connectivity type you want (USB, Wi-Fi, Ethernet): ")
        printer_resolution=input("Enter the resolution you want (600x600 dpi, 1200x1200 dpi, 2400x1200 dpi): ")
        printer_accessories_request=input("would you like to add accessories in your printer? (yes/no): ").lower()
        if printer_accessories_request.lower()=='yes':
            printer_accessories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if printer_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your printer:")
                print("=============================================================")
                print("accessories available:")
                print("1.Extra Ink Cartridges","price: Rs.1500")
                print("2.Paper Ream","price: Rs.800")
                printer_accessories=input("Enter the accessories you want (Extra Ink Cartridges, Paper Ream, Enter all if all accessories needed): ").lower()
                if "all" in printer_accessories or "everything" in printer_accessories:
                    print("Your selected accessories are added to cart")
                    printer_cost += 1500 + 800
                    print("total printer cost after adding accessories is Rs.",printer_cost)
                else:
                    if "extra ink cartridges" in printer_accessories:
                         print("Added extra ink cartridges to your cart.")
                         printer_cost += 1500
                         print("total printer cost after adding accessories is Rs.",printer_cost)
                    if "paper ream" in printer_accessories:
                        print("Added paper ream to your cart.")
                        printer_cost += 800
                        print("total printer cost after adding accessories is Rs.",printer_cost)
            elif printer_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                printer_accessories=input("Enter the accessories you want (Extra Ink Cartridges, Paper Ream, Enter all if all accessories needed): ").lower()
                if "all" in printer_accessories or "everything" in printer_accessories:
                    print("Your selected accessories are added to cart")
                    printer_cost += 1500 + 800
                    print("total printer cost after adding accessories is Rs.",printer_cost)
                else:
                    if "extra ink cartridges" in printer_accessories:
                         print("Added extra ink cartridges to your cart.")
                         printer_cost += 1500
                         print("total printer cost after adding accessories is Rs.",printer_cost)
                    if "paper ream" in printer_accessories:
                        print("Added paper ream to your cart.")
                        printer_cost += 800
                        print("total printer cost after adding accessories is Rs.",printer_cost)
        elif printer_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            printer_accessories='No accessories added'
        print("-------------------------------------------------------------")
        print("You have ordered a Printer with the following specifications:")
        print("-------------------------------------------------------------")
        print("Type:", printer_type)
        print("Color:", printer_color)
        print("Connectivity:", printer_connectivity)
        print("Resolution:", printer_resolution)
        print("Accessories:",printer_accessories)
        print("Total Cost (Rs):", printer_cost)
        print("-------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Printer", "Type":printer_type, "Color":printer_color, "Connectivity":printer_connectivity, "Resolution":printer_resolution, "Accessories":printer_accessories, "Total Cost (Rs)":printer_cost}
            amount_stored.append(printer_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
    elif order == '5':
        print("=======================================")
        print("You have selected Wearable accessories.")
        print("=======================================")
        wearable_type=input("Enter the type of wearable accessory you want (Smartwatch, Fitness Tracker, Smart Glasses): ")
        wearable_connectivity=input("Enter the connectivity type you want (Bluetooth, Wi-Fi, Cellular): ")
        wearable_backup_battery=input("Enter the backup battery time you want (1 day, 3 days, 7 days): ")
        wearable_color=input("Enter the color you want (Black, White, Blue, Red, Green): ")
        wearable_features=input("Enter any special features you want (Heart Rate Monitor, GPS, Sleep Tracking, Music Playback, SPO2 Monitor, enter all if all the special features needed): ")
        if "all" in wearable_features.lower() or "everything" in wearable_features.lower():
            wearable_cost += 3000 + 2000 + 1500 + 1000 + 2500
        else:
            if "heart rate monitor" in wearable_features.lower():
                print("Added heart rate monitor feature.")
                wearable_cost += 3000
            if "gps" in wearable_features.lower():
                print("Added GPS feature.")
                wearable_cost += 2000
            if "sleep tracking" in wearable_features.lower():
                print("Added sleep tracking feature.")
                wearable_cost += 1500
            if "music playback" in wearable_features.lower():
                print("Added music playback feature.")
                wearable_cost += 1000
            if "spo2 monitor" in wearable_features.lower():
                print("Added SPO2 monitor feature.")
                wearable_cost += 2500
        wearable_accessories_request=input("would you like to add accessories in your wearable? (yes/no): ").lower()
        if wearable_accessories_request.lower()=='yes':
            wearable_accessories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if wearable_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your wearable:")
                print("=============================================================")
                print("accessories available:")
                print("1.Charging Dock","price: Rs.2000")
                print("2.Extra Straps","price: Rs.1000")
                print("3.Ear buds","price: Rs.1500")
                print("4.Screen Protector","price: Rs.500")
                wearable_accessories=input("Enter the accessories you want (Charging Dock, Extra Straps, Earbuds, Screen Protector, Enter all if all accessories needed): ").lower()
                if "all" in wearable_accessories or "everything" in wearable_accessories:
                    print("Your selected accessories are added to cart")
                    wearable_cost += 2000 + 1000 + 1500 + 500
                    print("total wearable cost after adding accessories is Rs.",wearable_cost)
                else:
                    if "charging dock" in wearable_accessories:
                         print("Added charging dock to your cart.")
                         wearable_cost += 2000
                         print("total wearable cost after adding accessories is Rs.",wearable_cost)
                    if "extra straps" in wearable_accessories:
                        print("Added extra straps to your cart.")
                        wearable_cost += 1000
                        print("total wearable cost after adding accessories is Rs.",wearable_cost)
                    if "ear buds" in wearable_accessories:
                        print("Added ear buds to your cart.")
                        wearable_cost += 1500
                        print("total wearable cost after adding accessories is Rs.",wearable_cost)
                    if "screen protector" in wearable_accessories:
                        print("Added screen protector to your cart.")
                        wearable_cost += 500
                        print("total wearable cost after adding accessories is Rs.",wearable_cost)
            elif wearable_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                wearable_accessories=input("Enter the accessories you want (Charging Dock, Extra Straps, Earbuds, Screen Protector, Enter all if all accessories needed): ").lower()
                if "all" in wearable_accessories or "everything" in wearable_accessories:
                    print("Your selected accessories are added to cart")
                    wearable_cost += 2000 + 1000 + 1500 + 500
                    print("total wearable cost after adding accessories is Rs.",wearable_cost)
                else:
                    if "charging dock" in wearable_accessories:
                         print("Added charging dock to your cart.")
                         wearable_cost += 2000
                         print("total wearable cost after adding accessories is Rs.",wearable_cost)
                    if "extra straps" in wearable_accessories:
                        print("Added extra straps to your cart.")
                        wearable_cost += 1000
                        print("total wearable cost after adding accessories is Rs.",wearable_cost)
                    if "ear buds" in wearable_accessories:
                        print("Added ear buds to your cart.")
                        wearable_cost += 1500
                        print("total wearable cost after adding accessories is Rs.",wearable_cost)
                    if "screen protector" in wearable_accessories:
                        print("Added screen protector to your cart.")
                        wearable_cost += 500
                        print("total wearable cost after adding accessories is Rs.",wearable_cost)
        elif wearable_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            wearable_accessories='No accessories added'
        print("-----------------------------------------------------------------------")
        print("You have ordered a Wearable accessory with the following specifications:")
        print("-----------------------------------------------------------------------")
        print("Type:", wearable_type)
        print("Connectivity:", wearable_connectivity)
        print("Backup Battery Time:", wearable_backup_battery)
        print("Color:", wearable_color)
        print("Special Features:", wearable_features)
        print("Total Cost (Rs):", wearable_cost)
        print("-----------------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Wearable", "Type":wearable_type, "Connectivity":wearable_connectivity, "Backup Battery Time":wearable_backup_battery, "Color":wearable_color, "Special Features":wearable_features, "Accessories":wearable_accessories, "Total Cost (Rs)":wearable_cost}
            amount_stored.append(wearable_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
    elif order == '6':
        print("=====================================")
        print("You have selected Tv and accessories.")
        print("=====================================")
        tv_size=input("Enter the TV size you want (32 inch, 40 inch, 50 inch, 60 inch, 70 inch): ")
        tv_resolution=input("Enter the resolution you want (HD, Full HD, 4K, 8K): ")
        tv_display_type=input("Enter the display type you want (LED, OLED, QLED, 4K UHD, Smart): ")
        if "oled" in tv_display_type.lower():
            tv_cost += 10000
        elif "qled" in tv_display_type.lower():
            tv_cost += 8000
        elif "4k uhd" in tv_display_type.lower():
            tv_cost += 6000
        elif "led" in tv_display_type.lower():
            tv_cost += 0
        tv_special_features=input("Enter any special features you want (HDR, Voice Control, Screen Mirroring, Built-in Apps): ")
        tv_smart_features=input("Enter any smart features you want(Google TV, Android TV, Fire TV, Roku): ")
        tv_sound_output_preference=input("Enter any sound preference you want (Standard, Surround Sound, Dolby Atmos): ")
        if "surround sound" in tv_sound_output_preference.lower():
            tv_cost += 5000
        elif "dolby atmos" in tv_sound_output_preference.lower():
            tv_cost += 8000
        elif "standard" in tv_sound_output_preference.lower():
            tv_cost += 0
        tv_connectivity=input("Enter the connectivity type you want (HDMI, USB, Wi-Fi, Bluetooth): ")
        tv_accesories_request=input("would you like to add accessories in your TV? (yes/no): ").lower()
        if tv_accesories_request.lower()=='yes':
            tv_accesories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if tv_accesories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your TV:")
                print("=============================================================")
                print("accessories available:")
                print("1.Wall Mount","price: Rs.2000")
                print("2.Soundbar","price: Rs.5000")
                print("3.Remote Control","price: Rs.1500")
                print("4.TV Stand","price: Rs.3000")
                print("5.Extra HDMI Cable","price: Rs.800")
                print("6.Surge Protector","price: Rs.1200")
                print("7.Stabilizer","price: Rs.2500")
                tv_accessories=input("Enter the accessories you want (Wall Mount, Soundbar, Remote Control, TV Stand, Extra HDMI Cable, Surge Protector, Stabilizer, Enter all if all accessories needed): ").lower()
                if "all" in tv_accessories or "everything" in tv_accessories:
                    print("Your selected accessories are added to cart")
                    tv_cost += 2000 + 5000 + 1500 + 3000 + 800 + 1200 + 2500    
                else:
                    if "wall mount" in tv_accessories:
                         print("Added wall mount to your cart.")
                         tv_cost += 2000
                         print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "soundbar" in tv_accessories:
                        print("Added soundbar to your cart.")
                        tv_cost += 5000
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "remote control" in tv_accessories:
                        print("Added remote control to your cart.")
                        tv_cost += 1500
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "tv stand" in tv_accessories:
                        print("Added TV stand to your cart.")
                        tv_cost += 3000
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "extra hdmi cable" in tv_accessories:
                        print("Added extra HDMI cable to your cart.")
                        tv_cost += 800
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "surge protector" in tv_accessories:
                        print("Added surge protector to your cart.")
                        tv_cost += 1200
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "stabilizer" in tv_accessories:
                        print("Added stabilizer to your cart.")
                        tv_cost += 2500
                        print("total TV cost after adding accessories is Rs.",tv_cost)
            elif tv_accesories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                tv_accessories=input("Enter the accessories you want (Wall Mount, Soundbar, Remote Control, TV Stand, Extra HDMI Cable, Surge Protector, Stabilizer, Enter all if all accessories needed): ").lower()
                if "all" in tv_accessories or "everything" in tv_accessories:
                    print("Your selected accessories are added to cart")
                    tv_cost += 2000 + 5000 + 1500 + 3000 + 800 + 1200 + 2500    
                else:
                    if "wall mount" in tv_accessories:
                         print("Added wall mount to your cart.")
                         tv_cost += 2000
                         print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "soundbar" in tv_accessories:
                        print("Added soundbar to your cart.")
                        tv_cost += 5000
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "remote control" in tv_accessories:
                        print("Added remote control to your cart.")
                        tv_cost += 1500
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "tv stand" in tv_accessories:
                        print("Added TV stand to your cart.")
                        tv_cost += 3000
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "extra hdmi cable" in tv_accessories:
                        print("Added extra HDMI cable to your cart.")
                        tv_cost += 800
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "surge protector" in tv_accessories:
                        print("Added surge protector to your cart.")
                        tv_cost += 1200
                        print("total TV cost after adding accessories is Rs.",tv_cost)
                    if "stabilizer" in tv_accessories:
                        print("Added stabilizer to your cart.")
                        tv_cost += 2500
                        print("total TV cost after adding accessories is Rs.",tv_cost)
        elif tv_accesories_request.lower()=='no':
            print("No accessories added to your cart.")
            tv_accessories='No accessories added'
        print("-------------------------------------------------------------")
        print("You have ordered a TV with the following specifications:")
        print("-------------------------------------------------------------")
        print("Size:", tv_size)
        print("Resolution:", tv_resolution) 
        print("Display Type:", tv_display_type)
        print("Special Features:", tv_special_features)
        print("Smart Features:", tv_smart_features)
        print("Sound Output Preference:", tv_sound_output_preference)
        print("Connectivity:", tv_connectivity)
        print("Accessories:",tv_accessories)
        print("Total Cost (Rs):", tv_cost)
        print("-------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':  
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"TV", "Size":tv_size, "Resolution":tv_resolution, "Display Type":tv_display_type, "Special Features":tv_special_features, "Smart Features":tv_smart_features, "Sound Output Preference":tv_sound_output_preference, "Connectivity":tv_connectivity, "Accessories":tv_accessories, "Total Cost (Rs)":tv_cost}
            amount_stored.append(tv_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break 
    elif order == '7':
        print("===============================================")
        print("You have selected Audio devices and accessories.")
        print("===============================================")
        audio_device_type=input("Enter the type of audio device you want (Headphones, Speakers, Soundbars, Earbuds): ")
        audio_device_connectivity=input("Enter the connectivity type you want (Wired, Wireless, Bluetooth, Wi-Fi): ")
        audio_device_color=input("Enter the color you want (Black, White, Blue, Red, Green): ")
        audio_device_special_features=input("Enter any special features you want (Noise Cancellation, Waterproof, Voice Assistant, Surround Sound, Long Battery Life, enter all if all the special features needed): ")
        if "all" in audio_device_special_features.lower() or "everything" in audio_device_special_features.lower():
            audio_device_cost += 3000 + 2000 + 1500 + 2500 + 1800
        else:
            if "noise cancellation" in audio_device_special_features.lower():
                print("Added noise cancellation feature.")
                audio_device_cost += 3000
            if "waterproof" in audio_device_special_features.lower():
                print("Added waterproof feature.")
                audio_device_cost += 2000
            if "voice assistant" in audio_device_special_features.lower():
                print("Added voice assistant feature.")
                audio_device_cost += 1500
            if "surround sound" in audio_device_special_features.lower():
                print("Added surround sound feature.")
                audio_device_cost += 2500
            if "long battery life" in audio_device_special_features.lower():
                print("Added long battery life feature.")
                audio_device_cost += 1800
        audio_device_accessories_request=input("would you like to add accessories in your audio device? (yes/no): ").lower()
        if audio_device_accessories_request.lower()=='yes':
            audio_device_accessories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if audio_device_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your audio device:")
                print("=============================================================")
                print("accessories available:")
                print("1.Carrying Case","price: Rs.1000")
                print("2.Extra Ear Tips","price: Rs.500")
                print("3.Charging Cable","price: Rs.800")
                print("4.Wireless Adapter","price: Rs.1500")
                audio_device_accessories=input("Enter the accessories you want (Carrying Case, Extra Ear Tips, Charging Cable, Wireless Adapter, Enter all if all accessories needed): ").lower()
                if "all" in audio_device_accessories or "everything" in audio_device_accessories:
                    print("Your selected accessories are added to cart")
                    audio_device_cost += 1000 + 500 + 800 + 1500
                    print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                else:
                    if "carrying case" in audio_device_accessories:
                         print("Added carrying case to your cart.")
                         audio_device_cost += 1000
                         print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                    if "extra ear tips" in audio_device_accessories:
                        print("Added extra ear tips to your cart.")
                        audio_device_cost += 500
                        print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                    if "charging cable" in audio_device_accessories:
                        print("Added charging cable to your cart.")
                        audio_device_cost += 800
                        print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                    if "wireless adapter" in audio_device_accessories:
                        print("Added wireless adapter to your cart.")
                        audio_device_cost += 1500
                        print("total audio device cost after adding accessories is Rs.",audio_device_cost)
            elif audio_device_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                audio_device_accessories=input("Enter the accessories you want (Carrying Case, Extra Ear Tips, Charging Cable, Wireless Adapter, Enter all if all accessories needed): ").lower()
                if "all" in audio_device_accessories or "everything" in audio_device_accessories:
                    print("Your selected accessories are added to cart")
                    audio_device_cost += 1000 + 500 + 800 + 1500
                    print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                else:
                    if "carrying case" in audio_device_accessories:
                         print("Added carrying case to your cart.")
                         audio_device_cost += 1000
                         print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                    if "extra ear tips" in audio_device_accessories:
                        print("Added extra ear tips to your cart.")
                        audio_device_cost += 500
                        print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                    if "charging cable" in audio_device_accessories:
                        print("Added charging cable to your cart.")
                        audio_device_cost += 800
                        print("total audio device cost after adding accessories is Rs.",audio_device_cost)
                    if "wireless adapter" in audio_device_accessories:
                        print("Added wireless adapter to your cart.")
                        audio_device_cost += 1500
                        print("total audio device cost after adding accessories is Rs.",audio_device_cost)
        elif audio_device_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            audio_device_accessories='No accessories added'
        print("-----------------------------------------------------------------------")
        print("You have ordered an Audio Device with the following specifications:")
        print("-----------------------------------------------------------------------")
        print("Type:", audio_device_type)
        print("Connectivity:", audio_device_connectivity)
        print("Color:", audio_device_color)
        print("Special Features:", audio_device_special_features)
        print("Total Cost (Rs):", audio_device_cost)
        print("-----------------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Audio Device", "Type":audio_device_type, "Connectivity":audio_device_connectivity, "Color":audio_device_color, "Special Features":audio_device_special_features, "Accessories":audio_device_accessories, "Total Cost (Rs)":audio_device_cost}
            amount_stored.append(audio_device_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break   
    elif order == '8':
        print("=====================================")
        print("You have selected Gaming consoles.")
        print("=====================================")
        gaming_console_type=input("Enter the type of gaming console you want (PlayStation, Xbox, Nintendo Switch): ")
        gaming_console_storage=input("Enter the storage size you want (256GB, 512GB, 1TB, 2TB): ")
        gaming_console_color=input("Enter the color you want (Black, White, Blue, Red): ")
        gaming_console_accessories_request=input("would you like to add accessories in your gaming console? (yes/no): ").lower()
        if gaming_console_accessories_request.lower()=='yes':
            gaming_console_accessories_menu=input("would you like to see the accessories available? (yes/no): ").lower()
            if gaming_console_accessories_menu.lower()=='yes':
                print("=============================================================")
                print("Here are the available accessories for your gaming console:")
                print("=============================================================")
                print("accessories available:")
                print("1.Extra Controller","price: Rs.3000")
                print("2.Charging Dock","price: Rs.2000")
                print("3.Headset","price: Rs.2500")
                gaming_console_accessories=input("Enter the accessories you want (Extra Controller, Charging Dock, Headset, Enter all if all accessories needed): ").lower()
                if "all" in gaming_console_accessories or "everything" in gaming_console_accessories:
                    print("Your selected accessories are added to cart")
                    gaming_console_cost += 3000 + 2000 + 2500
                    print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
                else:
                    if "extra controller" in gaming_console_accessories:
                         print("Added extra controller to your cart.")
                         gaming_console_cost += 3000
                         print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
                    if "charging dock" in gaming_console_accessories:
                        print("Added charging dock to your cart.")
                        gaming_console_cost += 2000
                        print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
                    if "headset" in gaming_console_accessories:
                        print("Added headset to your cart.")
                        gaming_console_cost += 2500
                        print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
            elif gaming_console_accessories_menu.lower()=='no':
                print("Proceeding without showing accessories menu.")
                gaming_console_accessories=input("Enter the accessories you want (Extra Controller, Charging Dock, Headset, Enter all if all accessories needed): ").lower()
                if "all" in gaming_console_accessories or "everything" in gaming_console_accessories:
                    print("Your selected accessories are added to cart")
                    gaming_console_cost += 3000 + 2000 + 2500
                    print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
                else:
                    if "extra controller" in gaming_console_accessories:
                         print("Added extra controller to your cart.")
                         gaming_console_cost += 3000
                         print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
                    if "charging dock" in gaming_console_accessories:
                        print("Added charging dock to your cart.")
                        gaming_console_cost += 2000
                        print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
                    if "headset" in gaming_console_accessories:
                        print("Added headset to your cart.")
                        gaming_console_cost += 2500
                        print("total gaming console cost after adding accessories is Rs.",gaming_console_cost)
        elif gaming_console_accessories_request.lower()=='no':
            print("No accessories added to your cart.")
            gaming_console_accessories='No accessories added'
        print("-------------------------------------------------------------")
        print("You have ordered a Gaming Console with the following specifications:")
        print("-------------------------------------------------------------")
        print("Type:", gaming_console_type)
        print("Storage Size:", gaming_console_storage)
        print("Color:", gaming_console_color)
        print("Accessories:",gaming_console_accessories)
        print("Total Cost (Rs):", gaming_console_cost)
        print("-------------------------------------------------------------")
        print("Your order quantity is:",order_quantity + 1)
        reconformation=input("Do you want to confirm your order to be added into cart? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been added!")
            order_summary[order_quantity]={"category":"Gaming Console", "Type":gaming_console_type, "Storage Size":gaming_console_storage, "Color":gaming_console_color, "Accessories":gaming_console_accessories, "Total Cost (Rs)":gaming_console_cost}
            amount_stored.append(gaming_console_cost)
            reorder=input("Do you want to place another order? (yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
        else:
            print("Your order has been cancelled.")
            reorder=input("would you like to place a new order?(yes/no): ")
            if reorder.lower()=='yes':
                pass
            else:
                print("Thank you for visiting Tech Gazer. Have a great day!")
                break
    elif order == '9':
        print("Exiting the order placement section.")
        print("Thank you for visiting Tech Gazer. Have a great day!")
        break
if len(order_summary)==0:
    print("No orders placed. Exiting the program.")
    print("Thank you for visiting Tech Gazer. Have a great day!")
else:
    order_placement=input("Would you like to place your order now? (yes/no): ")
    if order_placement.lower()=='yes':
        cart=input("Would you like to see your cart before placing order? (yes/no): ")
        if cart.lower()=='yes':
            print("================================")
            print("here is your Order Summary:")
            print("================================")
            print()
            print("================================")
            print("Order Summary")
            print("================================")
            j=1
            for i in (order_summary):
                print("===============")
                print("Order",j,":")
                print("===============")
                for k in order_summary[i]:
                    print(k,':',order_summary[i][k])
                j+=1
            print("================================")
            print('proceeding to address selection...')
            print("================================")
            address=input("Enter your delivery address: ")
            print('your order will be delivered to:',address)
            print("================================")
            print('proceeding to payment...')
            print("================================")
            payment_amount=sum(amount_stored)
            print("Your total payment amount is Rs.",payment_amount)
            payment_method=input("Enter your payment method (Credit Card, Debit Card, UPI, Net Banking, Cash on Delivery): ")
            if payment_method.lower() in ['credit card','debit card','upi','net banking']:
                print('proceeding to',payment_method,'payment gateway...')
                print('your payment gateway is ready.')
                print('Kindly click on the link below to complete your payment:')
                print('https://chetan-go.github.io/tech-gazer/payment%20link1.html')
                payment=input('enter done after completing your payment:')
                if payment.lower()=='done':
                    print('your payment has been received successfully!')
                    print('Thank you for shopping with Tech Gazer. Your order will be delivered within 7 days.')
                else:
                    print('payment not completed. please try again later.')
                    print("exiting....")
            elif payment_method.lower()=='cash on delivery':
                print('You have selected Cash on Delivery. Please keep the exact amount ready at the time of delivery.')
                print('Thank you for shopping with Tech Gazer. Your order will be delivered within 7 days.')

        elif cart.lower()=='no':
            print("Proceeding without showing cart.")
            print("================================")
            print('proceeding to address selection...')
            print("================================")
            address=input("Enter your delivery address: ")
            print('your order will be delivered to:',address)
            print("================================")
            print('proceeding to payment...')
            print("================================")
            payment_amount=sum(amount_stored)
            print("Your total payment amount is Rs.",payment_amount)
            payment_method=input("Enter your payment method (Credit Card, Debit Card, UPI, Net Banking, Cash on Delivery): ")
            if payment_method.lower() in ['credit card','debit card','upi','net banking']:
                print('proceeding to',payment_method,'payment gateway...')
                print('your payment gateway is ready.')
                print('Kindly click on the link below to complete your payment:')
                print('https://chetan-go.github.io/tech-gazer/payment%20link1.html')
                payment=input('enter done after completing your payment:')
                if payment.lower()=='done':
                    print('your payment has been received successfully!')
                    print('Thank you for shopping with Tech Gazer. Your order will be delivered within 7 days.')
                else:
                    print('payment not completed. please try again later.')
                    print("exiting....")
            elif payment_method.lower()=='cash on delivery':
                print('You have selected Cash on Delivery. Please keep the exact amount ready at the time of delivery.')
                print('Thank you for shopping with Tech Gazer. Your order will be delivered within 7 days.')
        bill=input("Would you like to see your final bill? (yes/no): ")
        if bill.lower()=='yes':
            print("================================")
            print("here is your Final Bill:")
            print("================================")
            print()
            print("="*width)
            S_no_width=5
            item_width=20
            cost_width=30
            specification_width=width - (S_no_width + item_width + cost_width + 15)
            header='S_No {:<{S_no_width}} Item {:<{item_width}} Specifications {:<{specification_width}} Cost (Rs) {:>{cost_width}}'.format("", "", "", "", S_no_width=S_no_width, item_width=item_width, specification_width=specification_width, cost_width=cost_width)
            print(header)
            print("="*width)
            total_amount=sum(amount_stored)
            j=1
            specification_list={}
            n=""
            for i in order_summary:
                specification_list={}
                for k in order_summary[i]:
                    if k != "category" and k != "Total Cost (Rs)":
                        specification_list[k]=order_summary[i][k]
                S_no=str(j)
                Item=order_summary[i]["category"]        
                cost=str(order_summary[i]['Total Cost (Rs)'])
                row_format='{:<{S_no_width}}  {:<{item_width}}  {:<{specification_width}}  {:>{cost_width}}'.format(S_no,Item,'',cost, S_no_width=S_no_width, item_width=item_width, specification_width=specification_width, cost_width=cost_width)
                print(row_format)
                j+=1
                for spec in specification_list:
                    specs_format='{:<{S_no_width}}  {:<{item_width}}  {:<{specification_width}}  {:>{cost_width}}'.format(" ", " ", spec+':'+specification_list[spec], " ", S_no_width=S_no_width, item_width=item_width, specification_width=specification_width, cost_width=cost_width)
                    print(specs_format)                       
        total_amount_format="{:>{cost__width}}".format("Total Amount (Rs): "+str(total_amount), cost__width=width-cost_width)
        print(total_amount_format)   