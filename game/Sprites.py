import pygame
from Config import *
from GameObject import *
from Objects import *


class Player(GameObject):

    List = pygame.sprite.Group()

    def __init__(self, ID, x, y, imageString, scale):
        GameObject.__init__(self, ID, x, y, imageString, scale)
        Player.List.add(self)
        self.velx = 0
        self.vely = 0
        self.state = {
            'standing' : True,
            'movingLeft' : False,
            'movingRight' : False,
            'onGround' : True,
            'jumping' : False,
            'allowedToJump' : True
        }
        self.standingImages = self.loadImages(("images/standing1.png", "images/standing2.png"))
        self.currentStandingImage = 0

    ##########################################################
    ##                 FUNCTIONS / METHODS
    ##########################################################

    def motion(self, totalFrames):

        self.__runControl()

        # GRAVITY EFFECT
        self.vely += GRAVITY

        if self.vely < 2.5:
            self.state['onGround'] = False

        # MOVING EFFECT
        self.rect.left += self.velx
        self.collide(self.velx, 0, Block.List)
        self.rect.top += self.vely
        self.collide(0, self.vely, Block.List)

        # JUMPING MOTION
        self.__jumpMotion()

        # ANIMATIONS
        self.__animation(totalFrames)

    def __jumpMotion(self):
        if self.state['jumping']:
            self.__startJump()
        else:
            self.__endJump()

    def __startJump(self):
        if self.state['allowedToJump']:
            if self.state['onGround']:
                self.vely -= JUMP_VALUE
                self.state['onGround'] = False
                self.state['allowedToJump'] = False

    def __endJump(self):
        if self.state['onGround']:
            self.state['allowedToJump'] = True
            self.valy = 0
        elif self.vely < -MAX_FALLING_SPEED:
            self.vely = -MAX_FALLING_SPEED

    def run(self, direction):
        absoluteVelocity = abs(self.velx)
        # MOVE LEFT
        if direction == "left":
            self.__changeStance(False, True, False)
            if not self.velx <= 0:
                self.velx += -(self.velx * 0.2)
            if absoluteVelocity <= WALKING_THRESHOLD or not self.state['onGround']:
                self.velx += -WALKING_ACCELERATION
            else:
                self.velx += -RUNNING_ACCELERATION
        # MOVE RIGHT
        elif direction == "right":
            self.__changeStance(False, False, True)
            if not self.velx >= 0:
                self.velx += -(self.velx * 0.2)
            if absoluteVelocity <= WALKING_THRESHOLD or not self.state['onGround']:
                self.velx += WALKING_ACCELERATION
            else:
                self.velx += RUNNING_ACCELERATION
        # SLOW DOWN
        else:
            self.__changeStance(True, False, False)
            if absoluteVelocity < 0.7:
                self.velx = 0
            else:
                self.velx += -(self.velx * 0.2)

    def __runControl(self):
        if self.velx >= MAX_SPEED:
            self.velx = MAX_SPEED
        elif self.velx <= -MAX_SPEED:
            self.velx = -MAX_SPEED

    def __animation(self, totalFrames):
        if totalFrames % (FPS * 2) == 0:
            if self.state['standing']:
                if self.currentStandingImage == 1:
                    self.image = self.standingImages[0]
                    self.currentStandingImage = 0
                else:
                    self.image = self.standingImages[1]
                    self.currentStandingImage = 1
            elif self.state['movingLeft']:
                pass
            elif self.state['movingRight']:
                pass

    def collide(self, x, y, objectList):
        for obj in objectList:
            if pygame.sprite.collide_rect(self, obj):
                if x > 0:
                    self.rect.right = obj.rect.left
                    self.velx += -1
                if x < 0:
                    self.rect.left = obj.rect.right
                    self.velx += 1
                if y < 0:
                    self.rect.top = obj.rect.bottom
                    self.vely = 4
                if y > 0:
                    self.rect.bottom = obj.rect.top
                    self.state['onGround'] = True
                    self.vely = 0
                #else:
                #    self.state['onGround'] = False

    def __changeStance(self, standing, movingLeft, movingRight):
        self.state['standing'] = standing
        self.state['movingLeft'] = movingLeft
        self.state['movingRight'] = movingRight
