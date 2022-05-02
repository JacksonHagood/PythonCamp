# dictionaries in python

Dictionary = {'Company': 'Acer', 'RAM': '4GB', 'CPU': '1.1GHz'}
# dictionaries contain multiple items defined with keys
# items are contained within '{}' keys and values are separated with ':' and items are separated with a ', '
# can't concatenate a set

print(Dictionary)

for attribute in Dictionary:
    # can iterate through a dictionary
    print(Dictionary[attribute], end=' ')

print('')

print(Dictionary['Company'])
# can "index" a dictionary with the key

Dictionary1 = {'Company': 'Audi', 'Type': 'SUV', 'Color': 'Grey'}
Dictionary2 = {'Feature': 'Quatro', 'Year': '2016', 'Country': 'Germany'}

Dictionary1.update(Dictionary2)
# .update() will add the items from one dictionary to another

if 'Company' in Dictionary:
    # in works with dictionaries
    print('Python Works!')

print(Dictionary.keys())
print(Dictionary.values())
# can separate the keys and values from a dictionary

Dictionary3 = Dictionary1.copy()
# .copy() will copy a dictionary
