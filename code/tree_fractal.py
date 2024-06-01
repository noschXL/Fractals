import PointWalker as PointWalker
from settings import *

def start(n: int):
    l = width / (3**n)
    points = []
    walker = PointWalker.Point()
