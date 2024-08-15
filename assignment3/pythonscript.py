def print_table():
    """
    Print a table with specific number patterns as given.
    """
    print("11111")
    row2 = [2 * i for i in range(1, 5)]
    row2.append(2**4)
    print("".join(map(str, row2)))
    row3 = [3 * i for i in range(1, 4)]
    row3.extend([3**2, 3**3])
    print("".join(map(str, row3)))
    row4 = [4 * i for i in range(1, 3)]
    row4.extend([4**2, 4**3])
    print(f"{row4[0]}{row4[1]} {row4[2]} {row4[3]}")
    row5 = [5 * i for i in range(1, 4)]
    row5.extend([5**2, 5**3])
    print(f"{row5[0]}{row5[1]} {row5[2]} {row5[3]}")
print_table()
