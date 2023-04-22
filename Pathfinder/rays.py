import pygame, math, sys, colors
from pygame.locals import *
from ray import Ray, Rayball, Vector2D
import scipy.spatial

(mouseX, mouseY) = (0,0)
RAYLENGTH = 1000

walls = [([400,0],[400,400]),
         ([400,400],[400,800]),
         ([400,800],[0,400]),
         ([0,400],[400,0]),
         ([200,0],[500,400])]

ballpos = (0,0)
balldir = (0,0)
ball = None

pygame.init()
pygame.display.set_caption('- - - Hello world - - -')
(screenX, screenY) = 800, 800
screen = pygame.display.set_mode((screenX, screenY))
screen.fill(colors.GAME1)

def getInput():
    global mouseX, mouseY, ballpos, balldir, ball
    keystate = pygame.key.get_pressed()
    (mouseX, mouseY) = pygame.mouse.get_pos()

    # Quit event
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            ballpos = (mouseX, mouseY)
            if not ball:
                ball = Rayball(ballpos, 0)
            else:
                ball.update(ballpos, 0)
        if event.type == QUIT or (keystate[K_LCTRL] and keystate[K_q]):
            pygame.quit(); sys.exit()
    if ball:
        try:
            dx = mouseX - ball.pos[0]
            dy = mouseY - ball.pos[1]
            addpi = math.pi
            if dx > 0:
                addpi = 0
            lookat = math.atan(dy/dx) + addpi
            ball.update(ball.pos, lookat)
        except:
            pass

def draw():
    screen.fill(colors.GAME1)
    for wall in walls:
        pygame.draw.line(screen, colors.WHITE, wall[0], wall[1], 1)

    if ball:
        pygame.draw.circle(screen, colors.WHITE, ballpos, 4)
        for r in ball.rays:
            endpos = (ball.pos[0] + r.dirx * RAYLENGTH, ball.pos[1] + r.diry * RAYLENGTH)
            hitpoint = None
            dist = 10000
            for w in walls:
                # ra = Vector2D(ball.pos[0],ball.pos[1])
                # rb = Vector2D(ball.pos[0] + r.dirx * 100, ball.pos[1] + r.diry * 1000)
                # wa = Vector2D(w[0][0],w[0][1])
                # wb = Vector2D(w[1][0],w[1][1])
                x1 = ball.pos[0]
                y1 = ball.pos[1]
                x2 = ball.pos[0] + r.dirx * 1000
                y2 = ball.pos[1] + r.diry * 1000
                x3 = w[0][0]
                y3 = w[0][1]
                x4 = w[1][0]
                y4 = w[1][1]
                den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                unum = (x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)
                tnum = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
                if den != 0:
                    t = tnum/den
                    u = -unum/den
                    if 0 <= u <= 1 and 0 <= t <= 1:
                        px = x3+u*(x4-x3)
                        py = y3+u*(y4-y3)
                        if scipy.spatial.distance.euclidean((px,py),(x1,x2)) < dist:
                            dist = scipy.spatial.distance.euclidean((px,py),(x1,x2))
                            hitpoint = (px, py)
            if hitpoint:
                pygame.draw.line(screen, colors.WHITE, ball.pos, hitpoint, 1)
            # pygame.draw.line(screen, colors.BLUE, ball.pos, endpos, 1)
while True:

    getInput()
    draw()
    pygame.display.flip()
