# coś ma coś -- > samochód ma silnik
# dziedziczenie --> jest czymś ptak jest zwierzęciem

class Car:

    def __init__(self, brand, capacity):
        self.brand = brand
        self.engine = Engine(capacity)


class Engine:

    def __init__(self, capacity):
        self.capacity = capacity


first_car = Car('Toyota', 2.0)

print(first_car.engine.capacity)
