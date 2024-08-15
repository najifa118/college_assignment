def sum_series(n):
    """
    Computes the sum of the series 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n.
    
    Args:
    n (int): The number of terms in the series.
    
    Returns:
    float: The sum of the series up to n terms.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    total_sum = 0.0
    for i in range(1, n + 1):
        term = (-1)**(i + 1) / i
        total_sum += term
    
    return total_sum
n = int(input("Enter a positive integer n: "))
result = sum_series(n)
print(f"The sum of the series up to {n} terms is: {result:.5f}")
