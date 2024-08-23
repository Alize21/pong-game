import pygame

class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6
        self.speed_x = self.speed
        self.speed_y = self.speed

    def draw_ball(self,screen):
        pygame.draw.circle(screen, "white",(self.x,self.y),10)

    def ball_vel(self):
        self.x += self.speed_x
        self.y -= self.speed_y