import utils
import sorts
import numpy as np

"""
You recently began employment at “A Sorted Tale”, an independent 
bookshop. Every morning, the owner decides to sort the books in 
a new way.

Some of his favorite methods include:

* By author name
* By title
* By number of characters in the title
* By the reverse of the author’s name

Throughout the day, patrons of the bookshop remove books from 
the shelf. Given the strange ordering of the store, they do 
not always get the books placed back in exactly the correct location.

The owner wants you to research methods of fixing the book 
ordering throughout the day and sorting the books in the morning. 
It is currently taking too long!
"""


def by_title_ascending(book_a, book_b):
    if book_a["title_lower"] > book_b["title_lower"]:
        return True
    else:
        return False


def by_author_ascending(book_a, book_b):
    if book_a["author_lower"] > book_b["author_lower"]:
        return True
    else:
        return False


def by_total_length(book_a, book_b):
    return len(book_a["author_lower"]) + len(book_a["title_lower"]) > len(
        book_b["author_lower"]
    ) + len(book_b["title_lower"])


bookshelf = utils.load_books("books_small.csv")
long_bookshelf = utils.load_books("books_large.csv")

for book in bookshelf:
    print(book["title"])

print("\n")

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book["title"])

print("\n")

bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
    print(book["author"])

print("\n")

bookshelf_v2 = bookshelf.copy()
print(len(bookshelf_v2))
print(np.size(bookshelf_v2))
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
    print(book["author"])

print("\n")

# long_sort = sorts.bubble_sort(long_bookshelf, by_total_length)
# for book in long_sort:
# print(book["author"])

long_bookshelf_v1 = long_bookshelf.copy()
long_sort_1 = sorts.quicksort(
    long_bookshelf_v1, 0, len(long_bookshelf_v1) - 1, by_total_length
)

# string_caps = "MARLO"
# print(string_caps.lower())
