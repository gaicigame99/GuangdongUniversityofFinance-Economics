import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,800))
bj = pygame.image.load("tk.jpg")
bj = pygame.transform.scale(bj,(800,800))
qq = pygame.image.load("QQ.png")
qq = pygame.transform.scale(qq,(100,100))
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
font1 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 36)
fm = pygame.image.load("fm.jpg")
fm = pygame.transform.scale(fm, (800,800))
anniu = pygame.image.load("anniu.png")
word_list = list()
while True:
    word = chr(random.randint(65,90))
    word_list.append(word)
    word_list = list(set(word_list))
    if len(word_list) == 26:
        break
    else:
        word_list.append(chr(random.randint(65, 90)))
for i in range(len(word_list)):
    if len(word_list) == 26:
        break
    else:
        word_list.append(chr(random.randint(65,90)))
    print(word_list[i])

wx_position = list()
wy_position = list()

for i in range(len(word_list)):
    x = random.randint(0,800)
    y = random.randint(-300,-100)
    wx_position.append(x)
    wy_position.append(y)
speed = 0.1
score = 0
flag = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if flag == 0:
        screen.blit(fm, (0, 0))
        f_tip = font1.render("大吉大利，今晚打字", True, (110, 255, 255))
        screen.blit(f_tip,(230,72))
        screen.blit(anniu,(400-60,600))
        if event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x,mouse_y = pygame.mouse.get_pos()
             if 400 - 60 < mouse_x < 400 - 60 + 96 and 600 < mouse_y < 600 + 60:
                flag = 1

    if flag == 1:
        screen.blit(bj, (0, 0))
        for i in range(len(word_list)):
            text = font.render(word_list[i], True, (255, 255, 255))
            screen.blit(qq, (wx_position[i], wy_position[i]))
            screen.blit(text, (wx_position[i] + 40, wy_position[i] + 10))
            wy_position[i] += speed
            if wy_position[i] > 800:
                wy_position[i] = random.randint(-300, -100)
                wx_position[i] = random.randint(0, 800)
                score = score - 1
        if event.type == pygame.KEYDOWN:
            input = chr(event.key - 32)
            for letter in word_list:
                if input == letter and \
                    wy_position[word_list.index(letter)] > 0 and \
                    wy_position[word_list.index(letter)] < 800:
                    i = word_list.index(letter)
                    wy_position[i] = random.randint(-100, 0)
                    wx_position[i] = random.randint(0, 800)
                    score += 1
                elif input == letter and wy_position[word_list.index(letter)] < 0:
                    score -= 1

        if score > 0 and score % 20 == 0:
            speed += 0.01
            tip = font1.render("速度加快",True,(110,255,255))
            screen.blit(tip,(400,400))
        t_score = font.render("score:" + str(score), True, (255, 255, 255))
        screen.blit(t_score, (0, 36))

    pygame.display.update()