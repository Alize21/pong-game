import pygame
from paddle import *

pygame.init()
# Screen
width,height = 900,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

# Initialization
paddle_1 = Paddle(0,height//2)
paddle_2 = Paddle(width-15,height//2)
clock = pygame.time.Clock()

# Mainloop
running = True
while running:

    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    paddle_1.draw_paddle(screen)
    paddle_2.draw_paddle(screen)
    pygame.display.update()

    clock.tick(30)

pygame.quit()
