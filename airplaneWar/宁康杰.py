import pygame
import random
#飞机大战
#游戏规则：
#鼠标操作，点击开始游戏，开始游戏。击毁小中大型敌机飞机，获得（1，5，10）分，假如小中大型飞机安全离开界面，
# 减少我方敌机（1，5，8）血量。每1000分一关，随着关数的增加，敌机的速度会增加，道具的频率也会增加。拿一个
# 道具，子弹会变强，伤害加1。假如长时间没有拿道具，子弹会变为最弱的。
#爆炸效果          get
#添加游戏得分      get
#小，中，大型战机  血量1，10，80       get
#增加道具            get
#添加英雄生命值      get
#添加音效            get
#开始界面            get
#结束界面            get
#制作游戏关卡        get
pygame.init()
pygame.mixer.init()
back_mousic= pygame.mixer.Sound("sound\game_music.ogg")
back_mousic1= pygame.mixer.Sound("sound\enemy1_down.wav")
back_mousic2= pygame.mixer.Sound("sound\enemy2_down.wav")
back_mousic3= pygame.mixer.Sound("sound\enemy3_down.wav")
buttonm = pygame.mixer.Sound(r"sound\button.wav")
bulletm = pygame.mixer.Sound(r"sound\bullet.wav")
font = pygame.font.Font("C:\Windows\Fonts\msyh.ttf", 18)
font1 = pygame.font.Font("C:\Windows\Fonts\msyh.ttf", 36)
screen = pygame.display.set_mode((500,800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg,(500,800))
enemy0_down1 = pygame.image.load(r"images\enemy0_down1.png")
enemy0_down2 = pygame.image.load(r"images\enemy0_down2.png")
enemy0_down3 = pygame.image.load(r"images\enemy0_down3.png")
enemy0_down4 = pygame.image.load(r"images\enemy0_down4.png")
enemy1_down1 = pygame.image.load(r"images\enemy1_down1.png")
enemy1_down2 = pygame.image.load(r"images\enemy1_down2.png")
enemy1_down3 = pygame.image.load(r"images\enemy1_down3.png")
enemy1_down4 = pygame.image.load(r"images\enemy1_down4.png")
enemy2_down1 = pygame.image.load(r"images\enemy2_down1.png")
enemy2_down2 = pygame.image.load(r"images\enemy2_down2.png")
enemy2_down3 = pygame.image.load(r"images\enemy2_down3.png")
enemy2_down4 = pygame.image.load(r"images\enemy2_down4.png")
Key = pygame.image.load(r"images\button_nor.png")
Key2 = pygame.transform.scale(Key,(200,48))
# bg2 = pygame.image.load(r"1.jpg")
bg2 = pygame.image.load(r"images\background.png")
bg2 = pygame.transform.scale(bg2,(500,800))
bomb1 = pygame.image.load(r"images\bomb-1.gif")
bullet = pygame.image.load("images\\bullet.png")
bullet1 = pygame.image.load("images\\bullet1.png")
bullet2 = pygame.image.load("images\\bullet2.png")
Enemy = pygame.image.load("images\enemy0.png")
hero = pygame.image.load("images\hero.gif")

#我方战机
h_rect = hero.get_rect()      #获得飞机的模型
h_width = h_rect.width        #获得飞机宽度
h_height = h_rect.height      #获得飞机高度
hx = 100            #我方飞机开始的位置
hy = 100
#子弹
bx = []             #子弹的的坐标
by = []
vis = []            #标记子弹是否显示
times = 0          #标记出现子弹相隔的时间

#小型战机
Enemy_x = []        #敌机的坐标
Enemy_y = []
Enemy_times = []    #标记战机毁灭后的情景
vise = []           #标记敌机是否显示
times2 = 0         #标记出现敌机相隔的时间

#中型敌机
Enemy_mid = pygame.image.load("images\enemy1.png")
med_x = []
med_y = []
med_Q = []
med_times = []    #标记中型战机毁灭后的情景
times3 = 0         #标记出现中型敌机相隔的时间
vism2 = []           #标记中型敌机是否显示

#大型敌机
Enemy_max = pygame.image.load("images\enemy2.png")
max_x = []
max_y = []
max_Q = []
max_times = []    #标记大型战机毁灭后的情景
times4 = 0         #标记出现大型敌机相隔的时间
vism4 = []           #标记大型敌机是否显示

#道具
bomb1_x = 0
bomb1_y = 0
bomb1_vis = False
bomb1_times = 0

for i in range(200):    #初始化变量
    bx.append(0)              #子弹
    by.append(0)

    Enemy_x.append(0)         #小型战机
    Enemy_y.append(0)
    vis.append(False)
    vise.append(False)
    Enemy_times.append(500)

    med_x.append(0)           #中型战机
    med_y.append(0)
    med_Q.append(10)
    med_times.append(500)
    vism2.append(False)

    max_x.append(0)           #大型战机
    max_y.append(0)
    max_Q.append(80)
    max_times.append(500)
    vism4.append(False)
grade = 0                 #分数，小型敌机（1分），中型敌机（5分），大型敌机（10分）
bullet_vis = 0           #0(buttet号子弹)，1（buttet1号子弹），>2（buttet1号子弹）     三种子弹对应的伤害是（1，2，3）
kkk = 0
fa = 0
my_Q = 10               #如果小型战机安全离开（-1），中型（-5），大型（-8）
gu = 1
back_mousic.play(-1)
while True:
    #开始界面
    if fa==0:
        screen.blit(bg2, (0, 0))
        str1 = "请点击开始按键进入游戏 "
        t = font.render(str1, True, (0,0,0))
        screen.blit(t, (150, 550))
        screen.blit(Key, (180, 600))
        str2 = "开始游戏"
        t = font.render(str2, True, (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)))
        screen.blit(t, (210, 610))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                if x1>180 and x1<180+132 and y1>600 and y1<600+48:
                    fa = 1
        pygame.display.update()
