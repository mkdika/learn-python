class Person:

    can_run = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Maikel', 30)
print(f"Name: {person.name}, Age: {person.age}, can run:  {Person.can_run}")
