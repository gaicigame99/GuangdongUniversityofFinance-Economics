
import pygame
import random
def begin():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    background = pygame.image.load(r"images\bg.jpg")
    font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 36)
    ball = pygame.image.load(r"images\ball.png")
    play = pygame.image.load(r"images\play.png")
    play = pygame.transform.scale(play, (150,100))
    ball1 = pygame.image.load(r"images\Ball1.png")
    b1 = pygame.transform.scale(ball1, (30,30))
    b1_rect = b1.get_rect()
    bw =b1_rect.width
    while_cloar =(255,255,255)
    qiu = []
    r=[]
    x=[]
    y=[]
    x_speed=[]
    y_speed=[]
    for i in range(30):
        r.append(random.randint(10,90))
        x.append(random.randint(1, 800))
        y.append(random.randint(1, 600))
        x_speed.append(random.randint(-1,1))
        y_speed.append(random.randint(-1,1))
        qiu.append(1)
    speed=1
    bx=0
    by=0
    score=0
    flag =True
    fmouse =True
    def show_score(n_font, n_score, n_screen):
        # 显示分数
        text_score = n_font.render("分数:" + str(score), True, (255, 255, 255))
        n_screen.blit(text_score, (5, 10))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                fmouse =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.blit(background, (0, 0))
        bx, by = pygame.mouse.get_pos()
        if flag:
            screen.blit(b1, (bx, by))
            for i in range(len(r)):
                qiu[i]= pygame.transform.scale(ball, (r[i], r[i]))
                x[i] += x_speed[i]
                y[i] += y_speed[i]
                screen.blit(qiu[i], (x[i], y[i]))

                if y[i] < 0 or y[i]>600:
                    y_speed[i] = -y_speed[i]
                if x[i] > 800 - 16 or x[i] < 0:
                    x_speed[i] = -x_speed[i]
                if bx+bw>=x[i] and bx<=x[i]+r[i] and by+bw>=y[i] and by<=y[i]+r[i]:
                    if bw>=r[i]:
                        y[i]=-1000
                        score +=1
                        if bw <95:
                            bw += 3
                        b1 = pygame.transform.scale(ball1, (bw,bw))
                    else:
                        flag = False
        else:
            screen.blit(play, (300, 300))
            if fmouse and 300<=bx<=450 and 300<by<400:
                flag = True
                fmouse =False
                score =0
                b1 = pygame.transform.scale(ball1, (20, 20))
                for i in range(30):
                    r[i]=random.randint(10, 90)
                    x[i]=random.randint(1, 800)
                    y[i] = random.randint(1, 600)
        #print(bw)
        if len(r)==0 | score == 30:
            flag=False
        show_score(font, score, screen)
        pygame.display.update()