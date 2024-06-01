import PointWalker as PointWalker
import math
from settings import *

def start(n: int):
    l = (height / (2 ** min(n, 11))) * max(math.sqrt(min(n, 11)), 1) / 2 

    points = []
    walker = PointWalker.Point((width / 2,height / 2), -90)
    points.append(walker.get_pos())
    points.append(walker.forward(l))
    string = ''
    if n > 0:
        string = 'R'
        for _ in range(n - 1):
            newstr = list(string)
            newstr[math.floor(len(newstr) / 2)] = 'L'
            string += 'R'
            string += ''.join(newstr)
    return draw(string, l, points, walker)

def draw(instructions: str, lenght: float, points: list, walker: PointWalker.Point):
    for i in instructions:
        if i == 'R':
            walker.right(-90)
        elif i == 'L':
            walker.left(-90)
        else:
            continue
        walker.set_angle(round(walker.get_angle()))
        points.append(walker.forward(lenght))
    return points