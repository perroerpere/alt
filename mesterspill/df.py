import pygame
import sys
import random

width = 1500
height = 1000

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

background = pygame.image.load("GameBackground.jpg")

'#score'

score_start = 0

times_hit = 0


def scoreboard():
    font = pygame.font.SysFont("Arial", 26)
    score = font.render("score: " + str(score_start), True, black)
    screen.blit(score, ((width / 2), 50))


def score_check():
    with open("high_score.txt", "r") as file:
        old_score = file.read()
        file.close()
        old_score = int(old_score)
    new_score = score_start
    if new_score >= old_score:
        high_score = new_score
        print(f"You got the new high score with the score of {new_score}, the old high score was {old_score}")
    else:
        high_score = old_score
        print(f"high_score: {old_score}")
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))
        file.close()


'#score'


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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("lava.png")
        self.rect = self.image.get_rect()
        self.speed = random.randrange(1, 4)
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100 - height, -40 - height)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height + height:
            self.speed = random.randrange(1, 4)
            self.rect.x = random.randrange(width-self.rect.width)
            self.rect.y = random.randrange(-100-height, -40 - height)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(40, (width - 40))
        self.rect.y = random.randrange(40, (height-40))


class Boarders(pygame.sprite.Sprite):
    def __init__(self, brd_width, brd_height, brd_x, brd_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((brd_width, brd_height))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = brd_x
        self.rect.y = brd_y


class Hitpoints(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(50, 50)
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 100


def kode():
    exit()


# start game
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("WohoGaming")
pygame.key.set_repeat(True)

player_sprite = pygame.sprite.Group()
player = Player()
player_sprite.add(player)

'#boarders'

boarder_sprite1 = pygame.sprite.Group()
boarder1 = Boarders(width, 20, 0, 1000)
boarder_sprite1.add(boarder1)

boarder_sprite2 = pygame.sprite.Group()
boarder2 = Boarders(width, 20, 0, -20)
boarder_sprite2.add(boarder2)

boarder_sprite3 = pygame.sprite.Group()
boarder3 = Boarders(20, height, -20, 0)
boarder_sprite3.add(boarder3)

boarder_sprite4 = pygame.sprite.Group()
boarder4 = Boarders(20, height, 1500, 0)
boarder_sprite4.add(boarder4)

'#boarders'
'#hitpoints'

health_sprite = pygame.sprite.Group()
health = Hitpoints()
health_sprite.add(health)

'#hitpoints'


sprite_enemy = pygame.sprite.Group()


for fi in range(5):
    enemy = Enemy()
    sprite_enemy.add(enemy)

amount_of_coins = 4
coins_on_table = 4

sprite_coin = pygame.sprite.Group()
for i in range(amount_of_coins):
    coins = Coins()
    sprite_coin.add(coins)

'#game loop'

game_loop = True
menu = False

while game_loop:
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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.moving_right = False

            if event.key == pygame.K_a:
                player.moving_left = False

            if event.key == pygame.K_w:
                player.moving_up = False

            if event.key == pygame.K_s:
                player.moving_down = False

    get_hit = pygame.sprite.spritecollide(player, sprite_enemy, False)
    if get_hit:
        times_hit += 1


    stop_move_down = pygame.sprite.spritecollide(player, boarder_sprite1, False)
    if stop_move_down:
        player.moving_down = False
    stop_move_up = pygame.sprite.spritecollide(player, boarder_sprite2, False)
    if stop_move_up:
        player.moving_up = False

    stop_move_left = pygame.sprite.spritecollide(player, boarder_sprite3, False)
    if stop_move_left:
        player.moving_left = False

    stop_move_right = pygame.sprite.spritecollide(player, boarder_sprite4, False)
    if stop_move_right:
        player.moving_right = False

    if times_hit == 300:
        print(f"you got a score of {score_start}")
        score_check()
        sys.exit()

    points = pygame.sprite.spritecollide(player, sprite_coin, True)
    if points:
        score_start += 1
        coins_on_table -= 1
    if coins_on_table != 4:
        coins = Coins()
        sprite_coin.add(coins)
        coins_on_table += 1

    '#updates'

    player_sprite.update()
    sprite_enemy.update()
    player.update()

    '#updates'
    '#draw'

    screen.blit(background, (0, 0))
    sprite_coin.draw(screen)
    player_sprite.draw(screen)
    sprite_enemy.draw(screen)
    health_sprite.draw(screen)
    scoreboard()

    '#draw'

    pygame.display.flip()

    '#game loop'