import pygame

class missile(pygame.sprite.Sprite):
    def __init__(self, posx, posy, route, character):
        pygame.sprite.Sprite.__init__(self)
        self.missileImg = pygame.image.load(route)

        self.rect = self.missileImg.get_rect()
        self.rect.top = posy
        self.rect.left = posx
        self.speedMissile = 5

        self.shootCharacter = character

    def moveMissile(self):
        if self.shootCharacter is True :
            self.rect.top = self.rect.top - self.speedMissile
        else :
            self.rect.top = self.rect.top + self.speedMissile

    def drawMissile(self, surface):
        surface.blit(self.missileImg, self.rect)
