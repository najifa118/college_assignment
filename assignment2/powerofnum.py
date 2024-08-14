def power(base, exponent):
    """Calculate base raised to the power of exponent using recursion."""
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

def main():
    try:
        base = float(input("Enter the base: "))
        exponent = int(input("Enter the exponent (non-negative integer): "))
        if exponent < 0:
            print("Exponent must be a non-negative integer.")
            return
        result = power(base, exponent)
        print(f"{base} raised to the power of {exponent} is: {result}")
        
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
