"""
LIST COMPREHENSION
"""

comp_list = [x * 2 for x in range(10)]

print(comp_list)

comp_list = [x ** 2 for x in range(1, 7) if x % 2 == 0]

print(comp_list)


# combine list of list

nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]

print(nums_letters)
