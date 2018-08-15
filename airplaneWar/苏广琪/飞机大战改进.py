import pygame
import random
import time

pygame.init()
pygame.mixer.init()

zw = pygame.font.SysFont('SimHei', 32)
soundwav = pygame.mixer.Sound("sound\game_music.ogg")
sound1 = pygame.mixer.Sound("sound\\bullet.wav")
sound2 = pygame.mixer.Sound("sound\\button.wav")
sounde1 = pygame.mixer.Sound("sound\enemy1_down.wav")
sounde2 = pygame.mixer.Sound("sound\enemy2_down.wav")
sounde3 = pygame.mixer.Sound("sound\enemy3_down.wav")
soundeget = pygame.mixer.Sound("sound\get_bullet.wav")
soundme = pygame.mixer.Sound("sound\me_down.wav")
sound1.play()
screen = pygame.display.set_mode((400, 650))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (400, 650))
zd = pygame.image.load(r"images\bullet.png")
zd2 = pygame.image.load(r"images\bullet1.png")
hero = pygame.image.load("images\hero.gif")
palne = pygame.image.load("images\plane.png")
enemy = pygame.image.load(r"images\enemy0.png")
enemy1 = pygame.image.load(r"images\enemy1.png")
enemy2 = pygame.image.load(r"images\enemy2.png")
b1 = pygame.image.load(r"images\bomb-1.gif")
startgame = pygame.image.load(r"images\startgame.jpg")
startgame = pygame.transform.scale(startgame, (400, 650))
anniu = pygame.image.load(r"images\anniu.png")
over = pygame.image.load(r"images\gameover.png")
resume = pygame.image.load(r"images\game_resume_nor.png")
enem = pygame.image.load(r"images\bullet-2.gif")

ezd_rect = enem.get_rect()
ezd_width = ezd_rect.width
ezd_height = ezd_rect.height
over = pygame.transform.scale(over, (400, 650))
按钮 = pygame.transform.scale(anniu, (200, 200))
b1_rect = b1.get_rect()
b1_width = b1_rect.width
b1_height = b1_rect.height
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height
zd_rect = zd.get_rect()
zd_width = zd_rect.width
zd_height = zd_rect.height
zd2_rect = zd2.get_rect()
zd2_width = zd2_rect.width
zd2_height = zd2_rect.height
em_rect = enemy.get_rect()
em_width = em_rect.width
em_height = em_rect.height
em1_rect = enemy1.get_rect()
em1_width = em1_rect.width
em1_height = em1_rect.height
em2_rect = enemy2.get_rect()
em2_width = em2_rect.width
em2_height = em2_rect.height

ezd = []
zds = []
zds2 = []
zds3 = []
vis = []
vis2 = []
vis3 = []
evis = []
times = 0
list_flag = []
enemy_pos = []  # 小型机
enemy_vis = []
tis = []
enemy_pos1 = []  # 中型机
list_flag1 = []
tis1 = []
enemy_pos2 = []  # 大型机
list_flag2 = []
tis2 = []
h_vis = []
score = 0  # 得分
tt = []
bullet = 100000
b1x = -10
b1y = -10
b1t = 0
hl = 1  # 火力
spx, spy = -2, -2
life = 5
start = 0
for i in range(5):
    enemy_pos.append([random.randint(0, 400-em_width), random.randint(-100,-50)])
    list_flag.append(0)
    tis.append(0)  # 时间
    tt.append(0)
    h_vis.append(0)

for i in range(2):
    enemy_pos1.append([random.randint(0, 400 - em1_width), random.randint(-200,-100), 5])
    list_flag1.append(0)
    tis1.append(0)

for i in range(1):
    enemy_pos2.append([random.randint(0, 400 - em2_width), random.randint(-400, -300), 10])
    list_flag2.append(0)
    tis2.append(0)


