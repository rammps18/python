from utils import database

USER_MENU = """
'a' to add books,
'l' to list books,
'r' to mark book as read,
'd' to delete book
'q' to quit
Please enter valid option: """

database.create_books_table()


def menu():
    USER_INPUT = input(USER_MENU)
    while USER_INPUT != 'q':
        if USER_INPUT == 'a':
            prompt_add_book()
        elif USER_INPUT == 'l':
            view_books()
        elif USER_INPUT == 'r':
            prompt_read_book()
        elif USER_INPUT == 'd':
            prompt_delete_book()
        else:
            print(f"Enter the correct option")

        USER_INPUT=input(USER_MENU)


def prompt_add_book():
    name = input('Enter the name of the book: ')
    author = input('Enter the name of the author: ')

    database.add_book(name,author)


def view_books():
    books = database.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']} 'read':{book['read']}")


def prompt_read_book():
    name = input('Enter the name of the book: ')

    database.read_books(name)


def prompt_delete_book():
    name = input('Enter the name of the books you wish to delete: ')

    database.delete_books(name)


menu()




