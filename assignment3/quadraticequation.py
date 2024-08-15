import cmath

def solve_quadratic_eqn(a, b, c):
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.
    
    Args:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.
    
    Returns:
    tuple: A tuple containing the two solutions (roots) of the quadratic equation.
    """
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return (root1, root2)
a = 1
b = -3
c = 2
roots = solve_quadratic_eqn(a, b, c)
print(f"The roots of the equation are: {roots[0]} and {roots[1]}")

a = 1
b = 2
c = 5
roots = solve_quadratic_eqn(a, b, c)
print(f"The roots of the equation are: {roots[0]} and {roots[1]}")
