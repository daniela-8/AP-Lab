from operations.operations import BookService, CustomerService
from domain.book import Book
from domain.customer import Customer

class UI:
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
        print("9. Search books by title")
        print("10. Sort books by author")
        print("11. Search customers by name")
        print("12. Sort customers by CNP")
        print("0. Exit")

    def run(self):
        self.bookService.add_book(1, "Lord of the Rings", "An epic fantasy novel", "J.R.R. Tolkien")
        self.bookService.add_book(2, "Harry Potter", "A wizard's journey", "J.K. Rowling")
        self.bookService.add_book(3, "Punguta cu doi bani", "A classic tale", "Ion Creangă")
        self.customerService.add_customer(1, "Mihai", 1234)
        self.customerService.add_customer(2, "Ioana", 4567)
        self.customerService.add_customer(3, "John", 7896)

        while True:
            self.display_menu()
            try:
                command = int(input("Command: "))
                if command == 1:
                    id = int(input("Enter id: "))
                    title = input("Enter title: ")
                    description = input("Enter description: ")
                    author = input("Enter author: ")
                    self.bookService.add_book(id, title, description, author)
                    print("Book added successfully!")
                elif command == 2:
                    id = int(input("Enter id: "))
                    self.bookService.delete_book(id)
                    print("Book deleted.")
                elif command == 3:
                    id = int(input("Enter id: "))
                    name = input("Enter name: ")
                    CNP = int(input("Enter CNP: "))
                    self.customerService.add_customer(id, name, CNP)
                    print("Customer added successfully!")
                elif command == 4:
                    id = int(input("Enter id: "))
                    self.customerService.delete_customer(id)
                    print("Customer deleted.")
                elif command == 5:
                    books = self.bookService.get_books()
                    for book in books:
                        print(book)
                elif command == 6:
                    customers = self.customerService.get_customers()
                    for customer in customers:
                        print(customer)
                elif command == 7:
                    book_id = int(input("Enter id to be updated: "))
                    title = input("Enter new title: ")
                    description = input("Enter new description: ")
                    author = input("Enter new author: ")
                    self.bookService.update_book(book_id, title, description, author)
                    print("Book updated successfully!")
                elif command == 8:
                    customer_id = int(input("Enter id to be updated: "))
                    name = input("Enter new name: ")
                    CNP = int(input("Enter new CNP: "))
                    self.customerService.update_customer(customer_id, name, CNP)
                    print("Customer updated successfully!")
                elif command == 9:
                    search_term = input("Enter title to search for: ")
                    matched_books = self.bookService.search_books_by_title(search_term)
                    for book_data in matched_books:
                        book = Book(*book_data)
                        print(book)
                elif command == 10:
                    sorted_books = self.bookService.sort_books_by_author()
                    for book_data in sorted_books:
                        book = Book(*book_data)
                        print(book)
                elif command == 11:
                    search_term = input("Enter name to search for: ")
                    matched_customers = self.customerService.search_customers_by_name(search_term)
                    for customer_data in matched_customers:
                        customer = Customer(*customer_data)
                        print(customer)
                elif command == 12:
                    sorted_customers = self.customerService.sort_customers_by_CNP()
                    for customer_data in sorted_customers:
                        customer = Customer(*customer_data)
                        print(customer)
                elif command == 0:
                    print("Exited!")
                    break
                else:
                    print("Invalid command. Please try again.")
            except ValueError as error:
                print(f"Error: {error}")
