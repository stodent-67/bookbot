def get_num_words():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = len(text.split())
    print(f"Found {num_words} total words")