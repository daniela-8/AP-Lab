from datetime import date

class Borrowing:
    def __init__(self, borrowing_id, customer_id, book_id, borrow_date=None, return_date=None):
        self.borrowing_id = borrowing_id
        self.customer_id = customer_id
        self.book_id = book_id
        self.borrow_date = borrow_date if borrow_date else date.today()
        self.return_date = return_date

    def __str__(self):
        return (f"Borrowing ID: {self.borrowing_id}, Customer ID: {self.customer_id}, "
                f"Book ID: {self.book_id}, Borrow Date: {self.borrow_date}, "
                f"Return Date: {self.return_date if self.return_date else 'Not Returned'}")
