# 8. Please write a program which count and print the numbers of each character in a string input by console.

def main():
    s = input("Enter a string: ")

    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        print(f"{char}:\t{count}")

main()


