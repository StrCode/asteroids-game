# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FRAME_RATE


def main():
    pygame.init()
    print("Starting asteroids!")

    # creates a screen surface to be used to display the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(FRAME_RATE) / 1000


if __name__ == "__main__":
    main()
