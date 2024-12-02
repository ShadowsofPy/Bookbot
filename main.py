import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count(file_contents)

def word_count(text):
    words = text.split()
    print(len(words))

main()
