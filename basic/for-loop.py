"""
FOR LOOP
"""

for s in 'maikel':
    print(f"{s.upper()} ", end="")


print()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("arr: ", end="")
for a in arr:
    print(f"{a} ", end="")


print()
print("1..10 -> ", end="")
for i in range(1, 11):
    print(f"{i} ", end="")

# just range
print()
print("1 - 10: ", end="")
for i in range(11):
    print(f"{i} ", end="")


print()
hero = {'name': 'Max', 'level': 30, 'hp': 99.5, 'male': True}
for k, v in hero.items():
    print(f"{k} -> {v}")
