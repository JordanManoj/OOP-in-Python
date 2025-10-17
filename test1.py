class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
my_car = Car("honda", "amaze")
print(my_car.brand)
print(my_car.model)
my_car.display_info()
