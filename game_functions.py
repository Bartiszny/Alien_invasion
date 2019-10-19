import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reaction for keydown event"""
    if event.key == pygame.K_RIGHT:
        # Moving ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Moving ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Firing bullet if it's below limit"""
    # Creating a new bullet and adding to the group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    """Reaction for keyup event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Waiting for button"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Game screen update"""

    # Display refreshing each iteration
    screen.fill(ai_settings.bg_color)

    # Displaying all the bullets under ships' layers again
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Displaying last modified screen
    pygame.display.flip()


def update_bullets(bullets):
    """Updating bullets' positions and removing out-of-the-screen ones"""
    # Updating positions
    bullets.update()

    # Deleting off-screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))