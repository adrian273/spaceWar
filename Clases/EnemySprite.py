import pygame
import Missile
from random import randint

class enemySprite(pygame.sprite.Sprite):


    def __init__(self, posx, posy, distance, spriteOne, spriteTwo):
        pygame.sprite.Sprite.__init__(self)
        self.spriteE1 = pygame.image.load(spriteOne)
        self.spriteE2 = pygame.image.load(spriteTwo)

        self.listEnemy = [self.spriteE1, self.spriteE2]
        self.posImagen = 0
        self.spriteE = self.listEnemy[self.posImagen]

        self.rect = self.spriteE.get_rect()
        self.rect.top = posy
        self.rect.left = posx

        self.speedShoot = 2
        self.speedE = 5
        self.listShootE = []

        self.timeChange = 1
        self.rangeShoot = 1

        self.RIGTH = True
        self.count = 0
        self.maxDecline = self.rect.top + 40

        self.limitRight = posx + distance
        self.limitLeft = posx - distance

    def drawEnemy(self, surface):
        self.spriteE = self.listEnemy[self.posImagen]
        surface.blit(self.spriteE, self.rect)

    ''' comportamiento de enemigo '''
    def behaviorEnemy(self, time):
        self.__moveEnemy()
        self.__attackEnemy()
        if self.timeChange == time:
            self.posImagen += 1
            self.timeChange += 1
            if self.posImagen > len(self.listEnemy) - 1 :
                self.posImagen = 0


    def __moveEnemy(self):
        if self.count - 3:
            self.__moveSide()
        else :
            self.__declineEnemy()

    def __attackEnemy(self):
        if (randint(0,100) < self.rangeShoot):
            self.__shootEnemy()

    def __shootEnemy(self):
        x,y = self.rect.center
        missileEnemy = Missile.missile(x, y, 'sprites/balaFire.png', False)
        self.listShootE.append(missileEnemy)

    def __declineEnemy(self):
        if self.maxDecline == self.rect.top:
            self.count = 0
            self.maxDecline = self.rect.top + 10
        else :
            self.rect.top += 1

    def __moveSide(self):
        if self.RIGTH is True:
            self.rect.left = self.rect.left + self.speedE
            if self.rect.left > self.limitRight:
                self.RIGTH = False
                self.count += 1
        else :
            self.rect.left = self.rect.left - self.speedE
            if self.rect.left < self.limitLeft:
                self.RIGTH = True
