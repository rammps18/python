from utils import database

USER_CHOICE =  """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            pass
        elif user_input == 'r':
            pass
        else:
            print("Unknown command. Please try again.")





#def prompt_add_book()
# def list_books()
# def prompt_read_book()
# def prompt_delete_book()






