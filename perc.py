def perc(x, y):
    """% y of x """
    one = x/100
    result = y / one
    return result


def prnt_perc(x, y):
    print(str(y) + " is " + str(perc(x, y)) + " percents of " + str(x))


perc(100, 50)
prnt_perc(100, 4)