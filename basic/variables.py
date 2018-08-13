"""
VARIABLE
1. Variable decralation
2. Variable values
    - String
    - Numeric
    - Boolean
    - list, tuple, dict
"""

my_string1 = 'Hello, World!'
my_string2 = "Hello Mike!"
my_flt = 45.06
my_int = 123456
my_bool1 = 5 > 9  # A Boolean value will return either True or False
my_bool2 = True
my_list = ['item_1', 'item_2', 'item_3', 'item_4']
my_tuple = ('one', 'two', 'three')
my_dict = {'letter': 'g', 'number': 'seven', 'symbol': '&'}
_wierd_naming = "Hi I am Maikel"

print(my_string1)
print(my_string2)
print(my_flt)
print(my_int)
print(my_bool1)
print(my_bool2)
print(my_list)
print(my_tuple)
print(my_dict)
print(_wierd_naming)

# multiple assigning , single value

a = b = c = 666
print(a)
print(b)
print(c)

# multiple assigning, multiple values

name, age, isMale = "john", 20, True
print(name)
print(age)
print(isMale)
