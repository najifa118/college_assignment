def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)
number = int(input("Enter a number: "))
factors = find_factors(number)
print("Factors of", number, "are:", factors)
