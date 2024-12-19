

class BorrowService:
    def __init__(self, borrowRepository, bookRepository, customerRepository):
        self.borrowRepository = borrowRepository
        self.bookRepository = bookRepository
        self.customerRepository = customerRepository

    def borrow_book(self, customer_id, book_id):
        books = self.bookRepository.get_books()
        book = next((b for b in books if b.book_id == book_id), None)
        if not book:
            raise ValueError("Book not found.")

        customers = self.customerRepository.get_customers()
        customer = next((c for c in customers if c.customer_id == customer_id), None)
        if not customer:
            raise ValueError("Customer not found.")

        active_borrowings = [b for b in self.borrowRepository.get_borrowings()
                             if b.book_id == book_id and b.return_date is None]
        if active_borrowings:
            raise ValueError("Book is already borrowed and not yet returned.")

        borrowing = self.borrowRepository.create_borrowing(customer_id, book_id)
        return borrowing

    def return_book(self, borrowing_id):
        self.borrowRepository.return_book(borrowing_id)

    def get_all_borrowings(self):
        return self.borrowRepository.get_borrowings()

    def get_borrowings_by_customer(self, customer_id):
        return self.borrowRepository.get_borrowings_by_customer(customer_id)

    def get_borrowings_by_book(self, book_id):
        return self.borrowRepository.get_borrowings_by_book(book_id)
