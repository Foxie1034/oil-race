# Créé par Mathis, le 22/03/2023 en Python 3.7
import pygame

pygame.init()

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Oil Race")


    def run(self):
        running = True
        while running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()