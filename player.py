import pygame

from settings import *

class Player:

    def __init__(self, screen, velocity, max_speed):
        self.screen = screen
        self.current_speed = 0
        self.velocity = velocity
        self.max_speed = max_speed
        self.image = pygame.image.load("sprite/Topdown_vehicle_sprites_pack/Car.png")
        self.x = ( WIDTH - self.image.get_width() ) //2
        self.y = HEIGHT - self.image.get_height()
        self.box = pygame.Rect( 79,17, 93,215 )
        self.rect = pygame.Rect( self.x+self.box.x,self.y+self.box.y, self.box.width,self.box.height )
        self.total_distance = 0
        self.instant_distance_by_second = 0
        self.current_instant_distance = 0
        self.current_instant_start_time = pygame.time.get_ticks()
        self.oil = 100
        self.oil_comsumption = 0.01
        self.current_action = 'brake'

    def accelerate(self):
        self.current_action = 'accelerate'
        if self.oil > 0:
            self.current_speed += self.velocity
        else:
            self.brake()
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        self.travel_distance()

    def brake(self):
        self.current_action = 'brake'
        self.current_speed -= self.velocity
        if self.current_speed < 0:
            self.current_speed = 0
        self.travel_distance()

    def draw(self):
        #pygame.draw.rect(self.screen, (0,0,0), ( self.x+79,self.y+17, 93,215 ))
        self.screen.blit( self.image, (self.x, self.y), (0,0,256,256))

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
        self.compute_instant_distance()

    def compute_instant_distance(self):
        time = pygame.time.get_ticks()
        if time - self.current_instant_start_time > 100:
            self.current_instant_start_time = time
            self.instant_distance_by_second = self.current_instant_distance * 10
            self.current_instant_distance = 0
            if self.current_action == 'accelerate':
                self.oil -= self.oil_comsumption * self.instant_distance_by_second
                if self.oil < 0:
                    self.oil = 0
        self.current_instant_distance += self.current_speed * 4.84/215


    def actual_speed(self):
        pass
