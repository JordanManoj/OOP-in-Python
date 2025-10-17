import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

#list of shapes
shapes = [
    Rectangle(10,5),
    Circle(3),
    Triangle(6, 8)
]

for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")