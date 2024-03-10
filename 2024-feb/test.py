import unittest
from collections import namedtuple
from montecarlo import generate_radius, generate_midpoint

class TestSimulationLogic(unittest.TestCase):

    def test_generate_radius_pythagorean(self):
        Point = namedtuple('Point', ['x', 'y'])
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        expected = 2.5
        actual = generate_radius(p1, p2)
        self.assertEqual(actual, expected)

    def test_generate_radius_shift(self):
        Point = namedtuple('Point', ['x', 'y'])
        p1 = Point(1, 1)
        p2 = Point(4, 5)
        expected = 2.5
        actual = generate_radius(p1, p2)
        self.assertEqual(actual, expected)

    def test_generate_midpoint(self):
        Point = namedtuple('Point', ['x', 'y'])
        p1 = Point(1, 1)
        p2 = Point(3, 3)
        expected = Point(2, 2)
        actual = generate_midpoint(p1, p2)
        self.assertEqual(actual, expected)
