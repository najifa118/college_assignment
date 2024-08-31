# 1. Write a program to enter a string. Calculate the length of the string. Find the substring country. Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

import string

def main(input_string, substring):
    length_of_string = len(input_string)
    substring_found = substring.lower() in input_string.lower()
    substring_count = input_string.lower().count(substring.lower())

    words = input_string.lower().split()
    word_count = {}

    for word in words:
        word = word.strip(string.punctuation)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return length_of_string, substring_found, substring_count, word_count

input_string = input("Enter a string: ")
substring = input("Enter the substring you want to count: ")

length, substring_found, substring_count, counts = main(input_string, substring)

print(f"Length of the string: {length}")
print(f"Is '{substring}' in the string? {'Yes' if substring_found else 'No'}")
print(f"Count of the substring '{substring}': {substring_count}")
print("Word counts:")
for word, count in counts.items():
    print(f"{word}: {count}")
