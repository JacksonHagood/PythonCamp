# extra challenge 3

# create a program that takes in a number
# print random letters that many times
# the letters should be on the same line

# solution

import random

length = int(input('Please enter a length: '))

letters = 'abcdefghijklmnopqrstuvwxyz'

for  i in range(length):
    print(letters[random.randint(0, 25)], end ='')
