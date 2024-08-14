def decimal_to_binary_builtin(decimal_number):
    """Convert decimal number to binary using built-in function."""
    return bin(decimal_number)[2:]

def decimal_to_binary_manual(decimal_number):
    """Convert decimal number to binary manually."""
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

def main():
    try:
        decimal_number = int(input("Enter a decimal number: "))
        if decimal_number < 0:
            print("Please enter a non-negative integer.")
            return
        binary_builtin = decimal_to_binary_builtin(decimal_number)
        print(f"Binary representation (built-in): {binary_builtin}")
        binary_manual = decimal_to_binary_manual(decimal_number)
        print(f"Binary representation (manual): {binary_manual}")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
