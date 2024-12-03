import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = word_count(file_contents)
    print(f"Frankenstein has {words} words.")
    characters = char_count(file_contents)
    print(f"List of characters: {characters}")

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
    
main()