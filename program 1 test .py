import shutil

def print_centered(text):
    width = shutil.get_terminal_size((80, 20)).columns
    for line in str(text).splitlines():
        print(line.center(width))

if __name__ == "__main__":
    print_centered("================================")
    print_centered("Welcome to Tech gazer!")
    print_centered("================================")
print("We offer a wide range of tech products to cater to your needs.")

a=input("Enter yes if u want to see all products available in our stores, No to continue and select your order:")
if a.lower() == "yes":
    print_centered("====================================================")
    print_centered("Here are all the products available in our stores:")
    print_centered("====================================================")
    print("Product 1: \t Phones and accessories")
    print("Product 2: \t Laptops and accessories")
    print("Product 3: \t Desktops and accessories")
    print("Product 4: \t Printers and scanners") 
    print('Product 5: \t wearable accessories')
    print("Product 6: \t Tv and accessories")
    print("Product 7: \t Audio devices and accessories")
    print("Product 8: \t Gaming consoles and accessories")
    print("Product 9: \t Smart home devices and accessories")
    print_centered("=======================================")
    print_centered("Proceeding to order selection...")
    print_centered("=======================================")
else:
    print_centered("================================")
    print_centered("Proceeding to order selection...")
    print_centered("================================")
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
print("9. Smart home devices and accessories")
reorder='yes'
order_quantity=0
phone_cost=15000
order_summary=[]
order = input("Enter the product number you wish to order (1-9): ")
while reorder=='yes':
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
                print_centered("=============================================================")
                print_centered("Here are the available accessories for your phone:")
                print_centered("=============================================================")
                print("accessories available:")
                print("1.Charger","price: Rs.500")
                print("2.Earphones","price: Rs.1000")
                print("3.Case","price: Rs.700")
                print("4.Screen Protector","price: Rs.300")
                phone_accessories=input("Enter the accessories you want (charger, earphones, case, ccreen protector, Enter all if all accessories needed): ").lower()
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
            phone_accessories='No accessories added'    
        print("-------------------------------------------------------------")
        print("You have ordered a Phone with the following specifications:")
        print('-------------------------------------------------------------')
        print(f"RAM Size: {phone_ram}")
        print(f"Storage Size: {phone_storage}")
        print(f"Display Type: {phone_display}")
        print(f"Color: {phone_color}")
        print(f"SIM Type: {phone_sim}")
        print(f"Accessories: {phone_accessories}")
        print("your total phone cost is Rs.",phone_cost)
        print(f"Your order quantity is: {order_quantity + 1}")
        reconformation=input("Do you want to confirm your order? (yes/no): ")
        if reconformation.lower()=='yes':
            order_quantity=order_quantity + 1
            print("Your order has been confirmed!")
            order_summary.append(f"Phone - RAM: {phone_ram}, Storage: {phone_storage}, Display: {phone_display}, Color: {phone_color}, SIM: {phone_sim}, Accessories: {phone_accessories}, Total Cost: Rs.{phone_cost}")
            reorder=input("Do you want to place another order? (yes/no): ")
        else:
            print("Your order has been cancelled.")
            reorder=("would you like to place a new order?(yes/no): ")
        if reorder.lower()=='yes':
            phone_cost=15000
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
                        print_centered("=============================================================")
                        print_centered("Here are the available accessories for your phone:")
                        print_centered("=============================================================")
                        print("accessories available:")
                        print("1.Charger","price: Rs.500")
                        print("2.Earphones","price: Rs.1000")
                        print("3.Case","price: Rs.700")
                        print("4.Screen Protector","price: Rs.300")
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
                    phone_accessories='No accessories added'
                print("-------------------------------------------------------------")
                print("You have ordered a Phone with the following specifications:")
                print('-------------------------------------------------------------')
                print(f"RAM Size: {phone_ram}")
                print(f"Storage Size: {phone_storage}")
                print(f"Display Type: {phone_display}")
                print(f"Color: {phone_color}")
                print(f"SIM Type: {phone_sim}")
                print(f"Accessories: {phone_accessories}")
                print("your total phone cost is Rs.",phone_cost)
                print(f"Your order quantity is: {order_quantity + 1}")
                reconformation=input("Do you want to confirm your order? (yes/no): ")
                if reconformation.lower()=='yes':
                    order_quantity=order_quantity+1
                    print("Your order has been confirmed!")
                    order_summary.append(f"Phone - RAM: {phone_ram}, Storage: {phone_storage}, Display: {phone_display}, Color: {phone_color}, SIM: {phone_sim}, Accessories: {phone_accessories}, Total Cost: Rs.{phone_cost}")
                    reorder=input("Do you want to place another order? (yes/no): ")
                else:
                    print("Your order has been cancelled.")
                    reorder=("would you like to place a new order?(yes/no): ")
