import random
import math
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def simulate(iterations, square_size):
    """This will run a monte carlo simulation that generates
    two points inside of a square, connects them to get a midpoint,
    then draws a circle from the midpoint using the radius. It then determines
    if the given point is inside or outside the square.""" 
    
    inside = 0
    outside = 0
    for _ in range(iterations):
        p1 = Point(random.randint(0, square_size), random.randint(0, square_size))
        p2 = Point(random.randint(0, square_size), random.randint(0, square_size))
        center = generate_midpoint(p1, p2)
        radius = generate_radius(p1, p2)
        if is_inside_square(center, radius, square_size):
            inside += 1
        else:
            outside += 1
        
    return inside / iterations


def generate_midpoint(p1: Point, p2: Point) -> Point:
    """Determine the midpoint of two given points."""
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


def generate_radius(p1: Point, p2: Point) -> int:
    """Determine the diameter of a circle from two given points,
    then half it to return the radius."""
    return math.sqrt(abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2) / 2


def is_inside_square(center: Point, radius: int, square_size: int) -> bool:
    """determines if a point is inside or outside the square."""
    return (center.x - radius > 0 and center.x + radius < square_size
                and center.y - radius > 0 and center.y + radius < square_size)


if __name__ == '__main__':
    print(simulate(1_000_000_000, 10_000))
