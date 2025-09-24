import pygame
class Gun():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('img/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center  = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
    def output(self):
        self.screen.blit(self.image,self.rect)