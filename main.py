import pygame
from constants import *
from player import Player




def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(PLAYER_X, PLAYER_Y)

    while True:
        
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()           # double-buffer mechanic, this is basically a copy-paste function, rendering...

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                print(dt)
                return                  # break the loop

        dt = clock.tick(60) / 1000      # The .tick method returns Delta-t in ms
    
if __name__ == "__main__":
    main()