import pygame

class option:
    def __init__(self, font, title, x, y, reference, functionAssigned):
        self.imageNormal = font.render(title, 1, (255,255,255))
        self.imageVIP = font.render(title, 1, (200, 0, 0))
        self.image = self.imageNormal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * reference
        self.rect.y = y
        self.functionAssigned = functionAssigned
        self.x = float(self.rect.left)

    def update(self):
        destiny_x = 105
        self.x  += (destiny_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def spotlight(self, status):
        if status:
            self.image = self.imageVIP
        else:
            self.image = self.imageNormal

    def activate(self):
        self.functionAssigned()
