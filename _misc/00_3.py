l = [1, 2, 3, 4, 5] #список - изменяемый, содержит объекты одинаковой природы
t = (1, 2, 3, 4, 5) #кортеж - неизменяемый; как правило, элементы имеют разные смыслы
l1 = l[0]
t1 = t[0]
print(l1, t1)
l[0] = 10
print(l)
(d, m, y) = (10, 12, 2024)
print(y)
print(len(l), len(t), l[1:3])
l[1:3] = [7, 8]
print(l)
l[1:3] = [9, 10, 11]
l.append(12)
print(l)
print(30 in l)
r = range(1, 5)
print(r[3])
print(list(r))
s = 'test'
print(list(s), [s])

list1 = [100, 2, 13, 4, 50]
sorted_list1 = sorted(list1)
print(list1, '\n', sorted_list1)

list1.sort()
print(list1)