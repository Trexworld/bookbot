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

def sort_on(dict):
    return dict["num"]

def get_sorted_chars_list(text):
    sorted_chars = []
    for c in text:
        list = {"key" : c}
        list["num"] = text[c]
        sorted_chars.append(list)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

def alpha(list):
    alpha_list = []
    for cha in list:
        if cha["key"].isalpha() == True:
            alpha_list.append(cha)
    return alpha_list