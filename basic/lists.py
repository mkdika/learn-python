"""
LIST
"""

# list declaration

arr = [1, 2, 3, 4, 5]

print(arr)

# get & manipulate by index

arr[0] = True

print(arr)

print(arr[2])


# print length

print(len(arr))


# add element

arr.append('6')

print(arr)

arx = [1, 2, 3]

print(arx)


# remove element, by index

del arx[0]

print(arx)


# remove element slices

del arr[1:5]

print(arr)


# remove the first element

arx.pop()

print(arx)


# remove y index

arr.pop(0)

print(arr)


# traverst all list

arz = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for e in arz:
    print(e, end="")


# check element exist in list

print()
print(f"Is 10 in arz: {10 in arz}")
print(f"Is 5 in arz : {5 in arz}")
