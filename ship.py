
import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Ship init"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Image upload
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every new ship shows up at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Center point of the ship is stored in float variable
        self.center = float(self.rect.centerx)

        # Movement options
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship's center point position by movement option"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Rect object update based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Ship diplaying"""
        self.screen.blit(self.image, self.rect)
