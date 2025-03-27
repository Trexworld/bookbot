def get_book_text(book):
    with open(book) as f:
        file_contend = f.read()
    return file_contend

def get_book_words(book):
    book_text = get_book_text(book)
    words = book_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def character_per_book(book):
    book_text = get_book_text(book)
    words = book_text.lower()
    lower_words = words.split()
    character = {}
    for words in lower_words:
        for word in words:
            if word in character:
                character[word] += 1
            else:
                character[word] = 1
    return character

def words_sort(book):
    character = character_per_book(book)
    sorted_character = sorted(character.items(),reverse=True, key=lambda x:x[1])
    return sorted_character