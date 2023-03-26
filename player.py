import pygame

from settings import *

class Player:

    def __init__(self, screen, velocity, max_speed, oil_tank_size):
        self.screen = screen
        self.current_speed = 0
        self.velocity = velocity
        self.max_speed = max_speed
        self.image = pygame.image.load("sprite/Topdown_vehicle_sprites_pack/Car.png")
        self.brake_on_image = pygame.image.load("sprite/Topdown_vehicle_sprites_pack/brake_on.png")
        self.x = ( WIDTH - self.image.get_width() ) //2
        self.y = HEIGHT - self.image.get_height()
        self.box = pygame.Rect( 79,17, 93,215 )
        self.rect = pygame.Rect( self.x+self.box.x,self.y+self.box.y, self.box.width,self.box.height )
        self.total_distance = 0
        self.oil_tank_size = oil_tank_size
        self.oil = oil_tank_size
        self.oil_comsumption = 0.001 # 1 millième de la vitesse
        self.brake_on = False

    def accelerate(self):
        self.brake_on = False
        if self.oil > 0:
            self.current_speed += self.velocity
        else:
            self.brake()
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        self.travel_distance()
        self.compute_consumption()

    def brake(self):
        self.brake_on = True
        self.current_speed -= self.velocity
        if self.current_speed < 0:
            self.current_speed = 0
        self.travel_distance()

    def draw(self):
        #pygame.draw.rect(self.screen, (0,0,0), ( self.x+79,self.y+17, 93,215 ))
        self.screen.blit( self.image, (self.x, self.y), (0,0,256,256))
        if self.brake_on:
            self.screen.blit( self.brake_on_image, (self.x, self.y), (0,0,256,256))

    def move_left(self):
        if self.current_speed > 0:
            self.x -= 10
            self.rect.x = self.x + self.box.x
            self.rect.y = self.y+self.box.y

    def move_right(self):
        if self.current_speed > 0:
            self.x += 10
            self.rect.x = self.x+self.box.x
            self.rect.y = self.y+self.box.y

    def travel_distance(self):
        self.total_distance += self.current_speed * 4.84/215

    def compute_consumption(self):
        self.oil -= self.oil_comsumption * self.current_speed
        if self.oil < 0:
            self.oil = 0

    def fill_tank(self, oil):
        self.oil = self.oil + oil
        if self.oil > self.oil_tank_size:
            self.oil = self.oil_tank_size
