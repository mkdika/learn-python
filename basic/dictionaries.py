"""
DICTIONARY
"""

hero = {'name': 'Max', 'level': 30, 'hp': 99.5, 'male': True}

print(f"All Hero Attribute: {hero}\n")

# get dict value by key

print(f"Name\t: {hero['name']}\nlevel\t: {hero['level']}\nhp\t: {hero['hp']}")


# print all dict attribute with for each

print()
for k in hero:
    print(f"{k}\t: {hero[k]}")


# print all dict by items

print()
for k, v in hero.items():
    print(f"{k} -> {v}")


# manipulate value of element, inplace

print()
hero['level'] += 1

print(hero['level'])

hero['name'] = "Maximilian"

print(hero['name'])


# remove dict element

print()
hero.pop('male', None)
for k, v in hero.items():
    print(f"{k} -> {v}")


# check dict contain key or value

print()
print(f"Is 'name' in hero: {'name' in hero}")  # true
print(f"Is 'male' in hero: {'male' in hero}")  # false
