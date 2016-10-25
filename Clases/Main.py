import pygame
import Cursor
import Option

class main:
    def __init__(self, options):
        self.options = []
        font = pygame.font.Font("Fonts/dejavu.ttf", 20)
        x = 105
        y = 305
        reference = 1
        self.cursor = Cursor.cursor(x - 30, y, 30)

        for title, function in options:
            self.options.append(Option.option(font, title, x, y, reference, function))
            y += 30
            if reference == 1:
                reference = -1
            else:
                reference = 1

        self.select = 0
        self.total = len(self.options)
        self.m_pulse = False

    def update(self):
        k = pygame.key.get_pressed()

        if not self.m_pulse:
            if k[pygame.K_UP]:
                self.select -= 1
            elif k[pygame.K_DOWN]:
                self.select += 1
            elif k[pygame.K_RETURN]:
                self.options[self.select].activate()

        if self.select < 0:
            self.select = 0
        elif self.select > self.total -1:
            self.select = self.total - 1

        self.cursor.select(self.select)
        self.m_pulse = k[pygame.K_UP] or k[pygame.K_DOWN] or k[pygame.K_RETURN]
        self.cursor.update()

        for o in self.options:
            o.update()

    def draw(self, surface):
        self.cursor.draw(surface)

        for option in self.options:
            option.draw(surface)
