import pygame


class Egg(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Egg, self).__init__()
        
        
        self.picture = pygame.image.load('images/egg.png')