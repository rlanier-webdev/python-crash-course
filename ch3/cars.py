print('=====Lists=====')
cars = ['Chevrolet','Toyota','Honda']
print(f'I would like to own a {cars[0]} car.')
print(f'I would like to own a {cars[1]} car.')
print(f'I would like to own a {cars[2]} car.')

print('\n=====Changing the item in the list=====')
# Change the element
cars[0] = 'Tesla'
print(cars)

print('\n=====Adding an item=====')
'''Adding an element'''
# Appending to the end
cars.append('Tesla')
print(cars)

print('\n=====Inserting an item=====')
# Inserting an element
cars.insert(1, 'Mercedes')
print(cars)

print('=====Removing an item=====')
'''Removing an element'''
del cars[2]
print(cars)

print('=====Remove the last item=====')
# Remove the last item in the list
popped_cars = cars.pop()
print(popped_cars)

# Remove item from any position
third_owned = cars.pop(2)
print(f'The third car I owned was a {third_owned}.')

# Remove an item by value
cars.remove('Tesla')
print(cars)

'''Sorting a list'''
# sort() alphabetically
cars = ['Chevrolet','Toyota','Honda']
cars.sort()
print(cars)

# sort(reverse=True) reverse alphabetically
cars.sort(reverse=True)
print(cars)

print('=====Temporarily sorted=====')
# Sort Temporarily sorted()
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

# reverse order
print('=====Reverse Order=====')
cars.reverse()
print(cars)

'''Finding the length'''
length = len(cars)
print(length)



