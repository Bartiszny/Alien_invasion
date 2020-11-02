import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reaction for keydown event"""
    if event.key == pygame.K_RIGHT:
        # Moving ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Moving ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Firing bullet
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Game screen update"""

    # Display refreshing each iteration
    screen.fill(ai_settings.bg_color)

    # Displaying all the bullets under ships' layers again
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Displaying last modified screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Updating bullets' positions and removing out-of-the-screen ones"""
    # Updating positions
    bullets.update()

    # Deleting off-screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Reaction to collision between a bullet and an alien"""
    # Removing all colliding bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Removing on-screen bullets and creating a new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculating the number of aliens i one row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculating the number of rows with aliens"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creating an alien in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creating full alien fleet"""
    # Creating an alien and calculating number of aliens in a row
    # Space between particular aliens equals to one's width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Creating alien fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Creating an alien and placing it in a row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Reaction to alien reaching the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Moving whole fleet down and change the direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Reaction on hit"""
    # Decrementing value in ships_left
    stats.ships_left -= 1

    # Delete lists aliens and bullets
    aliens.empty()
    bullets.empty()

    # Constructing new fleet and centering a ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Pause
    sleep(0.5)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Checking edge condition and updating position of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Checking alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)





