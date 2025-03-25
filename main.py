from stats import get_book_words
from stats import character_per_book

def main():
    print(f"{get_book_words("books/frankenstein.txt")} words found in the document")
    print(character_per_book("books/frankenstein.txt"))

main()