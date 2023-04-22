# Modules
import sys
import pygame
from pygame.locals import *
# Custom Modules
import instructions, colors, thoughtprocess
from map import *
from ray import *
from unit import Unit

POPULATION = 50
NNVALUES = 54

instructions.game_help()

pygame.init()
pygame.display.set_caption('- - - Hello world - - -')
(screenX, screenY) = 800, 800
screen = pygame.display.set_mode((screenX, screenY))
screen.fill(colors.GAME1)

spawnpoint = None
walls = []
units = []

def loadmap():
    global spawnpoint, walls

    walls = []
    map_name = input("Map to load: ")
    file = open("maps/" + map_name + ".txt", "r")
    for index, line in enumerate(file):
        linevalues = line.split()
        for i in range(len(linevalues)):
            linevalues[i] = int(linevalues[i])
        if index == 0:
            spawnpoint = Spawnpoint((linevalues[0], linevalues[1]), (linevalues[2],linevalues[3]))
        else:
            newWall = Wall((linevalues[0],linevalues[1]),(linevalues[2],linevalues[3]))
            walls.append(newWall)

def firstgen():
    for x in range(POPULATION):
        tp = thoughtprocess.generaterandom(NNVALUES)

def draw():
    global spawnpoint, walls

    screen.fill(colors.GAME1)
    if spawnpoint:
        pygame.draw.circle(screen, colors.GREEN, (spawnpoint.x, spawnpoint.y), 2)
    for wall in walls:
        pygame.draw.line(screen, colors.WHITE, wall.a, wall.b, 1)
    pygame.display.flip()

def getinput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        # Loading a map
        if keystate[K_LCTRL] and keystate[K_l]:
            loadmap()
        # Quit event
        if event.type == QUIT or (keystate[K_LCTRL] and keystate[K_q]):
            pygame.quit(); sys.exit()




while True:
    getinput()
    draw()
