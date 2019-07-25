import pygame
from object import Object


class Airplane(Object):
    def __init__(self, pos):
        super() .__init__("airplane.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (70, 70))
        self.acce1 = pygame.math.Vector2(0, 0)

    def update(self):

        image_rect.move_ip(speed)
        if image_rect.right > width:
                speed.x *= -1
        if image_rect.left < 0:
                speed.x *= -1
        if image_rect.bottom > height:
                speed.y *= -1
        if image_rect.top < 0:
                speed.y *= -1
        super().update()