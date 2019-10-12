
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

        # Movement options
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship position by movement option"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Ship diplaying"""
        self.screen.blit(self.image, self.rect)
