class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self):
        return sum(product.price * product.quantity for product in self.products)

    def display_products(self):
        for product in self.products:
            print(f"Name: {product.name}, Price: Rs{product.price:.2f}, Quantity: {product.quantity}")
        print(f"Total Value: Rs{self.total_value():.2f}")

product1 = Product("S25", 71000, 5)
product2 = Product("Nothing 3a", 35000, 10)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.display_products()
