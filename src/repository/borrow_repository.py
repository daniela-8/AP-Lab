from domain.borrowing import Borrowing
from datetime import date

class BorrowRepository:
    def __init__(self):
        self.borrowings = []
        self.next_id = 1

    def _generate_borrowing_id(self):
        borrowing_id = self.next_id
        self.next_id += 1
        return borrowing_id

    def add_borrowing(self, borrowing):
        self.borrowings.append(borrowing)

    def create_borrowing(self, customer_id, book_id):
        borrowing_id = self._generate_borrowing_id()
        borrowing = Borrowing(borrowing_id, customer_id, book_id)
        self.add_borrowing(borrowing)
        return borrowing

    def return_book(self, borrowing_id):
        for borrowing in self.borrowings:
            if borrowing.borrowing_id == borrowing_id:
                if borrowing.return_date is not None:
                    raise ValueError("Book already returned.")
                borrowing.return_date = date.today()
                return
        raise ValueError("Borrowing record not found.")

    def get_borrowings(self):
        return self.borrowings

    def get_borrowings_by_customer(self, customer_id):
        return [b for b in self.borrowings if b.customer_id == customer_id]

    def get_borrowings_by_book(self, book_id):
        return [b for b in self.borrowings if b.book_id == book_id]

    def __str__(self):
        return '\n'.join(str(borrowing) for borrowing in self.borrowings)
