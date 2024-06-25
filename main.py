def main():
    file_path = "books/frankenstein.txt"
    book_text = open_txt_book(file_path)
    print("--- Begin report of " + file_path + "---")

    
    #print(book_text)

    words = book_text.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")
    print("")

    count_by_character = count_each_character(book_text)
    #print(count_by_character)

    alphabet_only_dict = get_alphabet_only(count_by_character)
    #print(alphabet_only_dict)


    sorted_alphabet_dict = sort_by_frequency(alphabet_only_dict)
    #print(sorted_alphabet_dict)

    for key in sorted_alphabet_dict:
        print(f"The '{key}' character was found {sorted_alphabet_dict[key]} times")



def open_txt_book(file_path):
    with open(file_path) as f:
        return f.read()

def count_each_character(book_text):
    all_lowered = book_text.lower()

    all_lowered_dict = dict()

    for letter in all_lowered:
        if letter in all_lowered_dict.keys():
            all_lowered_dict[letter] += 1
        else:
            all_lowered_dict[letter] = 1

    return all_lowered_dict

def get_alphabet_only(all_lowered_dict):
    alphabet_count_dict = dict()
    for key in all_lowered_dict.keys():
        if key.isalpha():
            alphabet_count_dict[key] = all_lowered_dict[key]

    return alphabet_count_dict

def sort_by_frequency(letter_dict):
    sorted_dict = dict()
    for key in sorted(letter_dict, key=letter_dict.get, reverse=True):
        sorted_dict[key] = letter_dict[key]

    return sorted_dict

if __name__ == "__main__":
    main()
