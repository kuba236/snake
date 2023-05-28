import pygame
import copy

class Segment(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Segment, self).__init__()
        self.position = pygame.Rect(-32,-32,32,32)
        self.picture = pygame.image.load('images/segment.png')
        self.last_position = None
        pass
    def move(self, new_position):
        self.last_position = copy.deepcopy(self.position)
        self.position = copy.deepcopy(new_position)