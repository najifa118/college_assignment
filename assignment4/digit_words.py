# 6. Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

def main():
    input_string = input("Enter a string: ")

    if input_string.lower() == "yes":
        print("Yes")
    else:
        print("No")

main()
