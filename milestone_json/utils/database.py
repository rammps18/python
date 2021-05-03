import json
"""
Concerned about storing and retrieving books using json
"""
books_file = 'books.json'


def create_books_table():
    with open(books_file,'w') as file:
        json.dump([], file)


def add_book(name,author):
    books = get_all_books()
    books.append({'name': name,'author': author,'read': False})
    _save_all_books(books)


def get_all_books():
    with open(books_file,'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books,file)


def read_books(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True

    _save_all_books(books)


def delete_books(name):
    books = get_all_books()
    books = [books for book in books if book['name'] != name ]
    _save_all_books(books)






