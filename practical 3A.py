# Creating a class book.
class Book:

    # Creating a function for accepting details of a book
    def accept_details(self):
        self.book_name = input("Enter name of the book:")
        self.book_author = input("Enter the author of the book:")
        self.book_price = int(input("Enter the price of the book:"))
        self.no_of_copies = int(input("Enter number of copies:"))
     
    # Calculating total price.
    def total_price(self):
        print(f"The total price is :{self.b_price * self.no_of_copies}")
    
    # Displaying details
    def details(self):
        print(f"The name of the book is :{self.book_name}")
        print(f"The author of the book is :{self.book_author}")
        print(f"The price of the book is :{self.book_price}")


book_object = Book()  # Creating an object for book.
book_object.accept_details()  # Calling the method for accepting details.

while True:
    
    print("1.Total price")
    print("2.Display details")
    print("3.quit")

    # Creating option system to call methods
    option = int(input("Enter option:"))  # User can enter options to navigate throught the functions.
    if option == 1:
        book_object.total_price()
    elif option ==2:
        book_object.details()
    elif option == 3:
        break
