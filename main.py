import pygame
from constants import *



def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill("black")
        pygame.display.flip() # double-buffer mechanic, this is basically a copy-paste function

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return        # break the loop
if __name__ == "__main__":
    main()