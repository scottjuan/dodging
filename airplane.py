import pygame


class Airplane(pygame.sprite.Sprite):
    def __init__(self, pos):
        super() .__init__()
        self.image = pygame.image.load("airplane.png")

    def update(self):
        super().update(self)