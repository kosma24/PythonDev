import pygame
import sys
from Pirate import *
from Processes import process
from Config import *

pygame.init()

# WINDOW
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

background = pygame.image.load("images/background.png")

# CLOCK FPS
clock = pygame.time.Clock()
FPS = 30
fiveSecondInterval = FPS * 5
totalFrames = 0

# OBJECTS
pirate = Pirate(0, FLOORLEVEL, 22, 29, "images/pirate_standing1.png", SPRITESCALE)

# ---------- Main Program Loop -------------
while True:
    process(pirate)
# LOGIC
    totalFrames += 1
    # if totalFrames % fiveSecondInterval == 0:

    pirate.motion(WINDOW_WIDTH, WINDOW_HEIGHT, FLOORLEVEL)
    # END LOGIC

# DRAW
    screen.blit(background, (0,0))
    BaseClass.spriteContainer.draw(screen)
    pygame.display.flip()


    # END DRAW

    clock.tick(FPS)
