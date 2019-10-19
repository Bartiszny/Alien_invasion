import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing bullets fired by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Initialization of the bullet in current ship position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating bullet's rectangle in 0,0 and defining proper position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Ship's position as float variable
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moving the bullet"""
        # Update position
        self.y -= self.speed_factor

        # Update position of the bullet's rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawing bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

