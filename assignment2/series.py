import math

def print_factorial_series(n):
    """Print the factorial series up to n terms."""
    for i in range(1, n + 1):
        term = math.factorial(i)
        print(term, end=", " if i < n else "\n")

def main():
    try:
        num_terms = int(input("Enter the number of terms to print in the series: "))
        if num_terms < 1:
            print("Please enter a positive integer greater than 0.")
            return
        print_factorial_series(num_terms)
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
