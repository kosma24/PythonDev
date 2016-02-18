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
        self.vely = 5
        self.jumping = False
        self.go_down = False

    def motion(self, WINDOW_WIDTH, WINDOW_HEIGHT, FLOORLEVEL):

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

        self.__jump(WINDOW_HEIGHT, FLOORLEVEL)

    def __jump(self, WINDOW_HEIGHT, FLOORLEVEL):
        max_jump = FLOORLEVEL - 100
        if self.jumping:

            if self.rect.y < max_jump:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.vely
                predictedLocation = self.rect.y + self.vely
                if predictedLocation > FLOORLEVEL:
                    self.jumping = False
                    self.go_down = False

            else:
                self.rect.y -= self.vely
