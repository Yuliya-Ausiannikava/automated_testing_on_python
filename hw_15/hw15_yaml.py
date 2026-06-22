"""
A program that reads data from a file and allows the user to add new books to the file.
"""

from pprint import pprint
import yaml

info_books = {
    1: {
        "name": "Gone with the Wind",
        "author": "Margaret Munnerlyn Mitchell",
        "year": 1936
    },
    2: {
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813
    },
    3: {
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    }
}

with open("info_about_books.yaml", 'w', encoding='utf-8') as book_file:
    yaml.dump(info_books, book_file)


# Reads a file
def read_yaml(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data_books = yaml.safe_load(f)
            pprint(data_books, width=50)
            return data_books
    except FileNotFoundError:
        print("File not found")
        return {}


# Adding a book to a file
def add_books(book_name, author, year, file_name):
    books_from_file = read_yaml(file_name)
    if books_from_file:
        next_id = max(books_from_file.keys()) + 1
    else:
        next_id = 1

    books_from_file[next_id] = {
        "name": book_name,
        "author": author,
        "year": year
    }

    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(books_from_file, file)
        print(f'\nThe book "{book_name}" has been added to the file.\n')
    return books_from_file[next_id]


add_books("The Great Gatsby", "Francis Scott Fitzgerald", 1925, "info_about_books.yaml")
read_yaml("info_about_books.yaml")
