import pygame
import sys

def events(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                # moving on the right
                gun.mright = True
            elif event.key == pygame.K_a:
                # moving on the left
                gun.mleft = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                # moving on the right (stop)
                gun.mright = False
            elif event.key == pygame.K_a:
                # moving on the left (stop)
                gun.mleft = False

def update(bg_color,screen,gun):
    # Закрашиваем область
    screen.fill(bg_color)
    # Выводим пушку
    gun.output()
    # Отображаем
    pygame.display.flip()
