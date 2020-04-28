from utils.Book import Book
from .database_connection import DatabaseConnection

"""
In list storing and retrieving books from a list
"""

books = []
books_file = 'books.txt'
database_location = 'data.db'


def create_book_table():
    with DatabaseConnection(database_location) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    # Create a File that saves data
    # with open(books_file, 'w'):
    #    pass  # To ensure that the file is created


def add_book(name, author):
    with DatabaseConnection(database_location) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    # Add a book into a file
    # new_book = Book(name, author, False)
    # books.append(new_book)
    # with open(books_file, 'a') as file:
    #     file.write(f"{new_book.name},{new_book.author},0\n")


def list_books():
    global books
    with DatabaseConnection(database_location) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT name, author, read FROM books')

        # Fetchall returns tuples => # [(name, author, read), (name, author, read)]
        books = [Book(row[0], row[1], row[2]) for row in cursor.fetchall()]
    return books

    # List all books from file
    # with open(books_file, 'r') as file:
    #     lines = [line.strip().split(',') for line in file.readlines()]
    #
    # new_books = [Book(line[0], line[1], line[2]) for line in lines]
    # return new_books


def mark_read(name):
    with DatabaseConnection(database_location) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    # Using Array
    # for book in books:
    #     if book.name == name:
    #         book.read = True

    # Using CSV
    # new_books = list_books()
    # for book in new_books:
    #     if book.name == name:
    #         book.read = '1'
    # _save_all_books(new_books)


def _save_all_books(new_books):
    with open(books_file, 'w') as file:
        for book in new_books:
            file.write(f"{book.name},{book.author},0\n")


def delete_book(name):
    with DatabaseConnection(database_location) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))

    # global books
    # books = [book for book in books if book.name != name]
    # Delete book in file
    # new_books = [book for book in list_books() if book.name != name]
    # _save_all_books(new_books)
