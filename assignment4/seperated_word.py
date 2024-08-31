# 7. Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

def main():
    input_string = input("Enter a sequence of words separated by whitespace: ")

    words = input_string.split()
    result = [word for word in words if word.isdigit()]

    print(result)

main()
     
