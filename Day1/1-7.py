# try, except, and finally in python

Integer = 5

try:
    # a try will go through the following code, but if there is an error skip it
    # no error message will be output
    print(integer)
except:
    # except is run if there is an error in try
    print("That didn't work")

try:
    print(Integer)
except:
    print("That didn't work")
finally:
    # finally will run regardless of whether try worked or not
    print('Done')

try:
    print(Integer)
except:
    print("That didn't work")
else:
    # an else will run if the try worked
    print('That worked fine')
