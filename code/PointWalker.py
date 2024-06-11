import math

class Point:
    def __init__(self, pos: tuple = (0,0), angle: float = 0) -> None:
        if not isinstance(pos, tuple):
            raise TypeError("pos must be a tuple")
        
        if not isinstance(angle, float) and not isinstance(angle, int):
            raise TypeError("angle must be a float")
        
        self.pos = pos
        self.angle = angle
        self.points: list = [self.get_pos()]

    def left(self, angle: float = 90):
        self.angle += angle

    def right(self, angle: float = 90):
        self.angle -= angle

    def forward(self, distance):
        self.pos = (self.pos[0] + distance * math.cos(math.radians(self.angle)), self.pos[1] + distance * math.sin(math.radians(self.angle)))
        self.points.append(self.pos)
        return self.pos
    
    def backward(self, distance):
        self.pos = (self.pos[0] - distance * math.cos(math.radians(self.angle)), self.pos[1] - distance * math.sin(math.radians(self.angle)))
        self.points.append(self.pos)
        return self.pos
    
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos: tuple = (0,0)):
        self.pos = pos
        self.points.append(self.pos)

    def get_angle(self):
        return self.angle
    
    def set_angle(self, angle: float):
        self.angle = angle

    def __add__(self, other):
        return Point((self.pos[0] + other.pos[0], self.pos[1] + other.pos[1]), self.angle + other.angle)
    
    def __sub__(self, other):
        return Point((self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]), self.angle - other.angle)
    
    def __mul__(self, other):
        return Point((self.pos[0] * other, self.pos[1] * other), self.angle * other)
    
    def __truediv__(self, other):
        return Point((self.pos[0] / other, self.pos[1] / other), self.angle / other)
    
def get_angle(points: list[tuple]):
    if not (isinstance(points, list) or isinstance(points, tuple)):
        raise TypeError(f"points is not a list but a {type(points)}")
    if not len(points) == 2:
        raise ValueError(f"points is {len(points)} long and not of lenght 2")
    
    return math.degrees(math.atan2(points[1][0] - points[0][0], points[1][1] - points[0][1]))

def get_distance(points: list[tuple]):
    if not (isinstance(points, list) or isinstance(points, tuple)):
        raise TypeError(f"points is not a list but a {type(points)}")
    if not len(points) == 2:
        raise ValueError(f"points is {len(points)} long and not of lenght 2")
    
    return math.sqrt(abs(((points[0][0] - points[1][0]) ** 2) + (points[0][1] - points[1][1] ** 2)))
