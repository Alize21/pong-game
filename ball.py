import pygame

class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def draw_ball(self,screen):
        pygame.draw.circle(screen, "white",(self.x,self.y),10)

    def ball_vel(self):
        self.x += self.speed_x
        self.y -= self.speed_y