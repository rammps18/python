from utils import database

USER_CHOICE="""
'a' to add book
'l' to list book
'r' to read book
'd' to delete book
'q' to quit
Enter your choice: """


def menu():
    USER_INPUT=input(USER_CHOICE)
    while USER_INPUT != 'q':
        if USER_INPUT == 'a':
            prompt_add_book()
        elif USER_INPUT == 'l':
            list_books()
        elif USER_INPUT == 'r':
            prompt_read_book()
        elif USER_INPUT == 'd':
            prompt_delete_book()
        else:
            print('Invalid choice. Please try again')

        USER_INPUT=input(USER_CHOICE)

def prompt_add_book():
    name = input("Enter the name of the book: ")
    author = input("Enter the name of the author")

    database.add_book(name,author)


def list_books():
    books = database.get_all_books()
    for book in books:
        print(f" {book['name']} by {book['author']} read is {book['read']}")

def prompt_read_book():
    name = input('Enter the name of the books you just finished reading: ')

    database.read_books(name)

def prompt_delete_book():
    name = input('Enter the name of the books you want to delete: ')

    database.delete_book(name)

menu()











