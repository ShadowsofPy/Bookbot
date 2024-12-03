import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = word_count(file_contents)
    characters = char_count(file_contents)
    print(sort(characters))

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


main()