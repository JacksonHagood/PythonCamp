# tuples in python

Tuple = 'a', 'b', 'c'
# tuples are immutable, ordered sets of data
# tuples cannot be changed at an index

print(Tuple)

for letter in Tuple:
    # can iterate through a tuple
    print(letter, end=' ')

print('')

print(Tuple[0])
# can index a tuple

print(Tuple + Tuple)
# adding two sets will concatenate them

if 'a' in Tuple:
    # in works with tuples
    print('Python Works!')

let1, let2, let3 = Tuple
# can assign multiple variables values with a tuple

print(let1, let2, let3)

Tuple = Tuple[0], 'r', Tuple[2]
# There are ways to get around not being able to change Tuples

print(Tuple)
