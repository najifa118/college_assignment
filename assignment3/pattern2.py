def print_patterns(n):
    """
    Print specific patterns up to N lines.
    
    Args:
    n (int): The number of lines to print.
    """
    # Pattern 1
    print("Pattern 1:")
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()
    
    print("\nPattern 2:")
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        num -= 2 * i
        for j in range(i):
            print(num, end=' ')
            num += 1
        num += i
        print()

    print("\nPattern 3:")
    num = 1
    for i in range(n):
        for j in range(n - i):
            print(num, end=' ')
            num += 1
        num -= (n - i) * 2
        print()
    
    print("\nPattern 4:")
    num = n * (n - 1) + 1
    for i in range(n):
        for j in range(n):
            print(num, end=' ')
            num -= 1
        print()
n = int(input("Enter the number of lines (N): "))
print_patterns(n)
