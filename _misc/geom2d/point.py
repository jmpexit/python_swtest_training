from math import sqrt


class Point:
    def __init__(self, iks, igrek):
        self.x = iks
        self.y = igrek

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other): #стандартный метод сравнения
        return self.x == other.x and self.y == other.y

    def __lt__(self, other): #стандартный метод сортировки точек
        return self.y < other.y

    def __repr__(self): #representation. стандартный метод отображения результатов
        #return "Point(" + str(self.x) + ", " + str(self.y) + ")"
        return "Point(%s, %s)" % (self.x, self.y) #использование кортежа для передачи значений в ф-ю форматирования
                                        #т.о. описываем формат строки с подстановкой значений
                                        # %s - подставить строку (с авто преобразованием)  %d - подставить число

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]

print(l1 == l2) #логически равны, физически - отличаются. без спец. функции сравнения eq будет false

l2 = l1
print(l1 == l2)

l2 = list(l1) #список состоит из объектов л1 - ссылок на объекты. одни и те же объекты
print(l1 == l2)

l2[0] = Point(0, 0)
print(l1 == l2)

l2 = sorted(l1)
print(l1, '\n', l2)