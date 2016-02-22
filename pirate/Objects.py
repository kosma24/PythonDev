import pygame
from Config import *
from GameObject import *

class Block(GameObject):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, imageString, scale):
        GameObject.__init__(self, x, y, width, height, imageString, scale)
