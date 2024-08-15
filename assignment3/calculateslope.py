def calculate_slope(point1, point2):
    """
    Calculate the slope of a line given two points.
    
    Args:
    point1 (tuple): A tuple representing the first point (x1, y1).
    point2 (tuple): A tuple representing the second point (x2, y2).

    Returns:
    float: The slope of the line.
    """
    x1, y1 = point1
    x2, y2 = point2
    if x2 == x1:
        raise ValueError("Slope is undefined for vertical lines (x1 and x2 cannot be the same).")
    slope = (y2 - y1) / (x2 - x1)
    return slope
point1 = (1, 2)
point2 = (3, 4)
print(calculate_slope(point1, point2))

point1 = (0, 0)
point2 = (4, 4)
print(calculate_slope(point1, point2))

point1 = (1, 2)
point2 = (1, 5)
