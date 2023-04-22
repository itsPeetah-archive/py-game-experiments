import pygame, math, sys, colors
from pygame.locals import *

BALL_RADIUS = 10
(mouseX, mouseY) = (0,0)

wall1 = [(200,150),(400,56)]
wall2 = [(15,20),(505,600)]
wall3 = [(240,190),(440,96)]

colliding = False

walls = [wall1, wall2, wall3]

pygame.init()
pygame.display.set_caption('- - - Hello world - - -')
(screenX, screenY) = 800, 800
screen = pygame.display.set_mode((screenX, screenY))
screen.fill(colors.GAME1)

def getInput():
    global mouseX, mouseY
    keystate = pygame.key.get_pressed()
    (mouseX, mouseY) = pygame.mouse.get_pos()

    # Quit event
    for event in pygame.event.get():
        if event.type == QUIT or (keystate[K_LCTRL] and keystate[K_q]):
            pygame.quit(); sys.exit()
def draw():
    if not colliding:
        screen.fill(colors.GAME1)
    else:
        screen.fill(colors.EDIT1)
    for w in walls:
        pygame.draw.line(screen, colors.WHITE, w[0], w[1], 1)
    pygame.draw.circle(screen, colors.WHITE, (mouseX, mouseY), BALL_RADIUS)

def dist(x1, y1, x2, y2, x3, y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1

    norm = px*px + py*py

    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance

    dist = (dx*dx + dy*dy)**.5

    return dist

while True:
    colliding = False
    for w in walls:
        if dist(w[0][0], w[0][1], w[1][0], w[1][1], mouseX, mouseY) < BALL_RADIUS:
            colliding = True
            break
    getInput()
    draw()
    pygame.display.flip()
