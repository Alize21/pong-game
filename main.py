import pygame
from paddle import *
from ball import *

pygame.init()

# Load assets
font = pygame.font.Font("font/game_over.ttf",70)

# Screen
width,height = 900,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

# Initialization
paddle_1 = Paddle(0,height//2)
paddle_2 = Paddle(width-15,height//2)
ball = Ball(width//2-10,height//2-10)
clock = pygame.time.Clock()

def score(screen,winner:str):
    score = font.render(winner,True,"white")
    screen.blit(score,(width//2-70,height//2))

# Mainloop
running = True
while running:

    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_1.direction = "up"
    if keys[pygame.K_s]:
        paddle_1.direction = "down"
    if keys[pygame.K_o]:
        paddle_2.direction = "up"
    if keys[pygame.K_l]:
        paddle_2.direction = "down"

    # Check collision with ball
    if ball.x < paddle_2.x+15 and ball.x+10 > paddle_2.x and ball.y < paddle_2.y+130 and ball.y+10 > paddle_2.y:
        ball.speed_x *= -1
    if ball.x < paddle_1.x+15 and ball.x+10 > paddle_1.x and ball.y < paddle_1.y+130 and ball.y+10 > paddle_1.y:
        ball.speed_x *= -1

    # Make the ball bounce back evertime it hit the wall
    if ball.y < 0 or ball.y > height-10:
        if ball.speed_x > 0:
            ball.speed_y *= -1
        elif ball.speed_x < 0:
            ball.speed_y *= -1

    # Decide the winner
    if ball.x < 0:
        score(screen,"player 2 win!")
    elif ball.x > width:
        score(screen,"player 1 win!")

    paddle_1.set_direction()
    paddle_2.set_direction()

    paddle_1.draw_paddle(screen)
    paddle_2.draw_paddle(screen)
    ball.draw_ball(screen)

    ball.ball_vel()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
