import pygame
from BaseClass import *
from Config import *

class Pirate(BaseClass):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, imageString, scale):
        BaseClass.__init__(self, x, y, width, height, imageString, scale)
        Pirate.List.add(self)
        self.velx = 0
        self.vely = 0
        self.jumping = False
        self.onGround = True
        self.allowedToJump = True

    def motion(self, WINDOW_WIDTH, WINDOW_HEIGHT, FLOORLEVEL):
        # Horizontal velocity + sprite's width
        predictedLocation = self.rect.x + self.velx

        # PREVENTING SPIRTE GOING OF THE WINDOW
        if predictedLocation < 0:
            self.velx = 0
        elif predictedLocation + self.width > WINDOW_WIDTH:
            self.velx = 0

        if self.velx >= MAX_SPEED:
            self.velx = MAX_SPEED
        elif self.velx <= -MAX_SPEED:
            self.velx = -MAX_SPEED

        # GRAVITY EFFECT
        self.vely += GRAVITY

        # MOVING EFFECt
        self.rect.x += self.velx
        self.rect.y += self.vely

        # PREVENTING SPRITE BEYOND FLOOR LEVEL
        if (self.rect.y >= FLOORLEVEL):
            self.rect.y = FLOORLEVEL
            self.vely = 0
            self.onGround = True


        # JUMPING MOTION
        if self.allowedToJump:
            if self.jumping:
                self.__startJump()
            else:
                self.__endJump()

##########################################################
##                 FUNCTIONS / METHODS
##########################################################
    def __startJump(self):
        if self.onGround:
            self.vely = -25
            self.onGround = False
            self.allowedToJump = False

    def __endJump(self):
        if self.vely < -10:
            self.vely = -10

    def run(self, direction):
        absoluteVelocity = abs(self.velx)
        # MOVE LEFT
        if direction == "left":
            if absoluteVelocity <= WALKING_THRESHOLD:
                self.velx -= WALKING_ACCELERATION
            else:
                self.velx -= RUNNING_ACCELERATION
        # MOVE RIGHT
        elif direction == "right":
            if absoluteVelocity <= WALKING_THRESHOLD:
                self.velx += WALKING_ACCELERATION
            else:
                self.velx += RUNNING_ACCELERATION
        # SLOW DOWN
        else:
            if absoluteVelocity < 0.5:
                self.velx = 0
            else:
                self.velx -= (self.velx * 0.1)
