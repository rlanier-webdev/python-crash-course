places = ['Martinique','Barcelona','Greece','Vegas','New York']
print(places)

print(f'Print sorted: {sorted(places)}')

print(places)

places.sort(reverse=True)
print(f'Print sorted reverse: {places}')

print(f'Original order: {places}')

places.reverse()
print(f'Reverse Order: {places}')

places.reverse()
print(f'Back to original: {places}')

places.sort()
print(f'Sorted: {places}')

places.sort(reverse=True)
print(f'Sorted again: {places}')