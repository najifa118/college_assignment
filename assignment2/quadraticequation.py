import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    return root1, root2

def main():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        if a == 0:
            print("Coefficient 'a' cannot be zero for a quadratic equation.")
            return
        result = solve_quadratic(a, b, c)
        
        if result == "No real roots":
            print(result)
        else:
            root1, root2 = result
            print(f"The roots of the quadratic equation are: {root1} and {root2}")
        
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
