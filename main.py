import pygame
import controls
from gun import Gun
from pygame.sprite import Group


def start():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Игра")
    BLACK = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    while True:
        # Записуаем функцию обработки событий
        controls.events(screen,gun,bullets)
        # update position a gun
        gun.update_gun()
        controls.update(BLACK, screen, gun,bullets)
        controls.update_bullets(bullets)

if __name__ =='__main__':
    start()
