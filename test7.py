class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, year, HP):
        super().__init__(make, model, year)
        self.HP = HP
    def vehicle_info(self):
        return f"{super().vehicle_info()} with {self.HP} HP"

    def __str__(self):
        return f"Car: {self.vehicle_info()}"
class Scooter(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    def vehicle_info(self):
        return f"{super().vehicle_info()} with {self.engine_size}cc engine"


    def __str__(self):
        return f"Bike: {self.vehicle_info()}"
car = Car("Honda", "Amaze", 2015, 100)
bike = Scooter("TVS", "Jupyter", 2021, 50)
print(car)
print(bike)