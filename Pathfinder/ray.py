import math

class Ray():
    def __init__(self, angle):
        self.angle = angle
        self.dirx = math.cos(angle)
        self.diry = math.sin(angle)
    def update(self, angle):
        self.angle = angle
        self.dirx = math.cos(self.angle)
        self.diry = math.sin(self.angle)
    def dir(self, length):
        return (self.dirx * length, self.diry * length)

class Rayball():
    def __init__(self, position, rotation):
        self.pos = position
        self.rot = rotation
        self.r = Ray(rotation - math.pi/2)
        self.rf = Ray(rotation - math.pi/4)
        self.f = Ray(rotation)
        self.lf = Ray(rotation + math.pi/4)
        self.l = Ray(rotation + math.pi/2)
        self.rays = [self.r, self.rf, self.f, self.lf, self.l]
    def update(self, position, rotation):
        self.pos = position
        self.rot = rotation

        self.r.update(rotation - math.pi/2)
        self.rf.update(rotation - math.pi/4)
        self.f.update(rotation)
        self.lf.update(rotation + math.pi/4)
        self.l.update(rotation + math.pi/2)

class Vector2D():
    '''A point or a 2-dimensional vector'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
