import PointWalker
from settings import *

def start(n):
    string = makestr(n)
    return followstr(string, n)
    
    
def makestr(n):
    start = "LF+RFR+FL-"
    
    rules = {"R": "-LF+RFR+FL-",
             "L": "+RF-LFL-FR+"}
    
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
    div = 3 ** n
    l = width / div - 1
    walker = PointWalker.Point((0, height - 1), -90)
    for char in string:
        if char == "F":
            walker.forward(l)
        elif char == "+":
            walker.left()
        elif char == "-":
            walker.right()
    
    return walker.points
        