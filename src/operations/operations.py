
from domain.book import Book
from domain.customer import Customer
class BookService:
    def __init__(self, bookRepository):
        self.bookRepository=bookRepository

    def add_book(self, book_id, title, description, author):
        try:
            books=self.bookRepository.get_books()
            for book in books:
                if book.get_book_id()==book_id:
                    raise ValueError
            book = Book(book_id, title, description, author)
            self.bookRepository.add_book(book)
        except:
            raise ValueError("Book id must be unique")

    def update_book(self, id, title, description, author):
        try:
            books = self.bookRepository.get_books()
            ids = []
            for book in books:
                ids.append(book.get_book_id())
            if not id in ids:
                raise ValueError
            book = Book(id, title, description, author)
            self.bookRepository.update_book(book)
        except:
            raise ValueError("Book not found!")


    def delete_book(self, book_id):
        try:
            books = self.bookRepository.get_books()
            found = False
            for book in books:
                if book.get_book_id() == book_id:
                    self.bookRepository.delete_book(book)
                    found = True
            if not found:
                raise ValueError
        except:
            raise ValueError("Book not found to be deleted")


    def get_books(self):
        self.bookRepository.get_books()

    def print_books(self):
        books=self.bookRepository.get_books()
        books_formated = []
        for book in books:
            books_formated.append(str(book))
        return books_formated


class CustomerService:
    def __init__(self, customerRepository):
        self.customerRepository=customerRepository

    def add_customer(self, customer_id, name, CNP):
        try:
            customers=self.customerRepository.get_customers()
            for customer in customers:
                if customer.get_id()==customer_id:
                    raise ValueError
            customer = Customer(customer_id, name, CNP)
            self.customerRepository.add_customer(customer)
        except:
            raise ValueError("Customer id must be unique")


    def delete_customer(self, customer_id):
        try:
            customers=self.customerRepository.get_customers()
            found = False
            for customer in customers:
                if customer.get_id()==customer_id:
                    self.customerRepository.remove_customer(customer)
                    found = True
            if not found:
                raise ValueError
        except:
            raise ValueError("Customer not found")

    def get_customers(self):
        self.customerRepository.get_customers()

    def print_customers(self):
        customers=self.customerRepository.get_customers()
        customers_formated = []
        for customer in customers:
            customers_formated.append(str(customer))

        return customers_formated

    def update_customer(self, id, name, CNP):
        try:
            customers = self.customerRepository.get_customers()
            ids = []
            for customer in customers:
                ids.append(customer.get_id())
            if not id in ids:
                raise ValueError
            customer = Customer(id, name, CNP)
            self.customerRepository.update_customer(customer)
        except:
            raise ValueError("Customer not found")

