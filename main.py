import pygame
import controls
from gun import Gun


def start():
    pygame.init()
    gamewindow = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Игра")
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    gun = Gun(gamewindow)
    while True:
        # Записуаем функцию обработки событий
        controls.events(gun)
        # Закрашиваем область
        gamewindow.fill(BLACK)
        # Выводим пушку
        gun.output()
        # Отображаем
        pygame.display.flip()
if __name__ =='__main__':
    start()
