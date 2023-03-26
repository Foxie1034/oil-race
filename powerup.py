import pygame
import random

from settings import *

class PowerUp:

    def __init__(self, screen, name, x, y, activation, capacity):
        self.screen = screen
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"sprite/{name}.png")
        self.rect = pygame.Rect(self.x,self.y,self.image.get_width(), self.image.get_height())
        self.velocity = 2
        self.activation = activation
        self.capacity = capacity

    def draw(self):
        if self.activation:
            self.screen.blit(self.image, (self.x,self.y), (0,0,self.image.get_width(),self.image.get_height()) )

    def move(self):
        if self.activation:
            self.y += self.velocity
            self.rect.x = self.x
            self.rect.y = self.y
        if self.y > HEIGHT:
            self.activation = False

    def reset(self):
        if not self.activation:
            self.y = 0
            self.x = random.randint((WIDTH-ROAD_WIDTH)//2, WIDTH - (ROAD_WIDTH//2))
            self.activation = True

class OilTank(PowerUp):

    def __init__(self, screen, activation):
        super().__init__(screen, "oiltank", WIDTH//2, 0, activation, 10)

