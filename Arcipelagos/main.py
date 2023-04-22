import pygame
from pygame.locals import *
from random import randint
import colors

# Settings
cell_size = 20

pygame.init()
done = False
screen_width, screen_height = 500,500
screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption("Arcipelagos")

px, py = 0, 0

while not done:

    # Get events
    pygame.event.pump()
    event=pygame.event.wait()
    keystate = pygame.key.get_pressed()
    if event.type==QUIT:
        pygame.display.quit()
        break
    elif event.type==VIDEORESIZE:
        screen_width, screen_height = event.dict['size']
        screen=pygame.display.set_mode((screen_width, screen_height),HWSURFACE|DOUBLEBUF|RESIZABLE)
    # Input
    if keystate[K_w]:
        py += 1
    elif keystate[K_s]:
        py -= 1
    elif keystate[K_d]:
        px += 1
    elif keystate[K_a]:
        px -= 1

    # Draw
    screen.fill(colors.SEA)

    # Cycle through the pixels
    for x in range(int(screen_width/cell_size)):
        for y in range(int(screen_height/cell_size)):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
            if (x+y) % 2 == 0: pygame.draw.rect(screen, colors.WHITE, rect)
            else: pygame.draw.rect(screen, colors.BLACK, rect)

    pygame.display.flip()
