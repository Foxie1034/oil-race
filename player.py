import pygame

WIDTH = 1300
HEIGHT = 600

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
        self.rect = pygame.Rect( self.x+self.box.x,self.y+self.box.y, self.box.width,self.box.height)

    def accelerate(self):
        self.current_speed += self.velocity
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def brake(self):
        self.current_speed -= self.velocity
        if self.current_speed < 0:
            self.current_speed = 0

    def draw(self):
        #pygame.draw.rect(self.screen, (0,0,0), ( self.x+79,self.y+17, 93,215 ))
        self.screen.blit( self.image, (self.x, self.y), (0,0,256,256))

    def move_left(self):
        if self.current_speed > 0:
            self.x -= 10
            self.rect = pygame.Rect( self.x+self.box.x,self.y+self.box.y, self.box.width,self.box.height)

    def move_right(self):
        if self.current_speed > 0:
            self.x += 10
            self.rect = pygame.Rect( self.x+self.box.x,self.y+self.box.y, self.box.width,self.box.height)

