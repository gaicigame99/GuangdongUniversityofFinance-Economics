import pygame
import random

pygame.init()
pygame.mixer.init()
backmusic = pygame.mixer.Sound("sound\game_music.ogg")
backmusic.play()
screen = pygame.display.set_mode((480, 800))

# 开始界面
startbg = pygame.image.load("start.jpg")
startbg = pygame.transform.scale(startbg, (480, 800))
button1 = pygame.image.load("button1.png")
button2 = pygame.image.load("button2.png")
background = pygame.image.load(r"images\background.png")
game_load = pygame.image.load("images\game_loading3.png")

# 英雄战机
hero1 = pygame.image.load("images\hero.gif")
hero1 = pygame.transform.scale(hero1, (75, 83))
hero1_down1 = pygame.image.load("images\hero_blowup_n1.png")
hero1_down1 = pygame.transform.scale(hero1_down1, (75, 83))
hero1_down2 = pygame.image.load("images\hero_blowup_n2.png")
hero1_down2 = pygame.transform.scale(hero1_down2, (75, 83))
hero1_down3 = pygame.image.load("images\hero_blowup_n3.png")
hero1_down3 = pygame.transform.scale(hero1_down3, (75, 83))
hero1_down4 = pygame.image.load("images\hero_blowup_n4.png")
hero1_down4 = pygame.transform.scale(hero1_down4, (75, 83))

# 子弹
bullet1 = pygame.image.load(r"images\bullet.png")
bullet2 = pygame.image.load(r"images\bullet1.png")

# 敌方战机
enemy1 = pygame.image.load("images\enemy1.png")
enemy1_down1 = pygame.image.load("images\enemy1_down1.png")
enemy1_down2 = pygame.image.load("images\enemy1_down2.png")
enemy1_down3 = pygame.image.load("images\enemy1_down3.png")
enemy1_down4 = pygame.image.load("images\enemy1_down4.png")

enemy0 = pygame.image.load("images\enemy0.png")
enemy0_down1 = pygame.image.load("images\enemy0_down1.png")
enemy0_down2 = pygame.image.load("images\enemy0_down2.png")
enemy0_down3 = pygame.image.load("images\enemy0_down3.png")
enemy0_down4 = pygame.image.load("images\enemy0_down4.png")

# 按钮参数
bu_rect = button1.get_rect()
bu_width = bu_rect.width
bu_height = bu_rect.height
# 英雄子弹参数
b_rect1 = bullet1.get_rect()
b_width1 = b_rect1.width
b_height1 = b_rect1.height

# 敌方子弹参数
b_rect2 = bullet2.get_rect()
b_width2 = b_rect2.width
b_height2 = b_rect2.height

# 英雄战机参数
h_rect1 = hero1.get_rect()
h_width1 = h_rect1.width
h_height1 = h_rect1.height

# 敌方战机参数
e_rect0 = enemy0.get_rect()
e_width0 = e_rect0.width
e_height0 = e_rect0.height
e_rect1 = enemy1.get_rect()
e_width1 = e_rect1.width
e_height1 = e_rect1.height

# 英雄战机坐标
hx = 100
hy = 100

# 英雄子弹坐标
b_hx = []
b_hy = []
h_bullet = []

# 敌方子弹坐标
b_ex0 = []
b_ey0 = []
e0_bullet = []
b_ex1 = []
b_ey1 = []
e1_bullet = []

# 敌方战机坐标
ex0 = []
ey0 = []
ex1 = []
ey1 = []

# 子弹移动速度
speed_hb = 5
speed_eb = 3

# 敌机移动速度
speed_e = 2

# 子弹发射频率
rate1 = 10
time1 = rate1
rate2 = 100
time2 = rate2

font1 = pygame.font.Font("C:\Windows\Fonts\ALGER.TTF", 20)
font2 = pygame.font.Font("C:\Windows\Fonts\ALGER.TTF", 50)
font3 = pygame.font.Font("C:\Windows\Fonts\STHUPO.TTF", 30)
start = font3.render("开始游戏", True, (0, 0, 0))
score1 = 0

for i in range(3):
    # 添加敌方战机坐标
    ex1.append(100 + i * (e_width1 + 40))
    ey1.append(20)
    ex0.append(150 + i * (e_width0 + 20))
    ey0.append(20 + e_height1 + 20)
    # 添加敌方子弹坐标
    b_ex1.append([])
    b_ey1.append([])
    b_ex0.append([])
    b_ey0.append([])

