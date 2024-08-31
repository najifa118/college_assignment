#   1.reverses it.
#   2.checks whether it is a palindrome.
#   3.checks whether it ends with a specific substring.
#   4.capitalize the first letter of each word in a string
#   5.check if a string is anagram of another string
#   6.remove vowels from string
#   7.find length of the longest word in a sentence


def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    reversed_s = reverse_string(s)
    return s == reversed_s

def ends_with_substring(s, substring):
    return s.endswith(substring)

def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words) if words else 0

def main():
    input_string = input("Enter a string: ")

    # 1. Reverse the string
    reversed_str = reverse_string(input_string)
    print(f"Reversed string: {reversed_str}")

    # 2. Check if the string is a palindrome
    palindrome = is_palindrome(input_string)
    print(f"Is palindrome: {'Yes' if palindrome else 'No'}")

    # 3. Check if the string ends with a specific substring
    substring = input("Enter the substring to check if the string ends with: ")
    ends_with = ends_with_substring(input_string, substring)
    print(f"Ends with '{substring}': {'Yes' if ends_with else 'No'}")

    # 4. Capitalize the first letter of each word
    capitalized_str = capitalize_first_letter(input_string)
    print(f"Capitalized string: {capitalized_str}")

    # 5. Check if two strings are anagrams
    another_string = input("Enter another string to check for anagram: ")
    anagram = are_anagrams(input_string, another_string)
    print(f"Are anagrams: {'Yes' if anagram else 'No'}")

    # 6. Remove vowels from the string
    no_vowels_str = remove_vowels(input_string)
    print(f"String without vowels: {no_vowels_str}")

    # 7. Find length of the longest word in a sentence
    sentence = input("Enter a sentence to find the length of the longest word: ")
    longest_word_len = longest_word_length(sentence)
    print(f"Length of the longest word: {longest_word_len}")

main()

     
