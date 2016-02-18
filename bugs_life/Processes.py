import pygame
import sys


def process(pirate):
# MAIN EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# KEY MAPPING AND REACTIONS
    keys = pygame.key.get_pressed()  # returns a list of pressed keys
    if keys[pygame.K_w]:
        pirate.vely = -5
    elif keys[pygame.K_s]:
        pirate.vely = 5
    elif keys[pygame.K_a]:
        pirate.velx = -5
    elif keys[pygame.K_d]:
        pirate.velx = 5
    else:
        pirate.velx = 0
        pirate.vely = 0
