from utils.Book import Book

"""
In list storing and retrieving books from a list
"""

books = []
books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'w'):
        pass  # To ensure that the file is created


def add_book(name, author):
    new_book = Book(name, author, False)
    books.append(new_book)
    with open(books_file, 'a') as file:
        file.write(f"{new_book.name},{new_book.author},0\n")


def list_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    new_books = [Book(line[0], line[1], line[2]) for line in lines]
    return new_books


def mark_read(name):
    for book in books:
        if book.name == name:
            book.read = True

    # Using CSV
    new_books = list_books()
    for book in new_books:
        if book.name == name:
            book.read = '1'

    _save_all_books(new_books)


def _save_all_books(new_books):
    with open(books_file, 'w') as file:
        for book in new_books:
            file.write(f"{book.name},{book.author},0\n")


def delete_book(name):
    global books
    books = [book for book in books if book.name != name]

    # Delete book in file
    new_books = [book for book in list_books() if book.name != name]
    _save_all_books(new_books)
