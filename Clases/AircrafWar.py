import pygame
import Missile
''' nave espacial '''


class aircrafWar(pygame.sprite.Sprite):

    ''' iniciando pygame.sprite '''
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.spriteAircrafWar = pygame.image.load('sprites/nave.gif')

        self.rect = self.spriteAircrafWar.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 65

        self.listShoot = []
        self.life = True
        self.speedAircrafWar = 16

        self.soundMissile = pygame.mixer.Sound('sounds/pistola_1.wav')

    ''' dibujar sprite '''
    def drawSpriteAircrafWar(self, surface):
        surface.blit(self.spriteAircrafWar, self.rect)

    def shootMissile(self, x, y):
        myMissile = Missile.missile(x, y, 'sprites/balaFire.png', True)
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

    def moveBottom(self):
        if self.life is True:
            self.rect.bottom += self.speedAircrafWar
            if self.rect.bottom > 680:
                self.rect.bottom = 680
