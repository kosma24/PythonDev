import pygame

class GameObject(pygame.sprite.Sprite):

    container = pygame.sprite.Group()

    def __init__(self, ID, (x, y), imageString, scale):
        pygame.sprite.Sprite.__init__(self)
        GameObject.container.add(self)
        self.ID = ID
        self.scale = scale
        self.image = pygame.image.load(imageString)

        self.width = self.image.get_rect().width * self.scale
        self.height = self.image.get_rect().height * self.scale

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loadImages(self, imagePaths):
        images = []
        for imagePath in imagePaths:
            img = pygame.image.load(imagePath)
            w = img.get_rect().width * self.scale
            h = img.get_rect().height * self.scale
            img = pygame.transform.scale(img, (w, h))
            images.append(img)

        return images

    def delete(self, ClassName):
        GameObject.container.remove(self)
        ClassName.List.remove(self)
        del self
