import PointWalker as PointWalker
from settings import *

def start(n: int):
    walker = PointWalker.Point((0, height / 2))
    points = [walker.get_pos()]
    l = width / 3 ** n
    fractal(n, l, points, walker)
    return points

    
    
def fractal(n: int, l: float, points, walker):
    if n == 0:
        points.append(walker.forward(l))
    else:
        fractal(n-1, l, points, walker)
        walker.right(60)
        fractal(n-1, l, points, walker)
        walker.left(120)
        fractal(n-1, l, points, walker)
        walker.right(60)
        fractal(n-1, l, points, walker)