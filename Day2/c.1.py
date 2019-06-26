# challenge 1

# create an program that generate a random number between 1 and 10
# the computer should prompt the user to guess the number
# the user must then guess numbers until they get the number right
# if the user guesses a number outside of the range the program must stop

# solution

import random

solution = random.randint(1, 10)

while True:
    guess = int(input('Please guess a number between 1 and 10: '))
    if guess < 0 or guess > 10:
        print('You guessed outside the range')
        break
    elif guess == solution:
        print('Correct! The number was', solution)
        break

# solution ++

while True:
    guess = int(input('Please guess a number between 1 and 10: '))
    if guess < 0 or guess > 10:
        print('You guessed outside the range')
        break
    elif guess == solution:
        print('Correct! The number was', solution)
        break
    elif guess > solution:
        print('Guess lower')
    else:
        print('Guess higher')
