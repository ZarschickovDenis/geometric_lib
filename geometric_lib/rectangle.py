def area(a, b):
    '''Принимает числа a и b возвращает и печатает площадь прямоугольника со сторонами a и b'''
    print(a * b)
    return a * b


def perimeter(a, b):
    '''Принимает числа a и b возвращает и печатает периметр прямоугольника со сторонами a и b'''
    print(2 * (a + b))
    return 2 * (a + b)




x = int(input())
y = int(input())
'''Задание сторон прямоугольника'''
area(x, y)
perimeter(x, y)

