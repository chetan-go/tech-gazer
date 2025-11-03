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
    print("Product 1: Tech Gadget A")
    print("Product 2: Tech Gadget B")
    print("Product 3: Tech Gadget C")
else:
    print("Proceeding to order selection...")