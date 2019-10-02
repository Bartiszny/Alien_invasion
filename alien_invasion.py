import sys
import pygame

from settings import Settings

def run_game():
    # Game initialization
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Main loop
    while True:

        # Waiting for button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Display refreshing each iteration
        screen.fill(ai_settings.bg_color)
        # Displaying last modified screen
        pygame.display.flip()


run_game()
