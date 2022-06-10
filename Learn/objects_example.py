class Person:
    surname = None
    age = None

    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def print_name(self):
        print(self.name)

    def __str__(self):
        return f'this is {self.name}'

    def __repr__(self):
        return f'This is {self.name}'

    def __eq__(self, other):
        return all([self.name == other.name,
                    self.surname == other.surname])


bogus = Person('Bogus', 'wow', 20)
bogdan = Person('Bogus', 'wow', 30)
list_of_names = [bogdan, bogus]
print(list_of_names)
print(bogus == bogdan)
