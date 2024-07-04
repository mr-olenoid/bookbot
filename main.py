path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = len(file_contents.split())

    chars = count_letters(file_contents)
    list_of_chars = []
    for key in chars:
        list_of_chars.append({"char": key, "count": chars[key]})

    list_of_chars.sort(reverse=True, key=sort_on)
    report(path_to_file, word_count, list_of_chars)


def sort_on(dict):
    return dict["count"]

def count_letters(text: str):
    char_count = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha(): 
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    return char_count

def report(path, word_count, char_list):
    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document')
    print()
    for val in char_list:
        char = val["char"]
        count = val["count"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()