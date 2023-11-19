from math import sqrt


def distance1(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx*dx + dy*dy)


print(distance1(0, 0, 3, 4))


# создадим класс
class Po:
    def __init__(self, iks, igrek): #определяем конструктор класса. параметры конструктора: (объект, параметры)
        # значения, которые передаются в параметрах iks, igrek, нужно присвоить в атрибуты объекта self
        self.x = iks
        self.y = igrek
        # iks, igrek - переменнрые-параметры, в кот. помещаются значения, которые мы передаем при вызове функции;
        # x, y - атрибуты объекта self


def distance2(p1, p2):
    dx = p2.x - p1.x #откуда известно, что такое x / y?
    dy = p2.y - p1.y
    return sqrt(dx*dx + dy*dy)


print(distance2(Po(0, 0), Po(3, 4)))


# создадим класс с методом и операцией
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


a = Point(0, 0)
b = Point(3, 4)
print(a.distance(b))
print(a == b)