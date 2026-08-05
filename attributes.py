# Attributes Example in Python

class Laptop:

    def __init__(self, brand, ram, storage):
        # Instance Attributes
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def show_details(self):
        print("----- Laptop Details -----")
        print(f"Brand   : {self.brand}")
        print(f"RAM     : {self.ram} GB")
        print(f"Storage : {self.storage} GB")
        print()


# Creating Objects
laptop1 = Laptop("HP", 8, 512)
laptop2 = Laptop("Dell", 16, 1024)
laptop3 = Laptop("Lenovo", 32, 512)

# Accessing Attributes
print(laptop1.brand)
print(laptop2.ram)
print(laptop3.storage)
print()

# Calling Method
laptop1.show_details()
laptop2.show_details()
laptop3.show_details()