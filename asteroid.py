import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __ini__(self, x, y, radius):
        super().__ini__(x, y, radius)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle)
        vector_b = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_a = Asteroid(self.position[0], self.position[1],new_radius)
        child_b = Asteroid(self.position[0], self.position[1],new_radius)

        child_a.velocity = vector_a * 1.2
        child_b.velocity = vector_b * 1.2

    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, 'white', self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt
