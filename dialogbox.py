import pygame

from settings import *

class DialogBox:

    LETTER_OFFSET=3
    LETTER_WIDTH=17
    LETTER_HEIGHT=29

    def __init__(self, screen):
        self.screen = screen
        self.letters = []
        self.image = pygame.image.load("sprite/Font Pixels 01.png").convert_alpha()
        for row in range (0, 3):
            for column in range (0, 9):
                self.letters.append(
                    self.image.subsurface(
                        self.LETTER_OFFSET+column*self.LETTER_WIDTH,
                        row*self.LETTER_HEIGHT,
                        self.LETTER_WIDTH,
                        self.LETTER_HEIGHT
                    )
                )

    def draw(self, *messages):
        nb_messages=len(messages)
        message_y = (HEIGHT - self.LETTER_HEIGHT*nb_messages) // 2 - self.LETTER_WIDTH
        for message in messages:
            message=message.upper()
            message_width = len(message) * self.LETTER_WIDTH
            message_x = (WIDTH - message_width) // 2
            message_y += self.LETTER_HEIGHT
            for i in range(0,len(message)):
                num_car = ord(message[i]) - ord("A")
                if num_car >=0 and num_car <=26:
                    self.screen.blit( self.letters[ num_car ], (message_x+i*self.LETTER_WIDTH, message_y), (0,0,self.LETTER_WIDTH,self.LETTER_HEIGHT) )

