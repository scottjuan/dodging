import pygame
import random
from enemy import Enemy
from airplane import Airplane



pygame.init()

screen_info = pygame.display.Info()


screen_size = (screen_width, screen_height) = \
    (int(screen_info.current_w * 1),
     int(screen_info.current_h * 1))



screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
character = Airplane((120, 120))
enemies = pygame.sprite.Group()
enemies.empty()
for i in range(10):
    enemies.add(Enemy)
def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character.acce1.x += 0.1
                if event.key == pygame.K_LEFT:
                    character.acce1.x-=0.1
                if event.key == pygame.K_UP:
                    character.acce1.y += -0.1
                if event.key == pygame.K_DOWN:
                    character.acce1.y += 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    character.acce1.x-= 0.1
                if event.key == pygame.K_LEFT:
                    character.acce1.x += 0.1
                if event.key == pygame.K_UP:
                    character.acce1.y -= -0.1
                if event.key == pygame.K_DOWN:
                    character.acce1.y -= 0.1

        character.update()
        enemies.update()
        screen.fill((90, 127, 255))
        character.draw(screen)
        enemies.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()



