import pygame
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((495, 800))
background = pygame.image.load("images\\background.png")        #导入背景
background = pygame.transform.scale(background, (495, 800))
yun = pygame.image.load("images\\cloud.png")
name = pygame.image.load("images\\name.png")                    #导入开始界面图片
name = pygame.transform.scale(name, (343, 67))
startgame = pygame.image.load("images\\开始游戏.png")
startgame = pygame.transform.scale(startgame, (370, 80))
shuomingshu = pygame.image.load("images\\操作界面.png")
shuomingshu = pygame.transform.scale(shuomingshu, (370, 80))
exitgame = pygame.image.load("images\\退出游戏.png")
exitgame = pygame.transform.scale(exitgame, (370, 80))
fanhui = pygame.image.load("images\\返回.png")
fanhui = pygame.transform.scale(fanhui, (270, 60))
pause = pygame.image.load("images\\game_pause_nor.png")             #导入暂停图标
resumegame = pygame.image.load("images\\game_resume_nor.png")       #导入继续图标
hero = pygame.image.load("images\hero.gif")                     #导入英雄机
hero = pygame.transform.scale(hero, (50, 50))
herodown1 = pygame.image.load("images\\hero_blowup_n1.png")     #英雄机炸掉
herodown2 = pygame.image.load("images\\hero_blowup_n2.png")
herodown3 = pygame.image.load("images\\hero_blowup_n3.png")
herodown4 = pygame.image.load("images\\hero_blowup_n4.png")
herodown1 = pygame.transform.scale(herodown1, (50, 50))
herodown2 = pygame.transform.scale(herodown2, (50, 50))
herodown3 = pygame.transform.scale(herodown3, (50, 50))
herodown4 = pygame.transform.scale(herodown4, (50, 50))
bullet = pygame.image.load("images\\bullet.png")                #导入子弹
enemy0 = pygame.image.load("images\\enemy0.png")                #导入敌人0
enemy0 = pygame.transform.scale(enemy0, (50, 50))
enemydown01 = pygame.image.load("images\\enemy0_down1.png")
enemydown02 = pygame.image.load("images\\enemy0_down2.png")
enemydown03 = pygame.image.load("images\\enemy0_down3.png")
enemydown04 = pygame.image.load("images\\enemy0_down4.png")
enemydown01 = pygame.transform.scale(enemydown01, (50, 50))
enemydown02 = pygame.transform.scale(enemydown02, (50, 50))
enemydown03 = pygame.transform.scale(enemydown03, (50, 50))
enemydown04 = pygame.transform.scale(enemydown04, (50, 50))
enemy1 = pygame.image.load("images\\enemy1.png")                #导入敌人1
enemy1 = pygame.transform.scale(enemy1, (60, 60))
enemydown11 = pygame.image.load("images\\enemy1_down1.png")
enemydown12 = pygame.image.load("images\\enemy1_down2.png")
enemydown13 = pygame.image.load("images\\enemy1_down3.png")
enemydown14 = pygame.image.load("images\\enemy1_down4.png")
enemydown11 = pygame.transform.scale(enemydown11, (60, 60))
enemydown12 = pygame.transform.scale(enemydown12, (60, 60))
enemydown13 = pygame.transform.scale(enemydown13, (60, 60))
enemydown14 = pygame.transform.scale(enemydown14, (60, 60))
enemy2 = pygame.image.load("images\\enemy2.png")
enemy2 = pygame.transform.scale(enemy2, (60, 60))
enemydown21 = pygame.image.load("images\\enemy2_down1.png")
enemydown22 = pygame.image.load("images\\enemy2_down2.png")
enemydown23 = pygame.image.load("images\\enemy2_down3.png")
enemydown24 = pygame.image.load("images\\enemy2_down4.png")
enemydown21 = pygame.transform.scale(enemydown21, (80, 80))
enemydown22 = pygame.transform.scale(enemydown22, (80, 80))
enemydown23 = pygame.transform.scale(enemydown23, (80, 80))
enemydown24 = pygame.transform.scale(enemydown24, (80, 80))
dijibiaoti = pygame.image.load("images\\敌机百科.PNG")
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)       #导入字体
font1 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 25)       #导入字体

