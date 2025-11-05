
class Publisher:
    def __init__(self, name):
        self.name = name
        print("Publisher constructor called")

    def display_info(self):
        print(f"Publisher Name: {self.name}")



class Book(Publisher):
    def __init__(self, name, title, author, price):
        
        super().__init__(name)
        self.title = title
        self.author = author
        self.price = price
        print("Book constructor called")


    def display_info(self):
        
        super().display_info()
        
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")



book1 = Book("Penguin Random House", "1984", "George Orwell", 15.99)
print("\nDisplaying Book Information:")
book1.display_info()
