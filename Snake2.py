import pygame
import time
from Direction2 import Direction
class Snake:
    def __init__(self):
        self.picture = pygame.image.load('images/head.png')
        self.copy = self.picture
        self.position = self.picture.get_rect(center = (12*32-16, 9*32-16))#pozycja
        self.direction = Direction.UP
        
        pass
    

    def check_direction(self, direction):
        is_change_possible = True
        if direction == Direction.UP and self.direction == Direction.DOWN:
            is_change_possible = False
            pass

        if direction == Direction.DOWN and self.direction == Direction.UP:
            is_change_possible = False
            pass

        if direction == Direction.RIGHT and self.direction == Direction.LEFT:
            is_change_possible = False
            pass

        if direction == Direction.LEFT and self.direction == Direction.RIGHT:
            is_change_possible = False
            pass
        elif is_change_possible:
            self.direction = direction
            
            pass
        
        pass
    def update(self):
        if self.direction == Direction.UP:
            self.position.move_ip(0,-32)
            self.picture = pygame.transform.rotate(self.copy,0)
            pass

        if self.direction == Direction.DOWN:
            self.position.move_ip(0,32)
            self.picture = pygame.transform.rotate(self.copy,180)
            pass

        if self.direction == Direction.LEFT:
            self.position.move_ip(-32,0)
            self.picture = pygame.transform.rotate(self.copy,90)
            pass

        if self.direction == Direction.RIGHT:
            self.position.move_ip(32,0)
            self.picture = pygame.transform.rotate(self.copy,270)
            pass


    pass