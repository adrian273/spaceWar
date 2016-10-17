import pygame

class backgroundGame(pygame.sprite.Sprite):
    def __init__(self, backgroundIMG):
        pygame.sprite.Sprite.__init__(self)

        self.backgroundImg = pygame.image.load(backgroundIMG)
        self.rect = self.backgroundImg.get_rect()

    ''' dibujando fondo '''
    def drawBackground(self, surface):
        surface.blit(self.backgroundImg, self.rect)
