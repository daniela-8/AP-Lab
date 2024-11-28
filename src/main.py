from repository.book_repository import BookRepository
from repository.customer_repository import CustomerRepository
from ui.ui import UI

if __name__ == "__main__":
    bookRepository = BookRepository()
    customerRepository = CustomerRepository()
    ui = UI(bookRepository, customerRepository)
    ui.run()
