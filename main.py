def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_chars(text)
    # print(f"{num_words} words found in the document")
    # print(f"{char_cout} is the dict of the chars in the doc")
    sorted_list = sorter(char_count)
    print(f" ---- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for item in sorted_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars(text):
    char_counter = {}
    words = text.split()
    for word in words:
        for char in word:
            if char.lower() in char_counter:
                char_counter[char.lower()] += 1
            else:
                char_counter[char.lower()] = 1
    return char_counter

def sort_on(dict):
    return dict['num']

def sorter(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({'char': key, 'num': dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

main()
