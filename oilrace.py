import pygame

from settings import *

from player import Player
from gauge import OilGauge, SpeedGauge
from powerup import OilTank
from dialogbox import DialogBox

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Oil Race")
        self.font = pygame.font.SysFont("comicsansms", 22)
        self.clock = pygame.time.Clock()

        self.player = Player(screen=self.screen, velocity=1, max_speed=299, oil_tank_size=100)
        self.oil_gauge = OilGauge(self.screen, self.player.oil_tank_size)
        self.speed_gauge = SpeedGauge(self.screen, self.player.max_speed)
        self.powers_up = [ OilTank(screen=self.screen, activation=True) ]
        self.dialog_box = DialogBox(self.screen)

        self.road_position = 0
        self.splash_screen = pygame.image.load("sprite/splash_screen.jpg")
        self.grass = pygame.image.load("sprite/grass.png")
        self.border_rects = { 'left': pygame.Rect( -10,0,10,HEIGHT ), 'right': pygame.Rect( WIDTH,0, 10,HEIGHT ) }
        self.grass_rects = [ pygame.Rect( 0,0,(WIDTH-ROAD_WIDTH)//2-ROAD_BORDER_WIDTH,HEIGHT ),  pygame.Rect( WIDTH-(WIDTH-ROAD_WIDTH)//2+ROAD_BORDER_WIDTH,0, (WIDTH-ROAD_WIDTH)//2-ROAD_BORDER_WIDTH,HEIGHT )]

        pygame.mixer.init()
        pygame.mixer.music.set_volume(10)
        pygame.mixer.music.load(f"sounds/music_track.mp3")
        pygame.mixer.music.play( loops=-1 )

        self.fill_tank_sound = pygame.mixer.Sound("sounds/fill_tank_sound.wav")

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

    def collide_powers_up(self):
        for powerup in self.powers_up:
            if powerup.activation:
                if self.player.rect.colliderect(powerup.rect):
                    if isinstance(powerup, OilTank):
                        pygame.mixer.Sound.play(self.fill_tank_sound)
                        self.player.fill_tank(powerup.capacity)
                        powerup.activation = False

    def handle_input(self):
        move_up=False
        move_down=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            if not move_down:
                move_up=True
                self.move_up()
        if keys[pygame.K_DOWN]:
            if not move_up:
                move_down=True
                self.move_down()

        if not move_up and not move_down:
            self.move_down()

        self.collide_powers_up()

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
            elif self.player.oil > 0:
                self.player.accelerate()
        else:
            self.player.accelerate()
        self.road_position = (self.road_position + self.player.current_speed) % HEIGHT

    def move_down(self):
        self.player.brake()
        self.road_position = (self.road_position + self.player.current_speed) % HEIGHT

    def run(self):
        running = True
        start_game = False
        while running:

            # get witch key is pressed
            self.handle_input()

            # show splash screen
            if not start_game:

                # draw splash screen
                self.screen.blit(self.splash_screen, (0,0), (0,0,WIDTH,HEIGHT))

                # draw message
                self.dialog_box.draw( "Ready GO", "Press enter key" )

                # in case of restarting game, fill player's car tank
                self.player.fill_tank(100)

            # Play the game
            else:

                # draw all road elements
                self.draw_road()

                # draw player's car
                self.player.draw()

                # draw gauges
                self.oil_gauge.current_value = self.player.oil
                self.oil_gauge.draw()

                self.speed_gauge.current_value = self.player.current_speed
                self.speed_gauge.draw()

                # activate when necessary and draw powers up
                for powerup in self.powers_up:
                    if self.player.total_distance % 1000 > 490:
                        powerup.reset()
                    powerup.move()
                    powerup.draw()

                # draw total distance
                self.draw_message((0,0,0),10,HEIGHT-50, "Distance parcourue : %0.2f km" % (self.player.total_distance/1000))

                # when no more oil and current_speed null, game is over
                if self.player.oil == 0 and self.player.current_speed == 0:
                    self.dialog_box.draw("Game Over")
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    start_game = False

            # update screen rendering
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start_game = True

            self.clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()