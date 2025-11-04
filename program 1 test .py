import shutil

def print_centered(text):
    width = shutil.get_terminal_size((80, 20)).columns
    for line in str(text).splitlines():
        print(line.center(width))

if __name__ == "__main__":
    print_centered("Welcome to Tech gazer!")

a=input("Enter yes if u want to see all products available in our stores, No to continue and select your order:")
if a.lower() == "yes":
    print("Here are all the products available in our stores:")
    print("Product 1: Phones and accessories")
    print("Product 2: Laptops and accessories")
    print("Product 3: Desktops and accessories")
    print("Product 4: Printers and scanners") 
    print('Product 5: wearable accessories')
    print("Product 6: Tv and accessories")
    print("Product 7: Audio devices and accessories")
    print("Product 8: Gaming consoles and accessories")
    print("Product 9: Smart home devices and accessories")
    print("Proceeding to order selection...")
else:
    print("Proceeding to order selection...")
print("Please select your order from the following options:")
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
order_number=0
order_summary=[]
order = input("Enter the product number you wish to order (1-9): ")
while reorder=='yes':
    if order == '1':
        print("You have selected Phones and accessories.")
        phone_ram=input("Enter the RAM size you want (4GB, 6GB, 8GB, 12GB): ")
        phone_storage=input("Enter the storage size you want (64GB, 128GB, 256GB, 512GB): ")
        phone_display=input("Enter the display type you want (LCD, AMOLED): ")
        phone_color=input("Enter the color you want (Black, White, Blue, Red): ")
        phone_sim=input("Enter the SIM type you want (Single SIM / Dual SIM): ")
        phone_accessories=input("Enter the accessories you want (Charger, Earphones, Case, Screen Protector,Enter all if all accessories needed and no if no accesories needed): ")
        print("You have ordered a Phone with the following specifications:")
        print(f"RAM Size: {phone_ram}")
        print(f"Storage Size: {phone_storage}")
        print(f"Display Type: {phone_display}")
        print(f"Color: {phone_color}")
        print(f"SIM Type: {phone_sim}")
        print(f"Accessories: {phone_accessories}")
        print(f"Your order quantity is: {order_number + 1}")
        print('cost of phone is Rs.30000')
        reconformation=input("Do you want to confirm your order? (yes/no): ")
        if reconformation.lower()=='yes':
            order_number=order_number + 1
            print("Your order has been confirmed!")
            order_summary.append(f"Order {order_number}: Phone - RAM: {phone_ram}, Storage: {phone_storage}, Display: {phone_display}, Color: {phone_color}, SIM: {phone_sim}, Accessories: {phone_accessories}")
            reorder=input("Do you want to place another order? (yes/no): ")
        else:
            print("Your order has been cancelled.")
            print("would you like to place a new order?")
        if reorder.lower()=='yes':
            order = input("Enter the product number you wish to order (1-9): ")
            if order == '1':
                print("You have selected Phones and accessories.")
                phone_ram=input("Enter the RAM size you want (4GB, 6GB, 8GB, 12GB): ")
                phone_storage=input("Enter the storage size you want (64GB, 128GB, 256GB, 512GB): ")
                phone_display=input("Enter the display type you want (LCD, AMOLED): ")
                phone_color=input("Enter the color you want (Black, White, Blue, Red): ")
                phone_sim=input("Enter the SIM type you want (Single SIM / Dual SIM): ")
                phone_accessories=input("Enter the accessories you want (Charger, Earphones, Case, Screen Protector,Enter all if all accessories needed and no if no accesories needed): ")
                print("You have ordered a Phone with the following specifications:")
                print(f"RAM Size: {phone_ram}")
                print(f"Storage Size: {phone_storage}")
                print(f"Display Type: {phone_display}")
                print(f"Color: {phone_color}")
                print(f"SIM Type: {phone_sim}")
                print(f"Accessories: {phone_accessories}")
                print(f"Your order quantity is: {order_number + 1}")
                print('cost of phone is Rs.30000')
                reconformation=input("Do you want to confirm your order? (yes/no): ")
                if reconformation.lower()=='yes':
                    order_number=order_number+1
                    print("Your order has been confirmed!")
                    order_summary.append(f"Order {order_number}: Phone - RAM: {phone_ram}, Storage: {phone_storage}, Display: {phone_display}, Color: {phone_color}, SIM: {phone_sim}, Accessories: {phone_accessories}")
                    reorder=input("Do you want to place another order? (yes/no): ")
                else:
                    print("Your order has been cancelled.")
                    print("would you like to place a new order?")
else:
    print("here is your Order Summary:")
    for summary in order_summary:
        print(summary,sep='\n')
    print("Thank you for your order!")           
