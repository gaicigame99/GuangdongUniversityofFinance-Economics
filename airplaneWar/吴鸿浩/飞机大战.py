import pygame
import random
import time

# 飞机大战
pygame.init()
pygame.mixer.init()
back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
bullet1_music = pygame.mixer.Sound(r"sound\bullet.wav")
edown_music = pygame.mixer.Sound(r"sound\enemy1_down.wav")
screen = pygame.display.set_mode((495, 800))
background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (495, 800))
hero = pygame.image.load("images\hero.gif")
enemy = pygame.image.load("images\enemy2.png")
enemy = pygame.transform.scale(enemy, (120, 140))
enemy1 = pygame.image.load("images\enemy-2.gif")
enemy1 = pygame.transform.scale(enemy1, (50, 70))
# 敌机死亡画面
enemy_down1_1 = pygame.image.load("images\enemy2_down1.png")
enemy_down1_1 = pygame.transform.scale(enemy_down1_1, (120, 140))
enemy_down1_2 = pygame.image.load("images\enemy2_down2.png")
enemy_down1_2 = pygame.transform.scale(enemy_down1_2, (120, 140))
enemy_down1_3 = pygame.image.load("images\enemy2_down3.png")
enemy_down1_3 = pygame.transform.scale(enemy_down1_3, (120, 140))
enemy_down1_4 = pygame.image.load("images\enemy2_down4.png")
enemy_down1_4 = pygame.transform.scale(enemy_down1_4, (120, 140))
enemy_down1_5 = pygame.image.load("images\enemy2_down5.png")
enemy_down1_5 = pygame.transform.scale(enemy_down1_5, (120, 140))
enemy_down1_6 = pygame.image.load("images\enemy2_down6.png")
enemy_down1_6 = pygame.transform.scale(enemy_down1_6, (120, 140))
enemy_down2 = pygame.image.load("images\enemy1_down3.png")
enemy_down2 = pygame.transform.scale(enemy_down2, (90, 120))
#子弹类型
bullet1 = pygame.image.load(r"images\bullet1.png")
bullet1 = pygame.transform.scale(bullet1, (15, 30))
bullet2 = pygame.image.load(r"images\bullet2.png")
bullet2 = pygame.transform.scale(bullet2, (15, 30))
bullet3 = pygame.image.load(r"images\bullet.png")
bullet3 = pygame.transform.scale(bullet3, (15, 15))
bullet4 = pygame.image.load(r"images\bullet4.png")
bullet4 = pygame.transform.scale(bullet4, (25, 25))
# 开始键
start = pygame.image.load("images\start.png")
start = pygame.transform.scale(start, (150, 150))
# 字体
font = pygame.font.Font("C:\Windows\Fonts\STENCIL.TTF", 50)
font1 = pygame.font.Font("C:\Windows\Fonts\STXINWEI.TTF", 30)
# 生命
live = pygame.image.load(r"images\live.png")
live = pygame.transform.scale(live, (25, 25))
# 加强道具
bomb1 = pygame.image.load(r"images\bomb-1.gif")
bomb1 = pygame.transform.scale(bomb1, (60, 90))
bomb2 = pygame.image.load(r"images\bomb-2.gif")
bomb2 = pygame.transform.scale(bomb2, (60, 90))
bomb3 = pygame.image.load(r"images\jialive.png")
bomb3 = pygame.transform.scale(bomb3, (30, 30))
# 获取自己飞机宽和高
hero = pygame.transform.scale(hero, (75, 100))
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height
hero_down = pygame.image.load("images\hero_blowup_n3.png")
hero_down = pygame.transform.scale(hero_down, (h_width, h_height))
# 获取敌人飞机宽和高
e_rect1 = enemy.get_rect()
e_width1 = e_rect1.width
e_height1 = e_rect1.height

e_rect2 = enemy1.get_rect()
e_width2 = e_rect2.width
e_height2 = e_rect2.height
# 敌机2数量
z1_num = 3
# 子弹列表
lbx = []
lby = []
lbx1 = []
lby1 = []
lbx1_1 = []
lby1_1 = []
ebx = []
eby = []
ebx_1 = []
eby_1 = []
ebx1 = []
eby1 = []
for i in range(z1_num):
    ebx1.append([])
    eby1.append([])
