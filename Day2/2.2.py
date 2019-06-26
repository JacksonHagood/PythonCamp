# for loops in python

for i in range(10):
    # a for loop will iterate multiple times according to a given range
    # for loops can be replace some while loops with if statements
    print(i, end='')

print('')

for i in range(5, 10):
    # a range can be given a minimum value
    print(i, end='')

print('')

for i in range(0, 10, 2):
    # a range can be iterate by a given number
    print(i, end='')

name = 'Jackson'

print('')

for i in range(0, len(name)):
    # len() can return the length of a given string
    print(name[i], end=' ')
    # can iterate through a string

print('')

for char in name:
    # can also iterator through a string as such
    print(char, end=' ')

print('')

for i in range(0, 5):
    for j in range(0, 5):
        # for loops can be contained within each other
        print('{0}*{1}={2}'.format(i, j, i*j), end='|')
        # there are complex applications of for loops
    print('\n')

i = 0

for i in range(5):
    print(i, end=' ')
else:
    # else can be used with a for loop
    # else will run once the for loop is finished
    print('i has reached its maximum value of', i)
