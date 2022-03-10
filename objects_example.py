class Person:
    surname = None
    age = None

    def __init__(self,name) -> None:
        self.name = name

    def print_name(self):
        print(self.name)

    def __str__(self):
        return f'this is {self.name}'


bogus = Person('Bogus')
print(bogus.name)
bogus.surname = 'Ninja'
bogus.age = 12
print(type(bogus.age))
bogus.print_name()
print(bogus)
