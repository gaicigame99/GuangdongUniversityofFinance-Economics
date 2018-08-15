import pygame
import random
import time

pygame.init()
pygame.mixer.init()

font = pygame.font.Font("C:\Windows\Fonts\simhei.ttf",20)
font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",60)
black_color = (0, 0, 0)

back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
bullet_music = pygame.mixer.Sound(r"sound\bullet.wav")
enemy_music = pygame.mixer.Sound(r"sound\enemy2_down.wav")
button_music = pygame.mixer.Sound(r"sound\button.wav")

screen = pygame.display.set_mode((495, 800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))

hero = pygame.image.load("images\hero.gif")
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height

bullet = pygame.image.load(r"images\bullet2.png")
b_rect = bullet.get_rect()
by_speed = 5
bx = []
by = []
time_t = 10
level1 = 1
score1 = 0
miss1 = 0
hit1 = 0
hp1= 3
count = 0

# 小飞机
enemy = pygame.image.load(r"images\enemy0.png")
e_rect = enemy.get_rect()
e_width = e_rect.width
e_height = e_rect.height
ex = []
ey = []
time_e =100
ey_speed = 1
enemy_1 = pygame.image.load(r"images\enemy0_down1.png")
enemy_2 = pygame.image.load(r"images\enemy0_down2.png")
enemy_3 = pygame.image.load(r"images\enemy0_down3.png")
enemy_4 = pygame.image.load(r"images\enemy0_down4.png")

# 大飞机
enemy1 = pygame.image.load(r"images\enemy1.png")
e_rect1 = enemy1.get_rect()
e_width1 = e_rect1.width
e_height1 = e_rect1.height
ex1 = []
ey1 = []
e_blood1 = []
ey_speed1 = 1
enemy1_1 = pygame.image.load(r"images\enemy1_down1.png")
enemy1_2 = pygame.image.load(r"images\enemy1_down2.png")
enemy1_3 = pygame.image.load(r"images\enemy1_down3.png")
enemy1_4 = pygame.image.load(r"images\enemy1_down4.png")

g_button = pygame.image.load(r"images\green_button.png")
r_button = pygame.image.load(r"images\red_button.png")
g_rect = g_button.get_rect()
r_rect = r_button.get_rect()
xx = 400
yy = 700

time1 =[]
tx1 = []
ty1 = []

time2 =[]
tx2 = []
ty2 = []

flag_s = 0
stop_flag = 0
button_flag = 1

gameover1 = pygame.image.load(r"images\gameover.png")

def hit(ex, ey, e_width, e_height, hit1, hx, hy, h_width, h_height): # 被敌机撞到
    for i in range(len(ex)):
        if ex[i] - h_width < hx - h_width / 2 < ex[i] + e_width and \
                ey[i] - h_height < hy - h_height / 2 < ey[i] + e_height:
            ex[i] = random.randint(50, 450)#
            ey[i] = random.randint(-200, -10)
            hit1 += 1
    return hit1

for i in range(5): # 初始化小飞机
    ex.append(random.randint(50, 450))
    ey.append(random.randint(-200, -10))

for i in range(3): # 初始化大飞机
    ex1.append(random.randint(50, 450))
    ey1.append(random.randint(-200, -10))
    e_blood1.append(20)


a, b, c = 0,0,0
mouse_x, mouse_y = pygame.mouse.get_pos()

start = pygame.image.load(r"images\start.png") # 开始按钮
s_rect = start.get_rect()
name = pygame.image.load(r"images\name.png")
exit1 = pygame.image.load(r"images\quit_sel.png")
exit1_rect= exit1.get_rect()

