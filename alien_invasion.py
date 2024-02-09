import sys
import pygame
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien invasion")
    # Game objects
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pygame.display.flip()

run_game()