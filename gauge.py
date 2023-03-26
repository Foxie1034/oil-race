import pygame

from settings import *

class AbstractGauge:

    GAUGE_WIDTH  = 309
    GAUGE_HEIGHT = 309

    def __init__(self, screen, x, y, type, max, orientation, init_value):
        if orientation == "standard":
            self.background = pygame.image.load("sprite/gauge/background.png").convert_alpha()
            self.gauge = pygame.image.load("sprite/gauge/gauge.png").convert_alpha()
        else:
            self.background = pygame.transform.flip( pygame.image.load("sprite/gauge/background.png"), True, False).convert_alpha()
            self.gauge = pygame.transform.flip( pygame.image.load("sprite/gauge/gauge.png"), True, False).convert_alpha()
        self.needle = pygame.image.load("sprite/gauge/needle.png").convert_alpha()
        self.type = pygame.image.load(f"sprite/gauge/{type}.png").convert_alpha()
        self.screen = screen
        self.x = x
        self.y = y
        self.current_value = init_value
        self.max = max

    def draw(self):
        self.screen.blit(self.background, (self.x,self.y), (0,0,self.GAUGE_WIDTH,self.GAUGE_HEIGHT) )
        self.screen.blit(self.gauge, (self.x,self.y), (0,0,self.GAUGE_WIDTH,self.GAUGE_HEIGHT) )
        self.screen.blit(self.type, (self.x,self.y), (0,0,self.GAUGE_WIDTH,self.GAUGE_HEIGHT) )
        rotated_needle = pygame.transform.rotate(self.needle, - self.current_value * 180 / self.max)
        rotated_rect = self.needle.get_rect()
        rotated_rect.x += self.x
        rotated_rect.y += self.y
        rotated_rect = rotated_needle.get_rect(center=rotated_rect.center)
        self.screen.blit(rotated_needle, rotated_rect)


class OilGauge(AbstractGauge):

    def __init__(self, screen):
        super().__init__(screen, 0, 0, "oil", 100, "flip", 100)

class SpeedGauge(AbstractGauge):

    def __init__(self, screen):
        super().__init__(screen, WIDTH - self.GAUGE_WIDTH, 0, "speed", 250, "standard", 0)


