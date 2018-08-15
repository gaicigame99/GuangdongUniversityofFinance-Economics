import pygame
import random
import time
#控制我方坦克不进入砖块
def fanfa1(block_x,block_y,tan1x,tan1y,direction):
    if (block_x < tan1x < block_x + 60 or block_x < tan1x + 55 < block_x + 60 or block_x < tan1x +27.5 < block_x+60) and \
            block_y < tan1y < block_y + 60 and direction == 0:
        tan1y += 3
    if (block_y < tan1y < block_y + 60 or block_y < tan1y + 55 < block_y +60 or block_y < tan1y+27.5 < block_y+60)\
            and block_x < tan1x < block_x + 60 and direction == 3:
        tan1x += 3
    if (block_x < tan1x < block_x + 60 or block_x < tan1x + 55< block_x + 60 or  block_x < tan1x+27.5< block_x+60) \
            and block_y < tan1y + 55 < block_y + 60 and direction == 1:
        tan1y -= 3
    if (block_y < tan1y < block_y + 60 or block_y < tan1y + 55 < block_y + 60 or block_y < tan1y+ 27.5 < block_y + 60) and \
            block_x < tan1x + 55 < block_x + 60 and direction == 2:
        tan1x -= 3
    return tan1x,tan1y
#控制敌方坦克不进入砖块
def fanfa2(block_x,block_y,tan2x,tan2y,direction):
    if (block_x < tan2x < block_x + 60 or block_x < tan2x + 55 < block_x + 60 or block_x < tan2x +27.5 < block_x+60) and \
            block_y < tan2y < block_y + 60 and direction == 0:
        tan2y += 3
    if (block_y < tan2y < block_y + 60 or block_y < tan2y + 55< block_y +60 or block_y < tan2y+27.5< block_y+60)\
            and block_x < tan2x < block_x + 60 and direction == 3:
        tan2x += 3
    if (block_x < tan2x < block_x + 60 or block_x < tan2x + 55 < block_x + 60 or  block_x < tan2x+27.5 < block_x+60) \
            and block_y < tan2y + 55 < block_y + 60 and direction == 1:
        tan2y -= 3
    if (block_y < tan2y < block_y + 60 or block_y < tan2y + 55 < block_y + 60 or block_y < tan2y+ 27.5 < block_y + 60) and \
            block_x < tan2x + 55 < block_x + 60 and direction == 2:
        tan2x -= 3
    return tan2x,tan2y
