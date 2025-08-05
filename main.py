from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path: str) -> str:
    with open(path) as f:
        text = f.read()
    return text

def main():
    text = get_book_text(path)
    print(f"Found {count_words(text)} total words")

    char_nums = get_char_nums(text)
    sorted_char_nums = sort_char_nums(char_nums)

    for tup in sorted_char_nums:
        if tup["char"].isalpha():
            char, num = tup["char"], tup["num"]
            print(f"{char}: {num}")

main()

'''
print("============ BOOKBOT ============",
          "\nAnalyzing book found at {}...",
          "\n----------- Word Count ----------",
          "\nFound 75767 total words",
          "\n--------- Character Count -------)",
    )
'''