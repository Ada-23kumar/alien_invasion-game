import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien invasion")
    # make a ship
    ship = Ship(screen)
    # set the background color.
    bg_color = pygame.Color(23, 193, 199)
    # Game objects
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw the sereen during each pass through the loop.
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()