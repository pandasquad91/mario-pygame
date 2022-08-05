"""
Mario Pygame
"""

import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Pygame")

WHITE = (255, 255, 255)
FPS = 60


def main():
    """
    basic game loop
    """
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
