from operations.operations import BookService, CustomerService

class UI():
    def __init__(self, bookRepository, customerRepository):
        self.bookService = BookService(bookRepository)
        self.customerService = CustomerService(customerRepository)

    def display_menu(self):
        print("Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Add customer")
        print("4. Remove customer")
        print("5. Display books")
        print("6. Display customers")
        print("7. Update book")
        print("8. Update customer")
        print("0. Exit")

    def run(self):
        self.bookService.add_book(1, "lord of the rings", "good", "idk")
        self.bookService.add_book(2,"harry potter", "excellent!", "j. k. rowling")
        self.bookService.add_book(3, "punguta cu doi bani", "mid", "someone")
        self.customerService.add_customer(1, "mihai", 1234)
        self.customerService.add_customer(2, "ioana", 4567)
        self.customerService.add_customer(3, "john", 7896)

        while True:

            self.display_menu()
            try:
                try:
                    command=int(input("Command:"))
                except:
                    raise ValueError("Command should be integer")

                if command==1:
                    id = int(input("Enter id:"))
                    title = input("Enter title:")
                    description = input("Enter description:")
                    author = input("Enter author:")
                    self.bookService.add_book(id, title, description, author)
                    print("Book added successfully!")
                elif command == 2:
                    id = int(input("Enter id:"))
                    self.bookService.delete_book(id)
                    print("Book deleted.")
                elif command == 3:
                    id = int(input("Enter id:"))
                    name = input("Enter name:")
                    CNP = int(input("Enter CNP:"))
                    self.customerService.add_customer(id, name, CNP)
                    print ("Customer added successfully!")
                elif command == 4:
                    id = int(input("Enter id:"))
                    self.customerService.delete_customer(id)
                    print("Customer deleted.")
                elif command == 5:
                    books = self.bookService.print_books()
                    for book in books:
                        print(book)
                elif command == 6:
                    customer = self.customerService.print_customers()
                    for customer in customer:
                        print(customer)
                elif command == 7:
                    book_id = int(input("Enter id to be updated:"))
                    title = input("Enter a title to be updated:")
                    description = input("Enter a description to be updated:")
                    author = input("Enter an author to be updated:")
                    self.bookService.update_book(book_id, title, description, author)
                elif command == 8:
                    customer_id = int(input("Enter id to be updated:"))
                    name = input("Enter a name to be updated:")
                    CNP = input("Enter a CNP to be updated:")
                    self.customerService.update_customer(customer_id, name, CNP)
                elif command==0:
                    print("Exited!")
                    break
            except ValueError as error:
                print(error)



