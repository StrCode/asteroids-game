# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, FRAME_RATE
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")

    # creates a screen surface to be used to display the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create a player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(FRAME_RATE) / 1000


if __name__ == "__main__":
    main()