#坦克大战
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((780, 780))
pygame.mixer.music.load(r"images\backgroundmusic.mp3")
pygame.mixer.music.play(1)
background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (780, 780))
start_interface = pygame.image.load(r"images\start_interface.png")
start_interface = pygame.transform.scale(start_interface, (780, 780))
stx = 0
sty = 0
#开始键
start_button = pygame.image.load(r"images\start_button.png")
start_button = pygame.transform.scale(start_button, (200, 100))
sx = 300
sy = 390
s_rect = start_button.get_rect()
s_width= s_rect.width
s_height = s_rect.height
#我方坦克
heroeast = pygame.image.load("images\hero_east.png")
herowest = pygame.image.load("images\hero_west.png")
heronorth = pygame.image.load("images\hero_north.png")
herosouth = pygame.image.load("images\hero_south.png")
heroeast = pygame.transform.scale(heroeast, (55, 55))
herowest = pygame.transform.scale(herowest, (55, 55))
heronorth = pygame.transform.scale(heronorth, (55, 55))
herosouth = pygame.transform.scale(herosouth, (55, 55))
hero_rect = heronorth.get_rect()
hero = [heronorth, herosouth,heroeast, herowest ]
h = 0
tan1x = 240
tan1y = 720
#敌方坦克
enemyeast = pygame.image.load("images\enemy2_east.png")
enemywest = pygame.image.load("images\enemy2_west.png")
enemynorth = pygame.image.load("images\enemy2_north.png")
enemysouth = pygame.image.load("images\enemy2_south.png")
enemyeast = pygame.transform.scale(enemyeast, (55, 55))
enemywest = pygame.transform.scale(enemywest, (55, 55))
enemynorth= pygame.transform.scale(enemynorth, (55, 55))
enemysouth = pygame.transform.scale(enemysouth, (55, 55))
enemy_rect = enemynorth.get_rect()
enemy = [enemynorth, enemysouth,enemyeast, enemywest ]
e = 1
tan2x = 240
tan2y = 0
#坦克速度
tan1speed = 3 #我方速度
tan2speed = 3 #敌方速度
# 字体
font = pygame.font.Font("C:\Windows\Fonts\STENCIL.TTF", 80)
font1 = pygame.font.Font("C:\Windows\Fonts\STXINWEI.TTF", 20)
# 子弹
bullet_n = pygame.image.load("images/bullet_up.png")
bullet_s = pygame.image.load("images/bullet_down.png")
bullet_e = pygame.image.load("images/bullet_right.png")
bullet_w = pygame.image.load("images/bullet_left.png")
bullet_n = pygame.transform.scale(bullet_n, (12, 12))
bullet_s = pygame.transform.scale(bullet_s, (12, 12))
bullet_e = pygame.transform.scale(bullet_e, (12, 12))
bullet_w = pygame.transform.scale(bullet_w, (12, 12))
bullet = [bullet_n, bullet_s, bullet_e, bullet_w]
bullet1 = [bullet_n, bullet_s, bullet_e, bullet_w]
bullet_rect = bullet_n.get_rect()
b1 = 0
bullet_x = -100
bullet_y = -100
b2 = 1
bullet1_x = -100
bullet1_y = -100
#子弹速度
bspeed = 6
# 生命
live = pygame.image.load(r"images\live.png")
live = pygame.transform.scale(live, (20, 20))
#水晶
home = pygame.image.load("images\home.png")
home = pygame.transform.scale(home, (60, 60))
home1 = pygame.image.load("images\home1.png")
home1 = pygame.transform.scale(home1, (60, 60))
homex = 360
homey = 720
home1x = 360
home1y = 0
h_shuijing = 1
e_shuijing = 1
#砖
brick = pygame.image.load(r"images\brick.png")
brick = pygame.transform.scale(brick, (60, 60))
brick1 = pygame.image.load(r"images\iron.png")
brick1 = pygame.transform.scale(brick1, (60, 60))
bx1 = 300
by1 = 0
bx2 = 420
by2 = 0
bx3 = 300
by3 = 60
bx4 = 360
by4 = 60
bx5 = 420
by5 = 60
bx6 = 300
by6 = 660
bx7 = 360
by7 = 660
bx8 = 420
by8 = 660
bx9 = 300
by9 = 720
bx10 = 420
by10 = 720
#爆炸
broke1 = pygame.image.load(r"images\broke.jpg")
broke1 = pygame.transform.scale(broke1, (30, 30))
broke2 = pygame.image.load(r"images\broke2.jpg")
broke2 = pygame.transform.scale(broke2, (60, 60))
#时间初始化
e_time = -100
e_time1 = -100
e_time2 = -100 #南
e_time3 = -100 #北
e_time4 = -100 #西
e_time5 = -100 #东
e_time6 = -100 #南
e_time7 = -100 #北
e_time8 = -100 #西
e_time9 = -100 #东
#判断
flag = 0
flag_1 = 1
flag_2 = 1
flag_3 = 1
flag_4 = 1
flag_5 = 1
flag_6 = 1
flag_7 = 1
flag_8 = 1
flag_9 = 1
flag_10 = 1
hero_num = 3#我方生命
enemy_num = 3#敌方生命
pressed_keys = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()
    #我方坦克移动
    if pressed_keys[pygame.K_UP]:  # 上
        h = 0
        tan1y -= tan1speed
    if pressed_keys[pygame.K_DOWN]:  # 下
        h = 1
        tan1y += tan1speed
    if pressed_keys[pygame.K_RIGHT]:  # 右
        h = 2
        tan1x += tan1speed
    if pressed_keys[pygame.K_LEFT]:  # 左
        h = 3
        tan1x -= tan1speed
    # 敌方坦克移动
    if pressed_keys[pygame.K_w]:   # 上W
        e = 0
        tan2y -= tan2speed
    if pressed_keys[pygame.K_s]:   # 下S
        e = 1
        tan2y += tan2speed
    if pressed_keys[pygame.K_d]:   # 右D
        e = 2
        tan2x += tan2speed
    if pressed_keys[pygame.K_a]:    # 左A
        e = 3
        tan2x -= tan2speed
    # 我方子弹发射
    if bullet_y < -12 or bullet_y > 780 or bullet_x < -12 or bullet_x > 780:
        if pressed_keys[pygame.K_KP0]:  # 发射键0键
            if h == 0:
                b1 = 0
                bullet_x = tan1x + hero_rect.width / 2 - bullet_rect.width / 2
                bullet_y = tan1y - bullet_rect.height
                screen.blit(bullet[b1], (bullet_x, bullet_y))
            if h == 1:
                b1 = 1
                bullet_x = tan1x + hero_rect.width / 2 - bullet_rect.width / 2
                bullet_y = tan1y + hero_rect.height
                screen.blit(bullet[b1], (bullet_x, bullet_y))
            if h == 2:
                b1 = 2
                bullet_x = tan1x + hero_rect.width
                bullet_y = tan1y + hero_rect.height / 2 - bullet_rect.height / 2
                screen.blit(bullet[b1], (bullet_x, bullet_y))
            if h == 3:
                b1 = 3
                bullet_x = tan1x - bullet_rect.width
                bullet_y = tan1y + hero_rect.height / 2 - bullet_rect.height / 2
                screen.blit(bullet[b1], (bullet_x, bullet_y))
    # 敌方子弹发射
    if bullet1_y < -12 or bullet1_y > 780 or bullet1_x < -12 or bullet1_x > 780:
        if pressed_keys[pygame.K_j]:  # 发射键j键
            if e == 0:
                b2 = 0
                bullet1_x = tan2x + enemy_rect.width / 2 - bullet_rect.width / 2
                bullet1_y = tan2y - bullet_rect.height
                screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
            if e == 1:
                b2 = 1
                bullet1_x = tan2x + enemy_rect.width / 2 - bullet_rect.width / 2
                bullet1_y = tan2y + enemy_rect.height
                screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
            if e == 2:
                b2 = 2
                bullet1_x = tan2x + enemy_rect.width
                bullet1_y = tan2y + enemy_rect.height / 2 - bullet_rect.height / 2
                screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
            if e == 3:
                b2 = 3
                bullet1_x = tan2x - bullet_rect.width
                bullet1_y = tan2y + enemy_rect.height / 2 - bullet_rect.height / 2
                screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
    # start键
    hx, hy = pygame.mouse.get_pos()
    a, c, d = pygame.mouse.get_pressed()
    screen.blit(start_interface, (stx, sty))
    screen.blit(start_button, (sx, sy))
    if hx <= sx + s_width and hx >= sx and hy >= sy and hy <= sy + s_height and a:
        sx = -1000
        sy = -1000
        stx = -1000
        sty = -1000
        flag = 1
    if flag == 1:
        screen.blit(background, (0, 0))
        #地图设计
        for c in range(2):
            for a in range(2):
                for b in range(3):
                    screen.blit(brick1, (60+120*a+480*c, 60+60*b))
                    screen.blit(brick1, (60+120*a+480*c, 540+60*b))
                    tan1x, tan1y = fanfa1(60+120*a+480*c, 60+60*b, tan1x, tan1y, h)
                    tan2x, tan2y = fanfa2(60+120*a+480*c, 60+60*b, tan2x, tan2y, e)
                    tan1x, tan1y = fanfa1(60+120*a+480*c, 540+60*b, tan1x, tan1y, h)
                    tan2x, tan2y = fanfa2(60+120*a+480*c, 540+60*b, tan2x, tan2y, e)
        for i in range(7):
            screen.blit(brick1,(180+60*i,360))
            tan1x, tan1y = fanfa1(180+60*i,360, tan1x, tan1y, h)
            tan2x, tan2y = fanfa2(180+60*i,360, tan2x, tan2y, e)
        for i in range(2):
            screen.blit(brick1,(0+720*i,360))
            tan1x, tan1y = fanfa1(0+720*i,360, tan1x, tan1y, h)
            tan2x, tan2y = fanfa2(0+720*i,360, tan2x, tan2y, e)
        for a in range(2):
            for b in range(3):
                screen.blit(brick1,(300+60*b,180+60*a))
                tan1x, tan1y = fanfa1(300+60*b,180+60*a, tan1x, tan1y, h)
                tan2x, tan2y = fanfa2(300+60*b,180+60*a, tan2x, tan2y, e)
        for a in range(2):
            for b in range(3):
                screen.blit(brick1, (300 + 60 * b, 480 + 60 * a))
                tan1x, tan1y = fanfa1(300 + 60 * b, 480 + 60 * a, tan1x, tan1y, h)
                tan2x, tan2y = fanfa2(300 + 60 * b, 480 + 60 * a, tan2x, tan2y, e)
        screen.blit(brick, (bx1, by1))
        screen.blit(brick, (bx2, by2))
        screen.blit(brick, (bx3, by3))
        screen.blit(brick, (bx4, by4))
        screen.blit(brick, (bx5, by5))
        screen.blit(brick, (bx6, by6))
        screen.blit(brick, (bx7, by7))
        screen.blit(brick, (bx8, by8))
        screen.blit(brick, (bx9, by9))
        screen.blit(brick, (bx10, by10))
        tan1x, tan1y = fanfa1(bx1, by1, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx1, by1, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx2, by2, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx2, by2, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx3, by3, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx3, by3, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx4, by4, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx4, by4, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx5, by5, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx5, by5, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx6, by6, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx6, by6, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx7, by7, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx7, by7, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx8, by8, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx8, by8, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx9, by9, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx9, by9, tan2x, tan2y, e)
        tan1x, tan1y = fanfa1(bx10, by10, tan1x, tan1y, h)
        tan2x, tan2y = fanfa2(bx10, by10, tan2x, tan2y, e)
        #   我方生命为0时
        if hero_num == 0:
            text_1 = font.render("RED WIN", True, (255, 0, 0))
            screen.blit(text_1, (220, 350))
            tan1x = -200
            tan1y = -200
        #   敌方生命为0时
        if enemy_num == 0:
            text_2 = font.render("BLUE WIN", True, (0, 0, 255))
            screen.blit(text_2, (220, 350))
            tan2x = -200
            tan2y = -200
        #   我方水晶被打爆
        if h_shuijing == 0:
            text_2 = font.render("RED WIN", True, (255, 0, 0))
            screen.blit(text_2, (220, 350))
            tan1x = -200
            tan1y = -200
        #   敌方水晶被打爆
        if e_shuijing == 0:
            text_2 = font.render("BLUE WIN", True, (0, 0, 255))
            screen.blit(text_2, (220, 350))
            tan2x = -200
            tan2y = -200
        #坦克不能超界限
        #我方坦克
        if (tan1x <0 and h == 3) :
            tan1x += tan1speed
        if (tan1x+ hero_rect.width >780 and h == 2) :
            tan1x -= tan1speed
        if (tan1y+ hero_rect.height >780 and h == 1) :
            tan1y -= tan1speed
        if (tan1y <0 and h == 0) :
            tan1y += tan1speed
        #敌方坦克
        if (tan2x <0 and e == 3) :
            tan2x += tan2speed
        if (tan2x+ hero_rect.width >780 and e == 2) :
            tan2x -= tan2speed
        if (tan2y+ hero_rect.height >780 and e == 1) :
            tan2y -= tan2speed
        if (tan2y <0 and e == 0) :
            tan2y += tan2speed
        #水晶位置
        screen.blit(home1, (home1x, home1y))
        screen.blit(home, (homex, homey))
        #坦克设计
        screen.blit(enemy[e], (tan2x, tan2y))
        screen.blit(hero[h], (tan1x, tan1y))
        # 我方子弹移动
        if b1 == 0:  #子弹碰南面
            bullet_y -= bspeed
            if bullet_y <= tan2y+hero_rect.height and bullet_y > tan2y and bullet_x > tan2x and bullet_x <tan2x+ hero_rect.width and enemy_num >0:
                bullet_x = -200
                bullet_y = -200
                enemy_num -=1
                e_time = time.time()
            if bullet_y <= 120 and bullet_y >=0 and bullet_x >= 300 and bullet_x + bullet_rect.width <=480:
                e_time2 = time.time()
            screen.blit(bullet[b1], (bullet_x, bullet_y))
        if b1 == 1:   #子弹碰北面
            bullet_y += bspeed
            if bullet_y >= tan2y and bullet_y < tan2y+hero_rect.height and bullet_x > tan2x and bullet_x <tan2x+ hero_rect.width and enemy_num >0:
                bullet_x = -200
                bullet_y = -200
                enemy_num -= 1
                e_time = time.time()
            if bullet_y + bullet_rect.height<=120  and bullet_y+ bullet_rect.height>=0 and bullet_x >= 300 and bullet_x + bullet_rect.width <=480:
                e_time3 = time.time()
            screen.blit(bullet[b1], (bullet_x, bullet_y))
        if b1 == 2:   #子弹碰西面
            bullet_x += bspeed
            if bullet_y > tan2y  and bullet_y < tan2y+hero_rect.height and bullet_x >= tan2x and bullet_x < tan2x + hero_rect.width and enemy_num >0:
                bullet_x = -200
                bullet_y = -200
                enemy_num -= 1
                e_time = time.time()
            if bullet_y <=120  and bullet_y >=0 and bullet_x >= 300 and bullet_x + bullet_rect.width <=480:
                e_time4 = time.time()
            screen.blit(bullet[b1], (bullet_x, bullet_y))
        if b1 == 3:    #子弹碰东面
            bullet_x -= bspeed
            if bullet_y > tan2y and bullet_y < tan2y + hero_rect.height and bullet_x > tan2x and bullet_x <= tan2x + hero_rect.width and enemy_num >0 :
                bullet_x = -200
                bullet_y = -200
                enemy_num -= 1
                e_time = time.time()
            if bullet_y <=120  and bullet_y >=0 and bullet_x >= 300 and bullet_x <=480:
                e_time5 = time.time()
            screen.blit(bullet[b1], (bullet_x, bullet_y))
        # 敌方子弹移动
        if b2 == 0:     #子弹碰南面
            bullet1_y -= bspeed
            if bullet1_y <= tan1y+hero_rect.height and bullet1_y > tan1y and bullet1_x > tan1x and bullet1_x <tan1x+ hero_rect.width and hero_num >0:
                bullet1_x = -200
                bullet1_y = -200
                hero_num -= 1
                e_time1 = time.time()
            if    660<= bullet1_y <= 780  and bullet1_x >= 300 and bullet1_x + bullet_rect.width <= 480:
                e_time6 = time.time()
            screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
        if b2 == 1:     #子弹碰北面
            bullet1_y += bspeed
            if bullet1_y >= tan1y and bullet1_y < tan1y+hero_rect.height and bullet1_x > tan1x and bullet1_x <tan1x+ hero_rect.width and hero_num >0:
                bullet1_x = -200
                bullet1_y = -200
                hero_num -= 1
                e_time1 = time.time()
            if 660<= bullet1_y + bullet_rect.height<=780  and bullet1_x >= 300 and bullet1_x + bullet_rect.width <=480:
                e_time7 = time.time()
            screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
        if b2 == 2:     #子弹碰西面
            bullet1_x += bspeed
            if bullet1_y > tan1y  and bullet1_y < tan1y+hero_rect.height and bullet1_x >= tan1x and bullet1_x < tan1x + hero_rect.width and hero_num >0:
                bullet1_x = -200
                bullet1_y = -200
                hero_num -= 1
                e_time1 = time.time()
            if 660<=bullet1_y <=780 and bullet1_x >= 300 and bullet1_x + bullet_rect.width <=480:
                e_time8 = time.time()
            screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
        if b2 == 3:     #子弹碰东面
            bullet1_x -= bspeed
            if bullet1_y > tan1y and bullet1_y < tan1y + hero_rect.height and bullet1_x > tan1x and bullet1_x <= tan1x + hero_rect.width and hero_num >0:
                bullet1_x = -200
                bullet1_y = -200
                hero_num -= 1
                e_time1 = time.time()
            if 660<=bullet1_y <=780 and bullet1_x >= 300 and bullet1_x <=480:
                e_time9 = time.time()
            screen.blit(bullet1[b2], (bullet1_x, bullet1_y))
        # 我方子弹不能进银砖
        if (180 <=bullet_x<=600 and 360<= bullet_y <=420)or(0<=bullet_x<=60 and 360<= bullet_y <=420)or(720<=bullet_x<=780 and 360<= bullet_y <=420):
            screen.blit(broke1, (bullet_x, bullet_y))
            bullet_x = -200
            bullet_y = -200
        for a in range(2):
            for b in range(2):
                if (60+120*a <= bullet_x<=120+120*a and 60+480*b<=bullet_y<=240+480*b  ):
                    screen.blit(broke1, (bullet_x, bullet_y))
                    bullet_x = -200
                    bullet_y = -200
                if (540+120*a <= bullet_x<=600+120*a and 60+480*b<=bullet_y<=240+480*b  ):
                    screen.blit(broke1, (bullet_x, bullet_y))
                    bullet_x = -200
                    bullet_y = -200
        for a in range(2):
            if (300<= bullet_x <= 480 and 180 + 300*a <= bullet_y <= 300 + 300*a):
                screen.blit(broke1, (bullet_x, bullet_y))
                bullet_x = -200
                bullet_y = -200
        # 敌方子弹不能进银砖
        if (180 <= bullet1_x <= 600 and 360 <= bullet1_y <= 420) or (0 <= bullet1_x <= 60 and 360 <= bullet1_y <= 420) or (720 <= bullet1_x <= 780 and 360 <= bullet1_y <= 420):
            screen.blit(broke1, (bullet1_x, bullet1_y))
            bullet1_x = -200
            bullet1_y = -200
        for a in range(2):
            for b in range(2):
                if (60+120*a <= bullet1_x<=120+120*a and 60+480*b<=bullet1_y<=240+480*b  ):
                    screen.blit(broke1, (bullet1_x, bullet1_y))
                    bullet1_x = -200
                    bullet1_y = -200
                if (540+120*a <= bullet1_x<=600+120*a and 60+480*b<=bullet1_y<=240+480*b  ):
                    screen.blit(broke1, (bullet1_x, bullet1_y))
                    bullet1_x = -200
                    bullet1_y = -200
        for a in range(2):
            if (300<= bullet1_x <= 480 and 180 + 300*a <= bullet1_y <= 300 + 300*a):
                screen.blit(broke1, (bullet1_x, bullet1_y))
                bullet1_x = -200
                bullet1_y = -200
        #子弹相互碰撞
        if  bullet1_x<= bullet_x <= bullet1_x + 12 and bullet1_y <=bullet_y <= bullet1_y+12:
            screen.blit(broke1, (bullet_x, bullet_y))
            bullet_x = -200
            bullet_y = -200
            bullet1_x = -200
            bullet1_y = -200
        # 敌方死亡画面
        if time.time() - e_time < 0.3:
            screen.blit(broke2, (tan2x, tan2y))
        elif time.time() - e_time < 0.4:
            tan2x = 240
            tan2y = 0
        # 我方死亡画面
        if time.time() - e_time1 < 0.3:
            screen.blit(broke2, (tan1x, tan1y))
        elif time.time() - e_time1 < 0.4:
            tan1x = 240
            tan1y = 720
        #我方射中敌方水晶附近砖块
        if time.time() - e_time2 < 0.0001: #南面
            if 300<=bullet_x <360 and 60<= bullet_y <=120 and flag_3 == 1:
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx3, by3))
                bx3 = -200
                by3 = -200
                flag_3 = 0
            elif 360<=bullet_x <420 and 60<= bullet_y <=120 and flag_4 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx4, by4))
                bx4 = -200
                by4 = -200
                flag_4 = 0
            elif 420<=bullet_x <=480 and 60<= bullet_y <=120 and flag_5 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx5, by5))
                bx5 = -200
                by5 = -200
                flag_5 = 0
            elif 300 <= bullet_x <= 360 and 0<= bullet_y <=60 and flag_1 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx1, by1))
                bx1 = -200
                by1 = -200
                flag_1 = 0
            elif 420 <= bullet_x <= 480 and 0<= bullet_y <=60 and flag_2 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx2, by2))
                bx2 = -200
                by2 = -200
                flag_2 = 0
            elif 360 < bullet_x < 420 and 0<= bullet_y <=60 and e_shuijing == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (home1x, home1y))
                home1x = -200
                home1y = -200
                e_shuijing = 0
        if time.time() - e_time3 < 0.0001:  # 北面
            if 300<=bullet_x <360 and 60<= bullet_y <=120 and flag_3 == 1:
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx3, by3))
                bx3 = -200
                by3 = -200
                flag_3 = 0
            elif 360<=bullet_x <420 and 60<= bullet_y <=120 and flag_4 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx4, by4))
                bx4 = -200
                by4 = -200
                flag_4 = 0
            elif 420<=bullet_x <=480 and 60<= bullet_y <=120 and flag_5 == 1  :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx5, by5))
                bx5 = -200
                by5 = -200
                flag_5 = 0
            elif 360 < bullet_x < 420 and 0 <= bullet_y <= 60 and e_shuijing == 1:
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (home1x, home1y))
                home1x = -200
                home1y = -200
                e_shuijing = 0
        if time.time() - e_time4 < 0.0001:  # 西面
            if 300<=bullet_x <360 and 60<= bullet_y <=120 and flag_3 == 1:
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx3, by3))
                bx3 = -200
                by3 = -200
                flag_3 = 0
            elif 360<=bullet_x <420 and 60<= bullet_y <=120 and flag_4 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx4, by4))
                bx4 = -200
                by4 = -200
                flag_4 = 0
            elif 420<=bullet_x <=480 and 60<= bullet_y <=120 and flag_5 == 1  :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx5, by5))
                bx5 = -200
                by5 = -200
                flag_5 = 0
            elif 300 <= bullet_x <= 360 and 0<= bullet_y <=60 and flag_1 == 1  :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx1, by1))
                bx1 = -200
                by1 = -200
                flag_1 = 0
            elif 420 <= bullet_x <= 480 and 0<= bullet_y <=60 and flag_2 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx2, by2))
                bx2 = -200
                by2 = -200
                flag_2 = 0
            elif 360 < bullet_x < 420 and 0<= bullet_y <=60 and e_shuijing == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (home1x, home1y))
                home1x = -200
                home1y = -200
                e_shuijing = 0
        if time.time() - e_time5 < 0.0001:  # 东面
            if 300<=bullet_x <360 and 60<= bullet_y <=120 and flag_3 == 1:
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx3, by3))
                bx3 = -200
                by3 = -200
                flag_3 = 0
            elif 360<=bullet_x <420 and 60<= bullet_y <=120 and flag_4 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx4, by4))
                bx4 = -200
                by4 = -200
                flag_4 = 0
            elif 420<=bullet_x <=480 and 60<= bullet_y <=120 and flag_5 == 1  :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx5, by5))
                bx5 = -200
                by5 = -200
                flag_5 = 0
            elif 300 <= bullet_x <= 360 and 0<= bullet_y <=60 and flag_1 == 1  :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx1, by1))
                bx1 = -200
                by1 = -200
                flag_1 = 0
            elif 420 <= bullet_x <= 480 and 0<= bullet_y <=60 and flag_2 == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (bx2, by2))
                bx2 = -200
                by2 = -200
                flag_2 = 0
            elif 360 < bullet_x < 420 and 0<= bullet_y <=60 and e_shuijing == 1 :
                bullet_x = -200
                bullet_y = -200
                screen.blit(broke2, (home1x, home1y))
                home1x = -200
                home1y = -200
                e_shuijing = 0
        # 敌方射中敌方水晶附近砖块
        if time.time() - e_time6 < 0.0001:  # 南面
            if 300 <= bullet1_x < 360 and 660 <= bullet1_y <= 720 and flag_6 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx6, by6))
                bx6 = -200
                by6 = -200
                flag_6 = 0
            elif 360 <= bullet1_x < 420 and 660 <= bullet1_y <= 720 and flag_7 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx7, by7))
                bx7 = -200
                by7 = -200
                flag_7 = 0
            elif 420 <= bullet1_x <= 480 and 660 <= bullet1_y <= 720 and flag_8 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx8, by8))
                bx8 = -200
                by8 = -200
                flag_8 = 0
            elif 300 <= bullet1_x <= 360 and 720 <= bullet1_y <= 780 and flag_9 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx9, by9))
                bx9 = -200
                by9 = -200
                flag_9 = 0
            elif 420 <= bullet1_x <= 480 and 720 <= bullet1_y <= 780 and flag_10 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx10, by10))
                bx10 = -200
                by10 = -200
                flag_10 = 0
            elif 360 < bullet1_x < 420 and 720 <= bullet1_y <= 780 and h_shuijing == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (homex, homey))
                homex = -200
                homey = -200
                h_shuijing = 0
        if time.time() - e_time7 < 0.0001:  # 北面
            if 300 <= bullet1_x < 360 and 660 <= bullet1_y <= 720 and flag_6 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx6, by6))
                bx6 = -200
                by6 = -200
                flag_6 = 0
            elif 360 <= bullet1_x < 420 and 660 <= bullet1_y <= 720 and flag_7 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx7, by7))
                bx7 = -200
                by7 = -200
                flag_7 = 0
            elif 420 <= bullet1_x <= 480 and 660 <= bullet1_y <= 720 and flag_8 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx8, by8))
                bx8 = -200
                by8 = -200
                flag_8 = 0
            elif 300 <= bullet1_x <= 360 and 720 <= bullet1_y <= 780 and flag_9 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx9, by9))
                bx9 = -200
                by9 = -200
                flag_9 = 0
            elif 420 <= bullet1_x <= 480 and 720 <= bullet1_y <= 780 and flag_10 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx10, by10))
                bx10 = -200
                by10 = -200
                flag_10 = 0
            elif 360 < bullet1_x < 420 and 720 <= bullet1_y <= 780 and h_shuijing == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (homex, homey))
                homex = -200
                homey = -200
                h_shuijing = 0
        if time.time() - e_time8 < 0.0001:  # 西面
            if 300 <= bullet1_x < 360 and 660 <= bullet1_y <= 720 and flag_6 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx6, by6))
                bx6 = -200
                by6 = -200
                flag_6 = 0
            elif 360 <= bullet1_x < 420 and 660 <= bullet1_y <= 720 and flag_7 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx7, by7))
                bx7 = -200
                by7 = -200
                flag_7 = 0
            elif 420 <= bullet1_x <= 480 and 660 <= bullet1_y <= 720 and flag_8 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx8, by8))
                bx8 = -200
                by8 = -200
                flag_8 = 0
            elif 300 <= bullet1_x <= 360 and 720 <= bullet1_y <= 780 and flag_9 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx9, by9))
                bx9 = -200
                by9 = -200
                flag_9 = 0
            elif 420 <= bullet1_x <= 480 and 720 <= bullet1_y <= 780 and flag_10 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx10, by10))
                bx10 = -200
                by10 = -200
                flag_10 = 0
            elif 360 < bullet1_x < 420 and 720 <= bullet1_y <= 780 and h_shuijing == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (homex, homey))
                homex = -200
                homey = -200
                h_shuijing = 0
        if time.time() - e_time9 < 0.0001:  # 东面
            if 300 <= bullet1_x < 360 and 660 <= bullet1_y <= 720 and flag_6 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx6, by6))
                bx6 = -200
                by6 = -200
                flag_6 = 0
            elif 360 <= bullet1_x < 420 and 660 <= bullet1_y <= 720 and flag_7 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx7, by7))
                bx7 = -200
                by7 = -200
                flag_7 = 0
            elif 420 <= bullet1_x <= 480 and 660 <= bullet1_y <= 720 and flag_8 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx8, by8))
                bx8 = -200
                by8 = -200
                flag_8 = 0
            elif 300 <= bullet1_x <= 360 and 720 <= bullet1_y <= 780 and flag_9 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx9, by9))
                bx9 = -200
                by9 = -200
                flag_9 = 0
            elif 420 <= bullet1_x <= 480 and 720 <= bullet1_y <= 780 and flag_10 == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (bx10, by10))
                bx10 = -200
                by10 = -200
                flag_10 = 0
            elif 360 < bullet1_x < 420 and 720 <= bullet1_y <= 780 and h_shuijing == 1:
                bullet1_x = -200
                bullet1_y = -200
                screen.blit(broke2, (homex, homey))
                homex = -200
                homey = -200
                h_shuijing = 0


        # 生命显示
        text_3 = font1.render("Life of red:", True, (255, 255, 255))
        screen.blit(text_3, (610, 10))
        for i in range(enemy_num):
            screen.blit(live, (710 + i * 22, 10))
        text_4 = font1.render("Life of blue:", True, (255, 255, 255))
        screen.blit(text_4, (0, 10))
        for i in range(hero_num):
            screen.blit(live, (110 + i * 22, 10))

    pygame.display.update()
