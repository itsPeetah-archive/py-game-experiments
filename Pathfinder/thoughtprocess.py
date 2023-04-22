from random import random as rnd
from random import randint

def generaterandom(valuecount):
    tp = ""
    for x in range(valuecount):
        n = rnd() * randint(-10,10)
        tp = tp + " " + str(n)
    return tp.strip()

def combine(a, b):
    tps = (a.split(), b.split())
    newtp = ""
    for x in range(54):
        y = randint(0,1)
        n = float(tps[y][x])
        if rnd() < 0.05:
            n = n + rnd()
        newtp = newtp + " " + str(n)
    return newtp.strip()
