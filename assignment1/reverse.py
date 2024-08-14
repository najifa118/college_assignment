def reverse_number(n):
    reversed_number = int(str(n)[::-1])
    return reversed_number
number = int(input("Enter a number: "))
print("Reversed number:", reverse_number(number))
