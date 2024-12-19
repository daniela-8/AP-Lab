from domain.book import Book
from domain.customer import Customer

class BookService:
    def __init__(self, bookRepository):
        self.bookRepository = bookRepository

    def add_book(self, book_id, title, description, author):
        books = self.bookRepository.get_books()
        for book in books:
            if book.book_id == book_id:
                raise ValueError("Book id must be unique")
        book = Book(book_id, title, description, author)
        self.bookRepository.add_book(book)

    def update_book(self, id, title, description, author):
        books = self.bookRepository.get_books()
        ids = [book.book_id for book in books]
        if id not in ids:
            raise ValueError("Book not found")
        new_book = Book(id, title, description, author)
        self.bookRepository.update_book(new_book)

    def delete_book(self, book_id):
        self.bookRepository.delete_book(book_id)

    def get_books(self):
        return self.bookRepository.get_books()

    def search_books_by_title(self, title):
        books = self.bookRepository.get_books()
        matched_books = []
        for book in books:
            if title.lower() in book.title.lower():
                matched_books.append(book)
        return matched_books

    def sort_books_by_author(self):
        books = self.bookRepository.get_books()
        sorted_books = sorted(books, key=lambda book: book.author.lower())
        return sorted_books


class CustomerService:
    def __init__(self, customerRepository):
        self.customerRepository = customerRepository

    def add_customer(self, customer_id, name, CNP):
        customers = self.customerRepository.get_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                raise ValueError("Customer id must be unique")
        customer = Customer(customer_id, name, CNP)
        self.customerRepository.add_customer(customer)

    def delete_customer(self, customer_id):
        self.customerRepository.remove_customer(customer_id)

    def get_customers(self):
        return self.customerRepository.get_customers()

    def update_customer(self, id, name, CNP):
        customers = self.customerRepository.get_customers()
        found = False
        for customer in customers:
            if customer.customer_id == id:
                found = True
                break
        if not found:
            raise ValueError("Customer not found")
        new_customer = Customer(id, name, CNP)
        self.customerRepository.update_customer(new_customer)

    def search_customers_by_name(self, name):
        customers = self.customerRepository.get_customers()
        matched_customers = [customer for customer in customers if name.lower() in customer.name.lower()]
        return matched_customers

    def sort_customers_by_CNP(self):
        customers = self.customerRepository.get_customers()
        sorted_customers = sorted(customers, key=lambda customer: customer.CNP)
        return sorted_customers
