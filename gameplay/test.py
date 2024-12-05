import pygame
import sys
import random



white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lime = (0, 255, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
fuchsia = (255, 0, 255)
silver = (192, 192, 192)
gray = (128, 128, 128)
maroon = (128, 0, 0)
olive = (128, 128, 0)
Purple = (128, 0, 128)
Teal = (0, 128, 128)
Navy = (0, 0, 128)


background = pygame.image.load("GameBackground.jpg")
background1 = pygame.image.load("mesteren.png")



width = 1500
height = 1000

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("WohoGaming")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mesteren.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

        self.moving_right = False
        self.moving_left = False

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.x += 2
        if self.moving_left:
            self.rect.x -= 2
        if self.moving_up:
            self.rect.y -= 2
        if self.moving_down:
            self.rect.y += 2





def mainmenu():
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_u:
                    gameloop()
                    print("hi")


        screen.blit(background1, (0, 0))
        pygame.display.flip()
        pygame.display.update()






def gameloop():
    player_sprite = pygame.sprite.Group()
    player = Player()
    player_sprite.add(player)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.moving_right = True

                if event.key == pygame.K_a:
                    player.moving_left = True

                if event.key == pygame.K_w:
                    player.moving_up = True

                if event.key == pygame.K_s:
                    player.moving_down = True

                if event.key == pygame.K_u:
                    mainmenu()
                    print("hi")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.moving_right = False

                if event.key == pygame.K_a:
                    player.moving_left = False

                if event.key == pygame.K_w:
                    player.moving_up = False

                if event.key == pygame.K_s:
                    player.moving_down = False



        pygame.display.update()
        player_sprite.update()
        player.update()

        screen.blit(background, (0, 0))
        player_sprite.draw(screen)




        pygame.display.flip()



mainmenu()