start_flag = 0 # 控制开始游戏

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果当前事件是退出事件
            exit()  # 退出

        # 暂停游戏
        if event.type == pygame.MOUSEBUTTONUP and a == 1:
            a = 0
            if xx < mouse_x < xx + g_rect.width and yy < mouse_y < yy + g_rect.height :
                if flag_s == 0:   # 按奇数次暂停
                    screen.blit(r_button, (xx, yy))
                    text1 = font.render("点击红色按钮继续游戏", True, black_color)
                    screen.blit(text1, (150, 380))
                    stop_flag = 1
                    a, b, c = 0, 0, 0
                    flag_s = 1
                elif flag_s == 1:   # 按偶数次继续
                    screen.blit(g_button, (xx, yy))
                    stop_flag = 0
                    a, b, c = 0, 0, 0
                    flag_s = 0

    mouse_x, mouse_y = pygame.mouse.get_pos()
    a, b, c = pygame.mouse.get_pressed()

    if start_flag == 1:
        if stop_flag == 0: # 开始游戏并无暂停游戏
            screen.blit(bg, (0, 0))
            screen.blit(g_button, (xx, yy))
            text1 = font.render("level:" + str(level1), True, black_color)
            screen.blit(text1, (10, 10))
            text1 = font.render("score:" + str(score1), True, black_color)
            screen.blit(text1, (10, 30))
            text1 = font.render(" miss:" + str(miss1), True, black_color)
            screen.blit(text1, (10, 50))
            text1 = font.render("   hp:", True, black_color)
            screen.blit(text1, (10, 70))
            pygame.draw.line(screen, (220, 220, 220), (70, 82), (120, 82), 6)  # 灰
            pygame.draw.line(screen, (255, 0, 0), (70, 82),(70 + 50/3*(3-hit1), 82), 6)  # 红

            hx, hy = pygame.mouse.get_pos()


            if time_e>0: # 开始游戏后loading时间
                time_e -=1
                text1 = font.render("loading……", True, black_color)
                screen.blit(text1, (200, 350))
            else :
                screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))
                for i in range(5):  # 敌人的位置
                    screen.blit(enemy, (ex[i], ey[i]))
                    ey[i] += ey_speed

                for i in range(3):  # 敌人的位置
                    screen.blit(enemy1, (ex1[i], ey1[i]))
                    pygame.draw.line(screen, (220, 220, 220), (ex1[i], ey1[i] - 2), (ex1[i] + e_width1, ey1[i]-2), 3) # 灰
                    pygame.draw.line(screen, (255, 0, 0), (ex1[i], ey1[i] - 2), (ex1[i] + e_width1/(20*level1)*e_blood1[i], ey1[i] - 2), 3) # 红
                    # text = font.render(str(e_blood1[i]), True, black_color)
                    # screen.blit(text, (ex1[i]+25, ey1[i]-15))
                    ey1[i] += ey_speed1

                if time_t > 0: #子弹射出的频率
                    time_t -= 1
                else :
                    bx.append(hx - b_rect.width / 2 )
                    by.append(hy - b_rect.height - h_height / 2)
                    bullet_music.play()
                    time_t = 10

                for i in by:
                    index = by.index(i)
                    if i < 0:
                        by.pop(index)
                        bx.pop(index)

                for i in range(len(bx)): # 射出子弹
                    screen.blit(bullet, (bx[i], by[i]))
                    by[i] -= by_speed

                for i in range(len(bx)):  # 小飞机中弹
                    for j in range(len(ex)):
                        if ex[j] - b_rect.width < bx[i] < ex[j] + e_width and ey[j] < by[i] < ey[j] + e_height:
                            time1.append(time.time())
                            tx1.append(ex[j])
                            ty1.append(ey[j])
                            bx[i] = -99
                            ex[j] = random.randint(50, 450)
                            ey[j] = random.randint(-200, -10)
                            score1 += 1
                        elif ey[j] > 800:
                            ex[j] = random.randint(50, 450)
                            ey[j] = random.randint(-200, -10)
                            miss1 += 1

                    if len(time1):
                        for i in range(len(time1)):
                            ttt = time.time()-time1[i]
                            if 0 < ttt < 0.1:
                                screen.blit(enemy_1,(tx1[i],ty1[i]))
                                enemy_music.play()
                            if 0.1 <= ttt < 0.2:
                                screen.blit(enemy_2,(tx1[i],ty1[i]))
                            if 0.2 <= ttt < 0.3:
                                screen.blit(enemy_3, (tx1[i], ty1[i]))
                            if 0.3 <= ttt < 0.4:
                                screen.blit(enemy_4,(tx1[i],ty1[i]))
                                enemy_music.play()
    #
                for i in range(len(bx)):  # 大飞机中弹
                    for j in range(len(ex1)):
                        if ex1[j] - b_rect.width < bx[i] < ex1[j]+e_width1 and ey1[j] < by[i] < ey1[j]+e_height1:
                            e_blood1[j] -= 10
                            bx[i] = -99
                            if e_blood1[j] <= 0:
                                time2.append(time.time())
                                tx2.append(ex1[j])
                                ty2.append(ey1[j])
                                ex1[j] = random.randint(50, 450)
                                ey1[j] = random.randint(-200, -10)
                                e_blood1[j] = 20 * level1
                                score1 += 1

                        elif ey1[j] > 800:
                            ex1[j] = random.randint(50, 450)
                            ey1[j] = random.randint(-200, -10)
                            e_blood1[j] = 20 * level1
                            miss1 += 1

                    if len(time2):
                        for i in range(len(time2)):
                            ttt = time.time() - time2[i]
                            if 0 < ttt < 0.1:
                                screen.blit(enemy1_1, (tx2[i], ty2[i]))
                                enemy_music.play()
                            if 0.1 <= ttt < 0.2:
                                screen.blit(enemy1_2, (tx2[i], ty2[i]))
                            if 0.2 <= ttt < 0.3:
                                screen.blit(enemy1_3, (tx2[i], ty2[i]))
                            if 0.3 <= ttt < 0.4:
                                screen.blit(enemy1_4, (tx2[i], ty2[i]))

                if score1 > 50 * level1: # 提高等级
                    level1 += 1
                    ey_speed += 0.2
                    ey_speed1 += 0.1
                    by_speed += 1
                    for i in range(len(e_blood1)):
                        if ey1[i]<-e_height1:
                            e_blood1[i] = level1 * 20

                hit1 = hit(ex, ey, e_width, e_height, hit1, hx, hy, h_width, h_height)
                hit1 = hit(ex1, ey1, e_width1, e_height1, hit1, hx, hy, h_width, h_height)
    else : # 开始界面
        screen.blit(bg, (0, 0))
        screen.blit(name, (30, 200))
        screen.blit(start, (170, 400))
        screen.blit(exit1, (350, 750))
        if 170 < mouse_x < 170 + s_rect.width and 400 < mouse_y < 400 + s_rect.height :
            if button_flag :
                button_music.play()
                button_flag = 0
            if a:
                start_flag = 1
        else:
            button_flag = 1

        if 350 < mouse_x < 350 + exit1_rect.width and 750 < mouse_y < 750 + exit1_rect.height and a:
            break

    if hit1 >= 3:  # 游戏结束
        screen.blit(gameover1, (0, 0))
        screen.blit(exit1, (350, 750))
        text1 = font1.render(str(score1), True, black_color)
        screen.blit(text1, (220, 350))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 350 < mouse_x < 350 + exit1_rect.width and 750 < mouse_y < 750 + exit1_rect.height and a:
            break
        stop_flag = 1

    pygame.display.update()