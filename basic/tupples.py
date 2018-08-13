"""
TUPPLE

Tupple is like List but immutable.
"""

tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# print out all tuples

print("tup is: ", end="")
for e in tup:
    print(e, end="")


# check length

print()
print(f"tup length is {len(tup)}")


# get by index

print(f"tup index-7 is {tup[6]}")

# check element exists

print(f"Is 3 in tup : {3 in tup}")
print(f"Is 11 in tup: {11 in tup}")


# test append and pop

# tup.pop() # will follow with error no attribute found

# tup.append(11) # will follow with error no attribute append found
