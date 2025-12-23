path_to_file = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
     
text = get_book_text(path_to_file)

def get_num_words():
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def get_num_char(text):
    num_char = {}
    for ch in text:
        ch = str.lower(ch)
        if ch in num_char:
            num_char[ch] = num_char[ch] + 1
        else:
            num_char[ch] = 1
    return num_char

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_char):
    new_list = []
    for key in num_char:
        new_list.append({"char": key, "num": num_char[key]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list