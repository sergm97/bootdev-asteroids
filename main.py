import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def run_game_loop(screen: pygame.Surface):
    screen.fill("black")
    pygame.display.flip()


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        run_game_loop(screen)


if __name__ == "__main__":
    main()
