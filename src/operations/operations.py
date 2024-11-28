from domain.book import Book
from domain.customer import Customer

class BookService:
    def __init__(self, bookRepository):
        self.bookRepository = bookRepository

    def add_book(self, book_id, title, description, author):
        books = self.bookRepository.get_books()
        for book in books:
            if book[0] == book_id:
                raise ValueError("Book id must be unique")
        book = Book(book_id, title, description, author)
        self.bookRepository.add_book(book)

    def update_book(self, id, title, description, author):
        books = self.bookRepository.get_books()
        ids = [book[0] for book in books]
        if id not in ids:
            raise ValueError("Book not found")
        new_book = Book(id, title, description, author)
        self.bookRepository.update_book(new_book)

    def delete_book(self, book_id):
        self.bookRepository.delete_book(book_id)

    def get_books(self):
        return self.bookRepository.get_books()

    def print_books(self):
        books = self.bookRepository.get_books()
        books_formatted = []
        for book_data in books:
            book = Book(*book_data)
            books_formatted.append(str(book))
        return books_formatted

    def search_books_by_title(self, search_term):
        books = self.bookRepository.get_books()
        matched_books = []
        for book_data in books:
            if search_term.lower() in book_data[1].lower():
                matched_books.append(book_data)
        return matched_books

    def sort_books_by_author(self):
        books = self.bookRepository.get_books()
        sorted_books = sorted(books, key=lambda book: book[3].lower())
        return sorted_books
    
    def find_equal_books(self, input_book):
        books = self.bookRepository.get_books()
        equal_books = []
        for book_data in books:
            book = Book(*book_data)
            if book == input_book and book.get_book_id() != input_book.get_book_id():
                equal_books.append(book)
        return equal_books

    def find_book_by_id(self, book_id):
        books = self.bookRepository.get_books()
        for book_data in books:
            if book_data[0] == book_id:
                return Book(*book_data)
        raise ValueError("Book not found")


class CustomerService:
    def __init__(self, customerRepository):
        self.customerRepository = customerRepository

    def add_customer(self, customer_id, name, CNP):
        customers = self.customerRepository.get_customers()
        for customer in customers:
            if customer[0] == customer_id:
                raise ValueError("Customer id must be unique")
        customer = Customer(customer_id, name, CNP)
        self.customerRepository.add_customer(customer)

    def delete_customer(self, customer_id):
        self.customerRepository.remove_customer(customer_id)

    def get_customers(self):
        return self.customerRepository.get_customers()

    def print_customers(self):
        customers = self.customerRepository.get_customers()
        customers_formatted = []
        for customer_data in customers:
            customer = Customer(*customer_data)
            customers_formatted.append(str(customer))
        return customers_formatted

    def update_customer(self, id, name, CNP):
        customers = self.customerRepository.get_customers()
        found = False
        for customer in customers:
            if customer[0] == id:
                found = True
                break
        if not found:
            raise ValueError("Customer not found")
        new_customer = Customer(id, name, CNP)
        self.customerRepository.update_customer(new_customer)

    def search_customers_by_name(self, search_term):
        customers = self.customerRepository.get_customers()
        matched_customers = [customer for customer in customers if search_term.lower() in customer[1].lower()]
        return matched_customers

    def sort_customers_by_CNP(self):
        customers = list(self.customerRepository.get_customers())
        sorted_customers = sorted(customers, key=lambda customer: customer[2])
        return sorted_customers
