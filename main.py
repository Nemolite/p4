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
        controls.update(BLACK, screen, gun)

if __name__ =='__main__':
    start()
