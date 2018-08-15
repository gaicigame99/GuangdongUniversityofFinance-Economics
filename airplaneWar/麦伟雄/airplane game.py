import pygame
import random
from time import sleep
# 飞机大战
# 手机上的，单手操作
# 长条形
# 鼠标操作
# 黄金比率:0.618(height:width)
pygame.init()
pygame.mixer.init() # 初始化声音
screen = pygame.display.set_mode((480, 800))
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",24)

back_ground = pygame.image.load("images\\background.png")
back_music = pygame.mixer.Sound("sound\game_music.ogg")
background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (500, 800))

bullet = pygame.image.load("images\\bullet.png")

plane = pygame.image.load("images\hero.gif")
self_break1 = pygame.image.load("images\hero_blowup_n1.png")
self_break2 = pygame.image.load("images\hero_blowup_n2.png")
self_break3 = pygame.image.load("images\hero_blowup_n3.png")
self_break4 = pygame.image.load("images\hero_blowup_n4.png")
plane_rect = plane.get_rect()

enemy_plane = pygame.image.load("images\enemy1.png")
enemy_break1 = pygame.image.load("images\enemy1_down1.png")
enemy_break2 = pygame.image.load("images\enemy1_down2.png")
enemy_break3 = pygame.image.load("images\enemy1_down3.png")
enemy_break4 = pygame.image.load("images\enemy1_down4.png")
enemy_blood1 = pygame.image.load("images\enemy_blood1.png")
enemy_blood2 = pygame.image.load("images\enemy_blood2.png")
enemy_blood3 = pygame.image.load("images\enemy_blood3.png")
enemy_blood4 = pygame.image.load("images\enemy_blood4.png")
enemy_blood1 = pygame.transform.scale(enemy_blood1, (69, 10))
enemy_blood2 = pygame.transform.scale(enemy_blood2, (69, 10))
enemy_blood3 = pygame.transform.scale(enemy_blood3, (69, 10))
enemy_blood4 = pygame.transform.scale(enemy_blood4, (69, 10))
enemy_plane_rect = enemy_plane.get_rect()
enemy_blood_rect = enemy_blood1.get_rect()

# background = pygame.image.load("images\\background.png")
# \b 由于\b是转义字符，\\之后才会得到b
# r 表示原样输出

sx, sy = 100, 100
flag = 1
flag_number = 0
label1 = 1

bx_list = []
by_list = []
frequency = 10
time = frequency

ex_list = []
ey_list = []
a = []
b = []
label = []
flag_number1 = []
for i in range(5):
    label.append(1)
    ex_list.append(random.randint(0, 500-enemy_plane_rect.width))
    ey_list.append(random.randint(-200, 0 - enemy_plane_rect.height))

