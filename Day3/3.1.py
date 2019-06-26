# sets in python

Set = {'Cow', 'Pig', 'Chicken'}
# sets are like lists, but unordered
# items are contained within '{}' and are separated with a ', '
# can't index or concatenate a set

print(Set)

for animal in Set:
    # can iterate through a set
    print(animal, end=' ')
    # sets will differ in order, regardless of how they were defined

print('')

Set.add('Horse')
# .add() will add an item to a set
# the item will be in no particular order

even = set(range(0, 10, 2))
odd = set([1, 3, 5, 7, 9])
# sets can be made from a range or list with set()
# similar functions exist for lists and dictionaries

print(even.union(odd))
# .union() will return two sets combined

if 'Horse' in Set:
    # in works with sets
    print('Python Works!')

even.discard(2)
# .discard will remove a given item from a set

print(even)
