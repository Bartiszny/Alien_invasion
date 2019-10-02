import sys
import pygame

def run_game():
    # Game initialization
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Main loop
    while True:

        # Waiting for button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Displaying last modified screen
        pygame.display.flip()


run_game()
