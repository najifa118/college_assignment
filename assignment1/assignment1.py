def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a, b = swap_numbers(a, b)
print(f"After swapping: \nFirst number: {a}\nSecond number: {b}")
