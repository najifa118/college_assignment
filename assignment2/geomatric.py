def print_geometric_sequence(first_term, common_ratio, number_of_terms):
    """Print the first `number_of_terms` terms of a geometric sequence."""
    terms = []
    for n in range(number_of_terms):
        term = first_term * (common_ratio ** n)
        terms.append(term)
    
    print(f"The first {number_of_terms} terms of the geometric sequence are:")
    for i, term in enumerate(terms, start=1):
        print(f"Term {i}: {term}")

def main():
    first_term = 2
    common_ratio = 3
    number_of_terms = 6
    print_geometric_sequence(first_term, common_ratio, number_of_terms)

if __name__ == "__main__":
    main()
