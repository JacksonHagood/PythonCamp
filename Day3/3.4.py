# iterators in python

List = ['This', 'is', 'a', 'list']

for word in List:
    # can iterate through a through variables with for loops
    print(word, end=' ')

print('')

Iterator = iter(List)
# alternatively, you can make an iterator with iter()

print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
print(next(Iterator))
# next() will print the next item in the iterator
# attempting to go past the end of the item will result in an error
# can iterate through strings, lists, sets, tuples, and dictionaries
