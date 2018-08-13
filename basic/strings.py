"""
STRING
"""

# declare string can use single or double quote

first_name = "Maikel"
last_name = 'Chandika'

print(first_name)
print(last_name)


# String concatination

print(first_name + " " + last_name)


# String length

print(len(first_name))


# String formatting - Old Style

print("My first name is %s and last name is %s." % (first_name, last_name))


# String formatting - New style

print("My surname name is {1} and given name is {0}."
      .format(first_name, last_name))

print("first name: {first_name}\tlast name: {last_name}"
      .format(first_name=first_name, last_name=last_name))


# String interpolation (only Python 3.6+)

print(f"My full name is {first_name+' '+last_name}")


# left padding

for i in range(0, 10):
    print(i, end=""),
print()
print("{:_>10}".format("12345"))


# right padding

print("{:_<10}".format("12345"))


# center padding

print("{:_^10}".format("1234"))


# paddding number

pi = 3.141592653589793

print("pi is {:.5f}".format(pi))
