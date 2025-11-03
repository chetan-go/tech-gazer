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
    print("Laptops and accessories")
    print("Desktops and accessories")
    print("printers and scanners")
    print(' wearable accessories')
    print("Tv and accessories")
    print("Audio devices and accessories")
    print("Gaming consoles and accessories")
    print("Smart home devices and accessories")
    print("Proceeding to order selection...")
else:
    print("Proceeding to order selection...")