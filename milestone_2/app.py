from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.add_book(name, author)


def list_books():
    for book in database.list_books():
        read = 'YES' if book.read == '1' else 'NO'
        print(f"{book.name} by {book.author} — Read: {read}")


def mark_book_read():
    name = input('Read this book: ')
    database.mark_read(name)


def delete_book():
    name = input('Delete this book: ')
    database.delete_book(name)


user_options = {
    "a": add_book,
    "l": list_books,
    "r": mark_book_read,
    "d": delete_book
}


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in user_options:
            selected_action = user_options[user_input]
            selected_action()
        else:
            print("Unknown Command. Please try again")

        user_input = input(USER_CHOICE)


menu()
