import pygame

GRAVITY = 1.5
WALKING_ACCELERATION = 0.5
RUNNING_ACCELERATION = 0.7
WALKING_THRESHOLD = 5
MAX_SPEED = 12

class BaseClass(pygame.sprite.Sprite):

    spriteContainer = pygame.sprite.Group()

    def __init__(self, x, y, width, height, imageString, scale):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.spriteContainer.add(self)

        self.width = width * scale
        self.height = height * scale

        self.image = pygame.image.load(imageString)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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
        self.walking = False
        self.running = False

    def motion(self, WINDOW_WIDTH, WINDOW_HEIGHT, FLOORLEVEL):
        # Horizontal velocity + sprite's width
        predictedLocation = self.rect.x + self.velx

        # PREVENTING SPIRTE GOING OF THE WINDOW
        if predictedLocation < 0:
            self.velx = 0
        elif predictedLocation + self.width > WINDOW_WIDTH:
            self.velx = 0

        if self.velx >= 12:
            self.velx = 12
        elif self.velx <= -12:
            self.velx = -12

        # GRAVITY EFFECT
        self.vely += GRAVITY
        # VELOCITY APPLICAITON
        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.walking:
            self.velx += 0.5

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

#  FUNCTIONS / METHODS
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

        if direction == "left":
            if absoluteVelocity <= WALKING_THRESHOLD:
                self.velx -= WALKING_ACCELERATION
            else:
                self.velx -= RUNNING_ACCELERATION

        elif direction == "right":
            if absoluteVelocity <= WALKING_THRESHOLD:
                self.velx += WALKING_ACCELERATION
            else:
                self.velx += RUNNING_ACCELERATION

        else:
            if absoluteVelocity < 0.5:
                self.velx = 0
            else:
                self.velx -= (self.velx * 0.1)
