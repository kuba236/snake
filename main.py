import pygame
import random
import time
from Apple import Apple
from Direction import Direction
from Snake import Snake

pygame.init()

WIDTH_DISPLAY = 800
HEIGHT_DISPLAY = 608

points = 0

background = pygame.Surface((800,608))
for i in range(25):
    for j in range(19):
        picture = pygame.image.load('images/background.png')
        mask = (random.randint(0,20),random.randint(0,20),random.randint(0,20))#trzy cyfry które pełnią funkcję rgb. 
        picture.fill(mask, special_flags=pygame.BLEND_ADD)#dodanie maski do każdego obraska
        background.blit(picture, (i*32, j*32)) 
        pass
    pass
display = pygame.display.set_mode([WIDTH_DISPLAY,HEIGHT_DISPLAY])
pygame.display.set_caption('snake')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 24)


snake = Snake()
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 200)



apples = pygame.sprite.Group()
apple = Apple()
apples.add(apple)






is_game_running = True

while is_game_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_game_running = False
                pass
            if event.key == pygame.K_w:
                snake.change_direction(Direction.UP)
                pass

            elif event.key == pygame.K_a:
                snake.change_direction(Direction.LEFT)
                pass
            elif event.key == pygame.K_d:
                snake.change_direction(Direction.RIGHT)
                pass
            elif event.key == pygame.K_s:
                snake.change_direction(Direction.DOWN)
                pass


        elif event.type == MOVE_SNAKE:
            snake.snake_update()
        elif event.type == pygame.QUIT:
            is_game_running = False
            pass  
    is_snake_collided_with_apple = pygame.sprite.spritecollideany(snake, apples)
    if is_snake_collided_with_apple != None:
        is_snake_collided_with_apple.kill()
        snake.eat_apple()
        apples.add(Apple())
        points +=1
        pass

    
    display.blit(background,(0,0))
    display.blit(snake.picture, snake.rect)
    snake.draw_segments(display)
    for a in apples:
        display.blit(a.picture, a.rect)
        pass
    
    if snake.check_collision():
        end_game_text = font.render("Lost", False, (200,0,0))
        display.blit(end_game_text, (WIDTH_DISPLAY/2-50, HEIGHT_DISPLAY/2))
        is_game_running = False
        pass

    points_counter_display = font.render(f'Wynik: {points}', False, (0,0,0))
    display.blit(points_counter_display, (16,16))
    
    clock.tick(30)
    pygame.display.flip()
    pass
time.sleep(0.5)
pygame.quit()        