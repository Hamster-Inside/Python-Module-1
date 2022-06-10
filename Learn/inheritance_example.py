class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hello(self):
        print(f'Hello {self.name}')


class Student(Person):
    def __init__(self, name, surname, year_of_studies):
        super().__init__(name, surname)
        self.year_of_studies = year_of_studies

    def say_something_student(self):
        print('Something Student')


class Worker(Person):
    def __init__(self, salary):
        self.salary = salary

    def say_something_worker(self):
        print('Something Worker')


student1 = Student('Boguś', 'Bogdanowy', 3)
student1.say_hello()
student1.say_something_student()
