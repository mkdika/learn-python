"""
PYTHON CONDITIONAL:
1. if
2. if..else
3. expression condition
4. boolean operator
"""

family_name = "chandika"

if family_name == "chandika":
    print('Good morning boss!')

age = 29

if age > 17:
    print('permit to enter')
else:
    print('age restriction')


# expression condition, ternary

birth_year = 1999

permission = 'Please Enter' if birth_year < 2000 else 'No Enter'

print(permission)

# boolean operator

if family_name == "chandika" and age < 20:
    print("You are my young master")
elif family_name == "chandika" or birth_year > 1990:
    print("Okay future master")

my_name = "john"

if my_name != "maikel":
    print("Sorry, you're not my master")
