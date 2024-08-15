def reverse_list(arr):
    """
    Reverses the given list using loops and returns the reversed list.
    
    Args:
    arr (list): The list to reverse.
    
    Returns:
    list: The reversed list.
    """
    reversed_list = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_list.append(arr[i])
    
    return reversed_list
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)
