# Create the sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# I. Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("it_companies after adding 'Twitter':", it_companies)

# III. Insert multiple IT companies at once into the set it_companies
new_companies = {'Tesla', 'Netflix', 'Zoom'}
it_companies.update(new_companies)
print("it_companies after adding multiple companies:", it_companies)

# IV. Remove one of the companies from the set it_companies
it_companies.remove('IBM')  # Removing 'IBM' as an example
print("it_companies after removing 'IBM':", it_companies)

# V. Difference between remove and discard
it_companies.discard('NETFLIX')  # Doesn't Raises KeyError
print("it_companies after removing 'IBM':", it_companies)
print("discard doenn't raise an error if it not in the set")

# remove(element) raises KeyError if the element does not exist
it_companies.remove('NETFLIX')  # Raises KeyError
print("it_companies after removing 'IBM':", it_companies)
print("remove raises an error if it not in the set")
