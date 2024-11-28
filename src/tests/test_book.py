import unittest
from domain.book import Book
from repository.book_repository import BookRepository
from operations.operations import BookService


class TestBook(unittest.TestCase):

    def test_book_initialization(self):
        book = Book(1, "Title", "Description", "Author")
        self.assertEqual(book.get_book_id(), 1)
        self.assertEqual(book.get_title(), "Title")
        self.assertEqual(book.get_description(), "Description")
        self.assertEqual(book.get_author(), "Author")

    def test_book_setters(self):
        book = Book(1, "Title", "Description", "Author")
        book.set_book_id(2)
        book.set_title("New Title")
        book.set_description("New Description")
        book.set_author("New Author")
        self.assertEqual(book.get_book_id(), 2)
        self.assertEqual(book.get_title(), "New Title")
        self.assertEqual(book.get_description(), "New Description")
        self.assertEqual(book.get_author(), "New Author")


class TestBookRepository(unittest.TestCase):

    def setUp(self):
        self.repository = BookRepository()

    def test_add_book(self):
        book = Book(1, "Title", "Description", "Author")
        self.repository.add_book(book)
        self.assertIn(book, self.repository.get_books())

    def test_delete_book(self):
        book = Book(1, "Title", "Description", "Author")
        self.repository.add_book(book)
        self.repository.delete_book(book)
        self.assertNotIn(book, self.repository.get_books())

    def test_update_book(self):
        book = Book(1, "Title", "Description", "Author")
        self.repository.add_book(book)
        updated_book = Book(1, "New Title", "New Description", "New Author")
        self.repository.update_book(updated_book)
        books = self.repository.get_books()
        self.assertEqual(books[0].get_title(), "New Title")
        self.assertEqual(books[0].get_description(), "New Description")
        self.assertEqual(books[0].get_author(), "New Author")


class TestBookService(unittest.TestCase):

    def setUp(self):
        self.repository = BookRepository()
        self.service = BookService(self.repository)

    def test_add_book_success(self):
        self.service.add_book(1, "Title", "Description", "Author")
        books = self.service.print_books()
        self.assertIn("1 - Title - Description - Author", books)

    def test_add_book_duplicate_id(self):
        self.service.add_book(1, "Title", "Description", "Author")
        with self.assertRaises(ValueError):
            self.service.add_book(1, "Another Title", "Another Description", "Another Author")

    def test_delete_book_success(self):
        self.service.add_book(1, "Title", "Description", "Author")
        self.service.delete_book(1)
        books = self.service.print_books()
        self.assertNotIn("1 - Title - Description - Author", books)

    def test_delete_book_not_found(self):
        with self.assertRaises(ValueError):
            self.service.delete_book(99)

    def test_update_book_success(self):
        self.service.add_book(1, "Title", "Description", "Author")
        self.service.update_book(1, "Updated Title", "Updated Description", "Updated Author")
        books = self.service.print_books()
        self.assertIn("1 - Updated Title - Updated Description - Updated Author", books)

    def test_update_book_not_found(self):
        with self.assertRaises(ValueError):
            self.service.update_book(99, "Title", "Description", "Author")


if __name__ == "__main__":
    unittest.main()
