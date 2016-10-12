''' <! {-KDRscript} > '''
#!/usr/bin/env python
# coding=utf-8

''' importando librerias '''
import pygame
import sys
from pygame.locals import *
from random import randint

''' Constantes '''
WIDTH = 900
HEIGHT = 680

''' nave espacial '''


class aircrafWar(pygame.sprite.Sprite):

    ''' iniciando pygame.sprite '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.spriteAircrafWar = pygame.image.load('sprites/nave.gif')

        self.rect = self.spriteAircrafWar.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 65

        self.listShoot = []
        self.life = True
        self.speedAircrafWar = 10

        self.soundMissile = pygame.mixer.Sound('sounds/pistola_1.wav')

    ''' dibujar sprite '''
    def drawSpriteAircrafWar(self, surface):
        surface.blit(self.spriteAircrafWar, self.rect)

    def shootMissile(self, x, y):
        myMissile = missile(x, y, 'sprites/balaFire.png', True)
        self.listShoot.append(myMissile)
        self.soundMissile.play()

    ''' movimientos de la nave '''
    def moveLeft(self):
        if self.life is True:
            self.rect.left -= self.speedAircrafWar
            if self.rect.left <= 0:
                self.rect.left = 0

    def moveRight(self):
        if self.life is True:
            self.rect.right += self.speedAircrafWar
            if self.rect.right > 880:
                self.rect.right = 870

    def moveTop(self):
        if self.life is True:
            self.rect.top -= self.speedAircrafWar
            if self.rect.top < 10:
                self.rect.top = 0


''' creando los misiles '''


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

''' enemigo '''


class enemySprite(pygame.sprite.Sprite):


    def __init__(self,posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.spriteE1 = pygame.image.load('sprites/enemigo.png')
        self.spriteE2 = pygame.image.load('sprites/enemig.gif')

        self.listEnemy = [self.spriteE1, self.spriteE2]
        self.posImagen = 0
        self.spriteE = self.listEnemy[self.posImagen]

        self.rect = self.spriteE.get_rect()
        self.rect.top = posy
        self.rect.left = posx

        self.speedShoot = 2
        self.speedE = 20
        self.listShootE = []

        self.timeChange = 1
        self.rangeShoot = 5

        self.RIGTH = True
        self.count = 0
        self.maxDecline = self.rect.top + 40

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
        missileEnemy = missile(x, y, 'sprites/balaFire.png', False)
        self.listShootE.append(missileEnemy)

    def __declineEnemy(self):
        if self.maxDecline == self.rect.top:
            self.count = 0
            self.maxDecline = self.rect.top + 40
        else :
            self.rect.top += 1

    def __moveSide(self):
        if self.RIGTH is True:
            self.rect.left = self.rect.left + self.speedE
            if self.rect.left > 500:
                self.RIGTH = False
                self.count += 1
        else :
            self.rect.left = self.rect.left - self.speedE
            if self.rect.left < 0:
                self.RIGTH = True


''' Fondo de Juego '''


class backgroundGame(pygame.sprite.Sprite):
    def __init__(self, backgroundIMG):
        pygame.sprite.Sprite.__init__(self)

        self.backgroundImg = pygame.image.load(backgroundIMG)
        self.rect = self.backgroundImg.get_rect()

    ''' dibujando fondo '''
    def drawBackground(self, surface):
        surface.blit(self.backgroundImg, self.rect)


def spaceWAR():
    ''' iniciando PYGAME '''
    pygame.init()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(' Space War v0.0.1')
    pygame.mixer.music.load('sounds/intro.mp3')
    pygame.mixer.music.play(3)
    ''' creando los objetos '''
    BACKGROUND = backgroundGame('sprites/fondo-espacial.jpg')
    PLAYER = aircrafWar()
    ENEMY = enemySprite(100,100)
    TIME = pygame.time.Clock()

    while True:
        TIME.tick(60)
        TIME2 = pygame.time.get_ticks() / 1000
        BACKGROUND.drawBackground(SCREEN)
        ''' eventos '''
        for event in pygame.event.get():
            ''' para salir del juego '''
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            ''' eventos del teclado '''
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    PLAYER.moveLeft()
                elif event.key == K_RIGHT:
                    PLAYER.moveRight()
                elif event.key == K_s:
                    x, y = PLAYER.rect.center
                    PLAYER.shootMissile(x, y)
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()

        if len(PLAYER.listShoot) > 0:
            for x in PLAYER.listShoot:
                x.drawMissile(SCREEN)
                x.moveMissile()
            if x.rect.top < -10:
                PLAYER.listShoot.remove(x)
        if len(ENEMY.listShootE) > 0:
            for x in ENEMY.listShootE:
                x.drawMissile(SCREEN)
                x.moveMissile()
            if x.rect.top < -10:
                ENEMY.listShootE.remove(x)
        ENEMY.behaviorEnemy(TIME2)
        ENEMY.drawEnemy(SCREEN)
        PLAYER.drawSpriteAircrafWar(SCREEN)
        pygame.display.update()

if __name__ == '__main__':
    spaceWAR()
