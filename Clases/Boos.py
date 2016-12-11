import pygame
import Missile
from random import randint


class boos(pygame.sprite.Sprite):

    def __init__(self, posx, posy, distance, spriteOne):
        pygame.sprite.Sprite.__init__(self)
        self.spriteBoos = pygame.image.load(spriteOne)

        self.rect = self.spriteBoos.get_rect()
        self.rect.top = posy
        self.rect.left = posx

        self.speedShoot = 2
        self.speedE = 5
        self.listShootB = []

        self.timeChange = 1
        self.rangeShoot = 1

        self.conquest = False

        self.RIGTH = True
        self.count = 0
        self.maxDecline = self.rect.top + 100

        self.limitRight = posx + distance
        self.limitLeft = posx - distance

    def drawBoos(self, surface):
        surface.blit(self.spriteBoos, self.rect)

    ''' comportamiento de enemigo '''
    def behaviorBoos(self, time):
        if self.conquest == False:
            self.__moveEnemy()
            self.__attackEnemy()
            if self.timeChange == time:
                self.posImagen += 1
                self.timeChange += 1
                if self.posImagen > len(self.listEnemy) - 1:
                    self.posImagen = 0

    def __moveEnemy(self):
        if self.count - 3:
            self.__moveSide()
        else:
            self.__declineEnemy()

    def __attackEnemy(self):
        if (randint(0, 100) < self.rangeShoot):
            self.__shootEnemy()

    def __shootEnemy(self):
        x, y = self.rect.center
        missileEnemy = Missile.missile(x, y, 'sprites/balaEnemy2.png', False)
        self.listShootB.append(missileEnemy)

    def __declineEnemy(self):
        if self.maxDecline == self.rect.top:
            self.count = 0
            self.maxDecline = self.rect.top + 10
        else:
            self.rect.top += 1

    def __moveSide(self):
        if self.RIGTH is True:
            self.rect.left = self.rect.left + self.speedE
            if self.rect.left > self.limitRight:
                self.RIGTH = False
                self.count += 1
        else:
            self.rect.left = self.rect.left - self.speedE
            if self.rect.left < self.limitLeft:
                self.RIGTH = True
