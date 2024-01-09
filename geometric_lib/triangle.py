def area(a, h):
    '''Принимает числа a, h  возвращает и печатает площадь треугольнка со стороной a и высотой h'''
    print((a * h)/2)
    return (a * h)/2


def perimeter(a, b, c):
    '''Принимает числа a, b, c  возвращает и печатает периметр треугольнка со сторонами a, b, c'''
    print(a + b + c)
    return a + b + c




x = int(input())
y = int(input())
z = int(input())
l = int(input())
'''Задание сторон треуголька и высоты к стороне a'''
area(x, l)
perimeter(x, y, z)

