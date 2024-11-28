
class BookRepository:
    def __init__(self):
        self.book_repository = []

    def add_book(self, book):
        self.book_repository.append(book)

    def delete_book(self, book):
        self.book_repository.remove(book)


    def get_books(self):
        return self.book_repository

    def update_book(self, new_book):
        for book in self.book_repository:
            if book.get_book_id() == new_book.get_book_id():
                book.set_title(new_book.get_title())
                book.set_description(new_book.get_description())
                book.set_author(new_book.get_author())


    def __str__(self):
        return '\n'.join(str(book) for book in self.book_repository)
