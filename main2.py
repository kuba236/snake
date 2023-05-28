import pygame
import time
import random
from Snake2 import Snake
from Direction2 import Direction
pygame.init()


WIDTH_DISPLAY = 800
HEIGHT_DISPLAY = 608

display = pygame.display.set_mode((800,608))
pygame.display.set_caption("Game Snake")

is_game_running = True
clock = pygame.time.Clock()
SNAKE_MOVE = pygame.USEREVENT +1
pygame.time.set_timer(SNAKE_MOVE, 200)

snake = Snake()
points = 0

font_points = pygame.font.SysFont('Segoe UI Semibold', 20)

background = pygame.Surface((800,608))
for i in range(32):
    for j in range(19):
        picture = pygame.image.load('images/background.png')
        mask = (random.randint(0,20),random.randint(0,20),random.randint(0,20))
        picture.fill(mask,special_flags=pygame.BLEND_ADD)
        background.blit(picture, (i*32,j*32))






while is_game_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_game_running = False
                pass

            if event.key == pygame.K_LEFT:
                snake.check_direction(Direction.LEFT)
            pass
            if event.key == pygame.K_RIGHT:
                snake.check_direction(Direction.RIGHT)
                pass
            if event.key == pygame.K_UP:
                snake.check_direction(Direction.UP)
                pass
            if event.key == pygame.K_DOWN:
                snake.check_direction(Direction.DOWN)
                pass
            
            
            
        
        elif event.type == pygame.QUIT:
            is_game_running = False
            pass
        elif event.type == SNAKE_MOVE:
            snake.update()
            points+=1
            pass
        

        pass
    display.blit(background, (0,0))
    display.blit(snake.picture, snake.position)
    points_caunter = font_points.render(f"Points: {points}", False, (0,0,0))
    display.blit(points_caunter, (30,30))





    clock.tick(30)
    pygame.display.flip()
    pass
time.sleep(0.5)
pygame.quit()  