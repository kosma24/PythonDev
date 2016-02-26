import pygame
import math
from Config import *
from GameObject import *

class Block(GameObject):

    List = pygame.sprite.Group()

    def __init__(self, ID, x, y, imageString, scale):
        GameObject.__init__(self, ID, x, y, imageString, scale)
        Block.List.add(self)


class Swing(pygame.sprite.Sprite):

    List = pygame.sprite.Group()

    def __init__(self, Player, cursor):
        pygame.sprite.Sprite.__init__(self)
        Swing.List.add(self)

        self.center = Player.rect.center
        self.cursor = cursor
        self.endPoint = self.__get_outer_point()

    def slash(self):
        pass

    def __fadeOut(self):
        pass

    def __delete(self):
        pass

    def __get_inner_point(self):
        pass

    def __get_outer_point(self):
        cursorX = float(self.cursor[0] - self.center[0])
        cursorY = float(self.cursor[1] - self.center[1])

        theta = math.degrees(math.atan(float(cursorY / cursorX)))
        alfa = theta + 35
        y = math.sin(math.radians(alfa)) * 75
        x = math.sqrt(math.pow(75, 2) - math.pow(y, 2))
        y = int(y + self.center[1])
        x = int(x + self.center[0])
        point = (x, y)
        return point
        # math.atanh(x)
