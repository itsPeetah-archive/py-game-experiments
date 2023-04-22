import math
import numpy as np

from neunet import NeuNet
import thoughtprocess
from ray import *
# from collisiondetect import dist

class Unit():
    def __init__(self, startpos, startrot, tp):
        self.pos = startpos
        self.rot = startrot
        self.maxspeed = 5
        self.speed = 0
        self.velocity = (0,0)
        self.tp = tp
        self.nn = NeuNet(self.tp)
        self.sensor = Rayball(startpos, startrot)
        self.alive = True
    def update(self, input):
        if not self.alive:
            return
        nnoutput = self.nn.feed(input)
        rotateamount = nnoutput[0]
        speed = nnoutput[1]
        self.speed = 0.1 + speed * self.maxspeed
        self.rot = self.rot + rotateamount
        self.velocity = np.dot((math.cos(self.rot), math.sin(self.rot)), speed)
        self.pos = np.add(self.pos, self.velocity)
        self.sensor.update(self.pos, self.rot)
    def distfromwall(self, x1, y1, x2, y2):
        px = x2-x1
        py = y2-y1
        norm = px*px + py*py
        u =  ((self.pos[0] - x1) * px + (self.pos[1] - y1) * py) / float(norm)
        if u > 1:
            u = 1
        elif u < 0:
            u = 0
        x = x1 + u * px
        y = y1 + u * py
        dx = x - self.pos[0]
        dy = y - self.pos[1]
        dist = (dx*dx + dy*dy)**.5
        return dist
