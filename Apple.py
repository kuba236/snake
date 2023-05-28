import pygame
import random
#sprite to duszek
class Apple(pygame.sprite.Sprite):
    def __init__(self,) -> None:
        super(Apple, self).__init__()
        random_pos = pygame.Rect(random.randrange(0,24)*32, random.randrange(0,18)*32,32,32)#pozycja dla każdego kwadratu
        self.rect = random_pos
        self.picture = pygame.image.load('images/apple.png')#załadowanie apple i nadanie zmiennej picture
        pass