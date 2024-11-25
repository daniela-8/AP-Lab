from domain.book import Book
from domain.customer import Customer
from repository.book_repository import BookRepository
from repository.customer_repository import CustomerRepository



c = Customer(1, "Lotsico", "1234")

customer_repository = CustomerRepository()

b = Book(1, "Harry Potter", "Magie", "J.K. Rowling")
book_repository = BookRepository()
book_repository.add_book(b)

#This should print the book details, not the memory address
print(book_repository)
