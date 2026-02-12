# 3.4 Guest List
guests = ['Jill Scott','Queen Latifah','Whitney Houston','Michael Jackson']
print(f'Dear {guests[0]}, You are invited to dinner.')
print(f'Dear {guests[1]}, You are invited to dinner.')
print(f'Dear {guests[2]}, You are invited to dinner.')
print(f'Dear {guests[3]}, You are invited to dinner.')

# 3.5 Changing Guest List
print(f"{guests[3]} can't make it.")
guests[3] = 'Lee'
print(f'Dear {guests[0]}, You are invited to dinner.')
print(f'Dear {guests[1]}, You are invited to dinner.')
print(f'Dear {guests[2]}, You are invited to dinner.')
print(f'Dear {guests[3]}, You are invited to dinner.')

# 3.6 More Guests
print('I found a bigger table!')
guests.insert(0,'Lane')
guests.insert(2,'Toya')
guests.append('Joy')

print(f'Dear {guests[0]}, You are invited to dinner.')
print(f'Dear {guests[1]}, You are invited to dinner.')
print(f'Dear {guests[2]}, You are invited to dinner.')
print(f'Dear {guests[3]}, You are invited to dinner.')
print(f'Dear {guests[4]}, You are invited to dinner.')
print(f'Dear {guests[5]}, You are invited to dinner.')
print(f'Dear {guests[6]}, You are invited to dinner.')

# 3.7 Shrinking Guest List
print("The table won't be here on time! I can only invite 2 people to dinner.")
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
print(f"Hey {guests[0]}, you're still invited to dinner.")
print(f"Hey {guests[1]}, you're still invited to dinner.")
del guests[0]
print(guests)
del guests[0]
print(guests)

print(f"How many people are coming to dinner? {len(guests)}")