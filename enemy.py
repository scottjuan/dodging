import pygame
from object import Object

class Enemy(Object):
    def __init__(self, pos):
        super().__init__("bullet.png", pos)
        self.image = pygame.transform.smotthscale(self.image, (40, 40))
        self.acce1 = pygame.math.Vector2()

        def update(self):
            super().update()