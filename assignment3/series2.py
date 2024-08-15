import math

def compute_sine(x, n):
    """
    Compute the sine of x using the Taylor series expansion up to n terms.
    
    Args:
    x (float): The angle in radians.
    n (int): The number of terms in the Taylor series to use.
    
    Returns:
    float: The computed value of sin(x).
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    sine_value = 0.0
    for i in range(n):
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)
        sine_value += term
    
    return sine_value
x = float(input("Enter the angle in radians (x): "))
n = int(input("Enter the number of terms in the Taylor series (n): "))
result = compute_sine(x, n)
print(f"The computed value of sin({x}) using {n} terms is: {result:.5f}")
