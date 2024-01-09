import math


def area(r):
    '''Принимает число r возвращает и печатает площадь круга радиуса r'''
    print(math.pi * r * r)
    return math.pi * r * r



def perimeter(r):
    '''Принимает число r возвращает и печатает периметр круга радиуса r'''
    print(2 * math.pi * r)
    return 2 * math.pi * r

y = int(input())
'''Задание радиуса круга'''
area(y)
perimeter(y)