e_rect0 = enemy0.get_rect()     #获得敌机长宽
e_rect1 = enemy1.get_rect()
e_rect2 = enemy2.get_rect()
ene_blood = 0

h_rect = hero.get_rect()        #获得英雄机长宽
h_width = h_rect.width
h_height = h_rect.height
b_rect = bullet.get_rect()      #获得子弹长宽
b_width = b_rect.width
b_height = b_rect.height

hx = 100                            #设定英雄机初始位置
hy = 100
b_x = []                            #设定子弹位置
b_y = []
bx = hx
by = hy
speed = 2
m = 0
#-------------------------------------------------敌机百科------------------------------------------------------------
list_enemy = []
kind = enemy0
kindname = "enemy0"
e_locx = random.randint(100, 400)
e_locy = 0
bomb1 = enemydown01
bomb2 = enemydown02
bomb3 = enemydown03
bomb4 = enemydown04
e_height = e_rect0.height
e_width = e_rect0.width
count = 0
dict_enemy = {"型号": kind, "型号名": kindname, "位置x": e_locx, "位置y": e_locy, "爆炸1": bomb1,
              "爆炸2": bomb2, "爆炸3": bomb3, "爆炸4": bomb4, "计数": count, "宽度": e_width,
              "高度": e_height, "血量": 500}
list_enemy.append(dict_enemy)

kind = enemy1
kindname = "enemy1"
e_locx = random.randint(100, 400)
e_locy = 0
bomb1 = enemydown11
bomb2 = enemydown12
bomb3 = enemydown13
bomb4 = enemydown14
e_height = e_rect1.height
e_width = e_rect1.width
count = 0
dict_enemy = {"型号": kind, "型号名": kindname, "位置x": e_locx, "位置y": e_locy, "爆炸1": bomb1,
              "爆炸2": bomb2, "爆炸3": bomb3, "爆炸4": bomb4, "计数": count, "宽度": e_width,
              "高度": e_height, "血量": 800}
list_enemy.append(dict_enemy)

kind = enemy2
kindname = "enemy2"
e_locx = 200
e_locy = -40
bomb1 = enemydown21
bomb2 = enemydown22
bomb3 = enemydown23
bomb4 = enemydown24
e_height = e_rect2.height
e_width = e_rect2.width
count = 1
dict_enemy = {"型号": kind, "型号名": kindname, "位置x": e_locx, "位置y": e_locy, "爆炸1": bomb1,
              "爆炸2": bomb2, "爆炸3": bomb3, "爆炸4": bomb4, "计数": count, "宽度": e_width,
              "高度": e_height, "血量": 1000}
list_enemy.append(dict_enemy)


#-------------------------------------------------敌机百科------------------------------------------------------------
dijifinal = []
ene_speedx = []
ene_speedy = []
#确定最后的敌机位置

