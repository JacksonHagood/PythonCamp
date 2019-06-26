# input in python

name = input('Please enter your name: ')
# input() can be used to collect user input

print(name, 'is a cool name!')

number = int(input('Please enter a number: '))
# int() will return the int value of a given string

print(number, 'squared is', number**2)

solution = 6

guess = int(input('Please guess a number between 1 and 10: '))
# lots of applications for user input

if guess == solution:
    print('You Won!')
else:
    print('You Lose')
