# extra challenge 1

# create a program that asks the user for to enter minimum and maximum value
# the even numbers within that range should then be printed as a list

# solution

min = int(input('Please enter a minimum value: '))
max = int(input('Please enter a maximum value: '))

List = []

for i in range(min, max + 1):
    if i % 2 == 0:
        List.append(i)

print('The even numbers between', min, 'and', max, 'are', List)
