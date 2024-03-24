from datetime import date

past = date(2000, 1, 1) #вызовется конструктор объекта класса и создастся новый объект этого класса
future = date(2077, 1, 1)

print(past)

#артибуты класса
print(past.year) #year - это артибут класса
print(str(future.year))

#метод объекта - функция, которая, помимо оперирования параметрами, оперирует объектом, в котором она вызвана,
# в качестве неявного параметра (и имеет доп. параметрами)
print(past.isoweekday())

# операторы
print(past < future)
print(str(future - past) + ' days')
print(str(past - future) + ' days')

#методы класса - функции, как правило исп для конструирования объектов (альтернатива конструкторам)
print(str(date.today()))
