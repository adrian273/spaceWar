''' <! {-KDRscript} > '''
#!/usr/bin/env python
# coding=utf-8

'''
    @importando librerias
'''
import pygame
import sys
from pygame.locals import *
from Clases import AircrafWar
from Clases import BackgroundGame as Background
from Clases import EnemySprite
from Clases import Main
from Clases import About_game as about
from Clases import Boos
'''
    __________________________________________________________________________________________________
    @Constantes
'''
WIDTH = 900
HEIGHT = 680
LISTE = []  # lista de los enemigos
LIFEPlAYER = 3
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
ListBoos = [] #lista de jefes

pygame.init()
pygame.display.set_caption(' Space War v0.0.1')
FONT = pygame.font.Font("Fonts/Blazed.ttf", 45)

'''
    __________________________________________________________________________________________________
    @detener juego al ganar el enemigo
'''
def stopAll(type):
    '''
        @ type = True:
            se para el juego al perder contra el enemigo
        @ type = False:
            el jeugo se detiene al perder contra el jefe final
    '''
    if type is True:
        for enemy in LISTE:
            for shoot in enemy.listShootE:
                enemy.listShootE.remove(shoot)
            enemy.conquest = True
    elif type is False:
        for boos in ListBoos:
            for shootB in boos.listShootB:
                boos.listShootB.remove(shootB)
            boos.conquest = True

'''
    __________________________________________________________________________________________________
    @cargar los  enemigos
'''
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
'''
    @cargando el jefe del juego
'''
def loadBoos():
    booss = Boos.boos(100, 0, 400, 'sprites/enemigo.png')
    ListBoos.append(booss)


