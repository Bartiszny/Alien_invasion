import sys
import pygame

def check_events(ship):
    """ Waiting for button"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Moving ship to the right
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                 # Moving ship to the left
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Game screen update"""

    # Display refreshing each iteration
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Displaying last modified screen
    pygame.display.flip()
