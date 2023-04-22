import random

# Base colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Editor
EDIT1 = (96, 10, 20)
EDIT2 = (109, 13, 58)
TRAIN = (11, 61, 142)
SETSPAWN = (147, 76, 8)

# Game
GAME1 = (47, 55, 68)

def random():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
