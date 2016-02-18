import pygame
import sys
from Classes import *
from Processes import process

pygame.init()

# WINDOW
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)


# CLOCK FPS
clock = pygame.time.Clock()
FPS = 30
fiveSecondInterval = FPS * 5
totalFrames = 0

# OBJECTS
pirate = Pirate(0, 100, 22, 29, "standing1.png", 3)

# ---------- Main Program Loop -------------
while True:
    process(pirate)
# LOGIC
    totalFrames += 1
    # if totalFrames % fiveSecondInterval == 0:

    pirate.motion(WINDOW_WIDTH)
    # END LOGIC

# DRAW
    screen.fill((50,50,50))
    BaseClass.spriteContainer.draw(screen)
    pygame.display.flip()


    # END DRAW

    clock.tick(FPS)
