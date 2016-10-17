''' <! {-KDRscript} > '''
#!/usr/bin/env python
# coding=utf-8

''' importando librerias '''
import pygame
import sys
from pygame.locals import *
from Clases import AircrafWar
from Clases import BackgroundGame as Background
from Clases import EnemySprite


''' Constantes '''
WIDTH = 900
HEIGHT = 680
LISTE = [] # lista de los enemigos


def loadEnemy():
    posx = 100
    for e in range(1, 5):
        enemy = EnemySprite.enemySprite(posx, 200, 400, 'sprites/enemi1.png', 'sprites/enemi1.png')
        LISTE.append(enemy)
        posx = posx + 200

    posx = 100
    for e in range(1, 5):
        enemy = EnemySprite.enemySprite(posx, 100, 400, 'sprites/enemi1.png', 'sprites/enemi1.png')
        LISTE.append(enemy)
        posx = posx + 200

    posx = 100
    for e in range(1, 5):
        enemy = EnemySprite.enemySprite(posx, 0, 400, 'sprites/enemi1.png', 'sprites/enemi1.png')
        LISTE.append(enemy)
        posx = posx + 200

def spaceWAR():
    ''' iniciando PYGAME '''
    pygame.init()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(' Space War v0.0.1')
    pygame.mixer.music.load('sounds/intro.mp3')
    pygame.mixer.music.play(3)
    ''' creando los objetos '''
    BACKGROUND = Background.backgroundGame('sprites/fondo-espacial.jpg')
    PLAYER = AircrafWar.aircrafWar(WIDTH,HEIGHT)
    #ENEMY = EnemySprite.enemySprite(100,100)
    TIME = pygame.time.Clock()
    loadEnemy()

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
                elif event.key == K_UP:
                    PLAYER.moveTop()
                elif event.key == K_DOWN:
                    PLAYER.moveBottom()
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()

        if len(PLAYER.listShoot) > 0:
            for player in PLAYER.listShoot:
                player.drawMissile(SCREEN)
                player.moveMissile()
                if player.rect.top < -10:
                    PLAYER.listShoot.remove(player)
                else:
                    for e in LISTE:
                        if player.rect.colliderect(e.rect):
                            LISTE.remove(e)
                            PLAYER.listShoot.remove(player)

        if len(LISTE) > 0:
            for e in LISTE:
                e.behaviorEnemy(TIME2)
                e.drawEnemy(SCREEN)
                if e.rect.colliderect(PLAYER.rect):
                    pass
                if len(e.listShootE) > 0:
                    for m in e.listShootE:
                        m.drawMissile(SCREEN)
                        m.moveMissile()
                        if m.rect.colliderect(PLAYER.rect):
                            pass
                        if m.rect.top > 880:
                            e.listShootE.remove(m)
                        else:
                            for d in PLAYER.listShoot:
                                if m.rect.colliderect(d.rect):
                                    PLAYER.listShoot.remove(d)
                                    e.listShootE.remove(m)


        PLAYER.drawSpriteAircrafWar(SCREEN)
        pygame.display.update()

if __name__ == '__main__':
    spaceWAR()
