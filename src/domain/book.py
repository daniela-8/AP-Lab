# domain/book.py

class Book:
    def __init__(self, book_id, title, description, author):
        self._book_id = book_id
        self._title = title
        self._description = description
        self._author = author

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Book ID must be an integer.")
        self._book_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty.")
        self._description = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty.")
        self._author = value

    def get_book(self):
        return [self.book_id, self.title, self.description, self.author]

    def __str__(self):
        return f"{self.book_id} - {self.title} - {self.description} - {self.author}"
