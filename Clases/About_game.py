import pygame

class about_game:

    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mov = True
        self.speedMove = 3

    def moveKDR(self):
        if self.mov:
            if self.rect.left < 450:
                self.rect.left += self.speedMove
                self.image = pygame.image.load("sprites/kdrscript.png")
            else:
                self.mov = False
        else:
            if self.rect.right > 400:
                self.rect.right -= self.speedMove
                self.image = pygame.image.load("sprites/kdrscript3.png")
            else:
                self.mov = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)
