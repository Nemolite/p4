import sys
import pygame
from gun import Gun
def start():
    pygame.init()
    gamewindow = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Игра")
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    gun = Gun(gamewindow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        gamewindow.fill(BLACK)
        gun.output()
        pygame.display.flip()
if __name__ =='__main__':
    start()
