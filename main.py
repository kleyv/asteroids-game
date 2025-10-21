import pygame
from constants import * 
from player import Player
def main():
    # print("Hello from asteroids-game!")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)
    # counter = 0
    # while counter < 2000:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        player.draw(screen)
        # counter += 1
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
