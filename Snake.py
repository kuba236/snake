import pygame
from Direction import Direction
from Segment import Segment
import copy

class Snake(pygame.sprite.Sprite):
    def __init__(self,) -> None:
        self.orgin_picture = pygame.image.load('images/head.png')
        self.picture = pygame.transform.rotate(self.orgin_picture,0)#obracająca się głowa
        self.rect = self.picture.get_rect(center = (12*32-16, 9*32-16))#pozycja
        self.direction = Direction.UP
        self.new_direction = Direction.UP
        self.last_position = self.rect
        self.is_adding_segment = False
        self.segments = []
        pass


    def change_direction(self, direction):
        is_change_possible = True
        if direction == Direction.UP and self.direction == Direction.DOWN:
            is_change_possible = False
            pass
        elif direction == Direction.DOWN and self.direction == Direction.UP:
            is_change_possible = False
            pass
        elif direction == Direction.LEFT and self.direction == Direction.RIGHT:
            is_change_possible = False
            pass
        elif direction == Direction.RIGHT and self.direction == Direction.LEFT:
            is_change_possible = False
            pass

        elif is_change_possible:
            self.direction = direction
            
            pass
        pass


    def snake_update(self):
        self.direction == self.new_direction
        self.picture = pygame.transform.rotate(self.orgin_picture, self.direction.value *-90)
        self.last_position = copy.deepcopy(self.rect)
        if self.direction == Direction.UP:
            self.rect.move_ip(0,-32)
            pass
        elif self.direction == Direction.DOWN:
            self.rect.move_ip(0,32)
            pass
        elif self.direction == Direction.RIGHT:
            self.rect.move_ip(32,0)
            pass
        elif self.direction == Direction.LEFT:
            self.rect.move_ip(-32,0)
            pass

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].move(self.last_position)
                pass
            else:
                self.segments[i].move(self.segments[i-1].last_position)
                pass
        if self.is_adding_segment:
            new_segment = Segment()
            new_position = None
            if len(self.segments) > 0:
                new_position = copy.deepcopy(self.segments[-1].position)
                pass
            else:
                new_position = copy.deepcopy(self.last_position)
                pass
            new_segment.position = new_position
            self.segments.append(new_segment)
            self.is_adding_segment = False
            pass
        pass

    def draw_segments(self,display):
        for segment in self.segments:
            display.blit(segment.picture, segment.position)
        pass  


    def eat_apple(self):
        self.is_adding_segment = True
        pass


    def check_collision(self):
        #ugryzienie ogona
        for segment in self.segments:
            if self.rect.topleft == segment.position.topleft:
                return True
            pass
        #wyjście poza ekran
        if self.rect.top < 0 or self.rect.top >=608:
            return True
        
        elif self.rect.left < 0 or self.rect.left >= 800:
            return True
        
        return False
        
        pass
    pass
        
    