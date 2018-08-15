import pygame
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((465, 700))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (465, 700))

# 音乐
back_music = pygame.mixer.Sound("sound\game_music.ogg")
bullet_music = pygame.mixer.Sound(r"sound\bullet.wav")
enemy_down_music = pygame.mixer.Sound("sound\enemy1_down.wav")
back_music.play(True)

# 敌机，英雄机和子弹图片
enemy0 = pygame.image.load(r"images\enemy0.png")
hero = pygame.image.load("images\hero.gif")
bullet = pygame.image.load(r"images\bullet.png")

# 开始背景
start_background = pygame.image.load("images\start_background.png")
start_background = pygame.transform.scale(start_background, (465, 700))
start_bg_x = 0
start_bg_y = 0
stat_list = [[start_bg_x, start_bg_y]]

# 按钮
blue_btn = pygame.image.load(r"images\blue_btn.png")
blue_btn = pygame.transform.scale(blue_btn, (220, 60))
green_btn = pygame.image.load("images\green_btn.png")
green_btn = pygame.transform.scale(green_btn, (220, 60))
start_btn_x = 120
start_btn_y = 500
stat_list.append([start_btn_x, start_btn_y])

# “游戏开始”文本
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
start_text = font.render("开始游戏", True, (0, 0, 0))
start_tx = 170
start_ty = 515
stat_list.append([start_tx, start_ty])

# 首页移动的速度
speed_x = 0
speed_y = 0

# 敌机enemy0爆炸
enemy0_down1 = pygame.image.load("images\enemy0_down1.png")
enemy0_down2 = pygame.image.load("images\enemy0_down2.png")
enemy0_down3 = pygame.image.load("images\enemy0_down3.png")
enemy0_down4 = pygame.image.load("images\enemy0_down4.png")

# 英雄战机长宽
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height

# 英雄子弹位置
bx = []
by = []

# 英雄子弹发射速率
hero_bullet_v = 30
my_time = hero_bullet_v

# 敌人位置
ex = []
ey = []
x_v = []  # 敌人左右移动的速度

# 敌人出现频率
enemy_v = 40
e_time = enemy_v

# 爆炸位置
bomb_x = []
bomb_y = []
bomb_y_temp = []

# 分数
score = 0

# 1为游戏未开始，0开始游戏
stat_flag = 1


def enemy0_down(x, y, y_temp):
    for i in range(len(x)):
        y[i] += 1
        if y[i] < y_temp[i] + 10:
            screen.blit(enemy0_down1, (x[i], y[i]))
        elif y_temp[i] + 10 <= y[i] < y_temp[i] + 20:
            screen.blit(enemy0_down2, (x[i], y[i]))
        elif y_temp[i] + 20 <= y[i] < y_temp[i] + 30:
            screen.blit(enemy0_down3, (x[i], y[i]))
        elif y_temp[i] + 30 <= y[i] < y_temp[i] + 40:
            screen.blit(enemy0_down4, (x[i], y[i]))


def enemy0_plane(x, y, xv):
    num = len(x)
    i = 0
    while i < num:
        # 移除不在屏幕中的敌人
        if x[i] == -100 or y[i] > 700:
            x.pop(i)
            y.pop(i)
            xv.pop(i)
            num -= 1
        screen.blit(enemy0, (x[i], y[i]))
        # 敌人战机左右移动
        if x[i] + 45 > 465:
            x[i] -= xv[i]
            xv[i] = -xv[i]
        elif x[i] < 0:
            x[i] -= xv[i]
            xv[i] = -xv[i]
        else:
            x[i] += xv[i]
        y[i] += 1
        i += 1


def remove_bullet(x, y):
    mum = len(x)
    i = 0
    while i < mum:
        if x[i] == 800:
            x.pop(i)
            y.pop(i)
            mum -= 1
        i += 1


def bullet_move(b_x, b_y, e_x, e_y, bombx, bomby, bomby_temp, s):
    for i in range(len(b_x)):
        if b_y[i] < 0:
            b_x[i] = 800
        for j in range(len(e_x)):
            if e_x[j] - 10 < b_x[i] < e_x[j] + 45 and e_y[j] < b_y[i] < e_y[j] + 35:
                enemy_down_music.play()
                # 获取敌机爆炸时的位置
                bombx.append(e_x[j])
                bomby.append(e_y[j])
                bomby_temp.append(e_y[j])
                # 把爆炸的敌机移除屏幕
                e_x[j] = -100
                bx[i] = 800
                s += 1
        screen.blit(bullet, (b_x[i], b_y[i]))
        b_y[i] -= 3
        bullet_music.play(True)
    return s


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # 游戏未开始
    if stat_flag:
        screen.blit(bg, (0, 0))
        screen.blit(start_background, (stat_list[0][0], stat_list[0][1]))
        a, b, c = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #
        if start_btn_x < mouse_x < start_btn_x + 247 and start_btn_y < mouse_y < start_btn_y + 80 and a:
            screen.blit(blue_btn, (stat_list[1][0], stat_list[1][1]))
            speed_y = -10
        else:
            screen.blit(green_btn, (stat_list[1][0], stat_list[1][1]))

        # 开始按钮文字
        screen.blit(start_text, (stat_list[2][0], stat_list[2][1]))

        for i in range(3):
            stat_list[i][0] += speed_x
            stat_list[i][1] += speed_y
            if stat_list[i][1]+700 < -800:
                stat_flag = 0

    # 游戏开始
    if stat_flag == 0:
        screen.blit(bg, (0, 0))
        hx, hy = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        h_x = hx-h_width/2
        h_y = hy-h_height/2
        if h_y < 0:
            h_y = 0
        screen.blit(hero, (h_x, h_y))

        # 每隔一个my_time时间英雄战机装一次弹
        if my_time:
            my_time -= 1
        else:
            bx.append(hx-42)
            by.append(hy-15)
            bx.append(hx+22)
            by.append(hy-15)
            # time重置
            my_time = hero_bullet_v

        # 每隔一个e_time，敌人随机出现
        if e_time:
            e_time -= 1
        else:
            ex.append(random.randint(0, 400))
            ey.append((random.randint(-250, -100)))
            e_time = enemy_v
            # 敌机左右移动的速度
            a = 1
            b = -1
            x_v.append(a)
            x_v.append(b)

        # 子弹移动，并打中敌人获得分数
        score = bullet_move(bx, by, ex, ey, bomb_x, bomb_y, bomb_y_temp, score)

        # 移除子弹
        remove_bullet(ex, ey)

        # 敌人战机
        enemy0_plane(ex, ey, x_v)

        # 敌人战机爆炸
        enemy0_down(bomb_x, bomb_y, bomb_y_temp)

        # 得分score
        score_text = font.render("分数："+str(score), True, (0, 0, 0))
        screen.blit(score_text, (0, 0))

    pygame.display.update()
