import pygame
import sys
import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
plate_farge = (255, 0, 0)

background = pygame.image.load("badskmfkdsf.png")
width = 750
height = 575

turncount = random.randrange(1,3)

print(turncount)
player1 = 1
player2 = 2

class Plates(pygame.sprite.Sprite):
    def __init__(self, corner_x, corner_y, farge):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill(farge)
        self.rect = self.image.get_rect()
        self.rect.x = corner_x
        self.rect.y = corner_y

def playercheck(turncount):
    if turncount % 2 == 0:
        return True
    else:
        return False

def whatplayer(turncount):
    if playercheck(turncount):
        return 1
    else:
        return 2

def highscore(turncount):
    font = pygame.font.SysFont("Arial", 26)
    scorenow = font.render("Player " + str(whatplayer(turncount)) + " Turn", True, white)
    screen.blit(scorenow, ((100), 50))



pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("WohoGaming")
pygame.key.set_repeat(True)

platefarge1 = white
platefarge2 = white
platefarge3 = white

platefarge4 = white
platefarge5 = white
platefarge6 = white

platefarge7 = white
platefarge8 = white
platefarge9 = white


sprite_plates = pygame.sprite.Group()

plateend = Plates(600,420, black)

platerestart = Plates(600,220,green)


sprite_plates.add(plateend)
sprite_plates.add(platerestart)


gameloop = True

while gameloop:
    plate1 = Plates(10, 110, platefarge1)
    sprite_plates.add(plate1)

    plate2 = Plates(120, 110, platefarge2)
    sprite_plates.add(plate2)

    plate3 = Plates(230, 110, platefarge3)
    sprite_plates.add(plate3)


    plate4= Plates(10, 220, platefarge4)
    sprite_plates.add(plate4)

    plate5 = Plates(120, 220, platefarge5)
    sprite_plates.add(plate5)

    plate6 = Plates(230, 220, platefarge6)
    sprite_plates.add(plate6)



    plate7 = Plates(10, 330, platefarge7)
    sprite_plates.add(plate7)

    plate8 = Plates(120, 330, platefarge8)
    sprite_plates.add(plate8)

    plate9 = Plates(230, 330, platefarge9)
    sprite_plates.add(plate9)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            #1
            if mx > 10 and mx < 110 and my > 110 and my < 210:

                if playercheck(turncount):
                    platefarge1 = red
                else:
                    platefarge1 = blue
                turncount += 1

            #2
            if mx > 120 and mx < 220 and my > 110 and my < 210:

                if playercheck(turncount):
                    platefarge2 = red
                else:
                    platefarge2 = blue
                turncount += 1

            #3
            if mx > 230 and mx < 330 and my > 110 and my < 210:
                if playercheck(turncount):
                    platefarge3 = red
                else:
                    platefarge3= blue
                turncount += 1


            #6
            if mx > 10 and mx < 110 and my > 220 and my < 320:
                if playercheck(turncount):
                    platefarge4 = red
                else:
                    platefarge4 = blue
                turncount += 1

            #7
            if mx > 120 and mx < 220 and my > 220 and my < 320:
                if playercheck(turncount):
                    platefarge5 = red
                else:
                    platefarge5 = blue
                turncount += 1

            #8
            if mx > 230 and mx < 330 and my > 220 and my < 320:
                if playercheck(turncount):
                    platefarge6 = red
                else:
                    platefarge6 = blue
                turncount += 1


            #11
            if mx > 10 and mx < 110 and my > 330 and my < 430:
                if playercheck(turncount):
                    platefarge7 = red
                else:
                    platefarge7 = blue
                turncount += 1

            #12
            if mx > 120 and mx < 220 and my > 330 and my < 430:
                if playercheck(turncount):
                    platefarge8 = red
                else:
                    platefarge8 = blue
                turncount += 1

            #13
            if mx > 230 and mx < 330 and my > 330 and my < 430:
                if playercheck(turncount):
                    platefarge9 = red
                else:
                    platefarge9 = blue
                turncount += 1



            #restart(platerestart)
            if mx > 600 and mx < 700 and my > 220 and my < 320:
                score = 0
                platefarge1 = white
                platefarge2 = white
                platefarge3 = white

                platefarge4 = white
                platefarge5 = white
                platefarge6 = white

                platefarge7 = white
                platefarge8 = white
                platefarge9 = white

                turncount = random.randrange(1,3)

                print(len(sprite_plates))
            '''
            if plate_farge == blue:
                plate_farge = red
            else:
                plate_farge = blue
            '''
    sprite_plates.update()

    screen.blit(background, (0, 0))
    sprite_plates.draw(screen)
    highscore(turncount)

    pygame.display.flip()
