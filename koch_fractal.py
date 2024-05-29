import Point_Walker
from settings import *

walker = Point_Walker.Point()

n = int(input("Enter n: "))

l = width / (3 ** n) * 3



points = []
def fractal(n):
    if n == 0:
        points.append(walker.forward(l))
    else:
        fractal(n-1)
        walker.left(60)
        fractal(n-1)
        walker.right(120)
        fractal(n-1)
        walker.left(60)
        fractal(n-1)
    