# 敌机数量列表
ex1 = []
ey1 = []
edx2 = []
edy2 = []
# 敌机位置
ex = 150
ey = -200
for j in range(z1_num):
    ex1.append(300)
    ey1.append(-200)
# 敌机死亡位置
edx1 = -200
edy1 = -200
for j in range(z1_num):
    edx2.append(-200)
    edy2.append(-200)
# 自己位置
hx = 100
hy = 100
# 自己死亡位置
hdx = -200
hdy = -200
# 道具位置
j_x = []
j_y = []
j_x1 = []
j_y1 = []
j_x2 = -200
j_y2 = -200
#时间初始化

e_time1 = 100

# 黑色道具x和y初始化
for a in range(1000):
    x = -200
    y = -200
    j_x.append(x)
    j_y.append(y)
# 红色道具x和y初始化
for a in range(1000):
    x = -200
    y = -200
    j_x1.append(x)
    j_y1.append(y)
# 判断
flag = 0
down_num = 0
down_num1 = []
for j in range(z1_num):
    down_num1.append(0)
herodown_num = 3#自己生命
jialife_num = 1#血包判断
jia_num = 0
jia_num1 = 0
b_speed = 0    # 自己子弹速度
zb_speed = 0   # 敌机子弹速度
zb_speed1 = 0  # 敌机提升子弹速度
pl = 15        # 子弹频率，越大频率越小
p2 = 250       # 敌机子弹频率，越大频率越小
e_speed = 0    # 敌机速度
time_1 = pl
time1 = p2
grade = 0
# 获取start 的宽高
s_rect = start.get_rect()
s_width = s_rect.width
s_height = s_rect.height
# start位置
sx = 180
sy = 300
while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 当自己死了，鼠标不能移动
    if herodown_num > 0:
        hx, hy = pygame.mouse.get_pos()
    elif herodown_num == 0:
        screen.blit(hero_down, (hdx, hdy))
        back_music.stop()
        text_1 = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text_1, (120, 350))
        hx = -200
        hy = -200
    # start键
    a, b, c = pygame.mouse.get_pressed()
    screen.blit(start, (sx, sy))
    if hx <= sx + s_width and hx >= sx and hy >= sy and hy <= sy + s_height and a:
        e_speed = 0.5
        b_speed = 3
        zb_speed = 1.5
        sx = -200
        sy = -200
        flag = 1
    if flag == 1:
        # 控制自己子弹频率
        if time_1:
            time_1 -= 1
        else:
            lbx.append(hx - 5)
            lby.append(hy - h_height / 2)
            lbx1.append(hx - 30)
            lby1.append(hy - h_height / 2)
            lbx1_1.append(hx + 20)
            lby1_1.append(hy - h_height / 2)
            time_1 = pl
        # 控制敌机子弹频率
        if time1:
            time1 -= 1
        else:
            ebx.append(ex + e_width1 / 2 - 10)
            eby.append(ey + e_height1)
            ebx_1.append(ex + e_width1 / 2 + 10)
            eby_1.append(ey + e_height1)
            for j in range(z1_num):
                ebx1[j].append(ex1[j] + e_width2 / 2 - 5)
                eby1[j].append(ey1[j] + e_height2)
            time1 = p2

        # 敌机1的子弹运动
        for i in range(len(ebx)):
            if grade < 20:  # 大型敌机单弹模式
                screen.blit(bullet2, (ebx[i], eby[i]))
                eby[i] += zb_speed
                # 子弹击中自己
                if eby[i] < hy + h_height / 2 and eby[i] + 30 >= hy - h_height / 2 and ebx[i] + 15 <= hx + h_width / 2 and \
                        ebx[i] >= hx - h_width / 2 and herodown_num > 0:
                    hdx = hx - h_width / 2
                    hdy = hy - h_height / 2
                    hx = -200
                    hy = -200
                    ebx[i] = -200
                    eby[i] = -200
                    herodown_num -= 1
                # 子弹超界限
                elif eby[i] > 800:
                    eby[i] = -300
                    ebx[i] = -300
            if grade >= 20:  # 大型敌机双弹模式（分数大于等于20分触发）
                screen.blit(bullet4, (ebx[i]-20, eby[i]))
                screen.blit(bullet4, (ebx_1[i]+10, eby_1[i]))
                eby[i] += zb_speed
                eby_1[i] += zb_speed
                # 双弹的第一个子弹击中自己
                if eby[i] < hy + h_height / 2 and eby[i] + 30 >= hy - h_height / 2 and ebx[i] + 15 <= hx + h_width / 2 and \
                        ebx[i] >= hx - h_width / 2 and herodown_num > 0:
                    hdx = hx - h_width / 2
                    hdy = hy - h_height / 2
                    hx = -200
                    hy = -200
                    ebx[i] = -200
                    eby[i] = -200
                    herodown_num -= 1
                elif eby[i] > 800:
                    eby[i] = -300
                    ebx[i] = -300
                # 双弹的第二个子弹击中自己
                if eby_1[i] < hy + h_height / 2 and eby_1[i] + 30 >= hy - h_height / 2 and ebx_1[
                    i] + 15 <= hx + h_width / 2 and ebx_1[i] >= hx - h_width / 2 and herodown_num > 0:
                    hdx = hx - h_width / 2
                    hdy = hy - h_height / 2
                    hx = -200
                    hy = -200
                    ebx_1[i] = -200
                    eby_1[i] = -200
                    herodown_num -= 1
                elif eby_1[i] > 800:
                    eby_1[i] = -300
                    ebx_1[i] = -300

        # 敌机2的子弹运动
        for j in range(z1_num):
            for i in range(len(ebx1[0])):
                screen.blit(bullet2, (ebx1[j][i], eby1[j][i]))
                eby1[j][i] += zb_speed
                # 子弹击中自己
                if eby1[j][i] < hy + h_height / 2 and eby1[j][i] + 30 >= hy - h_height / 2 and ebx1[j][i] + 15 <= hx + h_width / 2 and ebx1[j][i] >= hx - h_width / 2 and herodown_num > 0:
                    hdx = hx - h_width / 2
                    hdy = hy - h_height / 2
                    hx = -200
                    hy = -200
                    ebx1[j][i] = -200
                    eby1[j][i] = -200
                    herodown_num -= 1
                #子弹超界限
                elif eby1[j][i] > 800:
                    eby1[j][i] = -300
                    ebx1[j][i] = -300
        # screen.blit(hero_down, (hdx, hdy))
        # 自己子弹运动
        for i in range(len(lbx)):
            # 自己的子弹模式1
            if jia_num1 ==0 or jia_num1==2:
                screen.blit(bullet1, (lbx[i], lby[i]))
                lby[i] -= b_speed
                bullet1_music.play()
                # 击中大型敌机（只有击中一定数量的大型机才掉落道具）
                if lby[i] <= ey + e_height1 and lby[i] > ey and lbx[i] + 15 <= ex + e_width1 and lbx[i] >= ex and down_num == 0:
                    grade += 1
                    jia_num += 1
                    if jia_num % 7 == 0:  # 每击中7个大型机，获得子弹加速
                        j_x1[i] = random.randint(50, 350)
                        j_y1[i] = random.randint(200, 250)
                    if jia_num == 5 :  # 每击中5个大型机，获得子弹加倍
                        j_x[i] = random.randint(50, 350)
                        j_y[i] = random.randint(200, 250)
                    edown_music.play()
                    edx1 = ex
                    edy1 = ey
                    lbx[i] = -200
                    lby[i] = -200
                    down_num = 1
                    e_time1 = time.time()
                elif lby[i] < 0:
                    # del lby[i]
                    lby[i] = -300
                    lbx[i] = -300
                # 道具子弹加速
                if j_y1[i] + 90 >= hy - h_height / 2 and j_y1[i] < hy + h_height / 2 and j_x1[i] + 60 <= hx + h_width / 2 and j_x1[i] >= hx - h_width / 2:
                    j_x1[i] = -200
                    j_y1[i] = -200
                    b_speed += 2
                elif j_y1[i] >= 800:
                    j_y1[i] = -200
                    j_x1[i] = -200
                j_y1[i] += 3
                screen.blit(bomb2, (j_x1[i], j_y1[i]))
                # 道具子弹加倍
                if j_y[i] + 90 >= hy - h_height / 2 and j_y[i] < hy + h_height / 2 and j_x[i] + 60 <= hx + h_width / 2 and j_x[i] >= hx - h_width / 2:
                    j_x[i] = -200
                    j_y[i] = -200
                    if jia_num1 ==0:
                        jia_num1 = 1
                    else:
                        jia_num1 = 2
                elif j_y[i] >= 800:
                    j_y[i] = -200
                    j_x[i] = -200
                j_y[i] += 3
                screen.blit(bomb1, (j_x[i], j_y[i]))
                # 击中小型敌机
                for j in range(z1_num):
                    if lby[i] <= ey1[j] + e_height2 and lby[i] > ey1[j] and lbx[i] + 15 <= ex1[j] + e_width2 and lbx[i] >= ex1[j] and down_num1[j] == 0:
                        grade += 1
                        edown_music.play()
                        edx2[j] = ex1[j]
                        edy2[j] = ey1[j]
                        ex1[j] = -200
                        ey1[j] = -200
                        lbx[i] = -200
                        lby[i] = -200
                        down_num1[j] = 1
                    elif lby[i] < 0:
                        lby[i] = -300
                        lbx[i] = -300
                    screen.blit(enemy_down2, (edx2[j], edy2[j]))
            # 自己的子弹模式2
            if jia_num1 == 1 or jia_num1 ==2:
                screen.blit(bullet3, (lbx1[i], lby1[i]))
                screen.blit(bullet3, (lbx1_1[i], lby1_1[i]))
                lby1[i] -= b_speed
                lby1_1[i] -= b_speed
                bullet1_music.play()
                # 子弹模式二的子弹1击中大型敌机
                if lby1[i] <= ey + e_height1 and lby1[i] > ey and lbx1[i] + 15 <= ex + e_width1 and lbx1[i] >= ex and down_num == 0:
                    grade += 1
                    jia_num += 1
                    if jia_num % 7 == 0:  # 每击中7个大型机，获得子弹加速
                        j_x1[i] = random.randint(50, 350)
                        j_y1[i] = random.randint(200, 250)
                    if jia_num == 10:  # 每击中15个大型机，获得子弹加倍
                        j_x[i] = random.randint(50, 350)
                        j_y[i] = random.randint(200, 250)
                    edown_music.play()
                    edx1 = ex
                    edy1 = ey
                    # ex = -200
                    # ey = -200
                    lbx1[i] = -200
                    lby1[i] = -200
                    down_num = 1
                    e_time1 = time.time()
                elif lby1[i] < 0:
                    lby1[i] = -300
                    lbx1[i] = -300
                # 子弹模式二的子弹1击中小型敌机
                for j in range(z1_num):
                    if lby1[i] <= ey1[j] + e_height2 and lby1[i] > ey1[j] and lbx1[i] + 15 <= ex1[j] + e_width2 and lbx1[i] >= ex1[j] and down_num1[j] == 0:
                        grade += 1
                        edown_music.play()
                        edx2[j] = ex1[j]
                        edy2[j] = ey1[j]
                        ex1[j] = -200
                        ey1[j] = -200
                        lbx1[i] = -200
                        lby1[i] = -200
                        down_num1[j] = 1
                    elif lby1[i] < 0:
                        lby1[i] = -300
                        lbx1[i] = -300
                    screen.blit(enemy_down2, (edx2[j], edy2[j]))
                # 子弹模式二的子弹2击中大型敌机
                if lby1_1[i] <= ey + e_height1 and lby1_1[i] > ey and lbx1_1[i] + 15 <= ex + e_width1 and lbx1_1[i] >= ex and down_num == 0:
                    grade += 1
                    jia_num += 1
                    if jia_num % 7 == 0:  # 每击中7个大型机，获得子弹加速
                        j_x1[i] = random.randint(50, 350)
                        j_y1[i] = random.randint(200, 250)
                    if jia_num == 10:  # 每击中15个大型机，获得子弹加倍
                        j_x[i] = random.randint(50, 350)
                        j_y[i] = random.randint(200, 250)
                    edown_music.play()
                    edx1 = ex
                    edy1 = ey
                    # ex = -200
                    # ey = -200
                    lbx1_1[i] = -200
                    lby1_1[i] = -200
                    down_num = 1
                    e_time1 = time.time()
                elif lby1_1[i] < 0:
                    lby1_1[i] = -300
                    lbx1_1[i] = -300
                # 子弹模式二的子弹2击中小型敌机
                for j in range(z1_num):
                    if lby1_1[i] <= ey1[j] + e_height2 and lby1_1[i] > ey1[j] and lbx1_1[i] + 15 <= ex1[j] + e_width2 and lbx1_1[i] >= ex1[j] and down_num1[j] == 0:
                        grade += 1
                        edown_music.play()
                        edx2[j] = ex1[j]
                        edy2[j] = ey1[j]
                        ex1[j] = -200
                        ey1[j] = -200
                        lbx1_1[i] = -200
                        lby1_1[i] = -200
                        down_num1[j] = 1
                    elif lby1_1[i] < 0:
                        lby1_1[i] = -300
                        lbx1_1[i] = -300
                    screen.blit(enemy_down2, (edx2[j], edy2[j]))
                # 道具子弹加速
                if j_y1[i] + 90 >= hy - h_height / 2 and j_y1[i] < hy + h_height / 2 and j_x1[i] + 60 <= hx + h_width / 2 and j_x1[i] >= hx - h_width / 2:
                    j_x1[i] = -200
                    j_y1[i] = -200
                    b_speed += 2
                elif j_y1[i] >= 800:
                    j_y1[i] = -200
                    j_x1[i] = -200
                j_y1[i] += 3
                screen.blit(bomb2, (j_x1[i], j_y1[i]))
                # 道具子弹加倍
                if j_y[i] + 90 >= hy - h_height / 2 and j_y[i] < hy + h_height / 2 and j_x[i] + 60 <= hx + h_width / 2 and j_x[i] >= hx - h_width / 2:
                    j_x[i] = -200
                    j_y[i] = -200
                    jia_num1 = 2
                elif j_y[i] >= 800:
                    j_y[i] = -200
                    j_x[i] = -200
                j_y[i] += 3
                screen.blit(bomb1, (j_x[i], j_y[i]))

        #敌机死亡画面
        if time.time() - e_time1 < 0.05:
            screen.blit(enemy_down1_1, (edx1, edy1))
        elif time.time() - e_time1 < 0.1:
            screen.blit(enemy_down1_2, (edx1, edy1))
        elif time.time() - e_time1 < 0.15:
            screen.blit(enemy_down1_3, (edx1, edy1))
        elif time.time() - e_time1 < 0.20:
            screen.blit(enemy_down1_4, (edx1, edy1))
        elif time.time() - e_time1 < 0.25:
            screen.blit(enemy_down1_5, (edx1, edy1))
        elif time.time()- e_time1 < 0.30:
            screen.blit(enemy_down1_6, (edx1, edy1))
            edx1 = -200
            edy1 = -200
        # 大型机被击落和超界初始化
        if down_num == 1 or ey > 800:
            ex = random.randint(50, 400)
            ey = -200
            down_num = 0
        # 敌机运动
        ey += e_speed
        # 小型机被击落和超界初始化
        for j in range(z1_num):
            if down_num1[j] == 1 or ey1[j] > 800:
                edx2[j] = -200
                edy2[j] = -200
                ex1[j] = random.randint(50, 400)
                ey1[j] = random.randint(-200, -50)
                down_num1[j] = 0
            ey1[j] += e_speed
            screen.blit(enemy1, (ex1[j], ey1[j]))

        screen.blit(enemy, (ex, ey))
        screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))
        # 加生命道具
        if herodown_num == 1  and jialife_num ==1:
            x1 = random.randint(0,100)
            if x1 >= 50:   #50%概率掉血包
                j_x2 = random.randint(50, 350)
                j_y2 = random.randint(200, 250)
                jialife_num = 0
        j_y2 += 3
        if j_y2 + 30 >= hy - h_height / 2 and j_y2 < hy + h_height / 2 and j_x2 + 30 <= hx + h_width / 2 and j_x2 >= hx - h_width / 2:
            j_x2 = -200
            j_y2 = -200
            jialife_num = 1
            herodown_num += 1
        elif j_y2 >= 800:
            j_y2 = -200
            j_x2 = -200
            jialife_num = 1
        screen.blit(bomb3, (j_x2, j_y2))
        # 得分显示
        grade1 = "Scroe:" + str(grade)
        text_1 = font1.render(grade1, True, (0, 0, 220))
        # 生命显示
        screen.blit(text_1, (330, 40))
        text_2 = font1.render("Life:" , True, (0, 0, 220))
        screen.blit(text_2, (330, 15))
        for i in range(herodown_num):
             screen.blit(live, (390+i*30, 15))
    pygame.display.update()
