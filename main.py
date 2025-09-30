import pygame
import controls
from gun import Gun


def start():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Игра")
    BLACK = (0,0,0)
    gun = Gun(screen)
    while True:
        # Записуаем функцию обработки событий
        controls.events(gun)
        # update position a gun
        gun.update_gun()
        # Закрашиваем область
        screen.fill(BLACK)
        # Выводим пушку
        gun.output()
        # Отображаем
        pygame.display.flip()
if __name__ =='__main__':
    start()
