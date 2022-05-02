# string formatting in python

firstName = 'Jackson'
lastName = "Hagood"
# strings can be created with either '' or ""
# when making variable names with more than one word, use camel case

print(firstName, lastName)
# can print multiple items by separating them with ', '
# ', ' will automatically add spaces

print(firstName + lastName)
# + will not add spaces

print(firstName, lastName, sep='')
# sep= can be used to define what is displayed between the given items
# sep= is ' ' by default

print(firstName + '\n' + lastName)
# /n inside a string will go to the next line

print(firstName + '\t' + lastName)
# /t inside a string will tab over

print(firstName * 3)
# multiplying a variable will return it multiple times

print(firstName[0])
# can get a character from a string by indexing
# the first character is at position 0

print(firstName[0:3])
# can get a substring by placing two indexes with a ':'
# goes up to the second index, but doesn't include it

print(firstName[:3])
# leaving the first index blank will start it at index 0

print(firstName[2:])
# leaving the last index blank will go to the end

print(firstName[-1])
# can index backwards

print(firstName[0:7:2])
# can index by a number

age = 18

print('Jackson is {0} years old'.format(age))
# can use .format() to pass through variables into a string
# given by a {0}

paragraph = '''This string is spread
over multiple lines.
This is thanks to
multiline strings'''
# multiline strings can be made easier with '''text'''

print(paragraph)

print(firstName.upper())
# .upper() will return the string in upper case

print(firstName.lower())
# .lower() will return the string in lower case

print(firstName.replace('Jack', 'Ja'))
# .replace will return a new string that replaces a given string with another
