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

times_lipped = 0

score = 0

besterun = 0

with open("high_score.txt", "r") as file:
    ol_score = file.read()
    file.close()
    ol_score = int(ol_score)
    besterun = ol_score

'''
scoreboard
'''
def fargevalg():
    tall = random.randrange(0,2)
    if tall == 1:
        return white
    else:
        return red

def highscore():
    font = pygame.font.SysFont("Arial", 26)
    scorenow = font.render("Highscore: " + str(besterun), True, white)
    screen.blit(scorenow, ((width / 2 + 200), 100))

def scoreboard():
    font = pygame.font.SysFont("Arial", 26)
    scorenow = font.render("Flips: " + str(score), True, white)
    screen.blit(scorenow, ((width / 2 + 200), 50))

def score_check():
    with open("high_score.txt", "r") as file:
        old_score = file.read()
        file.close()
        old_score = int(old_score)
    new_score = score
    if new_score <= old_score:
        high_score = new_score
        print(f"You got the new high score with the score of {new_score}, the old high score was {old_score}")
    else:
        high_score = old_score
        print(f"high_score: {old_score}")
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))
        file.close()

class Plates(pygame.sprite.Sprite):
    def __init__(self, corner_x, corner_y, farge):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill(farge)
        self.rect = self.image.get_rect()
        self.rect.x = corner_x
        self.rect.y = corner_y



pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("WohoGaming")
pygame.key.set_repeat(True)

platefarge1 = fargevalg()
platefarge2 = fargevalg()
platefarge3 = fargevalg()
platefarge4 = fargevalg()
platefarge5 = fargevalg()
platefarge6 = fargevalg()
platefarge7 = fargevalg()
platefarge8 = fargevalg()
platefarge9 = fargevalg()
platefarge10 = fargevalg()
platefarge11 = fargevalg()
platefarge12 = fargevalg()
platefarge13 = fargevalg()
platefarge14 = fargevalg()
platefarge15 = fargevalg()
platefarge16 = fargevalg()
platefarge17 = fargevalg()
platefarge18 = fargevalg()
platefarge19 = fargevalg()
platefarge20 = fargevalg()
platefarge21 = fargevalg()
platefarge22 = fargevalg()
platefarge23 = fargevalg()
platefarge24 = fargevalg()
platefarge25 = fargevalg()

sprite_plates = pygame.sprite.Group()

plateend = Plates(600,420, black)

platerestart = Plates(600,220,green)


sprite_plates.add(plateend)
sprite_plates.add(platerestart)


gameloop = True

