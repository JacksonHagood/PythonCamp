# extra challenge 1

# create a program that takes in a persons name
# the characters should then be sorted alphabetically
# repeat characters are allowed

# solution

name = input('Please enter your name: ')

characters = []

for char in name.lower():
    characters.append(char)

print(sorted(characters))
