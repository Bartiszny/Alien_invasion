
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    """Main game method"""
    # Game initialization
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creating game button
    play_button = Button(ai_settings, screen, "Play")

    # Initializing object to store game data
    stats = GameStats(ai_settings)

    # Ship init
    ship = Ship(ai_settings, screen)
    # Group for bullets and aliens storing
    bullets = Group()
    aliens = Group()

    # Creating alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop
    while True:
        gf.check_events(ai_settings, screen, stats, ship, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, play_button, bullets)


run_game()
