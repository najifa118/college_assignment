# 4. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
def process_words():
    input_string = input("Enter a sequence of whitespace-separated words: ")

    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)

    print("Sorted words without duplicates:")
    print(" ".join(sorted_words))

process_words()

