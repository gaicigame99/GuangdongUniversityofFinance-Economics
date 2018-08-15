import pygame
import random
import time
pygame.init()
pygame.mixer.init()
backmusic = pygame.mixer.Sound("sound\game_music.ogg")
backmusic.play()

screen = pygame.display.set_mode((495, 800))
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (495, 800))
jie_bg = pygame.image.load("jiemian2.jpg")
jie_bg = pygame.transform.scale(jie_bg, (495, 800))
blue_button = pygame.image.load("bblue_button.png")
blue_button = pygame.transform.scale(blue_button, (300, 100))
green_button = pygame.image.load("bgreen_button.png")
green_button = pygame.transform.scale(green_button, (300, 100))
red_image = pygame.image.load("red_image.png")
red_image = pygame.transform.scale(red_image, (300, 100))
hero = pygame.image.load("images\hero.gif")
bullet = pygame.image.load("images\\bullet-3.gif")
# enemey = pygame.image.load("images\enemy0.png")
enemey = pygame.image.load("images\enemy1.png")
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 50)
fon = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 40)
bz_list = list()
bz_list.append(pygame.image.load("images\enemy1_down1.png"))
bz_list.append(pygame.image.load("images\enemy1_down2.png"))
bz_list.append(pygame.image.load("images\enemy1_down3.png"))
bz_list.append(pygame.image.load("images\enemy1_down4.png"))
bz_list.append(pygame.image.load("images\enemy1_down4.png"))
h_rect = hero.get_rect()
e_rect = enemey.get_rect()
b_rect = bullet.get_rect()
mx = 200  #airplant's start position
my = 600
blist = list() #我方英雄机子弹
e_blist = [] #敌机子弹
ennum = 5
bnum = 0
elist = [] #敌机
bspeed = -4
espeed = 1
e_bspeed = 3
e_bnum = []
e_jian = []
e_b_dis = 15
e_max_dis = 100
e_bztime = []
for i in range(ennum):
    elist.append([random.randint(10, 480), random.randint(-100, 0)])
    e_blist.append([])
    e_bnum.append(0)
    e_jian.append(0)
    e_bztime.append([-1, 0, 0])
h_bnum = 0
h_b_dis = 20
h_jian = 0
h_max_dis = 40
h_bztime = [-1, 0, 0]

def bullet_show(_blist, _speed, _screen):
    k = 0
    while k < len(_blist):
        _screen.blit(bullet, (_blist[k][0], _blist[k][1]))
        _blist[k][1] += _speed
        if _blist[k][1] <= 0 or _blist[k][1] >= 800:
            _blist.pop(k)                #优化子弹列表
        else:
            k += 1
    return _blist


def ad_bullet(_num, x, y, _blist, _dis, _jiange, _max_dis):  #加子弹
    if _jiange % 7 == 6:  # 6个球一次间断
        _jiange = 0
        _num = _max_dis
    elif _num == 0:
        _blist.append([x, y])
        _num = _dis
        _jiange += 1
    else:
        _num -= 1
    return _num, _blist, _jiange


def explox(bz_t, bz_image, _screen):
    if bz_t[0] >= 0:
        _screen.blit(bz_image[int(bz_t[0]/4)], (bz_t[1], bz_t[2]))
        if bz_t[0] == 19:
            bz_t[0] = -1
        else:
            bz_t[0] += 1
    return bz_t


def show_main(_screen):
    start_text0 = fon.render("欢迎进入飞机大战战场", True, (222, 22, 152))
    start_text1 = font.render("进入游戏", True, (102, 62, 112))
    _screen.blit(start_text0, (50, 100))
    while True:
        _screen.blit(green_button, (110, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        x, y, z = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if 110 <= mx <= 410 and 200 <= my <= 300:
            _screen.blit(blue_button, (110, 200))
        if x:
            break
        _screen.blit(start_text1, (150, 220))
        pygame.display.update()



screen.blit(jie_bg, (0, 0))
show_main(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
    screen.blit(bg, (0, 0))
    mx, my = pygame.mouse.get_pos()
    screen.blit(hero, (mx-h_rect.width//2, my-h_rect.height//2))
    h_bnum, blist, h_jian = ad_bullet(h_bnum, mx-b_rect.width//2, my-h_rect.height//2-b_rect.height, \
                                      blist, h_b_dis, h_jian, h_max_dis)
    for i in range(len(elist)):
        e_bztime[i] = explox(e_bztime[i], bz_list, screen)
    for i in range(len(elist)):
        screen.blit(enemey, (elist[i][0], elist[i][1]))
        flag = 0
        # for j in range(len(e_blist[i])):
        #     if mx - h_rect.width//2 < e_blist[i][j][0] + b_rect.width and \
        #     mx + h_rect.width // 2 > e_blist[i][j][0] and \
        #     my - h_rect.height // 2 < e_blist[i][j][1] + b_rect.height and \
        #     e_blist[i][j][1] < my + h_rect.height:
        #         h_bztime[0] = 0
        #         h_bztime[1] = mx - h_rect.width//2, my-h_rect.height//2
        #         h_bztime[2] = my - h_rect.height // 2
        #         h_bztime = explox(h_bztime, bz_list, screen)
        #         exit()
        if elist[i][1] > 0:
            e_bnum[i], e_blist[i], e_jian[i] = ad_bullet(e_bnum[i], elist[i][0]+e_rect.width//2 - b_rect.height//2,\
            elist[i][1]+e_rect.height, e_blist[i],  e_b_dis,e_jian[i], e_max_dis)
        e_blist[i] = bullet_show(e_blist[i], e_bspeed, screen)
        for j in range(len(blist)):
            if elist[i][0] < blist[j][0]+b_rect.width and \
                    elist[i][0] + e_rect.width > blist[j][0] and \
                    blist[j][1] < elist[i][1]+e_rect.height-20 and\
                    blist[j][1] + b_rect.height > elist[i][1]-20:
                e_bztime[i][0] = 0
                e_bztime[i][1] = elist[i][0]
                e_bztime[i][2] = elist[i][1]
                elist[i][1] = random.randint(-100, -50)
                elist[i][0] = random.randint(50, 450)
                e_bnum[i] = 0
                blist[j][1] = -200
                flag = 1
        if flag == 0:
            elist[i][1] += espeed
            if elist[i][1] > 800:
                elist[i][1] = random.randint(-100, -50)
    blist = bullet_show(blist, bspeed, screen)
    pygame.display.update()