cars = ['Chevrolet','Toyota','Honda']
print(f'I would like to own a {cars[0]} car.')
print(f'I would like to own a {cars[1]} car.')
print(f'I would like to own a {cars[2]} car.')

# Change the element
cars[0] = 'Tesla'
print(cars)

'''Adding an element'''
# Appending to the end
cars.append('Tesla')
print(cars)

# Inserting an element
cars.insert(1, 'Mercedes')
print(cars)

'''Removing an element'''
del cars[2]
print(cars)

# Remove the last item in the list
popped_cars = cars.pop()
print(popped_cars)

# Remove item from any position
third_owned = cars.pop(2)
print(f'The third car I owned was a {third_owned}.')

# Remove an item by value
cars.remove('Tesla')
print(cars)


