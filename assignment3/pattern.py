def print_pattern(n):
    """
    Prints a pattern of uppercase letters from A to the nth letter.
    
    Args:
    n (int): The number of lines to print.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    for i in range(n):
        char = chr(ord('A') + i)
        print(char)
n = int(input("Enter the number of lines (N): "))
print_pattern(n)
