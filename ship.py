
import pygame

class Ship:
    def __init__(self, screen):
        """Ship init"""
        self.screen = screen

        # Image upload
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every new ship shows up at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Ship diplaying"""
        self.screen.blit(self.image, self.rect)