###########################################################################################################################
    #结束界面
    if fa == 3:
        str1 = "游戏结束！ "
        t = font1.render(str1, True, (255, 0, 0))
        screen.blit(t, (170, 300))
        screen.blit(Key2, (150, 600))
        str2 = "充100元继续游戏"
        t = font.render(str2, True, (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)))
        screen.blit(t, (179, 610))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                if x1>180 and x1<180+132 and y1>600 and y1<600+48:
                    fa = 1
                    my_Q = 10
        pygame.display.update()
################################################################################################################################
    #游戏界面
    if fa == 1:
        screen.blit(bg,(0,0))
        gu = grade//500+1
        str1 = str(gu)  # 显示关卡
        text = font.render(str1, True, (0, 0, 255))
        screen.blit(text, (400, 2))
        str1 = "第        关 "
        text = font.render(str1, True, (0, 0, 0))
        screen.blit(text, (370, 2))

        str1 = str(grade)                             #显示得分
        text = font.render(str1, True, (0, 0, 255))
        screen.blit(text, (450,  20))
        str1 = "你的得分是: "
        text = font.render(str1, True, (0, 0, 0))
        screen.blit(text, (350, 20))
        times+=1                                   #这些变量只是一个时间上的一个辅助
        times2+=1
        times3+=1
        times4+=1
        bomb1_times += 1
        kkk += 1
        if kkk>600:                                #kkk控制1，2号子弹的时间，假如长时间没有吃道具，会变成0号子弹
            bullet_vis = 0
        if kkk>1000:
            kkk = 600
        hx, hy = pygame.mouse.get_pos()            #获取鼠标的坐标
    ###################################################################################################################################
        #子弹的显示与碰撞检测
        for i in range(200):       #子弹的位置小于0，置False
            if by[i]<0:
                vis[i]=False

        if times==1 or times>10:   #两个子弹出现的相隔时间
            for i in range(200):
                if vis[i]:
                    pass
                else:
                    bx[i] = hx-10
                    by[i] = hy
                    buttonm.play()
                    vis[i] = True   #加子弹
                    times = 2
                    break

        for i in range(200):
            if vis[i]:
                if bullet_vis==0:
                    screen.blit(bullet, (bx[i], by[i]))    #显示子弹
                if bullet_vis==1 :
                    screen.blit(bullet1, (bx[i], by[i]))  # 显示子弹
                if bullet_vis>=2:
                    screen.blit(bullet2, (bx[i], by[i]))  # 显示子弹
                by[i]-=9        #子弹速度
                for j in range(200):
                    if vise[j]:
                        if bx[i] + 22 > Enemy_x[j] and bx[i] < Enemy_x[j] + 51 and by[i] < Enemy_y[j] + 39 and by[i] + 22 > Enemy_y[j]:  #碰撞检测
                            back_mousic1.play()
                            vise[j] = False
                            grade+=1
                            Enemy_times[j] = 0
                            vis[i] = False

                    if vism2[j]:     #中型敌机的拼撞检测
                        if bx[i] + 22 > med_x[j] and bx[i] <med_x[j] + 69 and by[i] < med_y[j] + 89 and by[i] + 22 > med_y[j]:  #中型敌机拼撞检测
                            if bullet_vis<=2:
                                med_Q[j]-=(1+bullet_vis)
                            else:
                                med_Q[j] -= (1+2)
                            vis[i] = False
                            if med_Q[j]<0:
                                back_mousic2.play()
                                med_times[j] = 0
                                grade+=5
                                vism2[j] = False
                                med_Q[j] = 10

                    if vism4[j]:     #大型敌机的拼撞检测
                        if bx[i] + 22 > max_x[j] and bx[i] <max_x[j] + 165 and by[i] < max_y[j] + 246 and by[i] + 22 > max_y[j]:  #大型敌机拼撞检测
                            if bullet_vis<=2:
                                max_Q[j]-=(1+bullet_vis)
                            else:
                                max_Q[j] -= (1+2)
                            vis[i] = False
                            if max_Q[j]<0:
                                back_mousic3.play()
                                max_times[j] = 0
                                grade+=10
                                vism4[j] = False
                                max_Q[j] = 80

    ##############################################################################################################################
        #小型战机
        if times2 == 1 or times2 > 40:  #小型机出现的相隔时间
            for i in range(200):
                if vise[i]:
                    pass
                elif Enemy_times[i]<-2:
                    Enemy_x[i] = random.randint(50,450)
                    Enemy_y[i] = -50
                    vise[i] = True
                    times2 = 2
                    break

        for i in range(200):    #显示小型战机毁灭
            if vise[i]:
                pass
            elif Enemy_times[i]> -2 and Enemy_times[i]<35:
                if Enemy_times[i]<5:
                    screen.blit(enemy0_down1, (Enemy_x[i], Enemy_y[i]))
                if Enemy_times[i]<13 and Enemy_times[i]>5:
                    screen.blit(enemy0_down2, (Enemy_x[i], Enemy_y[i]))
                if Enemy_times[i]<21 and Enemy_times[i]>13:
                    screen.blit(enemy0_down3, (Enemy_x[i], Enemy_y[i]))
                if Enemy_times[i]<29 and Enemy_times[i]>21:
                    screen.blit(enemy0_down4, (Enemy_x[i], Enemy_y[i]))
                Enemy_times[i]+=1
            if Enemy_times[i]>29:
                Enemy_times[i] = -3

        for i in range(200):          #小型敌机的显示
            if vise[i]:
                if Enemy_y[i]>800:
                    my_Q-=1
                    vise[i] = False
                else:
                    screen.blit(Enemy,(Enemy_x[i],Enemy_y[i]))
                    # pygame.draw.line(screen, (205,186,150), (Enemy_x[i], Enemy_y[i]),
                    #                  (Enemy_x[i] + 51, Enemy_y[i]), 5)
                    Enemy_y[i]+=2+(gu-1)*0.5     #小型敌机的速度
    ##############################################################################################################################
        #中型敌机
        if times3 == 1 or times3 > 150:  #中型敌机出现的相隔时间
            for i in range(200):
                if vise[i]:
                    pass
                elif med_times[i]<-2:
                    med_x[i] = random.randint(50,450)
                    med_y[i] = -50
                    vism2[i] = True
                    times3 = 2
                    break

        for i in range(200):  # 显示中型战机毁灭
            if vism2[i]:
                pass
            elif med_times[i] > -2 and med_times[i] < 35:
                if med_times[i] < 5:
                    screen.blit(enemy1_down1, (med_x[i], med_y[i]))
                if med_times[i] < 13 and med_times[i] > 5:
                    screen.blit(enemy1_down2, (med_x[i], med_y[i]))
                if med_times[i] < 21 and med_times[i] > 13:
                    screen.blit(enemy1_down3, (med_x[i], med_y[i]))
                if med_times[i] < 29 and med_times[i] > 21:
                    screen.blit(enemy1_down4, (med_x[i], med_y[i]))
                med_times[i] += 1
            if med_times[i] > 29:
                med_times[i] = -3

        for i in range(200):  # 中型敌机的显示
            if vism2[i]:
                if med_y[i] > 800:
                    my_Q-=5
                    vism2[i] = False
                else:
                    screen.blit(Enemy_mid, (med_x[i], med_y[i]))
                    pygame.draw.line(screen, (144, 144, 144), (med_x[i], med_y[i]), (med_x[i]+69, med_y[i]), 6)
                    if med_Q[i]>2:
                        pygame.draw.line(screen, (205,186,150), (med_x[i], med_y[i]), (med_x[i]+(69/10)*med_Q[i], med_y[i]), 6)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (med_x[i], med_y[i]),(med_x[i] + (69 / 10) * med_Q[i], med_y[i]), 6)
                    med_y[i] += 2+(gu-1)*0.5    # 敌机的速度
    ################################################################################################################################
        # 大型敌机
        if times4 == 1 or times4 > 1500:  # 大型敌机出现的相隔时间
            for i in range(200):
                if vise[i]:
                    pass
                elif max_times[i] < -2:
                    max_x[i] = random.randint(50, 450)
                    max_y[i] = -150
                    vism4[i] = True
                    times4 = 2
                    break

        for i in range(200):  # 显示大型战机毁灭
            if vism4[i]:
                pass
            elif max_times[i] > -2 and max_times[i] < 35:
                if max_times[i] < 10:
                    screen.blit(enemy2_down1, (max_x[i], max_y[i]))
                if max_times[i] < 25 and max_times[i] > 10:
                    screen.blit(enemy2_down2, (max_x[i], max_y[i]))
                if max_times[i] < 40 and max_times[i] > 25:
                    screen.blit(enemy2_down3, (max_x[i], max_y[i]))
                if max_times[i] < 55 and max_times[i] > 40:
                    screen.blit(enemy2_down4, (max_x[i], max_y[i]))
                max_times[i] += 1
            if max_times[i] > 55:
                max_times[i] = -3

        for i in range(200):  # 大型敌机的显示
            if vism4[i]:
                if max_y[i] > 800:
                    my_Q-=8
                    vism4[i] = False
                else:
                    screen.blit(Enemy_max, (max_x[i], max_y[i]))
                    pygame.draw.line(screen, (144, 144, 144), (max_x[i], max_y[i]),(max_x[i] + 165, max_y[i]), 10)
                    if max_Q[i] > 3:
                        pygame.draw.line(screen, (255,165,79), (max_x[i], max_y[i]),
                                     (max_x[i] + (165 / 80) * max_Q[i], max_y[i]), 10)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (max_x[i], max_y[i]),
                                         (max_x[i] + (165 / 80) * max_Q[i], max_y[i]), 10)
                    max_y[i] += 0.3+(gu-1)*0.3   # 敌机的速度

    ################################################################################################################################
        #道具
        if bomb1_times>600-(gu-1)*50:
            bomb1_x = random.randint(50, 450)
            bomb1_y = -50
            bomb1_times = 0
            bomb1_vis = True
        if bomb1_vis:
            if hx + 100 > bomb1_x and hx < bomb1_x + 58 and hy < bomb1_y + 88 and hy + 124 > bomb1_y:  # 拼撞检测
                bulletm.play()
                bomb1_vis = False
                bullet_vis +=1
                kkk = 0
        if bomb1_vis:
            bomb1_y+=5
            screen.blit(bomb1,(bomb1_x,bomb1_y))
            if bomb1_y>800-(gu-1)*50*0.7:
                bomb1_vis = False

    ################################################################################################################################
        #结束界面
        if my_Q<=0:
            my_Q = -1
            fa = 3
        str1 = " Blood "
        t = font.render(str1, True, (0, 0, 0))
        screen.blit(t, (10, 2))
        pygame.draw.line(screen, (144, 144, 144), (10, 35), (150, 35), 12)
        if my_Q>5:
            pygame.draw.line(screen, (84,255,159), (10, 35), (((150-10) / 10) * my_Q + 10, 35), 10)
        elif my_Q>0:
            pygame.draw.line(screen, (255, 0, 0), (10, 35), (((150-10)/10)*my_Q+10, 35), 10)
    ################################################################################################################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(hero,(hx-h_width/2,hy-h_height/2))        #我方的战机的显示
        pygame.display.update()