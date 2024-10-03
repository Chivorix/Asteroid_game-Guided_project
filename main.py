import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, drawable, updatable)

    asteroid_spawner = AsteroidField()
    player = Player(PLAYER_X, PLAYER_Y)
    score = Score(SCREEN_WIDTH/2 - 50, 20, "blue")

    while True:
        
        screen.fill("black")
        score.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collision(player):
                score.sub()
                print("Game Over!")
                return 
            for bullet in bullets:
                if obj.collision(bullet):
                    obj.split()
                    bullet.kill()
                    score.add(obj.radius)

        pygame.display.flip()           # double-buffer mechanic, this is basically a copy-paste function, rendering...

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                score.save_score()
                return                  # break the loop

        dt = clock.tick(60) / 1000      # The .tick method returns Delta-t in ms
    
if __name__ == "__main__":
    main()