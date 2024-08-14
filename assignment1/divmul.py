def is_divisible_by_7_not_multiple_of_5(num):
    """Check if a number is divisible by 7 but not a multiple of 5."""
    return num % 7 == 0 and num % 5 != 0

def display_numbers(start, end):
    """Display numbers between start and end that are divisible by 7 but not multiples of 5."""
    for num in range(start, end + 1):
        if is_divisible_by_7_not_multiple_of_5(num):
            print(num, end=' ')
start_range = 1000
end_range = 2000
display_numbers(start_range, end_range)
