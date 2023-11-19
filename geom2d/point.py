from math import sqrt


class Point:
    def __init__(self, iks, igrek):
        self.x = iks
        self.y = igrek

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y