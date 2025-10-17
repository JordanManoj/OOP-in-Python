

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def get_total(self):
        return sum(item.total_price() for item in self.items)

    def __str__(self):
        cart_contents = "Cart Contents:\n"
        for item in self.items:
            cart_contents += f"{item.name} x {item.quantity} = Rs{item.total_price():.2f}\n"
        cart_contents += f"Total: Rs{self.get_total():.2f}"
        return cart_contents


item1 = Item("Milk",1.00, 5)
item2 = Item("Banana", 0.50, 3)
cart = Cart()
cart.add_item(item1)
cart.add_item(item2)
print(cart)
cart.remove_item("Milk")
print("\nAfter removing:")
print(cart)