import pygame
import sys

def process(player):
    # MAIN EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # KEY MAPPING AND REACTIONS
    keys = pygame.key.get_pressed()  # returns a list of pressed keys

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.image = pygame.image.load("images/pirate_left_move.png")
        player.image = pygame.transform.scale(player.image, (player.width, player.height))
        player.run("left")

    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.image = pygame.image.load("images/pirate_right_move.png")
        player.image = pygame.transform.scale(player.image, (player.width, player.height))
        player.run("right")

    else:
        player.run("stop")

    #  JUMPING REACTIONS
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.jumping = True

    if not keys[pygame.K_w] or keys[pygame.K_UP]:
        player.jumping = False
        #player.allowedToJump = True
