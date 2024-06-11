import PointWalker
from settings import *

def start(n):
    l = width / 2 / 3 ** n
    walker = PointWalker.Point((width / 4, 599), -90)
    
    
def fractal(n: int, l: float, right: bool, walker: PointWalker.Point):
    if n == 0:
        if right:
            walker.forward(l)
            walker.right()
            walker.forward(l)
            walker.right()
            walker.forward(l)
        else:
            walker.right()
            walker.forward(l)
            walker.left()
            walker.forward(l)
            walker.left()
            walker.forward(l)
    else:
        fractal(n-1, l, not right, walker)
        walker.right()
        walker.forward(l)
        fractal(n-1, l, not right, walker)
        walker.forward(l)
        fractal(n-1, l, not right, walker)
        walker.right()
        walker.forward(l)
        fractal(n-1, l, not right, walker)
        