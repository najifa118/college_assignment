import math

def is_krishnamurthy_number(number):
    """Check if the given number is a Krishnamurthy number."""
    digits = str(number)
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    return sum_of_factorials == number

def main():
    try:
        num = int(input("Enter a number to check if it's a Krishnamurthy number: "))
        if is_krishnamurthy_number(num):
            print(f"{num} is a Krishnamurthy number.")
        else:
            print(f"{num} is not a Krishnamurthy number.")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
