from typing import Any
import math

class Point:
    def __init__(self, pos: tuple = (0,0), angle: float = 0) -> None:
        self.pos = pos
        self.angle = angle

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle

    def forward(self, distance):
        self.pos = (self.pos[0] + distance * math.cos(self.angle), self.pos[1] + distance * math.sin(self.angle))
        return self.pos
    
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos

    def get_angle(self):
        return self.angle
    
    def set_angle(self, angle):
        self.angle = angle

    def __add__(self, other):
        return Point((self.pos[0] + other.pos[0], self.pos[1] + other.pos[1]), self.angle + other.angle)
    
    def __sub__(self, other):
        return Point((self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]), self.angle - other.angle)
    
    def __mul__(self, other):
        return Point((self.pos[0] * other, self.pos[1] * other), self.angle * other)
    
    def __truediv__(self, other):
        return Point((self.pos[0] / other, self.pos[1] / other), self.angle / other)