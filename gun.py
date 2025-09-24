import pygame
class Gun():
    def __init__(self,screen):
        self.screen = screen
        # Загружаем пушку
        self.image = pygame.image.load('img/gun.png')
        # Загружаем пушку как прямоугольник
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx  = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)