class BookRepository:
    def __init__(self):
        self.book_repository = [] 
    
    def add_book(self, book):
        self.book_repository.append(book.get_book())
    
    def delete_book(self, book_id):
        for book in self.book_repository:
            if book[0] == book_id:
                self.book_repository.remove(book)
                return
        raise ValueError("Book not found")
    
    def get_books(self):
        return self.book_repository
    
    def update_book(self, new_book):
        for idx, book in enumerate(self.book_repository):
            if book[0] == new_book.get_book_id():
                self.book_repository[idx] = new_book.get_book()
                return
        raise ValueError("Book not found")
    
    def __str__(self):
        return '\n'.join(str(book) for book in self.book_repository)
