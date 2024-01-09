import unittest
import math
from rectangle import area as rectangle_area
from circle import area as circle_area
from square import area as square_area
from triangle import area as triangle_area
from rectangle import perimeter as rectangle_perimeter
from circle import perimeter as circle_perimeter
from square import perimeter as square_perimeter
from triangle import perimeter as triangle_perimeter

class AreaAndPerimeterTest(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(3), math.pi*3*3)   # add assertion here
        self.assertEqual(circle_perimeter(5), math.pi*2*5)
        self.assertEqual(rectangle_area(4, 5), 4*5)
        self.assertEqual(rectangle_perimeter(3, 6), 2*(3+6))
        self.assertEqual(square_area(6), 6*6)
        self.assertEqual(square_perimeter(7), 7*4)
        self.assertEqual(triangle_area(5, 7), (5*7)/2)
        self.assertEqual(triangle_perimeter(2, 4, 5), 2+4+5)

