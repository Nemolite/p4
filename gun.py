import pygame
class Gun():
    def __init__(self,screen):
        self.screen = screen
        # Загружаем пушку
        self.image = pygame.image.load('img/gun.png')

        # Загружаем пушку как прямоугольник
        self.rect = self.image.get_rect()
        print(self.rect)
        self.screen_rect = screen.get_rect()
        self.rect.centerx  = self.screen_rect.centerx
        print(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # Переменная для сдвига пушки в динамике
        self.mright = False
    def output(self):
        self.screen.blit(self.image,self.rect)

    def update_gun(self):
        """ update position gun"""
        if self.mright==True:
            self.rect.centerx+=1