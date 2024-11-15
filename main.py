# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidFild = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for entity in updatable:
            entity.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.doesCollide(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.doesCollide(player):
                print("Game over!")
                sys.exit()
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()  