from stats import get_book_text, get_num_words, get_chars_dict, get_sorted_chars_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_sorted_chars_list(chars_dict)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{chars_list}""")

main()