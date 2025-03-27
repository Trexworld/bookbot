from stats import get_book_words, words_sort

def main():
    print(f"""{get_book_words("books/frankenstein.txt")} words found in the document")
{words_sort("books/frankenstein.txt")}
""")

main()