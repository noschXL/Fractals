import Point_Walker
from settings import *

def start(n: int):
    l = (height / (2 ** (max(n, 1) - 1))) / 2

    points = []
    walker = Point_Walker.Point((width / 2,height / 2), -90)
    points.append(walker.get_pos())
    points.append(walker.forward(l))
    string = ''
    if n > 0:
        string = 'R'
        for _ in range(n):
            new_string = string
            new_string = list(new_string)
            new_string.append("R")
            new_string[len(new_string) - 1] = 'L'
            new_string = ''.join(new_string)
            string += new_string
    return draw(string, l, points, walker)

def draw(instructions: str, lenght: float, points: list, walker: Point_Walker.Point):
    for i in instructions:
        if i == 'R':
            walker.right(-90)
        elif i == 'L':
            walker.left(-90)
        walker.set_angle(round(walker.get_angle()))
        points.append(walker.forward(lenght))
    return points