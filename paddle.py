import pygame

class Paddle:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw_paddle(self,screen):
        pygame.draw.rect(screen, "white", (self.x, self.y, 15, 130))
