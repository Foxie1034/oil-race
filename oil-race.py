# Créé par Mathis, le 22/03/2023 en Python 3.7
import pygame

WIDTH = 1300
HEIGHT = 600

ROAD_WIDTH = WIDTH//2
ROAD_BORDER_WIDTH = 20
ROAD_BORDER_HEIGHT = 100
ROAD_DASH_WIDTH = 10
ROAD_DASH_HEIGHT = 50

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Oil Race")


    def draw_road (self):
        self.draw_grass()
        self.draw_asphalt()


    def draw_grass (self):
        self.grass = pygame.image.load("sprite/grass.png")
        for x in range (0, (WIDTH//128)+1):
            for y in range (0, (HEIGHT//128)+1):
                self.screen.blit(self.grass, (x*128,y*128), (0,0,128,128))

    def draw_asphalt (self):
        road_x=(WIDTH - ROAD_WIDTH)//2
        pygame.draw.rect(self.screen, (128,128,128), ( road_x, 0, ROAD_WIDTH, HEIGHT ))
        pygame.draw.rect(self.screen, (255,0,0),     ( road_x - ROAD_BORDER_WIDTH, 0, ROAD_BORDER_WIDTH, HEIGHT ))
        pygame.draw.rect(self.screen, (255,0,0),     ( road_x + ROAD_WIDTH, 0, ROAD_BORDER_WIDTH, HEIGHT ))
        for num_white_border in range(0, HEIGHT//ROAD_BORDER_HEIGHT, 2):
            pygame.draw.rect(self.screen, (255,255,255), ( road_x - ROAD_BORDER_WIDTH, num_white_border*ROAD_BORDER_HEIGHT, ROAD_BORDER_WIDTH, ROAD_BORDER_HEIGHT ))
            pygame.draw.rect(self.screen, (255,255,255), ( road_x + ROAD_WIDTH,        num_white_border*ROAD_BORDER_HEIGHT, ROAD_BORDER_WIDTH, ROAD_BORDER_HEIGHT ))
        for num_white_dash in range(0, HEIGHT//ROAD_DASH_HEIGHT, 2):
            for num_dash in range(1, 3):
                pygame.draw.rect(self.screen, (255,255,255), ( road_x + ROAD_WIDTH//3 * num_dash, num_white_dash*ROAD_DASH_HEIGHT, ROAD_DASH_WIDTH, ROAD_DASH_HEIGHT ))

    def run(self):
        running = True
        while running:

            self.draw_road()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()