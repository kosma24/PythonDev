#! /usr/bin/python

import pygame
import sys
from Processes import process
from Pirate import *
from Config import *
from Structures import *

pygame.init()

# WINDOW
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

#background = pygame.image.load("images/background.png")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((30, 30, 30))

# CLOCK FPS
clock = pygame.time.Clock()
FPS = 30
totalFrames = 0

# OBJECTS
pirate = Pirate(0, FLOORLEVEL, 22, 29, "images/pirate_standing1.png", SPRITESCALE)

x = y = 0
level = [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                                          P",
    "P                                          P",
    "P                                          P",
    "P                    PPPPPPPPPPP           P",
    "P                                          P",
    "P                                          P",
    "P                                          P",
    "P    PPPPPPPP                              P",
    "P                                          P",
    "P                          PPPPPPP         P",
    "P                 PPPPPP                   P",
    "P                                          P",
    "P         PPPPPPP                          P",
    "P                                          P",
    "P                     PPPPPP               P",
    "P                                          P",
    "P   PPPPPPPPPPP                            P",
    "P                                          P",
    "P                 PPPPPPPPPPP              P",
    "P                                          P",
    "P                                          P",
    "P                                          P",
    "P                                          P",
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
# build the level
for row in level:
    for col in row:
        if col == "P":
            Block(x, y, 50, 50, "images/block.png", 1)
        x += 50
    y += 50
    x = 0
# ---------- Main Program Loop -------------
while True:
    process(pirate)
# LOGIC
    # if totalFrames % fiveSecondInterval == 0:

    pirate.motion(totalFrames)
    # END LOGIC

# DRAW
    #screen.fill(0,0,0)
    #screen.blit(pirate.image, (pirate.rect.x, pirate.rect.y))
    screen.blit(background, (0,0))
    BaseStructure.container.draw(screen)
    BaseClass.container.draw(screen)
    pygame.display.flip()


    # END DRAW
    totalFrames += 1
    clock.tick(FPS)
