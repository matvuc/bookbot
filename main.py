from stats import count_word, make_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    words = count_word(path)
    list = make_list(path)

    print("")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for letter in range(len(list)):
        print(f"{list[letter]['name']}: {list[letter]['num']}\n")
    print("============= END ===============")

main()