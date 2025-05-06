import sys

def get_book_text(book):
    # print("got book")
    contents = ""
    with open(book) as f:
        contents = f.read()
    return contents

from stats import word_count
from stats import character_count
from stats import sort_characters

def report(word_count, characters):
    print("============ BOOKBOT ============")
    print("Analyzing book...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in range(0, len(characters)):
        if characters[char]["char"].isalpha():
            print(f"{characters[char]["char"]}: {characters[char]["count"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = word_count(text)
    char_count = character_count(text)
    sort_count = sort_characters(char_count)
    report(count, sort_count)

main()