class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"Borrowed '{book.title}' by {book.author}")
                return
        print(f"'{title}' is not available or does not exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f"Returned '{book.title}' by {book.author}")
                return
        print(f"'{title}' is already available or does not exist.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"'{book.title}' by {book.author}")
        else:
            print("No books are available.")

library = Library()
book1 = Book("How to kill overthinking", "Random 1")
book2 = Book("1999", "Random 2")
book3 = Book("Pride and Prejudice", "Jane Austen")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.list_available_books()
library.borrow_book("How to kill overthinking")
library.borrow_book("1984")
library.list_available_books()
library.return_book("How to kill overthinking")
library.list_available_books()