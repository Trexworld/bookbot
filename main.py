from stats import get_book_text, get_num_words, get_chars_dict, get_sorted_chars_list, alpha

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_sorted_chars_list(chars_dict)
    sorted_letter_list = alpha(chars_list)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for i in range(len(sorted_letter_list)):
        print(f"{sorted_letter_list[i]["key"]}: {sorted_letter_list[i]["num"]}")

main()