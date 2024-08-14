def print_multiplication_table(number, up_to=10):
    """Print the multiplication table for the given number up to a specified limit."""
    print(f"Multiplication table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

def main():
    try:
        num = int(input("Enter a number to print its multiplication table: "))
        print_multiplication_table(num)
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
