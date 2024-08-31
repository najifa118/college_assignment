# I. Create fruits, vegetables, and animal products tuples
fruits = ('guava', 'kiwi', 'avocado')
vegetables = ('cucumbre', 'potato', 'tomato')
animal_products = ('butter', 'chicken', 'milk')

# II. Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# III. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# IV. Slice out the middle item or items from the food_stuff_lt list
n = len(food_stuff_lt)
if n % 2 == 0:
    middle_items = food_stuff_lt[n//2 - 1 : n//2 + 1]
else:
    middle_items = [food_stuff_lt[n//2]]
print("Middle item(s):", middle_items)

# V. Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

# VI. Delete the food_stuff_tp tuple completely
del food_stuff_tp
