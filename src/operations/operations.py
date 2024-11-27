from domain.book import Book
from domain.customer import Customer
class BookService:
    def __init__(self, bookRepository):
        self.bookRepository=bookRepository

    def add_book(self, book_id, title, description, author):
        book= Book(book_id, title, description, author)
        self.bookRepository.add_book(book)

    def delete_book(self, book_id):
        books=self.bookRepository.get_books()
        for book in books:
            if book.get_book_id()==book_id:
                self.bookRepository.delete_book(book)

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
        customer = Customer(customer_id, name, CNP)
        self.customerRepository.add_customer(customer)

    def delete_customer(self, customer_id):
        customers=self.customerRepository.get_customers()
        for customer in customers:
            if customer.get_id()==customer_id:
                self.customerRepository.remove_customer(customer)

    def get_customers(self):
        self.customerRepository.get_customers()

    def print_customers(self):
        customers=self.customerRepository.get_customers()
        customers_formated = []
        for customer in customers:
            customers_formated.append(str(customer))

        return customers_formated

