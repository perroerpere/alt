import pygame
import random



pygame.init()

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
plate_farge = (255, 0, 0)


spaceship = pygame.Rect(screen_width//2, screen_height - 100, 50, 50)
spaceship_speed = 5

asteroids = []
asteriod_speed = 5
asteroid_timer = 0

running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spaceship.left > 0:
            spaceship.x -= spaceship_speed
        if keys[pygame.K_RIGHT] and spaceship.right < screen_width:
            spaceship.x += spaceship_speed

        if asteroid_timer == 0:
            asteroid_x = random.randint(0, screen_width - 50)
            asteroid = pygame.Rect(asteroid_x, -50, 50, 50)
            asteroids.append(asteroid)
            asteroid_timer = 30
        else:
            asteroid_timer -= 1


        for asteroid in asteroids[:]:
            asteroid.y += asteriod_speed
            if asteroid.colliderect(spaceship):
                running = False
            if asteroid.top > screen_height:
                asteroids.remove(asteroid)


        pygame.draw.rect(screen, white, spaceship)

        for asteroid in asteroids:
            pygame.draw.rect(screen, white, asteroid)

        pygame.display.flip()

        pygame.time.Clock().tick(60)