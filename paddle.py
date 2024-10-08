import pygame

class Paddle:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 130
        self.direction = None
        self.speed = 12

    def set_direction(self):
        if self.direction == "up":
            self.y -= self.speed
            self.direction = None
        elif self.direction == "down":
            self.y += self.speed
            self.direction = None

    def draw_paddle(self,screen):
        pygame.draw.rect(screen, "white", (self.x, self.y, 15, self.height))
