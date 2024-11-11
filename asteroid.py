from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    containers = []

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new1 = self.velocity.rotate(angle)
            new2 = self.velocity.rotate(-angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid1.velocity = new1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid2.velocity = new2 * 1.2
