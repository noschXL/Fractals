import PointWalker as PointWalker
import math
from settings import *

def draw(l: float, string: str,points: list, walker: PointWalker.Point):
    for char in string:
        if char == "F":
            points.append(walker.forward(l))
        elif char == "+":
            walker.left(120)
        elif char == "-":
            walker.right(120)
        elif char == "G":
            points.append(walker.forward(l))

def make_str(n: int):
    start = "F-G-G"

    rules = {"F": "F-G+F+G-F",
             "G": "GG",
             "+": "+",
             "-": "-"}
    
    newstr = start
    for _ in range(n):
        newstr = ""
        for char in start:
            newstr += rules[char]

        start = newstr

    return start

def start(n: int):
    l = width / (2**n)

    points = []
    string = make_str(n)
    walker = PointWalker.Point((0, height - 1))
    points.append(walker.get_pos())
    draw(l, string, points, walker)

    return points