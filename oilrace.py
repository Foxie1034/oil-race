import pygame
import math

from settings import *

from player import Player
from gauge import OilGauge, SpeedGauge

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Oil Race")
        self.font = pygame.font.SysFont("comicsansms", 12)
        self.clock = pygame.time.Clock()
        self.road_position = 0
        self.player = Player(screen=self.screen, velocity=1, max_speed=99)
        self.oil_gauge = OilGauge(self.screen)
        self.speed_gauge = SpeedGauge(self.screen)
        self.grass = pygame.image.load("sprite/grass.png")
        self.border_rects = { 'left': pygame.Rect( -10,0,10,HEIGHT ), 'right': pygame.Rect( WIDTH,0, 10,HEIGHT ) }
        self.grass_rects = [ pygame.Rect( 0,0,(WIDTH-ROAD_WIDTH)//2-ROAD_BORDER_WIDTH,HEIGHT ),  pygame.Rect( WIDTH-(WIDTH-ROAD_WIDTH)//2+ROAD_BORDER_WIDTH,0, (WIDTH-ROAD_WIDTH)//2-ROAD_BORDER_WIDTH,HEIGHT )]

    def draw_road (self):
        self.draw_grass()
        self.draw_asphalt()

    def draw_message(self, color, x, y, message):
        text_img = self.font.render(message, True, color)
        self.screen.blit(text_img, (x, y))

    def draw_grass (self):
        for x in range (0, (WIDTH//128)+1):
            # frame top
            for y in range (0, (self.road_position//128)+2):
                self.screen.blit(self.grass, (x*128, self.road_position - y*128), (0,0,128,128))
                #self.draw_message((0,0,0), x*128+10, self.road_position - y*128, f"x={x*128} y={self.road_position - y*128}")
            # frame bottom
            for y in range (0, ((HEIGHT-self.road_position)//128)+1):
                self.screen.blit(self.grass, (x*128, self.road_position + y*128), (0,0,128,128))
                #self.draw_message((0,0,0), x*128+10, self.road_position + y*128, f"x={x*128} y={self.road_position + y*128}")

    def draw_asphalt (self):
        road_x=(WIDTH - ROAD_WIDTH)//2
        # draw asphalt
        pygame.draw.rect(self.screen, (128,128,128), ( road_x, 0, ROAD_WIDTH, HEIGHT ))
        # draw red borders
        pygame.draw.rect(self.screen, (255,0,0),     ( road_x - ROAD_BORDER_WIDTH, 0, ROAD_BORDER_WIDTH, HEIGHT ))
        pygame.draw.rect(self.screen, (255,0,0),     ( road_x + ROAD_WIDTH, 0, ROAD_BORDER_WIDTH, HEIGHT ))
        # draw white borders
        # on top
        for num_white_border in range(0, self.road_position//ROAD_BORDER_HEIGHT + 2, 2):
            pygame.draw.rect(self.screen, (255,255,255), ( road_x - ROAD_BORDER_WIDTH, self.road_position - num_white_border*ROAD_BORDER_HEIGHT, ROAD_BORDER_WIDTH, ROAD_BORDER_HEIGHT ))
            pygame.draw.rect(self.screen, (255,255,255), ( road_x + ROAD_WIDTH,        self.road_position - num_white_border*ROAD_BORDER_HEIGHT, ROAD_BORDER_WIDTH, ROAD_BORDER_HEIGHT ))
        # on bottom
        for num_white_border in range(0, (HEIGHT - self.road_position)//ROAD_BORDER_HEIGHT + 2, 2):
            pygame.draw.rect(self.screen, (255,255,255), ( road_x - ROAD_BORDER_WIDTH, self.road_position + num_white_border*ROAD_BORDER_HEIGHT, ROAD_BORDER_WIDTH, ROAD_BORDER_HEIGHT ))
            pygame.draw.rect(self.screen, (255,255,255), ( road_x + ROAD_WIDTH,        self.road_position + num_white_border*ROAD_BORDER_HEIGHT, ROAD_BORDER_WIDTH, ROAD_BORDER_HEIGHT ))
        # draw dashes
        # on top
        for num_white_dash in range(0, self.road_position//ROAD_DASH_HEIGHT + 2, 2):
            for num_dash in range(1, 3):
                pygame.draw.rect(self.screen, (255,255,255), ( road_x + ROAD_WIDTH//3 * num_dash, self.road_position - num_white_dash*ROAD_DASH_HEIGHT, ROAD_DASH_WIDTH, ROAD_DASH_HEIGHT ))
        # on bottom
        for num_white_dash in range(0, (HEIGHT - self.road_position)//ROAD_DASH_HEIGHT + 2, 2):
            for num_dash in range(1, 3):
                pygame.draw.rect(self.screen, (255,255,255), ( road_x + ROAD_WIDTH//3 * num_dash, self.road_position + num_white_dash*ROAD_DASH_HEIGHT, ROAD_DASH_WIDTH, ROAD_DASH_HEIGHT ))

    def collide_screen_borders (self, side):
        return self.player.rect.colliderect(self.border_rects[side])


    def collide_grass (self):
        return self.player.rect.collidelist(self.grass_rects)

    def handle_input(self):
        move_up=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            move_up=True
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

        if not move_up:
            self.move_down()

    def move_left(self):
        if not self.collide_screen_borders('left'):
            self.player.move_left()

    def move_right(self):
        if not self.collide_screen_borders('right'):
            self.player.move_right()

    def move_up(self):
        if self.collide_grass() > -1:
            if self.player.current_speed > 10:
                self.player.brake()
        else:
            self.player.accelerate()
        self.road_position = (self.road_position + self.player.current_speed) % HEIGHT

    def move_down(self):
        self.player.brake()
        self.road_position = (self.road_position + self.player.current_speed) % HEIGHT

    def run(self):
        running = True
        start_time = pygame.time.get_ticks()
        while running:

            # get witch key is pressed
            self.handle_input()

            # draw all road elements
            self.draw_road()

            # draw player's car
            self.player.draw()

            # draw gauges
            self.oil_gauge.current_value = self.player.oil
            self.oil_gauge.draw()

            self.speed_gauge.current_value = int(self.player.instant_distance_by_second * 3.6)
            self.speed_gauge.draw()

            self.draw_message((0,0,0),10,10,f"self.road_position={self.road_position}")
            self.draw_message((0,0,0),10,25,f"self.player.current_speed={self.player.current_speed} px")
            self.draw_message((0,0,0),10,40,f"self.player.distance={self.player.total_distance} m")
            self.draw_message((0,0,0),10,55,f"self.clock.get_fps={self.clock.get_fps()} fps")
            self.draw_message((0,0,0),10,70,f"nb milliseconds={pygame.time.get_ticks() - start_time} ms")
            self.draw_message((0,0,0),10,85,f"vitesse moyenne={self.player.total_distance / (pygame.time.get_ticks() - start_time) * 3.6 * 1000} km/h")
            self.draw_message((0,0,0),10,100,f"vitesse instantanée={int(self.player.instant_distance_by_second * 10 * 3.6)} km/h")

            # update screen rendering
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()