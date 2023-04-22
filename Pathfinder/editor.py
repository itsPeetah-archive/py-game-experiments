# Modules
import pygame
from pygame.locals import *
import math, random, sys, threading
import numpy as np
# Custom modules
import colors
from map import Wall, Spawnpoint
import instructions

instructions.editor_help()

gameModes = {
    "view":colors.BLACK,
    "wall_single":colors.EDIT1,
    "wall_continued":colors.EDIT2,
    "train":colors.TRAIN,
    "set_spawn":colors.SETSPAWN,
    }
currentMode = "view"
building = False
wallpos1 = (0,0)
wallpos2 = (0,0)
wallstart = (0,0)

spawnpos = (0,0)
spawndir = (0,0)

pygame.init()
pygame.display.set_caption('view mode')
(screenX, screenY) = 800, 800
screen = pygame.display.set_mode((screenX, screenY))
screen.fill(colors.WHITE)

spawnpoint = None
walls = []

def addWall(a,b):
    newWall = Wall(a,b)
    walls.append(newWall)
    print("Created wall from {} to {}".format(a,b))

def getInput():
    global currentMode
    global wallpos1
    global wallpos2
    global building
    global wallstart
    global walls
    global spawnpos
    global spawndir
    global spawnpoint
    keystate = pygame.key.get_pressed()
    (mouseX, mouseY) = pygame.mouse.get_pos()

    for event in pygame.event.get():
        # Mouse left click detection
        if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            if currentMode in ["wall_single", "wall_continued"]:
                if not building:
                    wallpos1 = (mouseX, mouseY)
                    building = True
                    wallstart = wallpos1
                else:
                    wallpos2 = (mouseX, mouseY)
                    building = False
                    addWall(wallpos1, wallpos2)
                    if currentMode == "wall_continued":
                        building = True
                        wallpos1 = wallpos2
            elif currentMode == "set_spawn":
                spawnpos = (mouseX, mouseY)
                print("Set spawn position")
        # Mouse right click detection
        if pygame.mouse.get_pressed()[2] and event.type == pygame.MOUSEBUTTONDOWN:
            if currentMode == "set_spawn":
                spawndir = (mouseX, mouseY)
                print("Set spawn point direction")
        # Close wall / save spawnpoint
        if keystate[K_RETURN]:
            if currentMode == "wall_continued" and building:
                wallpos2 = wallstart
                building = False
                addWall(wallpos1, wallpos2)
            if currentMode == "wall_single" and building:
                wallpos2 = (mouseX, mouseY)
                building = False
                addWall(wallpos1, wallpos2)
            if currentMode == "set_spawn":
                spawnpoint = Spawnpoint(spawnpos, spawndir)
        # Enter edit mode
        if keystate[K_w]:
            if currentMode == "wall_single":
                currentMode = "wall_continued"
                print("Building continued walls")
                pygame.display.set_caption('continued wall edit mode')
            else:
                currentMode = "wall_single"
                print("Building single walls")
                pygame.display.set_caption('single wall edit mode')
        # Clear all walls
        if keystate[K_c]:
            if currentMode in ["wall_single", "wall_continued"]:
                walls = []
                print("Cleared all walls")
        # Enter view mode:
        if keystate[K_v]:
            currentMode = "view"
            print("Now in view mode")
            pygame.display.set_caption('view mode')
        # Set spawn mode
        if keystate[K_a]:
            currentMode = "set_spawn"
            print("Setting the spawnpoint")
            pygame.display.set_caption('set spawn mode')
        # Saving
        if keystate[K_s]:
            if currentMode in ["wall_single", "wall_continued"]:
                file = open("walls.txt", "w")
                for wall in walls:
                    file.write("{} {} {} {}\n".format(wall.a[0], wall.a[1], wall.b[0], wall.b[1]))
                file.close()
                print("Saved walls")
        # Loading
        if keystate[K_l]:
            if currentMode in ["wall_single", "wall_continued"]:
                walls = []
                file = open("walls.txt", "r")
                for line in file:
                    coords = line.split()
                    a = (int(coords[0]), int(coords[1]))
                    b = (int(coords[2]), int(coords[3]))
                    addWall(a,b)
                file.close()
                print("Loaded walls")
        # Quit event
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()
        # SAVE MAP
        if keystate[K_m]:
            map_name = input("Map file name: ")
            file = open("maps/"+ map_name +".txt", "w")
            file.write("{} {} {} {}\n".format(spawnpoint.x, spawnpoint.y, spawnpoint.dirpos[0], spawnpoint.dirpos[1]))
            for wall in walls:
                file.write("{} {} {} {}\n".format(wall.a[0], wall.a[1], wall.b[0], wall.b[1]))
            file.close()
            print("Map saved")

def draw():
    screen.fill(gameModes[currentMode])
    for wall in walls:
        pygame.draw.line(screen, colors.WHITE, wall.a, wall.b, 1)
    if spawnpoint != None:
        pygame.draw.circle(screen, colors.GREEN, (spawnpoint.x, spawnpoint.y), 5)


while True:
    getInput()
    draw()
    pygame.display.flip()
