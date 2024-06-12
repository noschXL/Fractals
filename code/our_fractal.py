import PointWalker
import math
from settings import *

def makestr(n):
    start = "F--F--F"
    
    rules = {"F": "-F--F--F--F-"}
    
    newstr = start
    for _ in range(n):
        newstr = ""
        for char in start:
            try:
                newstr += rules[char]
            except KeyError:
                newstr += char

        start = newstr

    return start


def followstr(string, n):
    div = 1
    for _ in range(n):
        div *= 2
        div += 1
    l = width / (3**n)
    walker = PointWalker.Point((0, height - 1), 90)
    walker.right()
    for char in string:
        if char == "F":
            walker.forward(l)
        elif char == "+":
            walker.left(60)
        elif char == "-":
            walker.right(60)
        walker.angle = round(walker.angle)
            
    return walker.points
            

def start(n):
    string = makestr(n)
    print(string)
    return followstr(string, n)
    