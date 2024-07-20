import csv


# This code loads the current book
# shelf data from the csv file
def load_books(filename):
    bookshelf = []
    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            # add your code here
            # This code is converting the 'author' and 'title' values of 
            # each book to lowercase and storing them in new dic keys.
            # This makes searching or comparing these values easier
            # by standardizing the text format.
            book["author_lower"] = book["author"].lower()
            book["title_lower"] = book["title"].lower()
            bookshelf.append(book)

    return bookshelf
