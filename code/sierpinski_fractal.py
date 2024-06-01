import Point_Walker
import math
from settings import *

def fractal(n: int, l: float, points: list, walker: Point_Walker.Point):
    if n == 0:
        #*draw a triangle
        points.append(walker.forward(l))
        walker.left(120)
        points.append(walker.forward(l))
        walker.left(120)
        points.append(walker.forward(l))
        walker.left(120)
    else:
        fractal(n, l, points, walker)

def start(n: int):
    l = width

    walker = Point_Walker.Point((0, height - 1), -60)

    points = [walker.get_pos()]

    fractal(n, l, points, walker)

    print(points)

    return points