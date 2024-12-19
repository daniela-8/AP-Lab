from repository.book_repository import BookRepository
from repository.customer_repository import CustomerRepository
from repository.borrow_repository import BorrowRepository
from ui.ui import UI

if __name__ == "__main__":
    bookRepository = BookRepository()
    customerRepository = CustomerRepository()
    borrowRepository = BorrowRepository()
    ui = UI(bookRepository, customerRepository, borrowRepository)
    ui.run()
