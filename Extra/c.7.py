# extra challenge 5

# create a program that takes in two legs of a triangle
# the program should then print the hypotenuse

# solution

import math

leg1 = int(input('Please enter a leg: '))
leg2 = int(input('Please enter a leg: '))

print('The hypotenuse of a triangle with legs', leg1, 'and', leg2, 'is', math.sqrt((leg1 ** 2) + (leg2 ** 2)))
