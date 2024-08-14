def sum_of_digits(number):
    """Calculate the sum of the digits of a given number."""
    number = abs(number)
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    
    return total_sum

def main():
    try:
        num = int(input("Enter a number to find the sum of its digits: "))
        result = sum_of_digits(num)
        print(f"The sum of the digits of {num} is: {result}")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
