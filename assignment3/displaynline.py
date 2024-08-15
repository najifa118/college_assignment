def print_segment(num):
    """
    Print the number as an 8-segment display.
    
    Args:
    num (int): The number to print.
    """
    segments = [
        " --  |  |  |  | -- ",
        "    |  |    |    |  ",
        " --  |  | --  | -- ",
        " --  |  | --  | -- ",
        "    |  | --  |    |  ",
        " --  | --  | --  | -- ",
        " --  | --  | --  | -- ",
        " --  |  |    |    |  ",
        " --  | --  | --  | -- ",
        " --  | --  | --  | -- "
    ]
    if num < 0 or num > 9:
        raise ValueError("Number must be between 0 and 9")
    display = segments[num]
    print(display[:5])
    print(display[5:10])
    print(display[10:])
n = int(input("Enter the number to display (0-9): "))
print_segment(n)
