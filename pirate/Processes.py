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

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        pirate.image = pygame.image.load("images/pirate_left_move.png")
        pirate.image = pygame.transform.scale(pirate.image, (pirate.width, pirate.height))
        pirate.run("left")

    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        pirate.image = pygame.image.load("images/pirate_right_move.png")
        pirate.image = pygame.transform.scale(pirate.image, (pirate.width, pirate.height))
        pirate.run("right")

    else:
        pirate.run("stop")

    #  JUMPING REACTIONS
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        pirate.jumping = True

    if not keys[pygame.K_w] or keys[pygame.K_UP]:
        pirate.jumping = False
        #pirate.allowedToJump = True
