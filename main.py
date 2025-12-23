from stats import get_book_text, get_num_words, get_num_char, sort_on, chars_dict_to_sorted_list
path_to_file = "books/frankenstein.txt"
def main():
    text = get_book_text(path_to_file)
    get_num_char(text)

main()