def collection(bax,bay,ball_rt,blx,bly,block_rect):
    if h_vis[0] == 0:
        if bax + 10> blx and bax < blx + block_rect.width and \
                bay < bly + block_rect.height and \
                bay + 10 > bly:
            h_vis[0] = 1
            tt[0] = time.time()


def cdj(bax,bay,ball_rt,blx,bly,block_rect):
    if bax + ball_rt.width > blx and \
            bax < blx + block_rect.width and \
            bay < bly + block_rect.height and \
            bay + ball_rt.height > bly:
        bullet = time.time()
        return 1
    return 0

def FT(bx, by, spx, spy):
    if bx < 0.5 or bx > 360:
        spx = -spx
    if by < 5or by > 600:
        spy = -spy
    bx += spx
    by += spy

    return (bx, by, spx, spy)


def pz(x, y):
    vv = 0
    # 小型机
    for i in range(5):
        if list_flag[i] == 0:
            if x >= enemy_pos[i][0] and x + zd_width <= enemy_pos[i][0] + em_width and y <= enemy_pos[i][1]+em_height and y >=  enemy_pos[i][1]:
                list_flag[i] = 1
                vv = 1
                tis[i] = time.time()
                break
    # 中型机
    for i in range(2):
        if list_flag1[i] == 0:
            if x >= enemy_pos1[i][0] and x + zd_width <= enemy_pos1[i][0] + em1_width and y <= enemy_pos1[i][1]+em1_height and y >=  enemy_pos1[i][1]:
                enemy_pos1[i][2] -= 1
                vv = 1
                if enemy_pos1[i][2] == 0:
                    list_flag1[i] = 1
                    tis1[i] = time.time()
                break
    # 大型机
    for i in range(1):
        if list_flag2[i] == 0:
            if x >= enemy_pos2[i][0] and x + zd_width <= enemy_pos2[i][0] + em2_width and y <= enemy_pos2[i][1]+em2_height and y >=  enemy_pos2[i][1]:
                enemy_pos2[i][2] -= 1
                vv = 1
                if enemy_pos2[i][2] == 0:
                    list_flag2[i] = 1
                    tis2[i] = time.time()
                break
    if vv == 1:
        return 1
    else:
        return 0


init = time.time()
S_flag = 1
zhanting = -1

