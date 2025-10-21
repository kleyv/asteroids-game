import pygame
from constants import * 

def main():
    # print("Hello from asteroids-game!")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    counter = 0
    # while counter < 2000:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        # counter += 1
        pygame.display.flip()


if __name__ == "__main__":
    main()
