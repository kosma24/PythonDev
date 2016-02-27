import pygame
import os
from Config import *
from Objects import *

class Camera(object):
    def __init__(self, cameraFunction, width, height):
        self.cameraFunction = cameraFunction
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.cameraFunction(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return pygame.Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, spriteWidth, spriteHeight = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + HALF_WIDTH -(spriteWidth / 2), -t + HALF_HEIGHT -(spriteHeight / 2), w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width - WINDOW_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height - WINDOW_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return pygame.Rect(l, t, w, h)



class Level(object):

    def __init__(self, levelNum):
        self.levelNum = levelNum
        fileName = 'level%d.png' % (levelNum)
        self.map = pygame.image.load(os.path.join('levels', fileName))
        self.width = self.map.get_width()
        self.height = self.map.get_height()
        self.playerSpawnPoint = (100,100)

    def build(self):
        x = 0
        y = 0
        for row in range(0, self.height):
            for col in range(0, self.width):
                colour = self.map.get_at((col, row))
                #print(colour == (0, 0, 0, 255))
                if colour == (0, 0, 0, 255):
                    Block(BLOCK, (x, y), os.path.join('images', 'block.png'), 1)
                elif colour == (0,255,0,255):
                    self.playerSpawnPoint = (x, y)
                x += 50
            y += 50
            x = 0