'''
    __________________________________________________________________________________________________
    @iniciar el juego
'''
def spaceWAR():
    #__________@ muysica del juego ________________________________#
    pygame.mixer.music.load('sounds/intro.mp3')
    pygame.mixer.music.play(3)
    ''' @creando los objetos '''
    BACKGROUND = Background.backgroundGame('sprites/fondo-espacial.jpg')
    PLAYER = AircrafWar.aircrafWar(WIDTH, HEIGHT)
    TIME = pygame.time.Clock()
    TXTtime = pygame.font.SysFont('Arial',20)

    #_______ @cargando las funciones______________________________#
    loadEnemy() #enemigo
    loadBoos() #cargar boos

    #_________ @variables ________________________________________#

    count = 0
    inGame = True #new var
    WINNERPLAYER = False

    while True:

        TIME.tick(60)
        TIME2 = pygame.time.get_ticks() / 1000
        TXTRenderTime = TXTtime.render("Tiempo : " + str(TIME2), 0 , (136, 34, 115))
        BACKGROUND.drawBackground(SCREEN)
        ''' eventos '''
        for event in pygame.event.get():
            ''' para salir del juego '''
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            ''' eventos del teclado '''
            if inGame:
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
            else:
                if event.type == KEYDOWN:
                    if event.key == K_m:
                        spaceWAR()
                        pygame.display.flip()

        #____________@ para dibujar los misiles del jugador______________________________#
        if len(PLAYER.listShoot) > 0:
            for player in PLAYER.listShoot:
                player.drawMissile(SCREEN)
                player.moveMissile()
                if player.rect.top < -10:
                    PLAYER.listShoot.remove(player)
                    print "remove player in pos -10"
                else:
                    for e in LISTE:
                        #________________ @ colision entre jugador-enemigo_________________#
                        if player.rect.colliderect(e.rect):
                            LISTE.remove(e)
                            PLAYER.listShoot.remove(player)
                            count += 10
                            #sacar el largo despues **
                    for b in ListBoos:
                        #_______________@colision entre jugador-boos
                        if player.rect.colliderect(b.rect):
                            ListBoos.remove(b)
                            PLAYER.listShoot.remove(player)
                            count += 20

        #________________________@largo del enemigo_________________________________________#
        if len(LISTE) > 0:
            for e in LISTE:
                #____________ @dibujar enemigo y definir el comportamiento
                WinnerEnemy = True
                e.behaviorEnemy(TIME2)
                e.drawEnemy(SCREEN)
                #________________@colison entre enemigo-jugador
                if e.rect.colliderect(PLAYER.rect):
                    #new modific
                    PLAYER.destroy()
                    inGame = False
                    stopAll(WinnerEnemy)

                #___________________@para dibujar los misiles del enemigo____________________#
                if len(e.listShootE) > 0:
                    for m in e.listShootE:
                        m.drawMissile(SCREEN)
                        m.moveMissile()
                        #______________@colision entre misil y jugador______________________#
                        if m.rect.colliderect(PLAYER.rect):
                                PLAYER.destroy()
                                inGame = False
                                stopAll(WinnerEnemy)
                        #_____________@para remover los misisles del enemigo
                        if m.rect.top > 880:
                            e.listShootE.remove(m)
                        else:
                            for d in PLAYER.listShoot:
                                #__________ @colison entre misisles enemigo y jugador
                                if m.rect.colliderect(d.rect):
                                    PLAYER.listShoot.remove(d)
                                    e.listShootE.remove(m)
                                    count += 3

        #_________________________@largo del jefe______________________________________________#
        if len(LISTE) <= 0:
            if len(ListBoos) > 0:
                WinnerBoos = False
                #________________@ dibujar al jefe del nivel___________________________________#
                for boos in ListBoos:
                    boos.drawBoos(SCREEN)
                    boos.behaviorBoos(TIME2)
                    #_____________@colison entre boos-jugador
                    if boos.rect.colliderect(PLAYER.rect):
                        PLAYER.destroy()
                        inGame = False
                        stopAll(WinnerBoos)
                    #_____________ @largo de los misiles del jefe
                    if len(boos.listShootB) > 0:
                        #________________@dibujar el misil del jefe
                        for missileBoos in boos.listShootB:
                            missileBoos.drawMissile(SCREEN)
                            missileBoos.moveMissile()
                            if missileBoos.rect.colliderect(PLAYER.rect):
                                PLAYER.destroy()
                                inGame = False
                                stopAll(WinnerBoos)

                            else:
                                for x in PLAYER.listShoot:
                                    #______________@colison entre misiles de boos-jugador____________#
                                    if missileBoos.rect.colliderect(x.rect):
                                        PLAYER.listShoot.remove(x)
                                        boos.listShootB.remove(missileBoos)
                                        count += 10

        if len(ListBoos) <= 0:
            WINNERPLAYER = True #juego ganado


        #_______________ @ TEXTOS _______________________________________________________________#
        txtCountEnemy = TXTtime.render("puntos :" + str(count), 0 , (255, 0, 46))
        txtLifePlayer = TXTtime.render("Vidas:" + str(LIFEPlAYER), 0, (255, 0, 46))
        txtGameOver = FONT.render("Game OVER", 0, (255, 0, 0), (255, 255, 255))
        txtWinnerPlayer = FONT.render("Juego Ganado!", 0 ,(255, 0, 0), (255, 255, 255))
        txtTotalPoint = FONT.render("Puntos :" + str(count), 0 , (255, 0, 46), (255, 255, 255))
        #________________@dibujar _______________________________________________________________#

        SCREEN.blit(txtLifePlayer,(390,0))
        SCREEN.blit(txtCountEnemy,(780,0))
        SCREEN.blit(TXTRenderTime,(0,0))
        PLAYER.drawSpriteAircrafWar(SCREEN)

        #_______________@mensajes al acabar el juego______________________________________________#
        if inGame == False:
            pygame.mixer.music.fadeout(3000)
            SCREEN.blit(txtGameOver, (250, 350))

        if WINNERPLAYER == True:
            pygame.mixer.music.fadeout(3000)
            SCREEN.blit(txtWinnerPlayer, (255, 350))
            SCREEN.blit(txtTotalPoint, (300, 450))

        pygame.display.update()

'''
    ________________________________________________________________________________________________________
    @para salir del juego
'''
def exitGame():
    sys.exit(0)

'''
    _________________________________________________________________________________________________________
    @Creditos
'''
def aboutGame():
    posx = WIDTH / 4
    background = Background.backgroundGame('sprites/fondo.jpg')
    aboutG = about.about_game(100,100,"sprites/kdrscript.png")
    aboutA = about.about_game(20,400,"sprites/author.png")
    aboutV = about.about_game(posx,600,"sprites/volver.png")
    while True:
        for event in pygame.event.get():
            ''' para salir del juego '''
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_m:
                    optionGame()

        background.drawBackground(SCREEN)
        aboutG.draw(SCREEN)
        aboutA.draw(SCREEN)
        aboutV.draw(SCREEN)
        aboutG.moveKDR()
        pygame.display.update()

'''
    ________________________________________________________________________________________________________
    @Opciones del juego
'''
def optionGame():
    exit = False

    option = [
        ("Jugar",spaceWAR),
        ("Creditos",aboutGame),
        ("Salir",exitGame)
    ]

    pygame.font.init()
    main = Main.main(option)
    background = Background.backgroundGame('sprites/fondo.jpg')
    TitleMain = FONT.render("Space WAR", 0, (255, 255, 255))
    while not exit:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit = True

        background.drawBackground(SCREEN)
        SCREEN.blit(TitleMain, (250, 150))
        main.update()
        main.draw(SCREEN)

        pygame.display.flip()
        pygame.time.delay(10)

''' _______________________________________________________________________'''

if __name__ == '__main__':
    optionGame()
