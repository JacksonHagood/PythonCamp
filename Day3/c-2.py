# challenge 2

# create a program that takes in a sentence from a user
# the program should then print all the characters from that sentence
# should be printed in a random order with no repeats

# solution

text = input('Please enter a sentence: ')
characters = set()

for char in text:
    if char not in characters:
        characters.add(char)

print(characters)