while True:
    back_music.play()
    sleep(0.0001)
    screen.blit(back_ground, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # 我方战机爆炸效果
    if flag == 1:
        sx, sy = pygame.mouse.get_pos()
        screen.blit(plane, (sx - plane_rect.width // 2, sy - plane_rect.height // 2))
        if time:
            time -= 1
        else:
            bx_list.append(sx - 10)
            by_list.append(sy - plane_rect.height // 2)
            time = frequency
    elif flag == 2:
        flag_number += 1
        screen.blit(self_break1, (sx - plane_rect.width // 2, sy - plane_rect.height // 2))
        if flag_number > 50:
            flag = 3
            flag_number = 0
    elif flag == 3:
        flag_number += 1
        screen.blit(self_break2, (sx - plane_rect.width // 2, sy - plane_rect.height // 2))
        if flag_number > 50:
            flag = 4
            flag_number = 0
    elif flag == 4:
        flag_number += 1
        screen.blit(self_break3, (sx - plane_rect.width // 2, sy - plane_rect.height // 2))
        if flag_number > 50:
            flag = 5
            flag_number = 0
    elif flag == 5:
        flag_number += 1
        screen.blit(self_break4, (sx - plane_rect.width // 2, sy - plane_rect.height // 2))
        if flag_number > 50:
            flag = 0
            flag_number = 0

    # 敌机血量显示
    for j in range(5):
        if label[j] == 1:
            screen.blit(enemy_blood1, (ex_list[j] - 4, ey_list[j] - enemy_blood_rect.height))
        elif label[j] == 2:
            screen.blit(enemy_blood2, (ex_list[j] - 4, ey_list[j] - enemy_blood_rect.height))
        elif label[j] == 3:
            screen.blit(enemy_blood3, (ex_list[j] - 4, ey_list[j] - enemy_blood_rect.height))
        elif label[j] == 4:
            screen.blit(enemy_blood4, (ex_list[j] - 4, ey_list[j] - enemy_blood_rect.height))

    # 我方战机血量显示
    if label1 == 1:
        pygame.draw.rect(screen, (54, 147, 226),(sx - 36, sy - plane_rect.height // 2 - 4, 72 - (label1 - 1) * 18, 8))
    elif label1 == 2:
        pygame.draw.rect(screen, (54, 147, 226),(sx - 36, sy - plane_rect.height // 2 - 4, 72 - (label1 - 1) * 18, 8))
        pygame.draw.rect(screen, (211, 210, 217),(sx - 36 + (5 - label1) * 18, sy - plane_rect.height // 2 - 4, (label1 - 1) * 18, 8))
    elif label1 == 3:
        pygame.draw.rect(screen, (54, 147, 226),(sx - 36, sy - plane_rect.height // 2 - 4, 72 - (label1 - 1) * 18, 8))
        pygame.draw.rect(screen, (211, 210, 217),(sx - 36 + (5 - label1) * 18, sy - plane_rect.height // 2 - 4, (label1 - 1) * 18, 8))
    elif label1 == 4:
        pygame.draw.rect(screen, (54, 147, 226),(sx - 36, sy - plane_rect.height // 2 - 4, 72 - (label1 - 1) * 18, 8))
        pygame.draw.rect(screen, (211, 210, 217), (sx - 36 + (5 - label1) * 18, sy - plane_rect.height // 2 - 4, (label1 - 1) * 18, 8))

    # 子弹与敌机碰撞检测
    for i in range(len(bx_list)):
        screen.blit(bullet, (bx_list[i], by_list[i]))
        by_list[i] -= 4
        for j in range(5):
            if ex_list[j] < bx_list[i] < ex_list[j] + enemy_plane_rect.width and ey_list[j] < by_list[i] < ey_list[j] + enemy_plane_rect.height and 0 < by_list[i] < 800:
                label[j] += 1
                by_list[i] = -1000
                if label[j] == 5:
                    a.append(ex_list[j])
                    b.append(ey_list[j])
                    flag_number1.append(0)
                    ex_list[j] = random.randint(0, 500-enemy_plane_rect.width)
                    ey_list[j] = random.randint(-200, 0 - enemy_plane_rect.height)
                    label[j] = 1
            # 敌机与我方战机
            if ex_list[j] < sx < ex_list[j] + enemy_plane_rect.width and ey_list[j] < sy < ey_list[j] + enemy_plane_rect.height:
                a.append(ex_list[j])
                b.append(ey_list[j])
                flag_number1.append(0)
                ex_list[j] = random.randint(0, 500 - enemy_plane_rect.width)
                ey_list[j] = random.randint(-200, 0 - enemy_plane_rect.height)
                label1 += 1
                if label1 == 5:
                    flag = 2
                    label1 = 1
                    sy = -100

    # 敌机下降与出界检测
    for j in range(5):
        screen.blit(enemy_plane, (ex_list[j], ey_list[j]))
        ey_list[j] += 1
        if ey_list[j] > 800:
            label[j] = 1
            ex_list[j] = random.randint(0, 500 - enemy_plane_rect.width)
            ey_list[j] = random.randint(-100, 0 - enemy_plane_rect.height)

    #   敌机爆炸效果
    for j in range(len(a)):
        if 0 <= flag_number1[j] < 5:
            flag_number1[j] += 1
            screen.blit(enemy_break1, (a[j], b[j]))
        if 5 <= flag_number1[j] < 10:
            flag_number1[j] += 1
            screen.blit(enemy_break2, (a[j], b[j]))
        if 10 <= flag_number1[j] < 15:
            flag_number1[j] += 1
            screen.blit(enemy_break3, (a[j], b[j]))
        if 15 <= flag_number1[j] < 20:
            flag_number1[j] += 1
            screen.blit(enemy_break4, (a[j], b[j]))

    # 子弹优化效果，删除那些位置小于零的，减少内存
    aa = len(bx_list)
    i = 0
    for j in range(aa):
        if by_list[i] < 0:
            del by_list[i], bx_list[i]
        else:
            i += 1
            if i == len(bx_list):
                break

    # 敌机爆炸代码优化，删除已经爆炸的，减少内存
    aaa = len(flag_number1)
    ii = 0
    for j in range(aaa):
        if flag_number1[ii] >= 20:
            del a[ii], b[ii], flag_number1[ii]
        else:
            ii += 1
            if ii == len(flag_number1):
                break
    pygame.display.update()