while gameloop:
    plate1 = Plates(10, 10, platefarge1)
    sprite_plates.add(plate1)

    plate2 = Plates(120, 10, platefarge2)
    sprite_plates.add(plate2)

    plate3 = Plates(230, 10, platefarge3)
    sprite_plates.add(plate3)

    plate4 = Plates(340, 10, platefarge4)
    sprite_plates.add(plate4)

    plate5 = Plates(450, 10, platefarge5)
    sprite_plates.add(plate5)

    plate6 = Plates(10, 120, platefarge6)
    sprite_plates.add(plate6)

    plate7 = Plates(120, 120, platefarge7)
    sprite_plates.add(plate7)

    plate8 = Plates(230, 120, platefarge8)
    sprite_plates.add(plate8)

    plate9 = Plates(340, 120, platefarge9)
    sprite_plates.add(plate9)

    plate10 = Plates(450, 120, platefarge10)
    sprite_plates.add(plate10)

    plate11 = Plates(10, 230, platefarge11)
    sprite_plates.add(plate11)

    plate12 = Plates(120, 230, platefarge12)
    sprite_plates.add(plate12)

    plate13 = Plates(230, 230, platefarge13)
    sprite_plates.add(plate13)

    plate14 = Plates(340, 230, platefarge14)
    sprite_plates.add(plate14)

    plate15 = Plates(450, 230, platefarge15)
    sprite_plates.add(plate15)

    plate16 = Plates(10, 340, platefarge16)
    sprite_plates.add(plate16)

    plate17 = Plates(120, 340, platefarge17)
    sprite_plates.add(plate17)

    plate18 = Plates(230, 340, platefarge18)
    sprite_plates.add(plate18)

    plate19 = Plates(340, 340, platefarge19)
    sprite_plates.add(plate19)

    plate20 = Plates(450, 340, platefarge20)
    sprite_plates.add(plate20)

    plate21 = Plates(10, 450, platefarge21)
    sprite_plates.add(plate21)

    plate22 = Plates(120, 450, platefarge22)
    sprite_plates.add(plate22)

    plate23 = Plates(230, 450, platefarge23)
    sprite_plates.add(plate23)

    plate24 = Plates(340, 450, platefarge24)
    sprite_plates.add(plate24)

    plate25 = Plates(450, 450, platefarge25)
    sprite_plates.add(plate25)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            #1
            if mx > 10 and mx < 110 and my > 10 and my < 110:
                if platefarge1 == red:
                    platefarge1 = white
                else:
                    platefarge1 = red
                if platefarge2 == red:
                    platefarge2 = white
                else:
                    platefarge2 = red
                if platefarge6 == red:
                    platefarge6 = white
                else:
                    platefarge6 = red
                score += 1
            #2
            if mx > 120 and mx < 220 and my > 10 and my < 110:
                if platefarge2 == red:
                    platefarge2 = white
                else:
                    platefarge2 = red
                if platefarge1 == red:
                    platefarge1 = white
                else:
                    platefarge1 = red
                if platefarge3 == red:
                    platefarge3 = white
                else:
                    platefarge3 = red
                if platefarge7 == red:
                    platefarge7 = white
                else:
                    platefarge7 = red
                score += 1
            #3
            if mx > 230 and mx < 330 and my > 10 and my < 110:
                if platefarge3 == red:
                    platefarge3 = white
                else:
                    platefarge3 = red
                if platefarge2 == red:
                    platefarge2 = white
                else:
                    platefarge2 = red
                if platefarge4 == red:
                    platefarge4 = white
                else:
                    platefarge4 = red
                if platefarge8 == red:
                    platefarge8 = white
                else:
                    platefarge8 = red
                score += 1
            #4
            if mx > 340 and mx < 440 and my > 10 and my < 110:
                if platefarge4 == red:
                    platefarge4 = white
                else:
                    platefarge4 = red
                if platefarge3 == red:
                    platefarge3 = white
                else:
                    platefarge3 = red
                if platefarge5 == red:
                    platefarge5 = white
                else:
                    platefarge5 = red
                if platefarge9 == red:
                    platefarge9 = white
                else:
                    platefarge9 = red
                score += 1
            #5
            if mx > 450 and mx < 550 and my > 10 and my < 110:
                if platefarge5 == red:
                    platefarge5 = white
                else:
                    platefarge5 = red
                if platefarge4 == red:
                    platefarge4 = white
                else:
                    platefarge4 = red
                if platefarge10 == red:
                    platefarge10 = white
                else:
                    platefarge10 = red
                score += 1
            #6
            if mx > 10 and mx < 110 and my > 120 and my < 220:
                if platefarge6 == red:
                    platefarge6 = white
                else:
                    platefarge6 = red
                if platefarge1 == red:
                    platefarge1 = white
                else:
                    platefarge1 = red
                if platefarge7 == red:
                    platefarge7 = white
                else:
                    platefarge7 = red
                if platefarge11 == red:
                    platefarge11 = white
                else:
                    platefarge11 = red
                score += 1
            #7
            if mx > 120 and mx < 220 and my > 120 and my < 220:
                if platefarge7 == red:
                    platefarge7 = white
                else:
                    platefarge7 = red
                if platefarge2 == red:
                    platefarge2 = white
                else:
                    platefarge2 = red
                if platefarge6 == red:
                    platefarge6 = white
                else:
                    platefarge6 = red
                if platefarge8 == red:
                    platefarge8 = white
                else:
                    platefarge8 = red
                if platefarge12 == red:
                    platefarge12 = white
                else:
                    platefarge12 = red
                score += 1
            #8
            if mx > 230 and mx < 330 and my > 120 and my < 220:
                if platefarge8 == red:
                    platefarge8 = white
                else:
                    platefarge8 = red
                if platefarge3 == red:
                    platefarge3 = white
                else:
                    platefarge3 = red
                if platefarge7 == red:
                    platefarge7 = white
                else:
                    platefarge7 = red
                if platefarge9 == red:
                    platefarge9 = white
                else:
                    platefarge9 = red
                if platefarge13 == red:
                    platefarge13 = white
                else:
                    platefarge13 = red
                score += 1
            #9
            if mx > 340 and mx < 440 and my > 120 and my < 220:
                if platefarge9 == red:
                    platefarge9 = white
                else:
                    platefarge9 = red
                if platefarge4 == red:
                    platefarge4 = white
                else:
                    platefarge4 = red
                if platefarge8 == red:
                    platefarge8 = white
                else:
                    platefarge8 = red
                if platefarge10 == red:
                    platefarge10 = white
                else:
                    platefarge10 = red
                if platefarge14 == red:
                    platefarge14 = white
                else:
                    platefarge14 = red
                score += 1
            #10
            if mx > 450 and mx < 550 and my > 120 and my < 220:
                if platefarge10 == red:
                    platefarge10 = white
                else:
                    platefarge10 = red
                if platefarge5 == red:
                    platefarge5 = white
                else:
                    platefarge5 = red
                if platefarge9 == red:
                    platefarge9 = white
                else:
                    platefarge9 = red
                if platefarge15 == red:
                    platefarge15 = white
                else:
                    platefarge15 = red
                score += 1
            #11
            if mx > 10 and mx < 110 and my > 230 and my < 330:
                if platefarge11 == red:
                    platefarge11 = white
                else:
                    platefarge11 = red
                if platefarge6 == red:
                    platefarge6 = white
                else:
                    platefarge6 = red
                if platefarge12 == red:
                    platefarge12 = white
                else:
                    platefarge12 = red
                if platefarge16 == red:
                    platefarge16 = white
                else:
                    platefarge16 = red
                score += 1
            #12
            if mx > 120 and mx < 220 and my > 230 and my < 330:
                if platefarge12 == red:
                    platefarge12 = white
                else:
                    platefarge12 = red
                if platefarge7 == red:
                    platefarge7 = white
                else:
                    platefarge7 = red
                if platefarge11 == red:
                    platefarge11 = white
                else:
                    platefarge11 = red
                if platefarge13 == red:
                    platefarge13 = white
                else:
                    platefarge13 = red
                if platefarge17 == red:
                    platefarge17 = white
                else:
                    platefarge17 = red
                score += 1
            #13
            if mx > 230 and mx < 330 and my > 230 and my < 330:
                if platefarge13 == red:
                    platefarge13 = white
                else:
                    platefarge13 = red
                if platefarge8 == red:
                    platefarge8 = white
                else:
                    platefarge8 = red
                if platefarge12 == red:
                    platefarge12 = white
                else:
                    platefarge12 = red
                if platefarge14 == red:
                    platefarge14 = white
                else:
                    platefarge14 = red
                if platefarge18 == red:
                    platefarge18 = white
                else:
                    platefarge18 = red
                score += 1
            #14
            if mx > 340 and mx < 440 and my > 230 and my < 330:
                if platefarge14 == red:
                    platefarge14 = white
                else:
                    platefarge14 = red
                if platefarge9 == red:
                    platefarge9 = white
                else:
                    platefarge9 = red
                if platefarge13 == red:
                    platefarge13 = white
                else:
                    platefarge13 = red
                if platefarge15 == red:
                    platefarge15 = white
                else:
                    platefarge15 = red
                if platefarge19 == red:
                    platefarge19 = white
                else:
                    platefarge19 = red
                score += 1
            #15
            if mx > 450 and mx < 550 and my > 230 and my < 330:
                if platefarge15 == red:
                    platefarge15 = white
                else:
                    platefarge15 = red
                if platefarge10 == red:
                    platefarge10 = white
                else:
                    platefarge10 = red
                if platefarge14 == red:
                    platefarge14 = white
                else:
                    platefarge14 = red
                if platefarge20 == red:
                    platefarge20 = white
                else:
                    platefarge20 = red
                score += 1
            #16
            if mx > 10 and mx < 110 and my > 340 and my < 440:
                if platefarge16 == red:
                    platefarge16 = white
                else:
                    platefarge16 = red
                if platefarge11 == red:
                    platefarge11 = white
                else:
                    platefarge11 = red
                if platefarge17 == red:
                    platefarge17 = white
                else:
                    platefarge17 = red
                if platefarge21 == red:
                    platefarge21 = white
                else:
                    platefarge21 = red
                score += 1
            #17
            if mx > 120 and mx < 220 and my > 340 and my < 440:
                if platefarge17 == red:
                    platefarge17 = white
                else:
                    platefarge17 = red
                if platefarge12 == red:
                    platefarge12 = white
                else:
                    platefarge12 = red
                if platefarge16 == red:
                    platefarge16 = white
                else:
                    platefarge16 = red
                if platefarge18 == red:
                    platefarge18 = white
                else:
                    platefarge18 = red
                if platefarge22 == red:
                    platefarge22 = white
                else:
                    platefarge22 = red
                score += 1
            #18
            if mx > 230 and mx < 330 and my > 340 and my < 440:
                if platefarge18 == red:
                    platefarge18 = white
                else:
                    platefarge18 = red
                if platefarge13 == red:
                    platefarge13 = white
                else:
                    platefarge13 = red
                if platefarge17 == red:
                    platefarge17 = white
                else:
                    platefarge17 = red
                if platefarge19 == red:
                    platefarge19 = white
                else:
                    platefarge19 = red
                if platefarge23 == red:
                    platefarge23 = white
                else:
                    platefarge23 = red
                score += 1
            #19
            if mx > 340 and mx < 440 and my > 340 and my < 440:
                if platefarge19 == red:
                    platefarge19 = white
                else:
                    platefarge19 = red
                if platefarge14 == red:
                    platefarge14 = white
                else:
                    platefarge14 = red
                if platefarge18 == red:
                    platefarge18 = white
                else:
                    platefarge18 = red
                if platefarge24 == red:
                    platefarge24 = white
                else:
                    platefarge24 = red
                if platefarge20 == red:
                    platefarge20 = white
                else:
                    platefarge20 = red
                score += 1
            #20
            if mx > 450 and mx < 550 and my > 340 and my < 440:
                if platefarge20 == red:
                    platefarge20 = white
                else:
                    platefarge20 = red
                if platefarge15 == red:
                    platefarge15 = white
                else:
                    platefarge15 = red
                if platefarge19 == red:
                    platefarge19 = white
                else:
                    platefarge19 = red
                if platefarge25 == red:
                    platefarge25 = white
                else:
                    platefarge25 = red
                score += 1
            #21
            if mx > 10 and mx < 110 and my > 450 and my < 550:
                if platefarge21 == red:
                    platefarge21 = white
                else:
                    platefarge21 = red
                if platefarge22 == red:
                    platefarge22 = white
                else:
                    platefarge22 = red
                if platefarge16 == red:
                    platefarge16 = white
                else:
                    platefarge16 = red
                score += 1
            #22
            if mx > 120 and mx < 220 and my > 450 and my < 550: #22
                if platefarge22 == red:
                    platefarge22 = white
                else:
                    platefarge22 = red
                if platefarge21 == red:
                    platefarge21 = white
                else:
                    platefarge21 = red
                if platefarge23 == red:
                    platefarge23 = white
                else:
                    platefarge23 = red
                if platefarge17 == red:
                    platefarge17 = white
                else:
                    platefarge17 = red
                score += 1
            #23
            if mx > 230 and mx < 330 and my > 450 and my < 550: #23
                if platefarge23 == red:
                    platefarge23 = white
                else:
                    platefarge23 = red
                if platefarge18 == red:
                    platefarge18 = white
                else:
                    platefarge18 = red
                if platefarge22 == red:
                    platefarge22 = white
                else:
                    platefarge22 = red
                if platefarge24 == red:
                    platefarge24 = white
                else:
                    platefarge24 = red
                score += 1
            #24
            if mx > 340 and mx < 440 and my > 450 and my < 550:
                if platefarge24 == red:
                    platefarge24 = white
                else:
                    platefarge24 = red
                if platefarge19 == red:
                    platefarge19 = white
                else:
                    platefarge19 = red
                if platefarge23 == red:
                    platefarge23 = white
                else:
                    platefarge23 = red
                if platefarge25 == red:
                    platefarge25 = white
                else:
                    platefarge25 = red
                score += 1
            #25
            if mx > 450 and mx < 550 and my > 450 and my < 550:
                if platefarge25 == red:
                    platefarge25 = white
                else:
                    platefarge25 = red
                if platefarge20 == red:
                    platefarge20 = white
                else:
                    platefarge20 = red
                if platefarge24 == red:
                    platefarge24 = white
                else:
                    platefarge24 = red
                score += 1
            #finish(plateend)
            if mx > 600 and mx < 700 and my > 420 and my < 520:
                score_check()
            #restart(platerestart)
            if mx > 600 and mx < 700 and my > 220 and my < 320:
                score = 0
                platefarge1 = fargevalg()
                platefarge2 = fargevalg()
                platefarge3 = fargevalg()
                platefarge4 = fargevalg()
                platefarge5 = fargevalg()
                platefarge6 = fargevalg()
                platefarge7 = fargevalg()
                platefarge8 = fargevalg()
                platefarge9 = fargevalg()
                platefarge10 = fargevalg()
                platefarge11 = fargevalg()
                platefarge12 = fargevalg()
                platefarge13 = fargevalg()
                platefarge14 = fargevalg()
                platefarge15 = fargevalg()
                platefarge16 = fargevalg()
                platefarge17 = fargevalg()
                platefarge18 = fargevalg()
                platefarge19 = fargevalg()
                platefarge20 = fargevalg()
                platefarge21 = fargevalg()
                platefarge22 = fargevalg()
                platefarge23 = fargevalg()
                platefarge24 = fargevalg()
                platefarge25 = fargevalg()
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
    scoreboard()
    highscore()

    pygame.display.flip()