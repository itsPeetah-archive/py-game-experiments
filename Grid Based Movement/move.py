import pygame
from pygame.locals import *

(screenWidth, screenHeight) = (400,400)
BLACK = (0,0,0); WHITE = (255,255,255)
gridcellsize = 20
playerradius = int(gridcellsize / 2)

(playerX, playerY) = (4,15)

# PyGame init
pygame.init()
pygame.display.set_caption('Grid based movement study')
screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill(BLACK)



def userinput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit()
    pass




def update():
    pass








def draw():
    # Reset scrren
    screen.fill(BLACK)
    # Draw grid
    for x in range(int(screenWidth/gridcellsize)):
        pygame.draw.line(screen, WHITE, (x*gridcellsize,0),(x*gridcellsize,screenHeight), 1)
    for y in range(int(screenHeight/gridcellsize)):
        pygame.draw.line(screen, WHITE, (0,y*gridcellsize),(screenWidth,y*gridcellsize), 1)
    # Draw player
    # (playercellX, playercellY) = (int(playerX/gridcellsize), int(playerY/gridcellsize))
    playercenter = (playerX*gridcellsize + playerradius, playerY*gridcellsize + playerradius)
    pygame.draw.circle(screen, WHITE, playercenter, playerradius, playerradius)



# Main Loop
while True:
    userinput()
    update()
    draw()
    pygame.display.flip()
