# lists in python

List = ['This', 'is', 'a', 'list']
# a list is a sequence of multiple items
# items are contained within '[]' and are separated with a ', '

print(List)

for word in List:
    # can iterate through a list
    print(word, end=' ')

print('')

print(List[0])
# can index a list

List.append('cool')
# .append() will add an item to the end of a list

print(List + List)
# adding two lists will concatenate them

if 'list' in List:
    # in works with lists
    print('This is a list!')

numbers = [1, 2, 3, 4, 5]
numbers.sort()
# .sort will sort a list by value
# .sort() is a function that returns nothing, instead it writes over the given list

print(numbers)

print(sorted(numbers))
# sorted will return a sorted list

numbers = [3, 5, 1, 2, 4]

numbers.sort(reverse=True)
# passing a reverse=True into .sort() will sort the list in reverse order

print(numbers)

twoDimensional = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
# can construct list with lists inside

print(twoDimensional[0])
print(twoDimensional[1])
print(twoDimensional[2])
