import math

def sum_of_square_roots(a, b, c):
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    sqrt_c = math.sqrt(c)
    sum_sqrt = sqrt_a + sqrt_b + sqrt_c
    
    return sum_sqrt

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        if num1 < 0 or num2 < 0 or num3 < 0:
            print("Numbers must be non-negative.")
            return
        result = sum_of_square_roots(num1, num2, num3)
        print(f"The sum of the square roots is: {result}")
        
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