mouse = 1  # 游戏是否结束标志
flag_button = 0  # 游戏是否开始标志
flag = 0
glx = 0
# 生命值
live = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if flag_button == 0:
        # 游戏开始界面
        screen.blit(startbg, (0, 0))
        bx = 150
        by = 300
        screen.blit(game_load, (glx, by - 100))
        glx += 1
        if glx > 480:
            glx = 0
        screen.blit(button1, (bx, by))
        screen.blit(start, (bx + 60, by))
        a, b, c = pygame.mouse.get_pressed()
        hx, hy = pygame.mouse.get_pos()
        if bx < hx < bx + bu_width and by < hy < by + bu_height and a:
            screen.blit(button2, (bx, by))
            flag += 1
            if flag == 10:
                flag_button = 1
    if live == 0:
        screen.blit(over, (100, 300))
        speed_hb = 0
        speed_eb = 0
        speed_e = 0
        mouse = 0
    if flag_button and live > 0:
        screen.blit(background, (0, 0))
        score = font1.render("score:" + str(score1), True, (0, 0, 0))
        live_h = font1.render("live:"+str(live), True, (0, 0, 0))
        over = font2.render("GAME OVER!", True, (0, 0, 0))
        screen.blit(score, (370, 10))
        screen.blit(live_h, (370, 40))
        if mouse:
            hx, hy = pygame.mouse.get_pos()
            screen.blit(hero1, (hx - h_width1 / 2, hy - h_height1 / 2))

        if time1:
            time1 -= 1
        else:
            # 添加英雄子弹发射坐标
            b_hx.append(hx - b_width1 / 2)
            b_hy.append(hy - h_height1 / 2 - b_height1)
            time1 = rate1

        if time2:
            time2 -= 1
        else:
            # 添加敌方子弹发射坐标
            for i in range(3):
                b_ex1[i].append(ex1[i] + e_width1 / 2 - b_width2 / 2)
                b_ey1[i].append(ey1[i] + e_height1)
                b_ex0[i].append(ex0[i] + e_width0 / 2 - b_width2 / 2)
                b_ey0[i].append(ey0[i] + e_height0)
            time2 = rate2

        for i in range(3):
            # 敌方战机移动
            ey0[i] += speed_e
            ey1[i] += speed_e
            screen.blit(enemy1, (ex1[i], ey1[i]))
            screen.blit(enemy0, (ex0[i], ey0[i]))

        for i in range(len(b_hx)):
            # 英雄子弹发射
            h_bullet.append(screen.blit(bullet1, (b_hx[i], b_hy[i])))
            b_hy[i] -= speed_hb
            if b_hy[i] < 0:
                del h_bullet[i]

            for a in range(3):
                # 检测子弹碰撞敌机
                if b_hx[i] + b_width1 > ex1[a] and \
                        b_hx[i] < ex1[a] + e_width1 and \
                        b_hy[i] < ey1[a] + e_height1 and \
                        b_hy[i] + b_height1 > ey1[a]:
                    screen.blit(enemy1_down1, (ex1[a], ey1[a]))
                    screen.blit(enemy1_down2, (ex1[a], ey1[a]))
                    screen.blit(enemy1_down3, (ex1[a], ey1[a]))
                    screen.blit(enemy1_down4, (ex1[a], ey1[a]))
                    ey1[a] = -200
                    ex1[a] = random.randint(0, 480 - e_width1)
                    score1 += 1

                elif b_hx[i] + b_width1 > ex0[a] and \
                        b_hx[i] < ex0[a] + e_width0 and \
                        b_hy[i] < ey0[a] + e_height0 and \
                        b_hy[i] + b_height1 > ey0[a]:
                    screen.blit(enemy0_down1, (ex0[a], ey0[a]))
                    screen.blit(enemy0_down2, (ex0[a], ey0[a]))
                    screen.blit(enemy0_down3, (ex0[a], ey0[a]))
                    screen.blit(enemy0_down4, (ex0[a], ey0[a]))
                    ey0[a] = -200
                    ex0[a] = random.randint(0, 480 - e_width0)
                    score1 += 1
                # 检测敌机是否没被子弹击中
                elif ey0[a] > 800:
                    ey0[a] = -100
                    ex0[a] = random.randint(0, 480 - e_width0)
                elif ey1[a] > 800:
                    ey1[a] = -100
                    ex1[a] = random.randint(0, 480 - e_width0)

        for i in range(3):
            for a in range(len(b_ex1[0])):
                e1_bullet.append(screen.blit(bullet2, (b_ex1[i][a], b_ey1[i][a])))
                b_ey1[i][a] += speed_eb
                if b_ey1[i][a] > 800:
                    del e1_bullet[a]

                if b_ex1[i][a] + b_width2 > hx - h_width1 / 2 and \
                        b_ex1[i][a] < hx - h_width1 / 2 + h_width1 and \
                        b_ey1[i][a] < hy - h_height1 / 2 + h_height1 and \
                        b_ey1[i][a] + b_height2 > hy - h_height1 / 2 and \
                        live > 0:
                    screen.blit(hero1_down1, (hx - h_width1 / 2, hy - h_height1 / 2))
                    screen.blit(hero1_down2, (hx - h_width1 / 2, hy - h_height1 / 2))
                    screen.blit(hero1_down3, (hx - h_width1 / 2, hy - h_height1 / 2))
                    screen.blit(hero1_down4, (hx - h_width1 / 2, hy - h_height1 / 2))
                    b_ex1[i][a] = -200
                    b_ey1[i][a] = -200
                    live -= 1
        for i in range(3):
            for a in range(len(b_ex0[0])):
                e0_bullet.append(screen.blit(bullet2, (b_ex0[i][a], b_ey0[i][a])))
                b_ey0[i][a] += speed_eb
                if b_ey0[i][a] > 800:
                    del e0_bullet[a]
                if b_ex0[i][a] + b_width2 > hx - h_width1 / 2 and \
                        b_ex0[i][a] < hx - h_width1 / 2 + h_width1 and \
                        b_ey0[i][a] < hy - h_height1 / 2 + h_height1 and \
                        b_ey0[i][a] + b_height2 > hy - h_height1 / 2 and \
                        live > 0:
                    screen.blit(hero1_down1, (hx - h_width1 / 2, hy - h_height1 / 2))
                    screen.blit(hero1_down2, (hx - h_width1 / 2, hy - h_height1 / 2))
                    screen.blit(hero1_down3, (hx - h_width1 / 2, hy - h_height1 / 2))
                    screen.blit(hero1_down4, (hx - h_width1 / 2, hy - h_height1 / 2))
                    b_ex0[i][a] = -200
                    b_ey0[i][a] = -200
                    live -= 1

    pygame.display.update()
