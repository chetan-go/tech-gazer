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
    print("Product 10: Proceeding to order selection...")
else:
    print("Proceeding to order selection...")