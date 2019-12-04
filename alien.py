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

    def check_edges(self):
        """Returns True if alien's at the edge of the game screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moving an alien to the left or right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x