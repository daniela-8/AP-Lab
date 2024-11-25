
class Book:
    def __init__(self, book_id, title, description, author):
        self.book_id = book_id
        self.title = title
        self.description = description
        self.author = author

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    def get_author(self):
        return self.author

    def set_book_id(self, new_book_id):
        self.book_id = new_book_id

    def set_title(self, new_title):
        self.title = new_title

    def set_description(self, new_description):
        self.description = new_description

    def set_author(self, new_author):
        self.author = new_author

    def __str__(self):
        return f"{self.book_id} - {self.title} - {self.description} - {self.author}"
