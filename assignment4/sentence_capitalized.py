# 3. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

def main():
    print("Enter lines of text (press q finish):")

    lines = []
    while True:
        line = input()
        if line == "q":
            break
        lines.append(line)

    print("\nCapitalized lines:")
    for line in lines:
        print(line.upper())

main()


     
