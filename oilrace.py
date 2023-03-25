import pygame

from player import Player

WIDTH = 1300
HEIGHT = 600

ROAD_WIDTH = WIDTH//2
ROAD_BORDER_WIDTH = 20
ROAD_BORDER_HEIGHT = 100
ROAD_DASH_WIDTH = 10
ROAD_DASH_HEIGHT = 50
HITBOX_WIDTH=10

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.road_position = 0
        self.player = Player(screen=self.screen, velocity=1, max_speed=99)
        pygame.display.set_caption("Oil Race")
        self.font = pygame.font.SysFont("comicsansms", 12)
        self.grass = pygame.image.load("sprite/grass.png")
        self.border_rects = { 'left': pygame.Rect( -HITBOX_WIDTH,0,HITBOX_WIDTH,HEIGHT ), 'right': pygame.Rect( WIDTH,0, HITBOX_WIDTH,HEIGHT ) }

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
        self.player.accelerate()
        self.road_position = (self.road_position + self.player.current_speed) % HEIGHT

    def move_down(self):
        self.player.brake()
        self.road_position = (self.road_position + self.player.current_speed) % HEIGHT

    def run(self):
        running = True
        while running:

            # get witch key is pressed
            self.handle_input()

            # draw all road elements
            self.draw_road()

            # draw player's car
            self.player.draw()

            self.draw_message((0,0,0),10,10,f"self.road_position={self.road_position}")
            self.draw_message((0,0,0),10,20,f"self.player.current_speed={self.player.current_speed}")

            # update screen rendering
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()