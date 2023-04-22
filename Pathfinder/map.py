from math import sin, cos, atan, pi

class Wall():
    def __init__(self, pos1, pos2):
        self.a = pos1
        self.b = pos2

class Spawnpoint():
    def __init__(self, pos, dir):
        self.x = pos[0]
        self.y = pos[1]
        self.dirpos = dir
        diffx = dir[0] - self.x
        diffy = dir[1] - self.y
        try:
            self.angle = atan(diffy/diffx)
        except ZeroDivisionError:
            self.angle = pi/2
        self.dir = (cos(self.angle), sin(self.angle))
