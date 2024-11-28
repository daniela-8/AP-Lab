class Book:
    def __init__(self, book_id, title, description, author):
        self.book = [book_id, title, description, author]
    
    def get_book_id(self):
        return self.book[0]
    
    def get_title(self):
        return self.book[1]
    
    def get_description(self):
        return self.book[2]
    
    def get_author(self):
        return self.book[3]
    
    def set_book_id(self, new_book_id):
        self.book[0] = new_book_id
    
    def set_title(self, new_title):
        self.book[1] = new_title
    
    def set_description(self, new_description):
        self.book[2] = new_description
    
    def set_author(self, new_author):
        self.book[3] = new_author
    
    def get_book(self):
        return self.book
    
    def __sub__(self, words_to_remove):
        if isinstance(words_to_remove, list):
            new_description = ' '.join(
                word for word in self.get_description().split() if word not in words_to_remove
            )
            return Book(self.get_book_id(), self.get_title(), new_description, self.get_author())
        return NotImplemented
    
    def __str__(self):
        return f"{self.book[0]} - {self.book[1]} - {self.book[2]} - {self.book[3]}"
