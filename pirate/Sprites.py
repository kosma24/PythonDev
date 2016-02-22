import pygame
from GameObject import *
from Config import *


class Pirate(GameObject):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, imageString, scale):
        GameObject.__init__(self, x, y, width, height, imageString, scale)
        Pirate.List.add(self)
        self.velx = 0
        self.vely = 0
        self.jumping = False
        self.onGround = True
        self.allowedToJump = True
        self.standing = True
        self.runningLeft = False
        self.runningRight = False
        self.images = []
        self.images.append(pygame.image.load("images/standing1.png"))
        self.images.append(pygame.image.load("images/standing2.png"))
        self.images[0] = pygame.transform.scale(self.images[0], (self.width, self.height))
        self.images[1] = pygame.transform.scale(self.images[1], (self.width, self.height))
        self.current = 0
        self.image = self.images[0]


    def motion(self, totalFrames):
        # Horizontal velocity + sprite's width
        predictedLocation = self.rect.x + self.velx

        # PREVENTING SPIRTE GOING OF THE WINDOW
        if predictedLocation < 0:
            self.velx = 0
        elif predictedLocation + self.width > WINDOW_WIDTH:
            self.velx = 0

        self.__runControl()
        # GRAVITY EFFECT
        if not self.onGround:
            self.vely += GRAVITY

        # MOVING EFFECt
        self.rect.x += self.velx
        self.rect.y += self.vely

        # PREVENTING SPRITE BEYOND FLOOR LEVEL
        if self.rect.y >= FLOORLEVEL:
            self.rect.y = FLOORLEVEL
            self.vely = 0
            self.onGround = True

        # JUMPING MOTION
        self.__jumpMotion()
        self.__animation(totalFrames)


    ##########################################################
    ##                 FUNCTIONS / METHODS
    ##########################################################
    def __jumpMotion(self):
        if self.jumping:
            self.__startJump()
        else:
            self.__endJump()

    def __startJump(self):
        if self.allowedToJump:
            if self.onGround:
                self.vely = -25
                self.onGround = False
                self.allowedToJump = False

    def __endJump(self):
        if self.onGround:
            self.allowedToJump = True
        elif self.vely < -10:
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
        elif self.onGround:
            if absoluteVelocity < 0.5:
                self.velx = 0
            else:
                self.velx -= (self.velx * 0.2)

    def __runControl(self):
        if self.velx >= MAX_SPEED:
            self.velx = MAX_SPEED
        elif self.velx <= -MAX_SPEED:
            self.velx = -MAX_SPEED

    def __animation(self, totalFrames):
        if totalFrames % (FPS * 2) == 0:
            if self.standing:
                if self.current == 1:
                    self.image = self.images[0]
                    self.current = 0
                else:
                    self.image = self.images[1]
                    self.current = 1
            elif self.runningLeft:
                pass
            elif self.runningRight:
                pass
