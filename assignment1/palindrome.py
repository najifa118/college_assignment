def is_palindrome(num):
    """Check if a number is a palindrome."""
    num_str = str(num)
    return num_str == num_str[::-1]
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
