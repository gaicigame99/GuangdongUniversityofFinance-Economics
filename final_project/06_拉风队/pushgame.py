import pygame
import random
def begin():
    pygame.init()
    font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",25)
    screen=pygame.display.set_mode((800,600))
    background=pygame.image.load(r"images\背景.jpg")
    background=pygame.transform.scale(background,(800,600))
    biaoti=pygame.image.load(r"images\标题.png")
    biaoti=pygame.transform.scale(biaoti,(450,120))
    biaoti_y=80
    kaishi=pygame.image.load(r"images\开始.png")
    kaishi=pygame.transform.scale(kaishi,(200,50))
    kaishi_y=280
    tuichu=pygame.image.load(r"images\退出.png")
    tuichu=pygame.transform.scale(tuichu,(200,50))
    tuichu_y=380
    shuoming=pygame.image.load(r"images\说明.png")
    shuoming=pygame.transform.scale(shuoming,(200,50))
    shuoming_y=480
    lang=pygame.image.load(r"images\灰太狼2.png")
    lang=pygame.transform.scale(lang,(140,180))
    lang1=pygame.transform.scale(lang,(48,50))
    lang_y=280
    lang1_x=340
    lang1_y=170
    xiangzi=pygame.image.load(r"images\箱子.png")
    xiangzi=pygame.transform.scale(xiangzi,(100,120))
    xiangzi1=pygame.transform.scale(xiangzi,(40,40))
    xiangzi1_round1_x=[]
    xiangzi1_round1_y=[]

    for i in range(3):
        if i==0:
            xiangzi1_round1_x.append(341)
            xiangzi1_round1_y.append(253)
        if i==1:
            xiangzi1_round1_x.append(302)
            xiangzi1_round1_y.append(316)
        if i==2:
            xiangzi1_round1_x.append(420)
            xiangzi1_round1_y.append(285)
    xiangzi_y=300
    xiangzi1_rect= xiangzi1.get_rect()
    xiangzi1_height=xiangzi1_rect.height
    xiangzi1_width=xiangzi1_rect.width
    lang1_rect=lang1.get_rect()
    lang1_height=lang1_rect.height
    lang1_width=lang1_rect.width
    tree1=pygame.image.load(r"images\tree1.png")
    tree1=pygame.transform.scale(tree1,(80,80))
    tree1_y=100
    tree2=pygame.image.load(r"images\tree2.png")
    tree2=pygame.transform.scale(tree2,(60,60))
    tree2_y=400
    round_1=pygame.image.load(r"images\第一关.png")
    round_1=pygame.transform.scale(round_1,(800,600))
    jixu=pygame.image.load(r"images\继续.png")
    jixu=pygame.transform.scale(jixu,(140,42))
    chongwan=pygame.image.load(r"images\重玩.png")
    chongwan=pygame.transform.scale(chongwan,(140,42))
    zhuankuai=pygame.image.load(r"images\砖块.png")
    zhuankuai=pygame.transform.scale(zhuankuai,(600,330))
    hanbao=pygame.image.load(r"images\汉堡.png")
    hanbao=pygame.transform.scale(hanbao,(40,40))
    kaishi_rect=kaishi.get_rect()
    kaishi_width=kaishi_rect.width
    kaishi_height=kaishi_rect.height
    speed=0
    speed1=39
    speed2=39
    speed3=33
    speed4=33
    flag=0
    count=0
    flag_lang=0
    flag1_lang=0
    count1=0
    count2=0
    count3=0
    count4=0
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            mouse_x, mouse_y = pygame.mouse.get_pos()
            a, b, c = pygame.mouse.get_pressed()
            screen.blit(background, (0, 0))
            biaoti_y -= speed
            kaishi_y -= speed
            tuichu_y -= speed
            shuoming_y -= speed
            lang_y -= speed
            xiangzi_y -= speed
            tree1_y -= speed
            tree2_y -= speed

            if 300 < mouse_x < 300 + kaishi_width and 280 < mouse_y < 280 + kaishi_height and a:
                speed = 30
                flag = 1
            else:
                screen.blit(biaoti, (200, biaoti_y))
                screen.blit(kaishi, (300, kaishi_y))
                screen.blit(tuichu, (300, tuichu_y))
                screen.blit(shuoming, (300, shuoming_y))
                screen.blit(lang, (150, lang_y))
                screen.blit(xiangzi, (640, xiangzi_y))
                screen.blit(tree1, (100, tree1_y))
                screen.blit(tree2, (500, tree2_y))
            if flag == 1:
                flag1=0
                screen.blit(round_1, (0, 0))
                for i in range(3):
                    screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lang1_x -= speed1
                        count += 1
                        count1=1
                    if event.key == pygame.K_RIGHT:
                        lang1_x += speed2
                        count += 1
                        count2=1
                    if event.key == pygame.K_DOWN:
                        lang1_y += speed4
                        count += 1
                        count3=1
                    if event.key == pygame.K_UP:
                        lang1_y -= speed3
                        count += 1
                        count4=1
                for i in range(3):
                    if i==0:
                        if count3 == 1 :
                            if -5<xiangzi1_round1_x[i]-lang1_x<5and (-35<xiangzi1_round1_y[i]-lang1_y<-5 or 15<xiangzi1_round1_y[i]-lang1_y<45):

                                # lang1_y -= 33
                                xiangzi1_round1_y[i]+=34
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                flag1=1
                                print("第一个箱子:%d"%xiangzi1_round1_y[i])
                        if count4 == 1:
                            if -5 < xiangzi1_round1_x[i] - lang1_x < 5 and (-35<xiangzi1_round1_y[i]-lang1_y<-5 or 15<xiangzi1_round1_y[i]-lang1_y<45):
                                # lang1_y += 33
                                xiangzi1_round1_y[i]-=34
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                flag1=1
                                print(xiangzi1_round1_y[i])
                        if count1 == 1:
                            if (-58 < xiangzi1_round1_x[i] - lang1_x < -25 or 5 < xiangzi1_round1_x[i] - lang1_x < 48) and -5 < xiangzi1_round1_y[i] - lang1_y < 5:
                                # lang1_x -= 39
                                xiangzi1_round1_x[i]-=39
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                print(xiangzi1_round1_x[i])
                        if count2 == 1:
                            if (-58 < xiangzi1_round1_x[i] - lang1_x < -25 or 5 < xiangzi1_round1_x[i] - lang1_x < 48) and -5 < xiangzi1_round1_y[i] - lang1_y < 5:
                                xiangzi1_round1_x[i]+=39
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                print(xiangzi1_round1_x[i])
                    if i==1:
                        if count3 == 1:
                            if -5 < xiangzi1_round1_x[i] - lang1_x < 5 and (-35<xiangzi1_round1_y[i]-lang1_y<-5 or 15<xiangzi1_round1_y[i]-lang1_y<45):

                                # lang1_y -= 33
                                xiangzi1_round1_y[i] += 34
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                flag1=1
                                print(xiangzi1_round1_y[i])
                        if count4 == 1:
                            if -5 < xiangzi1_round1_x[i] - lang1_x < 5 and (-35<xiangzi1_round1_y[i]-lang1_y<-5 or 15<xiangzi1_round1_y[i]-lang1_y<45):
                                # lang1_y += 33
                                xiangzi1_round1_y[i] -= 34
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                flag1=1
                                print(xiangzi1_round1_y[i])
                        if count1 == 1:
                            if (-58 < xiangzi1_round1_x[i] - lang1_x < -25 or 5 < xiangzi1_round1_x[i] - lang1_x < 48) and -5 < xiangzi1_round1_y[i] - lang1_y < 5:

                                # lang1_x -= 39
                                xiangzi1_round1_x[i] -= 39
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                print(xiangzi1_round1_x[i])
                        if count2 == 1:
                            if (-58 < xiangzi1_round1_x[i] - lang1_x < -25 or 5 < xiangzi1_round1_x[i] - lang1_x < 48) and -5 < xiangzi1_round1_y[i] - lang1_y < 5:
                                xiangzi1_round1_x[i] += 39
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                print(xiangzi1_round1_x[i])
                    if i==2:
                        if count3 == 1:
                            if -5 < xiangzi1_round1_x[i] - lang1_x < 5 and (-35<xiangzi1_round1_y[i]-lang1_y<-5 or 15<xiangzi1_round1_y[i]-lang1_y<45):
                                # lang1_y -= 33
                                xiangzi1_round1_y[i] += 34
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                flag1=1
                                print(xiangzi1_round1_y[i])
                        if count4 == 1:
                            if -5 < xiangzi1_round1_x[i] - lang1_x < 5 and (-35<xiangzi1_round1_y[i]-lang1_y<-5 or 15<xiangzi1_round1_y[i]-lang1_y<45):
                                # lang1_y += 33
                                xiangzi1_round1_y[i] -= 34
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                flag1=1
                                print(xiangzi1_round1_y[i])
                        if count1 == 1:
                            if (-58 < xiangzi1_round1_x[i] - lang1_x < -25 or 5 < xiangzi1_round1_x[i] - lang1_x < 48) and -5 < xiangzi1_round1_y[i] - lang1_y < 5:

                                # lang1_x -= 39
                                xiangzi1_round1_x[i] -= 39
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                print(xiangzi1_round1_x[i])
                        if count2 == 1:
                            if (-58 < xiangzi1_round1_x[i] - lang1_x < -25 or 5 < xiangzi1_round1_x[i] - lang1_x < 48) and -5 < xiangzi1_round1_y[i] - lang1_y < 5:
                                xiangzi1_round1_x[i] += 39
                                screen.blit(xiangzi1, (xiangzi1_round1_x[i], xiangzi1_round1_y[i]))
                                print(xiangzi1_round1_x[i])


                screen.blit(xiangzi, (680, 60))
                font1 = font.render("第一关", True, (0, 0, 0, 50))
                screen.blit(font1, (660, 240))
                font2 = font.render("步数" + str(count), True, (0, 0, 0, 50))
                screen.blit(font2, (660, 280))
                screen.blit(jixu, (640, 380))
                screen.blit(chongwan, (640, 440))

                screen.blit(zhuankuai, (195, 178))
                screen.blit(hanbao, (420, 184))
                screen.blit(hanbao, (380, 184))
                screen.blit(hanbao, (460, 184))
                pygame.draw.line(screen, (0,0,0), (299, 218), (500, 218))#横2
                pygame.draw.line(screen, (0,0,0), (259, 286), (540, 286))#横四
                pygame.draw.line(screen, (0,0,0), (259, 320), (540, 320))#横五
                pygame.draw.line(screen, (0,0,0), (259, 354), (540, 354))#横六
                pygame.draw.line(screen, (0,0,0), (259, 388), (381, 388))#横七
                pygame.draw.line(screen, (0,0,0), (303, 188), (303, 390))#竖2
                pygame.draw.line(screen, (0,0,0), (343, 188), (343, 390))#竖3
                pygame.draw.line(screen, (0,0,0), (381, 188), (381, 390))#竖4
                pygame.draw.line(screen, (0,0,0), (423, 188), (423, 354))#竖5
                pygame.draw.line(screen, (0,0,0), (462, 188), (462, 354))#竖6
                pygame.draw.line(screen, (0,0,0), (502, 188), (502, 354))#竖7
                pygame.draw.line(screen, (0,0,0), (542, 253), (542, 354))#竖8
                pygame.draw.line(screen, (0,0,0), (303, 252), (540, 252))#横3
                pygame.draw.line(screen, (0,0,0), (303, 186), (502, 186))#横1
                pygame.draw.line(screen, (0,0,0), (259, 288), (259, 388))#竖1
                screen.blit(lang1, (lang1_x, lang1_y))


        pygame.display.update()


