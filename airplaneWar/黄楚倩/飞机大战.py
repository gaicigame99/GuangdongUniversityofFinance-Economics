import pygame
import random
import time

pygame.init()

font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 40)

screen = pygame.display.set_mode((495, 800))

bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))
backmusic = pygame.mixer.Sound("sound\game_music.ogg")
backmusic.play()

bullet = pygame.image.load(r"images\bullet-2.gif")
bullet_rect = bullet.get_rect()
bullet_w = bullet_rect.width
bullet_h = bullet_rect.height
by = []
bx = []
flag = 15            # 每颗子弹出现的间隔

# 英雄飞机的东西
hero = pygame.image.load("images\hero.gif")
hero_blood = 200  # 英雄的血
hero_die = 0      # 记录英雄死亡时间
herdie_f = 0      # 该标志控制显示英雄死后的画面
h_rect = hero.get_rect()
h_width = h_rect.width           # 英雄的宽
h_height = h_rect.height         # 英雄的高
hx = 100           # 英雄坐标
hy = 100
# 英雄爆炸的画面
h_blowup1 = pygame.image.load("images\hero_blowup_n1.png")
h_blowup2 = pygame.image.load("images\hero_blowup_n2.png")
h_blowup3 = pygame.image.load("images\hero_blowup_n3.png")
h_blowup4 = pygame.image.load("images\hero_blowup_n4.png")

kill, level, miss = 0, 0, 0
flag3 = 0    # 控制游戏暂停，继续
enemydown = []
downx = []
downy = []
downtime = []
enemy = []
ex = []
ey = []
plane_level = []
e_blood = []
eb = []
count = 5   # 控制屏幕上飞机个数
for i in range(count):
    enemy.append(pygame.image.load("images\enemy0.png"))
    ex.append(random.randint(0, 495 - 50))
    ey.append(random.randint(-300, -100))
    e_blood.append(50)
    eb.append(50)

e_rect = []
e_width = []                 # 存 敌机的宽
e_height = []                # 存 敌机的高
for i in range(count):       # 获取敌机宽高，因为敌机机型会改变所以放在数组里面
    e_rect.append(enemy[i].get_rect())
    e_width.append(e_rect[i].width)
    e_height.append(e_rect[i].height)

# 敌机爆炸画面
enemy0down1 = pygame.image.load("images\enemy0_down1.png")
enemy0down2 = pygame.image.load("images\enemy0_down2.png")
enemy0down3 = pygame.image.load("images\enemy0_down3.png")
enemy0down4 = pygame.image.load("images\enemy0_down4.png")

enemy1down1 = pygame.image.load("images\enemy1_down1.png")
enemy1down2 = pygame.image.load("images\enemy1_down2.png")
enemy1down3 = pygame.image.load("images\enemy1_down3.png")
enemy1down4 = pygame.image.load("images\enemy1_down4.png")

enemy2down1 = pygame.image.load("images\enemy2_down1.png")
enemy2down2 = pygame.image.load("images\enemy2_down2.png")
enemy2down3 = pygame.image.load("images\enemy2_down3.png")
enemy2down4 = pygame.image.load("images\enemy2_down4.png")
enemy2down5 = pygame.image.load("images\enemy2_down5.png")
enemy2down6 = pygame.image.load("images\enemy2_down6.png")


enemydown.append(enemy0down1)
enemydown.append(enemy0down2)
enemydown.append(enemy0down3)
enemydown.append(enemy0down4)

enemydown.append(enemy1down1)
enemydown.append(enemy1down2)
enemydown.append(enemy1down3)
enemydown.append(enemy1down4)

enemydown.append(enemy2down1)
enemydown.append(enemy2down2)
enemydown.append(enemy2down3)
enemydown.append(enemy2down4)
enemydown.append(enemy2down5)
enemydown.append(enemy2down6)

# 暂停按钮东西
stop = pygame.image.load("images\game_pause_pressed.png")
cont = pygame.image.load("images\game_resume_pressed.png")
stop_rect = stop.get_rect()
con_rect = cont.get_rect()
continue_button = pygame.image.load(r"images\resume_nor.png")
restart_button = pygame.image.load(r"images\restart_nor.png")
quit_button = pygame.image.load(r"images\quit_nor.png")
cb_rect = continue_button.get_rect()
rb_rect = restart_button.get_rect()
qb_rect = quit_button.get_rect()
qb_x, qb_y = 200, 450

stop_flag = False

m_l, m_m, m_r = 0, 0, 0

# 开始界面东西
name = pygame.image.load(r"images\name.png")
star = pygame.image.load(r"images\stargame.png")
load1 = pygame.image.load(r"images\game_loading1.png")
load2 = pygame.image.load(r"images\game_loading2.png")
load3 = pygame.image.load(r"images\game_loading3.png")
star_rect = star.get_rect()
star_w = star_rect.width
star_h = star_rect.height
loading_holdtime = 150
load_flag , starflag= 0, 0
startime, loadtime, star_button_f = 0, 0, 0

