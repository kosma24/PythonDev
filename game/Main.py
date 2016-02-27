#! /usr/bin/python

import pygame
import sys
from Config import *
from GameObject import *
from Objects import *
from Sprites import Player
from Processes import *
from Classes import *

pygame.init()

# WINDOW
pygame.display.set_caption("MaTi DevTeam")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

#background = pygame.image.load("images/background.png")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((20, 20, 20))

# CLOCK FPS
clock = pygame.time.Clock()
totalFrames = 0

# LEVEL GENERATOR
level = Level(2)
level.build()


# OBJECTSw
player = Player(PLAYER, (level.playerSpawnPoint) , "images/pirate_standing1.png", SPRITESCALE)

# CAMERA
total_level_width  = level.width * 50
total_level_height = level.height * 50
camera = Camera(complex_camera, total_level_width, total_level_height)


# ---------- Main Program Loop -------------
while True:
    cursor = pygame.mouse.get_pos()
    playerPos = camera.apply(player)
    camera.update(player)

    # PROCESSES
    process(player, playerPos, cursor)

    # MOTIONS
    player.motion(totalFrames, cursor)


    # SCREEN DRAWING
    screen.blit(background, (0,0))

    for obj in GameObject.container:
        screen.blit(obj.image, camera.apply(obj))


    pygame.draw.line(screen, (25, 76, 190), playerPos.center, cursor, 5)
    #pygame.draw.circle(screen, (190, 75, 24), playerPos.center, int(player.rect.width*0.75), 5)

    for swing in Swing.List:
        pygame.draw.line(screen, (250, 250, 250), swing.startPoint, swing.endPoint, 10)
        swing.slash()


    # UPDATE SCREEN
    pygame.display.update()

    totalFrames += 1
    clock.tick(FPS)
    pygame.time.wait(0)
