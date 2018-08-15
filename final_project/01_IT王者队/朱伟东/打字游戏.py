import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background,(800,600))
font = pygame.font.Font("C:\windows\Fonts\Arial.ttf",25)
text1 = font.render(chr(random.randint(65,66)),True,(0,0,0))
texts_working = []
diffcult = 1
score = 0
max_diffcult = 0
max_score = 0
num = 3
rightnum = 0
falsenum = 0
speed = 0.1
count = 1000
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            print(chr(event.key))
            for i in texts_working:
                if chr(event.key).upper() == i[3]:
                    texts_working.remove(i)
                    score += 5
                    rightnum += 1
                    if score > max_score:
                        max_score = score
                    break
            else:
                score -= 1
                falsenum += 1

                # screen.blit(i[0], (i[1], i[2]))
    if num:
        screen.blit(background, (0, 0))
    text2 = font.render("Score:" + str(score), True, (255, 255, 255))
    text3 = font.render("diffcult:" + str(diffcult), True, (255, 255, 255))
    try:
        text4 = font.render("Right:"+ str(int(rightnum*100/(rightnum+falsenum))) + "%", True, (255, 255, 255))
    except ZeroDivisionError:
        text4 = font.render("Right:" + str(int(rightnum * 100 / (rightnum + falsenum + 0.1))) + "%", True,
                            (255, 255, 255))
    screen.blit(text2, (0, 0))
    screen.blit(text3, (0, 30))
    screen.blit(text4, (0, 60))
    if count >= 1000:
        c = chr(random.randint(65, 66))
        text1 = font.render(c, True, (255, 255, 255))
        x = random.randint(100,700)
        texts_working.append([text1,x,-25,c])
        # screen.blit(text1,(x,-25))
        count = random.randint(0,300)
    for i in texts_working:
        i[2] += speed
        if i[2] >600:
            score -= 50
            texts_working.remove(i)
        screen.blit(i[0], (i[1], i[2]))

    if score > diffcult * 100 or score < diffcult * 100:
        diffcult = int(score/100)
        if diffcult > max_diffcult:
            max_diffcult = diffcult
        speed = 0.05 + diffcult * 0.01
        num = 2 + diffcult
    if score < -100:
        text3 = font.render("Game over", True, (255, 255, 255))
        count = 0
        num = 0
        texts_working.clear()
        screen.blit(background, (0, 0))
        screen.blit(text3, (340, 200))
        text2 = font.render("Max Score:" + str(max_score), True, (255, 255, 255))
        text3 = font.render("Max diffcult:" + str(max_diffcult), True, (255, 255, 255))
        screen.blit(text2, (0, 0))
        screen.blit(text3, (0, 30))
    count += num
    pygame.display.update()