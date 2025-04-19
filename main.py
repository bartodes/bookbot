from stats import get_number_words,get_number_char,sort_number_char
from sys import argv,exit

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    path = argv[1]
    print(f"""============ BOOKBOT ============\nAnalyzing book found at {path}...""")
    contents = get_book_text(path)
    # print(contents)
    print("----------- Word Count ----------")
    num_words = get_number_words(contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_number_char(contents)
    # print(num_chars)
    sorted_num_chars = sort_number_char(num_chars)
    for char_count in sorted_num_chars:
        print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()