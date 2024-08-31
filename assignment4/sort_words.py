
def sort_words(words):
    word_list = [word.strip() for word in words.split(',')]
    word_list.sort()
    return ', '.join(word_list)
input_words = input("Enter a comma-separated sequence of words: ")
sorted_words = sort_words(input_words)
print("Sorted words:", sorted_words)
