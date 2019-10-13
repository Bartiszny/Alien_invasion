
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Main game method"""
    # Game initialization
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship init
    ship = Ship(ai_settings, screen)
    # Group for bullets storing
    bullets = Group()

    # Main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Deleting off-screen bulltes
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