else:
    print("here is your Order Summary:")
    print_centered("================================")
    print_centered("Order Summary")
    print_centered("================================")
    for i, j in enumerate(order_summary, start=1):
        print("===============")
        print(f"Order {i}:")
        print("===============")
        print(j)
        print()
import shutil

term_width = shutil.get_terminal_size((100, 20)).columns
no_w = 4
product_w = 15
cost_w = 12 
specs_w = term_width - (no_w + product_w + cost_w + 6)

order_conformation = input("Do you want to confirm all your orders? (yes/no): ")
if order_conformation.lower() == 'yes':
    print_centered("================================")
    print_centered("All your orders have been confirmed!")
    print_centered("Thank you for shopping with Tech Gazer.")
    print_centered("================================")

    bill_display = input("Would you like to display your bill? (yes/no): ")
    if bill_display.lower() == 'yes':
        print_centered("================================")
        print_centered("🧾 FINAL BILL 🧾")
        print_centered("================================")
        print()

        total_bill = 0
        print("-" * term_width)
        header = f"{'No.':<{no_w}}  {'Product':<{product_w}}  {'Specifications':<{specs_w}}  {'Cost (Rs)':>{cost_w}}"
        print(header)
        print("-" * term_width)

        for i, item in enumerate(order_summary, start=1):
            cost_index = item.rfind("Rs.")
            if cost_index == -1:
                cost_index = item.rfind("Rs")
            if cost_index != -1:
                raw_cost = ''.join(ch for ch in item[cost_index+3:] if ch.isdigit())
                item_cost = int(raw_cost) if raw_cost else 0
            else:
                item_cost = 0

            total_bill += item_cost

            if '-' in item:
                product_name, specs_str = item.split('-', 1)
                product_name = product_name.strip()
                specs_str = specs_str.strip()
            else:
                product_name = item[:product_w].strip()
                specs_str = item
            specs_parts = [s.strip() for s in specs_str.split(',') if s.strip()]
            first_spec = specs_parts[0] if specs_parts else ""
            spec_preview = first_spec
            left_part = f"{str(i):<{no_w}}  {product_name:<{product_w}}  {spec_preview:<{specs_w}}"
            right_part = f"{item_cost:>{cost_w}}"
            print(left_part + "  " + right_part)
            for extra in specs_parts[1:]:
                print(" " * (no_w + 2 + product_w) + f"  {extra:<{specs_w}}")
            print()

        print("-" * term_width)
        print(f"{'':<{no_w + product_w + specs_w + 4}}{'TOTAL: Rs.' + str(total_bill):>{cost_w}}")
        print("-" * term_width)
        print_centered("================================")
        print_centered("Thank you for shopping with Tech Gazer!")
        print_centered("Visit Again ❤️")
        print_centered("================================")
    else:
        print_centered("================================")
        print_centered("Thank you for shopping with Tech Gazer!")
        print_centered("Visit Again ❤️")
        print_centered("================================")
else:
    print_centered("================================")
    print_centered("Your orders were not confirmed.")
    print_centered("Visit Again ❤️")
    print_centered("================================")


