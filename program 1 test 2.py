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
            S_no_width=4
            item_width=20
            cost_width=90
            specification_width=width - (S_no_width + item_width + cost_width+9)
            header='S_No {:<{S_no_width}}  Item {:<{item_width}}  Specifications {:<{specification_width}}  Cost (Rs) {:>{cost_width}}'.format("", "", "", "", S_no_width=S_no_width, item_width=item_width, specification_width=specification_width, cost_width=cost_width)
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
            total_amount_format="{:>{cost__width}}".format("Total Amount (Rs): "+str(total_amount), cost__width=cost_width)
            print(total_amount_format)   