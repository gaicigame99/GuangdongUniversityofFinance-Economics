import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# backmusic = pygame.mixer.Sound("")

#游戏界面
screen = pygame.display.set_mode((600,800))
background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background,(600,800))
name = pygame.image.load(r"images\name.png")
restart = pygame.image.load(r"images\restart_nor.png")
exit = pygame.image.load(r"images\quit_nor.png")
pause0 = pygame.image.load(r"images\game_pause_nor.png")
pause1 = pygame.image.load(r"images\game_pause_pressed.png")
go_on = pygame.image.load(r"images\resume_nor.png")

#按钮
class button():
    def __init__(self, image, x, y):
        rect = image.get_rect()
        self.width = rect.width
        self.height = rect.height
        self.x = x
        self.y = y
    def click(self, hx, hy, press):
        if self.x <= hx <= self.x + self.width and \
            self.y <= hy <= self.y + self.height and \
            press:
            return True
        else:
            return False

Restart = button(restart, 240,480)
Exit = button(exit, 240, 560)
Pause = button(pause0, 500, 50)
Go_on = button(go_on,240,400)

#自己的飞机
hero = pygame.image.load(r"images\hero1.png")
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height
hx = 100
hy = 100

#子弹
bullet = pygame.image.load(r"images\bullet.png")
bullet = pygame.transform.scale(bullet,(15,15))
b_rect = bullet.get_rect()
b_width = b_rect.width
b_height = b_rect.height
bx = []
by = []
b_v = 50
b_time = b_v

#空投
airdrop = pygame.image.load(r"images\bomb-1.gif")
a_rect = airdrop.get_rect()
a_width = a_rect.width
a_height = a_rect.height
ax = []
ay = []
a_x = random.randint(0, 500)
a_y = -50
a_v = 1000
a_time = a_v

#小型敌机
enemy = pygame.image.load(r"images\enemy0.png")
e_rect = enemy.get_rect()
e_width = e_rect.width
e_height = e_rect.height
ex = [300]
ey = [-10]
e_y = -20
e_v = 1000
e_time = e_v

#小敌机爆炸
enemy_down1 = pygame.image.load(r"images\enemy0_down1.png")
enemy_down2 = pygame.image.load(r"images\enemy0_down2.png")
enemy_down3 = pygame.image.load(r"images\enemy0_down3.png")
enemy_down4 = pygame.image.load(r"images\enemy0_down4.png")
enemy_boom = [enemy_down1,enemy_down2,enemy_down3,enemy_down4]
dx = [200]
dy = [-50]

#中型敌机
m_enemy = pygame.image.load(r"images\enemy1.png")
m_rect = m_enemy.get_rect()
m_width = m_rect.width
m_height = m_rect.height
mx = [-200]
my = [-100]
m_v = 1000
m_time = m_v
#颜色
red = (216, 3, 3)
grey=(153,153,153)

#中型敌机爆炸
m_enemy_down1 = pygame.image.load(r"images\enemy1_down1.png")
m_enemy_down2 = pygame.image.load(r"images\enemy1_down2.png")
m_enemy_down3 = pygame.image.load(r"images\enemy1_down3.png")
m_enemy_down4 = pygame.image.load(r"images\enemy1_down4.png")
dx1 = [200]
dy1 = [-50]

#大型敌机
l_enemy = pygame.image.load(r"images\enemy2.png")
l_rect = l_enemy.get_rect()
l_width = l_rect.width
l_height = l_rect.height
lx = [-200]
ly = [-100]
l_v = 100
l_time = l_v

#大型敌机爆炸
l_enemy_down1 = pygame.image.load(r"images\enemy2_down1.png")
l_enemy_down2 = pygame.image.load(r"images\enemy2_down2.png")
l_enemy_down3 = pygame.image.load(r"images\enemy2_down3.png")
l_enemy_down4 = pygame.image.load(r"images\enemy2_down4.png")
l_enemy_down5 = pygame.image.load(r"images\enemy2_down5.png")
l_enemy_down6 = pygame.image.load(r"images\enemy2_down6.png")
dx2 = [200]
dy2 = [-50]

time_0 = 0
time_m = 0
time_l = 0
flag = 0 #被击中的小飞机数量
flag_1 = [0] #某架中型飞机中子弹数
flag_2 = [0] #某架大型飞机中子弹数
flag_m = 0  #被击中中型飞机数
flag_l = 0  #被击中大型飞机数
skr = 0 #标记飞出屏幕的子弹数
begin = 0

