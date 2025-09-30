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
        self.center = float(self.rect.centerx)

        self.rect.bottom = self.screen_rect.bottom
        # Переменная для сдвига пушки в динамике
        self.mright = False
        self.mleft = False
    def output(self):
        self.screen.blit(self.image,self.rect)

    def update_gun(self):
        """ update position gun"""
        if self.mright==True and self.rect.right<self.screen_rect.right:
            self.center+=1.5
        if self.mleft == True and self.rect.left>0:
            self.center-=1.5

        self.rect.centerx = self.center