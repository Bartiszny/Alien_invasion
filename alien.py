import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing single alien in a fleet """
    def __init__(self, ai_settings, screen):
        """ALien initialisation and defining its start position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Alien's image opening and defining its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Placing new element in upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing exact position of an alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Displaying an alien in its current position"""
        self.screen.blit(self.image, self.rect)
