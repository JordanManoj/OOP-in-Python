class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
p4 = p1 - p2
p5 = Point(2, 3)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2: {p3}")
print(f"p1 - p2: {p4}")
print(f"p1 == p5: {p1 == p5}")