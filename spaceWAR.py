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

def spaceWAR():
    ''' iniciando PYGAME '''
    pygame.init()

    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
    pygame.display.set_caption(' Space War v0.0.1')
    while True :
        ''' eventos '''
        for event in pygame.event.get():
            ''' para salir del juego '''
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    spaceWAR()
