import pygame

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

    def motion(self, WINDOW_WIDTH):

        predictedLocation = self.rect.x + self.velx

        if predictedLocation < 0:
            self.velx = 0
        elif predictedLocation + self.width > WINDOW_WIDTH:
            self.velx = 0

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.width > WINDOW_WIDTH:
            self.rect.x = WINDOW_WIDTH - self.width

        self.rect.x += self.velx
        self.rect.y += self.vely
