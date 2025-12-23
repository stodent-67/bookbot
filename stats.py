def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = len(text.split())
    print(f"Found {num_words} total words")