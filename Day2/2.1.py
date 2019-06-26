# while loops in python

i = 0

while i < 5:
    # while will continue to loop until the given conditional becomes false
    print(i, end=' ')
    # end= will define what ends a print statement
    i += 1

print('')
i = 0

while True:
    # a while true will run until a break
    print(i, end=' ')
    i += 1
    if i == 5:
        break
        # break will go out of the nearest loop regardless of conditional

print('')
i = 0

while i < 4:
    i += 1
    if i == 3:
        continue
        # continue will stop the current iteration, and move to the next
    print(i, end=' ')

print('')
i = 0

while False:
    # a while false would never run
    print('Python is Broken')

print('')
i = 0
while i < 5:
    i += 1
else:
    # else can be used with a while loop
    # else will run once the while loop is finished
    # else will not run if a break is used in the while loop
    print('i is now', i)