def zantingjiemian(time, score, countup, yunx, yuny, speedx, speedy):
    while True:                                                         #暂停界面
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                inx, iny = pygame.mouse.get_pos()
                if 250 <= inx <= 250 + 42 and 400 <= iny <= 400 + 45:
                    mainscreen(time, score, countup, yunx, yuny, speedx, speedy)
                if 205 <= inx <= 205 + 60 and 743 <= iny <= 743 + 30:
                    score = 0
                    kaishijiemian(time, score, countup, yunx, yuny, speedx, speedy)
        screen.blit(background, (0, 0))                                         #画屏幕
        cuita = font1.render("(ノ￣▽￣)不来玩吗大爷", True, [238, 0, 238])
        zaicui = font1.render("还不来吗大爷(*/ω＼*)", True, [179, 238, 58])
        yonglicui = font1.render("真的还不来吗大爷(～￣▽￣)～ ", True, [255, 106, 106])
        screen.blit(resumegame, (250, 400))
        screen.blit(name, (78, 200))
        screen.blit(fanhui, (100, 730))
        pygame.draw.rect(screen, [255, 255, 255], [205, 743, 60, 30], 2)
        countup += 1                                                            #骚一波
        if countup >= 200:
            screen.blit(cuita, (78, 500))
        if countup >= 400:
            screen.blit(zaicui, (100, 600))
        if countup >= 600:
            screen.blit(yonglicui, (120, 700))
        screen.blit(yun, (yunx, yuny))                                          #云
        if yunx < 0:
            speedx = 1
        if yunx > 495 - 51:
            speedx = -1
        if yuny < 0:
            speedy = 1
        if yuny > 800 - 32:
            speedy = -1
        yunx += speedx
        yuny += speedy
        pygame.display.update()

def jieshujiemiena(time, score, countup, yunx, yuny, speedx, speedy):
    while True:                                                                    #结束界面
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:  # 监听器
                inx, iny = pygame.mouse.get_pos()
                if 180 <= inx <= 180 + 25 and 480 <= iny <= 480 + 25:
                    score = 0
                    mainscreen(time, score, countup, yunx, yuny, speedx, speedy)
                if 300 <= inx <= 300 + 25 and 480 <= iny <= 480 + 25:
                    score = 0
                    kaishijiemian(time, score, countup, yunx, yuny, speedx, speedy)
        screen.blit(background, (0, 0))
        finalscore = font.render("GAMEOVER", True, [0, 0, 0])
        caozuo = font1.render("是否继续", True, [0, 0, 0])
        caozuo1 = font1.render("是", True, [0, 0, 0])
        caozuo2 = font1.render("否", True, [0, 0, 0])
        screen.blit(finalscore, (200, 180))
        screen.blit(caozuo, (200, 380))
        screen.blit(caozuo1, (180, 480))
        screen.blit(caozuo2, (300, 480))
        screen.blit(name, (78, 200))
        screen.blit(yun, (yunx, yuny))
        if yunx < 0:
            speedx = 1
        if yunx > 495 - 51:
            speedx = -1
        if yuny < 0:
            speedy = 1
        if yuny > 800 - 32:
            speedy = -1
        yunx += speedx
        yuny += speedy
        pygame.display.update()

def kaishijiemian(time, score, countup, yunx, yuny, speedx, speedy):
    while True:                                                 #开始界面
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:                   #监听器
                inx, iny = pygame.mouse.get_pos()
                if 167 <= inx <= 167 + 170 and 400 <= iny <= 400 + 50:
                    mainscreen(time, score, countup, yunx, yuny, speedx, speedy)
                if 167 <= inx <= 167 + 170 and 500 <= iny <= 500 + 50:
                    caozuojiemian(time, score, countup, yunx, yuny, speedx, speedy)
                if 167 <= inx <= 167 + 170 and 600 <= iny <= 600 + 50:
                    exit(0)
        screen.blit(background, (0, 0))                                     #↓画界面↓
        screen.blit(name, (78, 200))
        pygame.draw.rect(screen, [255, 255, 255], [167, 400, 170, 50], 2)
        pygame.draw.rect(screen, [255, 255, 255], [167, 500, 170, 50], 2)
        pygame.draw.rect(screen, [255, 255, 255], [167, 600, 170, 50], 2)
        screen.blit(startgame, (70, 390))
        screen.blit(shuomingshu, (70, 490))
        screen.blit(exitgame, (70, 590))
        screen.blit(yun, (yunx, yuny))
        if yunx < 0:
            speedx = 1
        if yunx > 495 - 51:
            speedx = -1
        if yuny < 0:
            speedy = 1
        if yuny > 800 - 32:
            speedy = -1
        yunx += speedx
        yuny += speedy
        pygame.display.update()

