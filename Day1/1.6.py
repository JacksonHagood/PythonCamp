# if statements in python

if 1 == 1:
    # '==' check whether or not two items have the same value
    # indentation is a part of how python interprets code
    print('Python Works 1')
    # this is only executed if the above conditional returns a true

if 'word' == 'word':
    # '==' can be used with strings just like integers
    print('Python Works 2')

if 2 > 1:
    # '>', '<', '>=', '<=', and '!=' can be used as well
    print('Python Works 3')

if '1' == 1:
    # a string can never equal an integer
    print('Python is Broken')
else:
    # an else will be executed only if the previous if statement returns a false
    print('Python Works 4')

if 1 == 2:
    print('Python is Broken')
elif 1 == 1:
    # elif is executed only if the previous if statement returns a false and the given conditional is true
    print('Python Works 5')
else:
    print('Python is Broken')

Boolean = True
# a boolean is either True or False
# can be assigned to a variable

if Boolean:
    print('Python Works 6')

if True:
    # will always be executed
    print('Python Works 7')

if not False:
    # not will reverse the boolean
    print('Python Works 8')

if 1 == 1 and 2 == 2:
    # and will only return a true if both of the surrounding conditionals are true
    print('Python Works 9')

if 1 == 1 or 2 == 1:
    # or will return a true if either of the surrounding conditionals are true
    print('Python Works 10')

if 1 is 1:
    # is will return true if the two items are the same
    print('Python Works 11')

name = 'Jackson'

if 'Jack' in name:
    # in will return true if the given item is contained within the other item
    print('Python Works 12')
