import pygame
from Config import *


class BaseStructure(pygame.sprite.Sprite):

    container = pygame.sprite.Group()

    def __init__(self, x, y, width, height, imageString, scale):
        pygame.sprite.Sprite.__init__(self)
        BaseStructure.container.add(self)

        self.width = width * scale
        self.height = height * scale

        self.image = pygame.image.load(imageString)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Block(BaseStructure):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, imageString, scale):
        BaseStructure.__init__(self, x, y, width, height, imageString, scale)