def caozuojiemian(time, score, countup, yunx, yuny, speedx, speedy):
    while True:                                                 #说明书界面
        for event in pygame.event.get():                        #监听器
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                inx, iny = pygame.mouse.get_pos()
                if 205 <= inx <= 205 + 60 and 743 <= iny <= 743 + 30:
                    kaishijiemian(time, score, countup, yunx, yuny, speedx, speedy)
        screen.blit(background, (0, 0))                                     #↓画界面↓
        screen.blit(dijibiaoti, (0, 0))
        screen.blit(enemy0, (60, 120))
        screen.blit(enemy1, (60, 310))
        screen.blit(enemy2, (60, 500))
        test_ene01 = font.render(list_enemy[0]["型号名"], True, [0, 0, 0])
        test_ene02 = font.render(str(list_enemy[0]["血量"]), True, [0, 0, 0])
        test_ene11 = font.render(list_enemy[1]["型号名"], True, [0, 0, 0])
        test_ene12 = font.render(str(list_enemy[1]["血量"]), True, [0, 0, 0])
        test_ene21 = font.render(list_enemy[2]["型号名"], True, [0, 0, 0])
        test_ene22 = font.render(str(list_enemy[2]["血量"]), True, [0, 0, 0])
        test_xinghao = font1.render("型号：", True, [0, 0, 0])
        test_xueliang = font1.render("血量：", True, [0, 0, 0])
        test_jieshao = font1.render("介绍：干就是了那么多废话", True, [0, 0, 0])
        screen.blit(test_xinghao, (135, 100))
        screen.blit(test_xueliang, (135, 140))
        screen.blit(test_jieshao, (135, 180))
        screen.blit(test_ene01, (200, 98))
        screen.blit(test_ene02, (200, 138))
        screen.blit(test_xinghao, (135, 300))
        screen.blit(test_xueliang, (135, 340))
        screen.blit(test_jieshao, (135, 380))
        screen.blit(test_ene11, (200, 298))
        screen.blit(test_ene12, (200, 338))
        screen.blit(test_xinghao, (135, 500))
        screen.blit(test_xueliang, (135, 540))
        screen.blit(test_jieshao, (135, 580))
        screen.blit(test_ene21, (200, 498))
        screen.blit(test_ene22, (200, 538))
        test_caozuo = font1.render("鼠标操作不用教了吧", True, [0, 0, 0])
        screen.blit(test_caozuo, (100, 700))
        screen.blit(fanhui, (100, 730))
        pygame.draw.rect(screen, [255, 255, 255], [205, 743, 60, 30], 2)
        screen.blit(yun, (yunx, yuny))
        if yunx < 0:
            speedx = 1
        if yunx > 495 - 51:
            speedx = -1
        if yuny < 0:
            speedy = 1
        if yuny > 800 - 32:
            speedy = -1
        yunx += speedx
        yuny += speedy
        pygame.display.update()

