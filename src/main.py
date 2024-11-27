from domain.book import Book
from domain.customer import Customer
from repository.book_repository import BookRepository
from repository.customer_repository import CustomerRepository
from ui.ui import UI



bookRepository = BookRepository()
customerRepository = CustomerRepository()
ui = UI(bookRepository, customerRepository)

ui.run()