import sys
import pygame
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien invasion")
    # set the background color.
    bg_color = pygame.Color(23, 193, 199)
    # Game objects
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw the sereen during each pass through the loop.
        screen.fill(bg_color)
        pygame.display.flip()

run_game()