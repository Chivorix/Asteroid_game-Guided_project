import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)

        self.rotation = 0

    def triangle(self):                                         # using vectors to draw a triangle("The Ship")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position - forward * self.radius
        b = self.position + forward * self.radius - right
        c = self.position + forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt                   # ensures smooth rotation

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()                         # returns a list (or array) of boolean values, where each index corresponds to a specific key on the keyboard. If a key is being pressed, the value at its index is True, otherwise, it’s False.

        if keys[pygame.K_a]:                                    
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.move(dt)