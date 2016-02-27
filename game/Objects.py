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
    Count = 0
    def __init__(self, playerPos, cursor, degree):
        pygame.sprite.Sprite.__init__(self)
        Swing.List.add(self)
        Swing.Count += 1
        self.playerPos = playerPos
        self.center = playerPos.center
        self.cursor = cursor
        self.degree = degree
        self.startPoint = self.__getSwingPoint(45)
        self.endPoint = self.__getSwingPoint(150)
        self.framesToLive = 1

    def slash(self):

        if Swing.Count < 10:
            Swing(self.playerPos, self.cursor, self.degree-25)
        self.__delete()


    def __fadeOut(self):
        pass

    def __delete(self):
        Swing.List.remove(self)
        del self

    def __getSwingPoint(self, lengthFromCenter):
        cursorX = float(self.cursor[0] - self.center[0])
        cursorY = float(self.cursor[1] - self.center[1])
        if cursorY == 0:
            cursorY == 1
        if cursorX == 0:
            cursorX = 1

        theta = math.degrees(math.atan(float(cursorY / cursorX)))
        alfa = theta -self.degree
        y = math.cos(math.radians(alfa)) * lengthFromCenter
        x = math.sqrt(math.pow(lengthFromCenter, 2) - math.pow(y, 2))
        y = int(y + self.center[1])
        x = int(x + self.center[0])
        return (x, y)
