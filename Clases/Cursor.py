import pygame

class cursor:


    def __init__(self, x, y, dy):
        self.image = pygame.image.load('sprites/balaFire.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_init = y
        self.dy = dy
        self.y = 0
        self.select(0)

    def update(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def select(self, index):
        self.to_y = self.y_init + index * self.dy

    def draw(self, surface):
        surface.blit(self.image, self.rect)
