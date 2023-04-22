import math

class Vector2():
    '''Representing a point or a 2-dimensional vector'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ldistance(self, other):
        '''Linear distance from an other point'''
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Ray():
    '''A ray starting from a point and going in a direction'''
    def __init__(self, start_x, start_y, angle):
        self.start = Vector2(start_x, start_y)
        self.angle = angle
        self.direction = Vector2(math.cos(angle),math.sin(angle))
    def cast(self, length):
        '''Returns the ending point of the ray cast from the starting point for a given length'''
        return (self.start.x + self.direction.x * length, self.start.y + self.direction.y * length)
    def update(self, newstartx, newstarty, newangle):
        self.__init__(self, newstartx, newstarty, newangle)

class Wall():
    '''A line segment from point a to point b'''
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector2(x1, y1)
        self.b = Vector2(x2, y2)

class Spawnpoint():
    '''A point facing a direction'''
    def __init__(self, x, y, dirx, diry):
        self.pos = Vector2(x, y)
        diffx = dirx - x
        diffy = diry - y
        try:
            self.angle = math.atan(diffy/diffx)
        except ZeroDivisionError:
            if diffx >= 0:
                self.angle = 0
            else:
                self.angle = math.pi/2
        self.direction = self.direction = Vector2(math.cos(self.angle),math.sin(self.angle))