def mainscreen(time, score, countup, yunx, yuny, speedx, speedy):
    #游戏界面
    for i in range(20):                                     #确定敌机位置
        ran_de = random.randint(0, 2)
        dijifinal.append(list_enemy[ran_de])
        ene_speedx.append(0.2)
        ene_speedy.append(0.2)
    for i in range(20):
        dijifinal[i]["位置x"] = random.randint(100, 310)
        dijifinal[i]["位置y"] = random.randint(-1600, -20)

    while True:
        for event in pygame.event.get():                        #监控事件
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                inx, iny = pygame.mouse.get_pos()
                if 440 <= inx <= 440 + 42 and 10 <= iny <= 10 + 45:
                    zantingjiemian(time, score, countup, yunx, yuny, speedx, speedy)
        hx, hy = pygame.mouse.get_pos()

        if time:                                                #子弹填装
            time -= 1
        else:
            b_x.append(hx - b_rect.width / 2)
            b_y.append(hy - b_rect.height / 2)
            time = 10
        screen.blit(background, (0, 0))                        #打印背景
        screen.blit(hero, (hx - h_width / 2, hy - h_height / 2)) #打印英雄机
        if score < 0:
            jieshujiemiena(time, score, countup, yunx, yuny, speedx, speedy)
        for i in range(20):                                     #打印敌机 & 移动
            xinghao = dijifinal[i]['型号']
            x = dijifinal[i]["位置x"]
            y = dijifinal[i]["位置y"]
            screen.blit(xinghao, (x, y))
            if dijifinal[i]["位置y"] < 800:
                dijifinal[i]["位置y"] += ene_speedy[i]
            else:
                dijifinal[i]["位置y"] = -1000
                dijifinal[i]["位置x"] = random.randint(100, 310)
                if dijifinal[i]["型号名"] == "enemy0":
                    score -= 10
                if dijifinal[i]["型号名"] == "enemy1":
                    score -= 30
                if dijifinal[i]["型号名"] == "enemy2":
                    score -= 50
            if dijifinal[i]["位置x"] < 100 or dijifinal[i]["位置x"] > 310:
                ene_speedx[i] = -ene_speedx[i]
            dijifinal[i]["位置x"] += ene_speedx[i]

        score_test = font.render("SCORE=", True, [255, 255, 255])   #画分数
        test_score = font.render(str(score), True, [255, 255, 255])
        screen.blit(score_test, (10, 10))
        screen.blit(test_score, (130, 10))
        screen.blit(pause, (440, 10))                               #画暂停

        for k in range(len(b_x)):                                   #打击敌人检测
            screen.blit(bullet, (b_x[k], b_y[k]))
            b_y[k] -= speed * 2
            for j in range(20):
                if dijifinal[j]["位置x"] < b_x[k] < dijifinal[j]["位置x"] + dijifinal[j]["宽度"] and \
                        dijifinal[j]["位置y"] < b_y[k] < dijifinal[j]["位置y"] + float(dijifinal[j]["宽度"]):
                    if 0 <= dijifinal[j]["位置y"] <= 800:
                        dijifinal[j]["计数"] = dijifinal[j]["计数"] + 1
                        if 2 <= dijifinal[j]["计数"] < dijifinal[j]["血量"] / 3:
                            screen.blit(dijifinal[j]["爆炸1"], (dijifinal[j]["位置x"], dijifinal[j]["位置y"]))
                        if dijifinal[j]["血量"] / 3 <= dijifinal[j]["计数"] < dijifinal[j]["血量"] / 2:
                            screen.blit(dijifinal[j]["爆炸2"], (dijifinal[j]["位置x"], dijifinal[j]["位置y"]))
                        if dijifinal[j]["血量"] * 2 <= dijifinal[j]["计数"] < dijifinal[j]["血量"] * 2 / 3:
                            screen.blit(dijifinal[j]["爆炸3"], (dijifinal[j]["位置x"], dijifinal[j]["位置y"]))
                        if dijifinal[j]["血量"] * 2 / 3<= dijifinal[j]["计数"] < dijifinal[j]["血量"]:
                            screen.blit(dijifinal[j]["爆炸4"], (dijifinal[j]["位置x"], dijifinal[j]["位置y"]))
                        if dijifinal[j]["计数"] == dijifinal[j]["血量"]:
                            dijifinal[j]["位置x"] = random.randint(100, 400)
                            dijifinal[j]["位置y"] = random.randint(-30, -5)
                            dijifinal[j]["计数"] = 0
                            if dijifinal[j]["型号名"] == "enemy0":
                                score += 10
                            if dijifinal[j]["型号名"] == "enemy1":
                                score += 30
                            if dijifinal[j]["型号名"] == "enemy2":
                                score += 50
        pygame.display.update()

if __name__ == '__main__':
    time = 10
    score = 0
    countup = 0
    yunx = random.randint(100, 400)
    yuny = random.randint(100, 400)
    speedx = 1
    speedy = 1
    kaishijiemian(time, score, countup, yunx, yuny, speedx, speedy)