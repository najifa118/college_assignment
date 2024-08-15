import math

def compute_cosine(x, n):
    """
    Compute the cosine of x using the Taylor series expansion up to n terms.
    
    Args:
    x (float): The angle in radians.
    n (int): The number of terms in the Taylor series to use.
    
    Returns:
    float: The computed value of cos(x).
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    cosine_value = 0.0
    for i in range(n):
        exponent = 2 * i
        term = ((-1)**i * x**exponent) / math.factorial(exponent)
        cosine_value += term
    
    return cosine_value
x = float(input("Enter the angle in radians (x): "))
n = int(input("Enter the number of terms in the Taylor series (n): "))
result = compute_cosine(x, n)
print(f"The computed value of cos({x}) using {n} terms is: {result:.5f}")