while True:
    # soundwav.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            zhanting = -zhanting
            screen.blit(resume,(190,300))
    if start == 0:
        screen.blit(startgame, (0, 0))
        screen.blit(按钮, (100,400))
        mx, my = pygame.mouse.get_pos()
        if mx >= 143 and mx <= 261 and my >= 485 and my <= 524:
            pressed_array = pygame.mouse.get_pressed()
            if pressed_array[0] == 1:
                start = 1
                sound2.play()

    if start == 2:
        screen.blit(over, (0, 0))
        ze = zw.render("分数：" + str(score), True, (255, 0, 0))
        screen.blit(ze, (120, 440))
    if start == 1 and zhanting == 1:
        sound1.play()
        hx, hy = pygame.mouse.get_pos()
        if times:
            times -= 1
        else:
            if hl == 1:
                zds.append([hx-10, hy-h_height/2])
            elif hl == 2:
                zds.append([hx-20, hy-h_height/2])
                zds.append([hx, hy-h_height/2])
            else:
                zds.append([hx - 20, hy - h_height / 2])
                zds.append([hx, hy - h_height / 2])
                zds2.append([hx-20, hy - h_height / 2])
                zds3.append([hx, hy - h_height / 2])
            times = 10
        screen.blit(bg, (0, 0))
        te = zw.render("得分：" + str(score), True, (0, 0, 0))
        screen.blit(te, (0, 20))
        screen.blit(palne, (0, 550))
        cheng = zw.render(" X " + str(life), True, (0, 0, 0))
        screen.blit(cheng, (30, 550))
        if life == -1:
            start = 2
        leng = len(zds)
        leng2 = len(zds2)
        leng3 = len(zds3)
        eleng = len(ezd)
        vis.clear()
        vis2.clear()
        vis3.clear()
        evis.clear()
        for i in range(eleng):
            ezd[i][1] += 5
            collection(hx, hy, h_rect, ezd[i][0], ezd[i][1], ezd_rect)
            if ezd[i][1] < 0:
                evis.append([ezd[i][0], ezd[i][1]])
            screen.blit(enem, (ezd[i][0], ezd[i][1]))
        vi= len(evis)
        for i in range(vi):
            if evis[i] in ezd:
                ezd.remove(evis[i])
        for i in range(leng3):
            zds3[i][1] -= 10
            zds3[i][0] += 4
            xx = pz(zds3[i][0], zds3[i][1])
            if xx == 1:
                vis.append([zds3[i][0], zds3[i][1]])
            if zds3[i][1] < 0:
                vis.append([zds3[i][0], zds3[i][1]])
            screen.blit(zd2, (zds3[i][0], zds3[i][1]))
        vislen3 = len(vis3)
        for i in range(vislen3):
            if vis3[i] in zds:
                zds.remove(vis3[i])

        for i in range(leng2):
            zds2[i][1] -= 10
            zds2[i][0] -= 4
            xx = pz(zds2[i][0], zds2[i][1])
            if xx == 1:
                vis2.append([zds2[i][0], zds2[i][1]])
            if zds2[i][1] < 0:
                vis2.append([zds2[i][0], zds2[i][1]])
            screen.blit(zd2, (zds2[i][0], zds2[i][1]))
        vislen2 = len(vis2)
        for i in range(vislen2):
            if vis2[i] in zds2:
                zds2.remove(vis2[i])
        for i in range(leng):
            zds[i][1] -= 10
            xx = pz(zds[i][0], zds[i][1])
            if xx == 1:
                vis.append([zds[i][0], zds[i][1]])
            if zds[i][1] < 0:
                vis.append([zds[i][0], zds[i][1]])
            screen.blit(zd, (zds[i][0], zds[i][1]))
        vislen = len(vis)
        for i in range(vislen):
            if vis[i] in zds:
                zds.remove(vis[i])

        # 英雄
        if time.time() - bullet < 0.1:
            soundme.play()
        if cdj(hx, hy, h_rect, b1x, b1y, b1_rect):
            hl += 1
            b1x, b1y = (-100, -100)
        if h_vis[0] == 0:
            screen.blit(hero, (hx-h_width/2, hy-h_height/2))
        # 小型机敌人
        for i in range(5):
            if list_flag[i] == 0:
                collection(hx, hy, h_rect, enemy_pos[i][0], enemy_pos[i][1], em_rect)
                screen.blit(enemy, (enemy_pos[i][0], enemy_pos[i][1]))
            if enemy_pos[i][1] < 650:
                enemy_pos[i][1] += 1
            else:
                enemy_pos[i][0] = random.randint(0, 400-em_width)
                enemy_pos[i][1] = random.randint(-100, -50)
        # 中型机敌人
        for i in range(2):
            #zs(enemy_pos1[i][0], enemy_pos1[i][1], hx, hy)
            if list_flag1[i] == 0:
                collection(hx, hy, h_rect, enemy_pos1[i][0], enemy_pos1[i][1], em1_rect)
                screen.blit(enemy1, (enemy_pos1[i][0], enemy_pos1[i][1]))
            if enemy_pos1[i][2] == 5:
                pygame.draw.line(screen, (255, 0, 0), (enemy_pos1[i][0]+7, enemy_pos1[i][1] + em1_height+5),\
                                 (enemy_pos1[i][0] + 57, enemy_pos1[i][1] + em1_height+5), 3)
            else:
                pygame.draw.line(screen, (255, 0, 0), (enemy_pos1[i][0] + 7, enemy_pos1[i][1] + em1_height + 5), \
                                 (enemy_pos1[i][0] + 57, enemy_pos1[i][1] + em1_height + 5), 3)
                pygame.draw.line(screen, (144, 144, 144), (enemy_pos1[i][0] + 7 + enemy_pos1[i][2] * 10, enemy_pos1[i][1] + em1_height + 5), \
                                 (enemy_pos1[i][0] + 57, enemy_pos1[i][1] + em1_height + 5), 3)
            if enemy_pos1[i][1] < 650:
                enemy_pos1[i][1] += 1
                if enemy_pos1[i][1] > 1 and enemy_pos1[i][1] < 3 :
                    ezd.append([enemy_pos1[i][0] + 25, enemy_pos1[i][1] + em1_height ])
            else:
                enemy_pos1[i][0] = random.randint(0, 400-em1_width)
                enemy_pos1[i][1] = random.randint(-200, -50)
                enemy_pos1[i][2] = 5
        # 大型机
        for i in range(1):
            #pzzs(enemy_pos2[i][0], enemy_pos2[i][1], hx, hy)
            if list_flag2[i] == 0:
                collection(hx, hy, h_rect, enemy_pos2[i][0], enemy_pos2[i][1], em2_rect)
                screen.blit(enemy2, (enemy_pos2[i][0], enemy_pos2[i][1]))
                pygame.draw.line(screen, (255, 0, 0), (enemy_pos2[i][0] + 30, enemy_pos2[i][1] + em2_height + 5), \
                                 (enemy_pos2[i][0] + 130, enemy_pos2[i][1] + em2_height + 5), 3)
            if enemy_pos2[i][2] == 10:
                pygame.draw.line(screen, (255, 0, 0), (enemy_pos2[i][0] + 30, enemy_pos2[i][1] + em2_height+5),\
                                 (enemy_pos2[i][0] + 130, enemy_pos2[i][1] + em2_height+5), 3)
            else:
                pygame.draw.line(screen, (255, 0, 0), (enemy_pos2[i][0] + 30, enemy_pos2[i][1] + em2_height + 5), \
                                 (enemy_pos2[i][0] + 130, enemy_pos2[i][1] + em2_height + 5), 3)
                pygame.draw.line(screen, (144, 144, 144), (enemy_pos2[i][0] + 30 + enemy_pos2[i][2] * 10, enemy_pos2[i][1] + em2_height + 5), \
                                 (enemy_pos2[i][0] + 130, enemy_pos2[i][1] + em2_height + 5), 3)
            if enemy_pos2[i][1] < 650:
                if enemy_pos2[i][1] > -100 and enemy_pos2[i][1] < -90 :
                    ezd.append([enemy_pos2[i][0] + 100, enemy_pos2[i][1]+285])
                enemy_pos2[i][1] += 1
            else:
                enemy_pos2[i][0] = random.randint(0, 400-em2_width)
                enemy_pos2[i][1] = random.randint(-400, -300)
                enemy_pos2[i][2] = 10
        if h_vis[0]:
            if time.time()-tt[0]> 0 and time.time()-tt[0] < 0.2:
                soundme.play()
                h1 = pygame.image.load(r"images\hero_blowup_n1.png")
                screen.blit(h1, (hx - h_width / 2, hy - h_height / 2))
            elif time.time()-tt[0] < 0.4:
                h2 = pygame.image.load(r"images\hero_blowup_n2.png")
                screen.blit(h2, (hx - h_width / 2, hy - h_height / 2))
            elif time.time()-tt[0] < 0.6:
                h3 = pygame.image.load(r"images\hero_blowup_n3.png")
                screen.blit(h3, (hx - h_width / 2, hy - h_height / 2))
            elif time.time()-tt[0] < 0.8:
                h4 = pygame.image.load(r"images\hero_blowup_n4.png")
                screen.blit(h4, (hx - h_width / 2, hy - h_height / 2))
            else:
                screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))
                h_vis[0] = 0
                hl = 1
                life -= 1

        if time.time() - b1t < 20:
            screen.blit(b1, (b1x, b1y))
            b1x, b1y, spx, spy = FT(b1x, b1y, spx, spy)



    # 爆炸小型机
        for i in range(5):
            if list_flag[i]:
                if time.time()-tis[i] > 0 and time.time()-tis[i] < 0.1:
                    sounde1.play()
                    e1 = pygame.image.load(r"images\enemy0_down1.png")
                    screen.blit(e1, (enemy_pos[i][0], enemy_pos[i][1]))
                elif time.time()-tis[i] < 0.2:
                    e2 = pygame.image.load(r"images\enemy0_down2.png")
                    screen.blit(e2, (enemy_pos[i][0], enemy_pos[i][1]))
                elif time.time()-tis[i] < 0.3:
                    e3 = pygame.image.load(r"images\enemy0_down3.png")
                    screen.blit(e3, (enemy_pos[i][0], enemy_pos[i][1]))
                elif time.time()-tis[i] < 0.4:
                    e4 = pygame.image.load(r"images\enemy0_down4.png")
                    screen.blit(e4, (enemy_pos[i][0], enemy_pos[i][1]))
                else:
                    enemy_pos[i][0] = random.randint(0, 400 - em_width)
                    enemy_pos[i][1] = random.randint(-100, -50)
                    list_flag[i] = 0
                    score += 2
        # 爆炸中型机
        for i in range(2):
            if list_flag1[i]:
                if time.time()-tis1[i] > 0 and time.time()-tis1[i] < 0.1:
                    sounde2.play()
                    e1 = pygame.image.load(r"images\enemy1_down1.png")
                    screen.blit(e1, (enemy_pos1[i][0], enemy_pos1[i][1]))
                elif time.time()-tis1[i] < 0.2:
                    e2 = pygame.image.load(r"images\enemy1_down2.png")
                    screen.blit(e2, (enemy_pos1[i][0], enemy_pos1[i][1]))
                elif time.time()-tis1[i] < 0.3:
                    e3 = pygame.image.load(r"images\enemy1_down3.png")
                    screen.blit(e3, (enemy_pos1[i][0], enemy_pos1[i][1]))
                elif time.time()-tis1[i] < 0.4:
                    e4 = pygame.image.load(r"images\enemy1_down4.png")
                    screen.blit(e4, (enemy_pos1[i][0], enemy_pos1[i][1]))
                else:
                    enemy_pos1[i][0] = random.randint(0, 400 - em1_width)
                    enemy_pos1[i][1] = random.randint(-100, -50)
                    enemy_pos1[i][2] = 5
                    list_flag1[i] = 0
                    score += 5
        # 爆炸大型机
        for i in range(1):
            if list_flag2[i]:
                if time.time()-tis2[i] > 0 and time.time()-tis2[i] < 0.1:
                    sounde3.play()
                    e1 = pygame.image.load(r"images\enemy2_down1.png")
                    screen.blit(e1, (enemy_pos2[i][0], enemy_pos2[i][1]))
                elif time.time()-tis2[i] < 0.2:
                    e2 = pygame.image.load(r"images\enemy2_down2.png")
                    screen.blit(e2, (enemy_pos2[i][0], enemy_pos2[i][1]))
                elif time.time()-tis2[i] < 0.3:
                    e3 = pygame.image.load(r"images\enemy2_down3.png")
                    screen.blit(e3, (enemy_pos2[i][0], enemy_pos2[i][1]))
                elif time.time()-tis2[i] < 0.4:
                    e4 = pygame.image.load(r"images\enemy2_down4.png")
                    screen.blit(e4, (enemy_pos2[i][0], enemy_pos2[i][1]))
                else:
                    b1x = enemy_pos2[i][0]
                    b1y = enemy_pos2[i][1]
                    b1t = time.time()
                    enemy_pos2[i][0] = random.randint(0, 400 - em2_width)
                    enemy_pos2[i][1] = random.randint(-400, -300)
                    enemy_pos2[i][2] = 10
                    list_flag2[i] = 0
                    score += 10
    pygame.display.update()