def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_chars_list(text):
    new = []
    for c in text:
        list = [{"key" : c}]
        list[0]["num"] = text[c]
        new.append(list)
    return new