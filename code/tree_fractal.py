import PointWalker #type:ignore
import math
from settings import * #type:ignore

alpha = 53
beta = 90 - alpha

def start(n: int):
    string = makestr(n)
    ret =  followstr(string, n)
    print(string)
    return ret
    
    
    
def makestr(n):
    start = "FFLOBRROBL"
    rules = {
            "O": "FFLOBRROBL",
            "F": "FF",
            "B": "BB"
            }
    
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

def followstr(string, n) -> list[tuple]:
    walker = PointWalker.Point((width / 2, 599), -90)
    l = height / (2 ** (n + 2))
    points = [walker.get_pos()]
    for char in string:
        if char == "F" or char == "O":
            points.append(walker.forward(l))
        elif char == "B":
            points.append(walker.backward(l))
        elif char == "L":
            walker.left(45)
        elif char == "R":
            walker.right(45)
            
    return points

if __name__ == "__main__":
    string = makestr(1)
    
