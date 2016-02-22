#! /usr/bin/python

import pygame
import sys
from Config import *
from GameObject import *
from Sprites import *
from Objects import *
from Processes import *
from Classes import *

pygame.init()

# WINDOW
pygame.display.set_caption("Player Game by MaTi DevTeam")
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
player = Player(50, FLOORLEVEL, 22, 29, "images/pirate_standing1.png", SPRITESCALE)

# LEVEL GENERATOR
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
for row in level:
    for col in row:
        if col == "P":
            Block(x, y, 50, 50, "images/block.png", 1)
        x += 50
    y += 50
    x = 0

# CAMERA
total_level_width  = len(level[0]) * 50
total_level_height = len(level) * 50
camera = Camera(complex_camera, total_level_width, total_level_height)


# ---------- Main Program Loop -------------
while True:
    process(player)
# LOGIC
    # if totalFrames % fiveSecondInterval == 0:

    player.motion(totalFrames)
    # END LOGIC

# DRAW
    #screen.blit(player.image, (player.rect.x, player.rect.y))
    screen.blit(background, (0,0))

    #BaseStructure.container.draw(screen)
    #BaseClass.container.draw(screen)

    camera.update(player)
    for obj in GameObject.container:
        screen.blit(obj.image, camera.apply(obj))

    pygame.display.update()

    # END DRAW
    totalFrames += 1
    clock.tick(FPS)