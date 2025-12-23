from stats import get_book_text, get_num_words, get_num_char, sort_on, chars_dict_to_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def main():
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    dict = get_num_char(text)
    sorted_dict = chars_dict_to_sorted_list(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_dict:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()