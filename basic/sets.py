"""
SET

Set can not have an dupplicate elements
"""

# declare

sets = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(f"Sets is: {sets}")


# travest

print("Sets is: ", end="")
for i in sets:
    print(i, end="")


# print size/length

print()
print(f"Sets length: {len(sets)}")


# get by index

# print(f"sets index-7 is {sets[6]}") # will error


# check element exits

print(f"Is 11 in sets: {11 in sets}")


# test insert duplicate

sets.update([5, 11])
sets.update({7})
print("Add new element: 5, 7, 11")
print(f"Sets length: {len(sets)}")
print(f"Now sets is: {sets}")

# remove element
