class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: Rs{self.price:.2f}")

    def discount(self, percent):
        self.price *= (1 - percent / 100)
        print(f"Discount applied. New price: Rs{self.price:.2f}")

book = Book("48 laws of power", "Robert Greene", 500.0)

book.display_details()
book.discount(8)
book.display_details()