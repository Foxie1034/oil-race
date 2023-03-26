import pygame

from settings import *

class AbstractGauge:

    GAUGE_WIDTH  = 309
    GAUGE_HEIGHT = 309

    def __init__(self, screen, x, y, type, max, orientation, init_value):
        self.font = pygame.font.SysFont("comicsansms", 22)
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
        self.draw_message((211,211,210), self.x + self.GAUGE_WIDTH//2, self.y++ self.GAUGE_HEIGHT//2 - 50, f"{int(self.current_value)}")

    def draw_message(self, color, x, y, message):
        text_img = self.font.render(message, True, color)
        self.screen.blit(text_img, (x - text_img.get_width()//2, y - text_img.get_height()//2))


class OilGauge(AbstractGauge):

    def __init__(self, screen, oil_tank_size):
        super().__init__(screen, x=0, y=0, type="oil", max=oil_tank_size, orientation="flip", init_value=oil_tank_size)



class SpeedGauge(AbstractGauge):

    def __init__(self, screen, max_speed):
        super().__init__(screen, x=WIDTH - self.GAUGE_WIDTH, y=0, type="speed", max=max_speed, orientation="standard", init_value=0)


