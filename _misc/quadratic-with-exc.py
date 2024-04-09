from math import sqrt
def solve(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print('no roots')
    elif d == 0:
        x = -b / (2*a)
        print('1 root ' + str(x))
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print('2 roots ' + str(x1) + ' ' + str(x2))
    else:
        print('improbable!')


try :
    solve(1, 5, m)
except NameError:
    print('NameError Эксепшун!')
