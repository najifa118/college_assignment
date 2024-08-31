# 5. Write a program that accepts a sentence and calculate the number of letters and digits.

def count_letters_digits(s):
    letters = 0
    digits = 0

    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    return letters, digits

s = input("Enter a sentence: ")
letters, digits = count_letters_digits(s)

print(f"LETTERS: {letters}")
print(f"DIGITS:\t {digits}")

