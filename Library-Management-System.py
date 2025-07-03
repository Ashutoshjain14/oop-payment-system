from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    @abstractmethod
    def get_info(self):
        pass

class Book(LibraryItem):
    def get_info(self):
        print(f"Book: {self.title} by {self.author} ({self.year})")

class Magazine(LibraryItem):
    def get_info(self):
        print(f"Magazine: {self.title} by {self.author} ({self.year})")

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    def show_all_items(self):
        for item in self.items:
            item.get_info()

    def start(self):
        while True:
            print("Please choose from the following options: ")
            print("1. Add Book")
            print("2. Add Magazine")
            print("3. Show All Items")
            print("4. Exit!")
            try:
                choice = int(input("Choose from options 1-4 : "))
            except ValueError:
                print("Please enter a valid number from 1-4.")
            else:
                if choice == 1:
                    title = input("Please enter the title of the book: ")
                    author = input("Please enter the name of the author: ")
                    year = input("Please enter the year in YYYY format: ")
                    item = Book(title, author, year)
                    self.add_item(item)
                elif choice == 2:
                    title = input("Please enter the title of the Magazine: ")
                    author = input("Please enter the name of the author: ")
                    year = input("Please enter the year in YYYY format: ")
                    item = Magazine(title, author, year)
                    self.add_item(item)
                elif choice == 3:
                    self.show_all_items()
                elif choice == 4:
                    print("Exiting!")
                    break
                else:
                    print("Please choose a valid option")


l = Library()
l.start()