# 不同等级机型不同
level1_f = 0
level2_f = 0
lu_holdtime = 0   # 控制升级提醒停留时间
old_level = 0  # 记录上一个等级

# 道具
propert = pygame.image.load(r"images\game_loading3.png")

while True:
    for event in pygame.event.get():    # 序列
        if event.type == pygame.QUIT:   # 如果当前事件是退出事件
            exit()                      # 退出
        # 暂停游戏按键
        if event.type == pygame.MOUSEBUTTONUP and m_l == 1:
            m_l = 0
            if 495 - stop_rect.width <= hx < 495 and 800 - stop_rect.height < hy <= 800:
                if flag3 == 0:
                    screen.blit(cont, (495 - stop_rect.width, 800 - stop_rect.height))
                    stop_flag = False
                    screen.blit(bg, (0, 0))
                    screen.blit(continue_button, (220, 250))
                    screen.blit(restart_button, (200, 350))
                    screen.blit(quit_button, (200, 450))
                    m_l, m_m, m_r = 0, 0, 0
                    flag3 = 1
            # 暂停后，继续 按钮
            if 220 <= hx < 220 + cb_rect.width and 250 < hy <= 250 + cb_rect.height:
                if flag3 == 1:
                    stop_flag = True
                    m_l, m_m, m_r = 0, 0, 0
                    flag3 = 0

            # 暂停后，重新开始 按钮
            if 200 <= hx < 220 + rb_rect.width and 350 < hy <= 350 + rb_rect.height:
                if flag3 == 1:
                    stop_flag = True
                    m_l, m_m, m_r = 0, 0, 0
                    flag3 = 0
                    miss, level, kill = 0, 0, 0
                    for i in range(count):
                        ey[i] = random.randint(-300, -100)
                        ex[i] = random.randint(0, 495 - 50)
                        enemy[i] = pygame.image.load("images\enemy0.png")
                        e_rect.append(enemy[i].get_rect())
                        e_width.append(e_rect[i].width)
                        e_height.append(e_rect[i].height)
                        eb[i] = 50
                        e_blood[i] = 50
                        plane_level.clear()
                        downtime.clear()
                        downx.clear()
                        downy.clear()
                        level2_f = 0
                        level1_f = 0
                    print(eb)
            # 暂停后，退出游戏 按钮
            if qb_x <= hx < qb_x + qb_rect.width and qb_y < hy <= qb_y + qb_rect.height:
                exit()

            # 开始界面，开始游戏按钮
            if 150 <= hx < 150 + star_w and 400 < hy <= 400 + star_h and star_button_f == 0:
                startime = time.time()
                stop_flag = True
                m_l, m_m, m_r = 0, 0, 0
                star_button_f = 1
            if 200 <= hx < 200 + qb_rect.width and 600 < hy <= 600 + qb_rect.height and star_button_f == 0:
                exit()

    m_l, m_m, m_r = pygame.mouse.get_pressed()

    hx, hy = pygame.mouse.get_pos()

    # 开始界面
    if stop_flag == False and starflag == 0:
        screen.blit(bg, (0, 0))  # 显示背景
        screen.blit(name, (35, 125))
        screen.blit(star, (150, 400))
        screen.blit(quit_button, (200, 600))
        starflag = 1
    # 加载画面
    if loading_holdtime > 0 and stop_flag == True:
        loadtime = time.time() - startime
        screen.blit(bg, (0, 0))
        if 0 < loadtime < 0.3:
            screen.blit(load1, (150, 350))
        if 0.3 < loadtime < 0.6:
            screen.blit(load2, (150, 350))
        if 0.6 < loadtime < 0.9:
            screen.blit(load3, (150, 350))
        loading_holdtime -= 1
    elif loading_holdtime <= 0:
        load_flag = 1

    # 优化子弹列表，range（）括号里的不会实时改变
    for i in by:
        index = by.index(i)
        if i < 0:
            by.pop(index)
            bx.pop(index)

    # 会动的所有
    if stop_flag == True and load_flag == 1:
        screen.blit(bg, (0, 0))  # 显示背景
        if hero_blood > 0:
            screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))  # 显示英雄飞
            pygame.draw.line(screen, (100, 149, 237), (hx - h_width / 2, hy + h_height / 2), (hx + h_width/2, hy + h_height / 2), 3)
            pygame.draw.line(screen, (255, 0, 0), ((hx - h_width / 2), hy + h_height / 2), ((hx - h_width / 2) + h_width / 200 * hero_blood, hy + h_height / 2), 3)
        screen.blit(stop, (495 - stop_rect.width, 800 - stop_rect.height))  # 显示暂停按钮
        # 存子弹位置
        if flag > 0:
            flag -= 1
        else:
            bx.append(hx - bullet_w / 2 + 2)
            by.append(hy - h_height / 2 - bullet_h)
            flag = 10
        # 显示子弹，并让子弹动起来
        if hero_blood > 0:
            for i in range(len(bx)):
                screen.blit(bullet, (bx[i], by[i]))
                by[i] -= 7
        # 敌机显示
        for i in range(count):
            screen.blit(enemy[i], (ex[i], ey[i]))
            pygame.draw.line(screen, (100, 149, 237), (ex[i], ey[i]-2), (ex[i]+e_width[i], ey[i]-2), 3)
            pygame.draw.line(screen, (255, 0, 0), (ex[i], ey[i] - 2), (ex[i] + e_width[i]/eb[i]*e_blood[i], ey[i] - 2), 3)
            ey[i] += 1
            if ey[i] > 800:
                miss += 1
                hero_blood -= 10
                ey[i] = random.randint(-500, -300)
                ex[i] = random.randint(0, 495 - 50)
                if hero_blood <= 0:
                    hero_die = time.time()

        # 控制英雄爆炸
        if hero_die != 0:
            hero_boom = time.time() - hero_die
            if 0 < hero_boom < 0.1:
                screen.blit(h_blowup1, (hx - h_width / 2, hy - h_height / 2))
            if 0.1 < hero_boom < 0.2:
                screen.blit(h_blowup2, (hx - h_width / 2, hy - h_height / 2))
            if 0.3 < hero_boom < 0.4:
                screen.blit(h_blowup3, (hx - h_width / 2, hy - h_height / 2))
            if 0.5 < hero_boom < 0.6:
                screen.blit(h_blowup4, (hx - h_width / 2, hy - h_height / 2))
                herdie_f = 1
        if herdie_f == 1:
            op_text = font.render("you lose!", True, (0, 0, 0))
            screen.blit(bg, (0, 0))
            screen.blit(op_text, (170, 250))
            screen.blit(restart_button, (200, 350))
            screen.blit(quit_button, (200, 450))
            stop_flag = False

        # 检测子弹碰撞敌机
        for i in range(count):
            for j in range(len(bx)):
                if ex[i] <= bx[j] <= ex[i] + e_width[i]:
                    if by[j] <= ey[i] + e_height[i] and by[j] + bullet_h > ey[i] + e_height[i]:
                        by[j], bx[j] = -20, -20
                        e_blood[i] -= 10
                        if e_blood[i] <= 0:
                            downx.append(ex[i])
                            downy.append(ey[i])
                            downtime.append(time.time())
                            ex[i] = random.randint(0, 495 - 50)
                            ey[i] = random.randint(-300, -100)
                            e_blood[i] = eb[i]
                            kill += 1
                            if e_width[i] == 51:
                                plane_level.append(0)
                            elif e_width[i] == 69:
                                plane_level.append(1)
                            else:
                                plane_level.append(2)
        # 控制敌机爆炸形态
        if len(downtime):
            for i in range(len(downtime)):
                a = time.time() - downtime[i]
                if 0 < a < 0.1:
                    screen.blit(enemydown[0 + plane_level[i]*4], (downx[i], downy[i]))
                if 0.1 < a < 0.2:
                    screen.blit(enemydown[1 + plane_level[i]*4], (downx[i], downy[i]))
                if 0.2 < a < 0.3:
                    screen.blit(enemydown[2 + plane_level[i]*4], (downx[i], downy[i]))
                if 0.3 < a < 0.4:
                    screen.blit(enemydown[3 + plane_level[i]*4], (downx[i], downy[i]))
                if plane_level[i] == 2:
                    if 0.4 < a < 0.5:
                        screen.blit(enemydown[12], (downx[i], downy[i]))
                    if 0.5 < a < 0.6:
                        screen.blit(enemydown[13], (downx[i], downy[i]))

        str_kill = "kill:" + str(kill)
        op_kill = font.render(str_kill, True, (0, 0, 0))
        screen.blit(op_kill, (20, 50))

        str_level = "level:" + str(level)
        op_level = font.render(str_level, True, (0, 0, 0))
        screen.blit(op_level, (20, 80))

        str_miss = "miss:" + str(miss)
        op_miss = font.render(str_miss, True, (0, 0, 0))
        screen.blit(op_miss, (20, 110))

    # 计算等级
    old_level = level
    level = kill // 10

    if lu_holdtime > 0:
        op_text = font.render("level up!", True, (0, 0, 0))
        screen.blit(op_text, (200, 350))
        lu_holdtime -= 1

    if level > old_level:
        lu_holdtime = 100

    # 等级增加，改变机型
    # 等级2之后出现中型机
    if level >= 2 and level1_f < 4:
        for i in range(count):
            if ey[i] < -50:
                enemy[i] = pygame.image.load("images\enemy1.png")
                e_blood[i] = 100
                e_rect[i] = enemy[i].get_rect()
                e_width[i] = e_rect[i].width
                e_height[i] = e_rect[i].height
                eb[i] = 100
                level1_f += 1
    #等级4之后出现大型机
    if level >= 4 and level2_f < 2:
        for i in range(count):
            if ey[i] < -100:
                enemy[i] = pygame.image.load("images\enemy2.png")
                e_blood[i] = 150
                e_rect[i] = enemy[i].get_rect()
                e_width[i] = e_rect[i].width
                e_height[i] = e_rect[i].height
                eb[i] = 150
                level2_f += 2

    pygame.display.update()

