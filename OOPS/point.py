import math


class Point:
    'represents a point in geometrical cordiantes'

    def __init__(self, x, y):
        """initialize the position of new point.
        The x and y cordinates can be specified.
        If not origin is used as cordinates"""
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
                        (self.x - other_point.x) ** 2 +
                        (self.y - other_point.y) ** 2)

p1 = Point(1, 3)
p2 = Point(2, 5)

p1.move(2, 3)
p2.reset()

print(p1.calculate_distance(p2))
assert(p1.calculate_distance(p2) == p2.calculate_distance(p2))

