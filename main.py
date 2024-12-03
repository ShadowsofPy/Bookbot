import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = word_count(file_contents)
    characters = char_count(file_contents)
    sorted_chars = sort(characters)
    report(sorted_chars, words)

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    letters = {}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def sort(dict):
    chars = []
    for item in dict:
        if item.isalpha():
            temp = {"character" : item, "num" : dict[item]}
            chars.append(temp)
    chars.sort(reverse=True, key=sort_on)
    return chars

def report(list, count):
    print("--- Report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print("")
    for item in list:
        character = item["character"]
        num = item["num"]
        print(f"The '{character}' character was found {num} times")
    print("--- End report ---")

main()