
class BookRepository:
    def __init__(self):
        self.book_repository = []

    def add_book(self, book):
        self.book_repository.append(book)

    def delete_book(self, book):
        self.book_repository.remove(book)

    def get_books(self):
        return self.book_repository

    def __str__(self):
        return '\n'.join(str(book) for book in self.book_repository)
