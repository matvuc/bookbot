def  get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def count_word(text):
    book_text = get_book_text(text)
    words = book_text.split()
    num_words = len(words)
    return num_words

def count_letters(text):
    book_text = get_book_text(text).lower()
    letter_to_num = {}
    for letter in book_text:
        if letter.isalpha():
            if letter in letter_to_num:
                letter_to_num[letter] += 1
            else:
                letter_to_num[letter] = 1
    return letter_to_num

def make_list(items):
    sorted_list = []
    letters = count_letters(items)
    for item in letters:
        new_entry = {"name": item, "num": letters[item]}
        sorted_list.append(new_entry)

    sorted_list.sort(reverse=True, key=sort_on)
    print(sorted_list)
    return sorted_list

def sort_on(items):
    return items["num"]


