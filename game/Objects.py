import pygame
from Config import *
from GameObject import *

class Block(GameObject):

    List = pygame.sprite.Group()

    def __init__(self, ID, x, y, imageString, scale):
        GameObject.__init__(self, ID, x, y, imageString, scale)
        Block.List.add(self)
