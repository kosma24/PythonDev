import pygame
import sys


def process(pirate):
# MAIN EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# KEY MAPPING AND REACTIONS
    pressed_keys = pygame.key.get_pressed()  # returns a list of pressed keys
    released_keys = pygame.key.get_released()
    if pressed_keys[pygame.K_a]:
        pirate.image = pygame.image.load("images/pirate_left_move.png")
        pirate.image = pygame.transform.scale(pirate.image, (pirate.width, pirate.height))
        pirate.velx = -5
    elif pressed_keys[pygame.K_d]:
        pirate.image = pygame.image.load("images/pirate_right_move.png")
        pirate.image = pygame.transform.scale(pirate.image, (pirate.width, pirate.height))
        pirate.velx = 5
    else:
        pirate.image = pygame.image.load("images/pirate_standing1.png")
        pirate.image = pygame.transform.scale(pirate.image, (pirate.width, pirate.height))
        pirate.velx = 0

    if pressed_keys[pygame.K_w]:
        pirate.jumping = True