#检测碰撞
def crash(ex, ey, e_width, e_height, bx, by, b_width, b_height):
    if bx + b_width >= ex and \
            bx <= ex + e_width and \
            by <= ey + e_height and \
            by + b_height >= ey and \
            by > 0:
        return True
    else:
        return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        press = pygame.mouse.get_pressed()

    #初始界面
    screen.blit(background, (0, 0))
    screen.blit(name, (80,200))
    screen.blit(restart,(Restart.x, Restart.y))
    screen.blit(exit, (Exit.x, Exit.y))


    hx, hy = pygame.mouse.get_pos()
    if Restart.click(hx, hy, press[0]):
        begin = 1
    if Exit.click(hx, hy, press[0]):
        break

    #开始游戏
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            press = pygame.mouse.get_pressed()

        screen.blit(background, (0, 0))
        screen.blit(pause0, (Pause.x, Pause.y))

        #储存子弹
        hx, hy = pygame.mouse.get_pos()

        if b_time:
            b_time -= 1
        else:
            bx.append(hx)
            by.append(hy - b_height - h_height / 2)
            b_time = b_v

        #储存小敌机
        e_x = random.randint(0,500)
        e_y = -50
        if e_time:
            e_time -= 1
        else:
            ex.append(e_x)
            ey.append(e_y)
            e_time = e_v

        #储存中型敌机
        m_x = random.randint(0, 500)
        m_y = -50
        if m_time:
            m_time -= 1
        else:
            mx.append(m_x)
            my.append(m_y)
            m_time = m_v
            flag_1.append(0)

        #储存大型敌机
        l_x = random.randint(0, 500)
        l_y = -50
        if l_time:
            l_time -= 1
        else:
            lx.append(l_x)
            ly.append(l_y)
            l_time = l_v
            flag_2.append(0)

        #储存空投
        if a_time:
            a_time -= 1
        else:
            a_x = random.randint(0, 500)
            ax.append(a_x)
            ay.append(a_y)
            a_time = a_v

        screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))

        #优化子弹
        if len(by):
            for i in range(len(by)):
                if by[i] < -10:
                    del by[i],bx[i]
                    skr += 1
                # 防止列表越界
                if i >= len(by) - skr:
                    break

        #发出子弹
        for i in range(len(bx)):
            screen.blit(bullet, (bx[i], by[i]))
            by[i] -= 3

        #小敌机出现
        for i in range(len(ex)):
            screen.blit(enemy,(ex[i],ey[i]))
            ey[i] += 2
            for n in range(len(bx)):
                #判断子弹是否打中敌机
                if crash(ex[i], ey[i], e_width, e_height, bx[n], by[n], b_width, b_height):
                    time_0 = time.time() #获取爆炸时的时间
                    by[n] = -20 #清除子弹
                    flag += 1
                    dx.append(ex[i]) #获得飞机爆炸时的坐标
                    dy.append(ey[i])

                    ex[i] = random.randint(0,500)
                    ey[i] = random.randint(-200,-50)

            #敌机爆炸
            time_1 = time.time()
            if time_1-time_0 <= 0.15:
                screen.blit(enemy_down1,(dx[flag],dy[flag]))
            if 0.15 < time_1 - time_0 <= 0.3:
                screen.blit(enemy_down2, (dx[flag], dy[flag]))
            if 0.3 < time_1 - time_0 <= 0.45:
                screen.blit(enemy_down3, (dx[flag], dy[flag]))
            if 0.45 < time_1 - time_0 <= 0.6:
                screen.blit(enemy_down4, (dx[flag], dy[flag]))

        #中型敌机出现
        for i in range(len(mx)):
            screen.blit(m_enemy,(mx[i],my[i]))
            pygame.draw.line(screen, red, (mx[i], my[i] + m_height+3), (mx[i] + m_width * ((5 - flag_1[i]) / 5), my[i] + m_height+3), 5)
            pygame.draw.line(screen, grey, (mx[i] + m_width * ((5 - flag_1[i]) / 5), my[i] + m_height + 3),
                             (mx[i] + m_width, my[i] + m_height + 3), 5)
            my[i] += 2
            for n in range(len(bx)):
                #判断子弹是否打中敌机
                if crash(mx[i], my[i], m_width, m_height, bx[n], by[n], b_width, b_height):
                    by[n] = -20 #清除子弹
                    flag_1[i] += 1
                    #打中五次使敌机爆炸
                    if flag_1[i] == 5:
                        flag_m += 1
                        flag_1[i] = 0
                        time_m = time.time()  # 获取爆炸时的时间
                        dx1.append(mx[i]) # 获得飞机爆炸时的坐标
                        dy1.append(my[i])

                        mx[i] = random.randint(0,500)
                        my[i] = random.randint(-200,-50)

            #敌机爆炸
            time_2 = time.time()
            if time_2-time_m <= 0.15:
                screen.blit(m_enemy_down1,(dx1[flag_m],dy1[flag_m]))
            if 0.15 < time_2 - time_m <= 0.3:
                screen.blit(m_enemy_down2, (dx1[flag_m], dy1[flag_m]))
            if 0.3 < time_2 - time_m <= 0.45:
                screen.blit(m_enemy_down3, (dx1[flag_m], dy1[flag_m]))
            if 0.45 < time_2 - time_m <= 0.6:
                screen.blit(m_enemy_down4, (dx1[flag_m], dy1[flag_m]))

        #大型敌机出现
        for i in range(len(lx)):
            screen.blit(l_enemy,(lx[i],ly[i]))
            pygame.draw.line(screen, red, (lx[i], ly[i] + l_height+3), (lx[i] + l_width * ((10 - flag_2[i]) / 10), ly[i] + l_height+3), 5)
            pygame.draw.line(screen, grey, (lx[i] + l_width * ((10 - flag_2[i]) / 10), ly[i] + l_height + 3),
                             (lx[i] + l_width, ly[i] + l_height + 3), 5)
            ly[i] += 0.5
            for n in range(len(bx)):
                #判断子弹是否打中敌机
                if crash(lx[i], ly[i], l_width, l_height, bx[n], by[n], b_width, b_height):
                    by[n] = -20 #清除子弹
                    flag_2[i] += 1
                    #打中五次使敌机爆炸
                    if flag_2[i] == 10:
                        flag_l += 1
                        flag_2[i] = 0
                        time_l = time.time()  # 获取爆炸时的时间
                        dx2.append(lx[i]) # 获得飞机爆炸时的坐标
                        dy2.append(ly[i])

                        lx[i] = random.randint(0,500)
                        ly[i] = random.randint(-200,-50)

            # 大型敌机爆炸
            time_3 = time.time()
            if time_3 - time_l <= 0.15:
                screen.blit(l_enemy_down1, (dx2[flag_l], dy2[flag_l]))
            if 0.15 < time_3 - time_l <= 0.3:
                screen.blit(l_enemy_down2, (dx2[flag_l], dy2[flag_l]))
            if 0.3 < time_3 - time_l <= 0.45:
                screen.blit(l_enemy_down3, (dx2[flag_l], dy2[flag_l]))
            if 0.45 < time_3 - time_l <= 0.6:
                screen.blit(l_enemy_down4, (dx2[flag_l], dy2[flag_l]))
            if 0.6 < time_3 - time_l <= 0.75:
                screen.blit(l_enemy_down5, (dx2[flag_l], dy2[flag_l]))
            if 0.75 < time_3 - time_l <= 0.9:
                screen.blit(l_enemy_down6, (dx2[flag_l], dy2[flag_l]))
        #空投出现
        if len(ax):
            for i in range(len(ax)):
                screen.blit(airdrop,(ax[i],ay[i]))
                ay[i] += 2
                #自己的飞机接到空投
                if crash(hx - h_width / 2, hy - h_height / 2, h_width, h_height, ax[i], ay[i], a_width, a_height):
                    ay[i] = random.randint(-200, -50)
                    del ax[i]
                    del ay[i]
                    b_v = int(b_v / 2) #子弹频率翻倍
                    #防止列表越界
                    if i == len(ax) -1:
                        break

        #暂停
        if Pause.click(hx, hy, press[0]):
            begin = 2
            print(begin)

        while begin == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                press = pygame.mouse.get_pressed()

            hx, hy = pygame.mouse.get_pos()
            if Pause.click(hx, hy, press[0]):
                begin = 1
                break

            pygame.display.update()

        pygame.display.update()

    pygame.display.update()