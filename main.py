import pygame
from paddle import *
from ball import *
from button import *
import math

pygame.init()

# Screen
width,height = 900,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

# Load assets
font = pygame.font.Font("assets/font/game_over.ttf",70)
restart_button_img = pygame.image.load("assets/button/restart.png").convert_alpha()
exit_button_img = pygame.image.load("assets/button/exit.png").convert_alpha()

# Initialization
paddle_1 = Paddle(20,height//2)
paddle_2 = Paddle(width-35,height//2)
ball = Ball(width//2-10,height//2-10)
restart_button = Button(610//2,580//2,restart_button_img,0.3)
exit_button = Button(930//2,580//2,exit_button_img,0.3)
clock = pygame.time.Clock()

# Score
winner = None
def draw_score(screen):

    score = font.render(winner,True,"white")
    screen.blit(score,(width//2-83,height//2-65))

state = "play"
# Mainloop
running = True
while running:

    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state == "play":

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_1.direction = "up"
        if keys[pygame.K_s]:
            paddle_1.direction = "down"
        if keys[pygame.K_o]:
            paddle_2.direction = "up"
        if keys[pygame.K_l]:
            paddle_2.direction = "down"

        # Prevent the paddle from crossing the window
        if paddle_1.y < 0:
            paddle_1.y = 0
        if paddle_1.y + paddle_1.height > height:
            paddle_1.y = height - paddle_1.height
        if paddle_2.y < 0:
            paddle_2.y = 0
        if paddle_2.y + paddle_2.height > height:
            paddle_2.y = height - paddle_2.height

        # Check collision paddle with ball
        if ball.x < paddle_1.x+15 and ball.x+10 > paddle_1.x and ball.y < paddle_1.y+130 and ball.y+10 > paddle_1.y:
            
            paddle_center = paddle_1.y + (paddle_1.height/2)

            # count the offset position
            offset = (ball.y+10)-paddle_center
            max_offset = paddle_1.height/2
            normalized_offset = offset / max_offset

            max_angle = math.radians(60)  # 60 degrees to radians

            # Bounce angle
            angle = normalized_offset * max_angle

            # original speed
            global original_speed
            original_speed = math.sqrt(ball.speed**2 + ball.speed**2)
            
            # Add a new speed base on angle
            ball.speed_x = original_speed * math.cos(angle)
            ball.speed_y = original_speed * math.sin(angle)
    
            ball.speed_y *= -1 
            ball.speed += 0.2 

        if ball.x < paddle_2.x+15 and ball.x+10 > paddle_2.x and ball.y < paddle_2.y+130 and ball.y+10 > paddle_2.y:

            paddle_center = paddle_2.y + (paddle_2.height/2)

            offset = (ball.y+10)-paddle_center

            max_offset = paddle_2.height/2
            normalized_offset = offset / max_offset
            max_angle = math.radians(60)  

            angle = normalized_offset * max_angle

            original_speed = math.sqrt(ball.speed**2 + ball.speed**2)

            ball.speed_x = original_speed * math.cos(angle)
            ball.speed_y = original_speed * math.sin(angle)

            ball.speed_x *= -1
            ball.speed_y *= -1
            ball.speed += 0.2 
            
        # Make the ball bounce back evertime it hit the wall
        if ball.y < 0 or ball.y > height-10:
            if ball.speed_x > 0:
                ball.speed_y *= -1
            elif ball.speed_x < 0:
                ball.speed_y *= -1

        # Decide the winner
        if ball.x < 0 or ball.x > width:
            state = "pause"

        paddle_1.set_direction()
        paddle_2.set_direction()

        paddle_1.draw_paddle(screen)
        paddle_2.draw_paddle(screen)
        ball.draw_ball(screen)

        ball.ball_vel()

    elif state == "pause":

        if ball.x < 0:
            draw_score(screen)
            winner = "player 2 win!"          
        elif ball.x > width:
            draw_score(screen)
            winner = "player 1 win!"        

        if restart_button.click():
            ball.x,ball.y = width//2-10,height//2-10
            state = "play"

            # Change y velocity to 0 at the start of the game
            if winner == "player 1 win!":
                ball.speed_x = 7
                ball.speed_y = 0
                print("player 1 win")
            elif winner == "player 2 win!":
                ball.speed_x = -7
                ball.speed_y = 0
                print("player 2 win")

        if exit_button.click():
            running = False

        paddle_1.draw_paddle(screen)
        paddle_2.draw_paddle(screen)
        ball.draw_ball(screen)

        restart_button.draw_image(screen)
        exit_button.draw_image(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
