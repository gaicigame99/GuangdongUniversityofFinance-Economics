import pygame
import os
import sys
pygame.init()
screen = pygame.display.set_mode((600,600))
font = pygame.font.Font("C:\Windows\Fonts\FZSTK.TTF", 100)
font1 = pygame.font.Font("C:\Windows\Fonts\FZSTK.TTF", 20)
t_1 = pygame.transform.scale(pygame.image.load("1.jpg"),(100,100))
t_2 = pygame.transform.scale(pygame.image.load("2.jpg"),(100,100))
t_3 = pygame.transform.scale(pygame.image.load("3.jpg"),(100,100))
t_4 = pygame.transform.scale(pygame.image.load("4.jpg"),(100,100))

# file = open(r'贪吃蛇.py')

class interface_button(object):
    def __init__(self,screen,button,button_x,button_y):
        self.screen = screen
        self.button = button
        self.x = button_x
        self.y = button_y
        self.rect = button.get_rect()
    def show(self):
        self.screen.blit(self.button,(self.x,self.y))
    def move(self):
        if self.y > -self.rect.height:
            self.y -=3
    # 判读鼠标点击
    def press(self,mouse_x,mouse_y,mouse_press):
        if self.x < mouse_x < self.rect.width + self.x and self.y < mouse_y < self.y + self.rect.height and mouse_press:
            return True
        else:
            return False


t1 = interface_button(screen,t_1,170,230,)
t2 = interface_button(screen,t_1,370,230,)
t3 = interface_button(screen,t_1,170,410,)
t4 = interface_button(screen,t_1,370,410,)

screen.blit(font1.render("飞机大战", True, (255, 255, 255)), (180,330 ))
screen.blit(font1.render("贪吃蛇", True, (255, 255, 255)), (390,330 ))
screen.blit(font1.render("弹一弹", True, (255, 255, 255)), (190,510 ))

while True:
    x,y = pygame.mouse.get_pos()
    z,m,n = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(font.render("游戏平台",True,(255,255,255)),(100,10))
    pygame.draw.line(screen,(255,255,255),(0,150),(600,150))
    t1.show()
    t2.show()
    t3.show()
    t4.show()

    if t1.press(x,y,z):
        import pygame
        import random

        pygame.init()  # 背景及字体
        screen = pygame.display.set_mode((600, 1000))
        background = pygame.image.load(r"images\background.png")
        background = pygame.transform.scale(background, (600, 1000))
        RED_COLOR = (255, 0, 0)

        hero = pygame.image.load("images\hero.gif")  # 自己那架飞机
        hx = 100
        hy = 800
        h_rect = hero.get_rect()
        h_width = h_rect.width
        h_height = h_rect.height
        h_blood = 5
        h1x = 500  # 多人模式第二架
        h1y = 800
        h1_blood = 5
        protect = 0
        protect1 = 0
        protect_speed = 0
        protect1_speed = 0

        bullet1 = pygame.image.load(r"images\bullet-1.gif")  # 子弹
        b_rect = bullet1.get_rect()
        b_width = b_rect.width
        b_height = b_rect.height
        b_x = []
        b_y = []
        b1_x = []
        b1_y = []
        b_speed = 6
        b_v = 20  # 发射频率
        time = b_v
        b1_speed = 6
        b1_v = 20
        time1 = b1_v

        enemy_bullet = pygame.image.load(r"images\bullet.png")
        enemy = pygame.image.load("images\enemy0.png")  # 小敌人
        enemy_x = []
        enemy_y = []
        enemy_x_speed = []
        enemy_y_speed = []

        enemy_time = 40
        enemy1_bullet_speed = 1
        enemy1 = pygame.image.load("images\enemy1.png")  # 中敌人
        enemy1_x = []
        enemy1_y = []
        blood_enemy1 = []
        enemy1_x_speed = []
        enemy1_y_speed = []
        enemy1_bullet = []

        enemy2_bullet_speed = 1
        enemy2 = pygame.image.load("images\enemy2.png")  # 大敌人
        enemy2_x = []
        enemy2_y = []
        blood_enemy2 = []
        enemy2_x_speed = []
        enemy2_y_speed = []
        enemy2_bullet = []

        font = pygame.font.Font("C:\Windows\Fonts\Verdana.ttf", 30)  # 字体
        PURPLE_COLOR = (100, 100, 200)
        score = 0

        kaishijiemian = pygame.image.load("images\kaishijiemian.png")  # 开始界面
        kaishijiemian = pygame.transform.scale(kaishijiemian, (600, 1000))
        kaishi_x = 0
        kaishi_y = 0
        kaishi_speed = 0
        button_speed = 0

        # 单人多人
        danren_button = pygame.image.load('images\danren.png')
        duoren_button = pygame.image.load('images\duoren.png')
        danren_button_x = 100
        danren_button_y = 700
        duoren_button_x = 375
        duoren_button_y = 700
        danren_button_rect = danren_button.get_rect()
        duoren_button_rect = duoren_button.get_rect()

        e_rect = enemy.get_rect()  # 敌人像素
        e_width = e_rect.width
        e_height = e_rect.height
        e_rect1 = enemy1.get_rect()
        e_width1 = e_rect1.width
        e_height1 = e_rect1.height
        e_rect2 = enemy2.get_rect()
        e_width2 = e_rect2.width
        e_height2 = e_rect2.height

        baozha1 = pygame.image.load("images\enemy0_down1.png")  # 爆炸图片
        baozha2 = pygame.image.load("images\enemy0_down2.png")
        baozha3 = pygame.image.load("images\enemy0_down3.png")
        baozha4 = pygame.image.load("images\enemy0_down4.png")
        baozha5 = pygame.image.load("images\enemy1_down1.png")
        baozha6 = pygame.image.load("images\enemy1_down2.png")
        baozha7 = pygame.image.load("images\enemy1_down3.png")
        baozha8 = pygame.image.load("images\enemy1_down4.png")
        baozha9 = pygame.image.load("images\enemy2_down1.png")
        baozha10 = pygame.image.load("images\enemy2_down2.png")
        baozha11 = pygame.image.load("images\enemy2_down3.png")
        baozha12 = pygame.image.load("images\enemy2_down4.png")
        baozha13 = pygame.image.load("images\enemy2_down5.png")
        baozha14 = pygame.image.load("images\enemy2_down6.png")

        baozha1_x = []
        baozha1_y = []
        baozha2_x = []
        baozha2_y = []
        baozha3_x = []
        baozha3_y = []
        chixushijian1 = []
        chixushijian2 = []
        chixushijian3 = []

        tuichu = pygame.image.load("images\quit_sel.png")
        tuichu_rect = tuichu.get_rect()  # 退出按钮设定
        tuichu_x = 230
        tuichu_y = 700
        flag = 0

        buji1 = pygame.image.load(r"images\bomb-1.gif")  # 补给初始化
        buji2 = pygame.image.load(r"images\bomb-2.gif")
        buji1_x = []
        buji1_y = [-130, -900, -1800, -2100]
        buji1_rect = buji1.get_rect()
        buji1_speed = 1
        buji2_x = []
        buji2_y = [-200, -800, -1500, -1900]
        buji2_rect = buji2.get_rect()
        buji2_speed = 1
        zhadan = 0

        for i in range(4):
            a = random.randint(50, 550)
            buji1_x.append(a)
            b = random.randint(50, 550)
            buji2_x.append(b)

        back_music = pygame.mixer.Sound("sound\game_music.ogg")  # 音乐
        bullet1_music = pygame.mixer.Sound(r"sound\bullet.wav")
        enemy_music = pygame.mixer.Sound(r"sound\enemy1_down.wav")
        enemy1_music = pygame.mixer.Sound(r"sound\enemy1_down.wav")
        enemy2_music = pygame.mixer.Sound(r"sound\enemy1_down.wav")
        back_music.play()

        d = 1
        game_start = 165
        game_start_speed = 0
        mode = 0

        for i in range(15):  # 小敌人初始坐标
            a = random.randint(10, 550)
            enemy_x.append(a)
            b = random.randint(-150, -100)
            enemy_y.append(b * (i + 1))
            enemy_x_speed.append(1)
            enemy_y_speed.append(1)
        for i in range(8):  # 中敌人初始坐标
            a = random.randint(10, 550)
            enemy1_x.append(a)
            b = random.randint(-300, -200)
            enemy1_y.append(b * (i + 1))
            enemy1_x_speed.append(1)
            enemy1_y_speed.append(1)
            blood_enemy1.append(7)
        for i in range(5):  # 大敌人初始坐标
            a = random.randint(10, 550)
            enemy2_x.append(a)
            b = random.randint(-500, -400)
            enemy2_y.append(b * (i + 1))
            enemy2_x_speed.append(1)
            enemy2_y_speed.append(1)
            blood_enemy2.append(15)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if (game_start > 0):  # 开始封面
                screen.blit(background, (0, 0))
            game_start -= game_start_speed
            kaishi_y -= kaishi_speed
            screen.blit(kaishijiemian, (kaishi_x, kaishi_y))

            danren = font.render('SinglePlayer', True, PURPLE_COLOR)
            duoren = font.render('MultiPlayer', True, PURPLE_COLOR)
            screen.blit(danren, (danren_button_x - 10, danren_button_y + 130))
            screen.blit(duoren, (duoren_button_x - 10, duoren_button_y + 130))
            screen.blit(danren_button, (danren_button_x, danren_button_y))
            screen.blit(duoren_button, (duoren_button_x, duoren_button_y))
            danren_button_y -= button_speed
            duoren_button_y -= button_speed
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click, b, c = pygame.mouse.get_pressed()

            if (mouse_x > danren_button_x and mouse_x < danren_button_x + danren_button_rect.width and  # 单人模式
                    mouse_y > danren_button_y and mouse_y < danren_button_y + danren_button_rect.height):
                if (click == 1):
                    kaishi_speed = 15
                    button_speed = 15
                    game_start_speed = 2
                    mode = 1

            if (mouse_x > duoren_button_x and mouse_x < duoren_button_x + duoren_button_rect.width and  # 双人模式
                    mouse_y > duoren_button_y and mouse_y < duoren_button_y + duoren_button_rect.height):
                if (click == 1):
                    kaishi_speed = 15
                    button_speed = 15
                    game_start_speed = 2
                    mode = 2
            if (game_start <= 0 and mode == 1):
                screen.blit(background, (0, 0))
                defen = font.render('Score: ', True, PURPLE_COLOR)
                screen.blit(defen, (10, 10))
                hx, hy = pygame.mouse.get_pos()
                if time:  # 装填子弹
                    time -= 1
                else:
                    b_x.append(hx - b_rect.width / 2 + 2)
                    b_y.append(hy - h_height / 2 - b_rect.height)
                    time = b_v
                for i in range(len(b_x)):  # 子弹移动
                    screen.blit(bullet1, (b_x[i], b_y[i]))
                    b_y[i] -= b_speed
                    bullet1_music.play()
                    if (b_y[i] < 0 - b_rect.height):
                        del b_y[i]
                        del b_x[i]
                        break

                    for j in range(len(enemy_y)):
                        if (b_y[i] < enemy_y[j] + e_rect.height and b_x[i] + b_rect.width > enemy_x[j]  # 子弹碰到小敌人
                                and b_x[i] < enemy_x[j] + e_rect.width and b_y[i] + b_height > enemy_y[j]):
                            b_y[i] = -1500
                            b_x[i] = -1500
                            score += 1
                            baozha1_x.append(enemy_x[j])
                            baozha1_y.append(enemy_y[j])
                            chixushijian1.append(40)
                            del enemy_y[j]
                            del enemy_x[j]
                            del enemy_x_speed[j]
                            del enemy_y_speed[j]
                            break

                    for j in range(len(enemy1_y)):
                        if (b_y[i] < enemy1_y[j] + e_rect1.height and b_x[i] + b_rect.width > enemy1_x[j]  # 子弹碰到中敌人
                                and b_x[i] < enemy1_x[j] + e_rect1.width and b_y[i] + b_height > enemy1_y[j]):
                            score += 1
                            b_y[i] = -1500
                            b_x[i] = -1500
                            blood_enemy1[j] = blood_enemy1[j] - 1
                            if (blood_enemy1[j] <= 0):
                                baozha2_x.append(enemy1_x[j])
                                baozha2_y.append(enemy1_y[j])
                                chixushijian2.append(40)
                                del enemy1_y[j]
                                del enemy1_x[j]
                                del blood_enemy1[j]
                                del enemy1_x_speed[j]
                                del enemy1_y_speed[j]
                                break

                    for j in range(len(enemy2_y)):
                        if (b_y[i] < enemy2_y[j] + e_rect2.height and b_x[i] + b_rect.width > enemy2_x[j]  # 子弹碰到大敌人
                                and b_x[i] < enemy2_x[j] + e_rect2.width and b_y[i] + b_height > enemy2_y[j]):
                            b_y[i] = -1500
                            b_x[i] = -1500
                            score += 1
                            blood_enemy2[j] = blood_enemy2[j] - 1
                            if (blood_enemy2[j] <= 0):
                                baozha3_x.append(enemy2_x[j])
                                baozha3_y.append(enemy2_y[j])
                                chixushijian3.append(60)
                                del enemy2_y[j]
                                del enemy2_x[j]
                                del blood_enemy2[j]
                                del enemy2_x_speed[j]
                                del enemy2_y_speed[j]
                                break

                protect -= protect_speed
                for i in range(len(enemy_y)):

                    if (hy < enemy_y[i] + e_rect.height and hx + h_rect.width > enemy_x[i]  # 飞机1碰撞扣血
                            and hx < enemy_x[i] + e_rect.width and hy + h_rect.height > enemy_y[i]):
                        protect_speed = 1
                        if (protect <= 0):
                            h_blood -= 1
                            protect = 50
                            protect_speed = 0

                for i in range(len(enemy1_y)):
                    if (hy < enemy1_y[i] + e_rect1.height and hx + h_rect.width > enemy1_x[i]  # 飞机1碰撞扣血
                            and hx < enemy1_x[i] + e_rect1.width and hy + h_rect.height > enemy1_y[i]):
                        protect_speed = 1
                        if (protect <= 0):
                            h_blood -= 1
                            protect = 50
                            protect_speed = 0

                for i in range(len(enemy2_y)):
                    if (hy < enemy2_y[i] + e_rect2.height and hx + h_rect.width > enemy2_x[i]  # 飞机1碰撞扣血
                            and hx < enemy2_x[i] + e_rect2.width and hy + h_rect.height > enemy2_y[i]):
                        protect_speed = 1
                        if (protect <= 0):
                            h_blood -= 1
                            protect = 50
                            protect_speed = 0

                for i in range(len(buji1_x)):  # 补给1效果
                    buji1_y[i] += buji1_speed
                    screen.blit(buji1, (buji1_x[i], buji1_y[i]))
                    if (hy < buji1_y[i] + buji1_rect.height and hx + h_rect.width > buji1_x[i]
                            and hx < buji1_x[i] + buji1_rect.width and hy + h_rect.height > buji1_y[i]):
                        del buji1_x[i]
                        del buji1_y[i]
                        bullet1 = pygame.image.load(r"images\bullet2.png")
                        b_speed += 5
                        b_v -= 4
                        break

                for i in range(len(buji2_x)):  # 补给2效果
                    buji2_y[i] += buji2_speed
                    screen.blit(buji2, (buji2_x[i], buji2_y[i]))
                    if (hy < buji2_y[i] + buji2_rect.height and hx + h_rect.width > buji2_x[i]
                            and hx < buji2_x[i] + buji2_rect.width and hy + h_rect.height > buji2_y[i]):
                        del buji2_x[i]
                        del buji2_y[i]
                        zhadan += 1
                        break
                if (zhadan > 0):
                    zhadan -= 1
                    for j in range(len(enemy_y)):
                        if (0 < enemy_y[j] and enemy_y[j] < 1000):
                            score += 1
                            baozha1_x.append(enemy_x[j])
                            baozha1_y.append(enemy_y[j])
                            chixushijian1.append(40)
                            del enemy_y[j]
                            del enemy_x[j]
                            del enemy_x_speed[j]
                            del enemy_y_speed[j]
                            break
                    for j in range(len(enemy1_y)):
                        if (0 < enemy1_y[j] and enemy1_y[j] < 1000):
                            score += 1
                            baozha2_x.append(enemy1_x[j])
                            baozha2_y.append(enemy1_y[j])
                            chixushijian2.append(40)
                            del enemy1_y[j]
                            del enemy1_x[j]
                            del blood_enemy1[j]
                            del enemy1_x_speed[j]
                            del enemy1_y_speed[j]
                            break
                    for j in range(len(enemy2_y)):
                        if (0 < enemy2_y[j] and enemy2_y[j] < 1000):
                            score += 1
                            baozha3_x.append(enemy2_x[j])
                            baozha3_y.append(enemy2_y[j])
                            chixushijian3.append(60)
                            del enemy2_y[j]
                            del enemy2_x[j]
                            del blood_enemy2[j]
                            del enemy2_x_speed[j]
                            del enemy2_y_speed[j]
                            break

                if (d == 1):  # 小敌人爆炸效果
                    if (len(baozha1_x) != 0):
                        for i in range(len(baozha1_x)):
                            if (41 > chixushijian1[i] > 30):
                                enemy_music.play()
                                screen.blit(baozha1, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1
                            if (30 >= chixushijian1[i] > 20):
                                enemy_music.play()
                                screen.blit(baozha2, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1
                            if (20 >= chixushijian1[i] > 10):
                                enemy_music.play()
                                screen.blit(baozha3, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1
                            if (10 >= chixushijian1[i] > 0):
                                enemy_music.play()
                                screen.blit(baozha4, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1

                if (d == 1):  # 中敌人爆炸效果
                    if (len(baozha2_x) != 0):
                        for i in range(len(baozha2_x)):
                            if (41 > chixushijian2[i] > 30):
                                enemy1_music.play()
                                screen.blit(baozha5, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1
                            if (30 >= chixushijian2[i] > 20):
                                enemy1_music.play()
                                screen.blit(baozha6, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1
                            if (20 >= chixushijian2[i] > 10):
                                enemy1_music.play()
                                screen.blit(baozha7, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1
                            if (10 >= chixushijian2[i] > 0):
                                enemy1_music.play()
                                screen.blit(baozha8, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1

                if (d == 1):  # 大敌人爆炸效果
                    if (len(baozha3_x) != 0):
                        for i in range(len(baozha3_x)):
                            if (61 > chixushijian3[i] > 50):
                                enemy2_music.play()
                                screen.blit(baozha9, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (50 >= chixushijian3[i] > 40):
                                enemy2_music.play()
                                screen.blit(baozha10, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (40 >= chixushijian3[i] > 30):
                                enemy2_music.play()
                                screen.blit(baozha11, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (30 >= chixushijian3[i] > 20):
                                enemy2_music.play()
                                screen.blit(baozha12, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (20 >= chixushijian3[i] > 10):
                                enemy2_music.play()
                                screen.blit(baozha13, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (10 >= chixushijian3[i] > 0):
                                enemy2_music.play()
                                screen.blit(baozha14, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1

                defen1 = font.render(str(score), True, PURPLE_COLOR)
                screen.blit(defen1, (110, 10))

                for i in range(len(enemy_y)):  # 小敌人飞行
                    if (enemy_x[i] + e_rect.width > 600 or enemy_x[i] - e_rect.width < 0):
                        enemy_x_speed[i] = -enemy_x_speed[i]
                    if (enemy_y[i] > 1000):
                        h_blood -= 1
                        enemy_y[i] = random.randint(-100, -60)
                    enemy_y[i] += enemy_y_speed[i]
                    enemy_x[i] += enemy_x_speed[i]
                    screen.blit(enemy, (enemy_x[i], enemy_y[i]))

                for i in range(len(enemy1_y)):  # 中敌人飞行
                    if (enemy1_x[i] + e_rect1.width > 600 or enemy1_x[i] - e_rect1.width < 0):
                        enemy1_x_speed[i] = -enemy1_x_speed[i]
                    if (enemy1_y[i] > 1000):
                        h_blood -= 1
                        enemy1_y[i] = random.randint(-100, -60)
                    enemy1_y[i] += enemy1_y_speed[i]
                    enemy1_x[i] += enemy1_x_speed[i]
                    screen.blit(enemy1, (enemy1_x[i], enemy1_y[i]))

                for i in range(len(enemy2_y)):  # 大敌人飞行
                    if (enemy2_x[i] + e_rect2.width > 600 or enemy2_x[i] - e_rect2.width < 0):
                        enemy2_x_speed[i] = -enemy2_x_speed[i]
                    if (enemy2_y[i] > 1000):
                        h_blood -= 1
                        enemy2_y[i] = random.randint(-250, -150)

                    enemy2_y[i] += enemy2_y_speed[i]
                    enemy2_x[i] += enemy2_x_speed[i]
                    screen.blit(enemy2, (enemy2_x[i], enemy2_y[i]))

                for i in range(len(enemy1_x)):  # 中敌人血量显示
                    pygame.draw.line(screen, PURPLE_COLOR, (enemy1_x[i], enemy1_y[i] + e_height1 + 2),
                                     (enemy1_x[i] + blood_enemy1[i] * 10,
                                      enemy1_y[i] + e_height1 + 2), 5)
                    pygame.draw.line(screen, RED_COLOR, (enemy1_x[i] + 7 * 10, enemy1_y[i] + e_height1 + 2),
                                     (enemy1_x[i] + 7 * 10 - (7 - blood_enemy1[i]) * 10,
                                      enemy1_y[i] + e_height1 + 2), 5)

                for i in range(len(enemy2_x)):  # 大敌人血量显示
                    pygame.draw.line(screen, PURPLE_COLOR, (enemy2_x[i] + 20, enemy2_y[i] + e_height2 + 2),
                                     (enemy2_x[i] + blood_enemy2[i] * 8 + 20,
                                      enemy2_y[i] + e_height2 + 2), 5)
                    pygame.draw.line(screen, RED_COLOR, (enemy2_x[i] + 8 * 15 + 20, enemy2_y[i] + e_height2 + 2),
                                     (enemy2_x[i] + 8 * 15 - (15 - blood_enemy2[i]) * 8 + 20,
                                      enemy2_y[i] + e_height2 + 2), 5)

                pygame.draw.line(screen, PURPLE_COLOR, (hx - 55, hy + h_height - 60),  # 自己血量
                                 (hx - 55 + h_blood * 23,
                                  hy + h_height - 60), 5)
                pygame.draw.line(screen, RED_COLOR, (hx - 55 + 5 * 23, hy + h_height - 60),
                                 (hx - 55 + 5 * 23 - (5 - h_blood) * 23,
                                  hy + h_height - 60), 5)

                if (len(enemy_x) == 0 and len(enemy1_x) == 0 and len(enemy2_x) == 0):  # 游戏结束条件—击杀全部
                    screen.blit(tuichu, (tuichu_x, tuichu_y))
                    end1 = font.render('Penta Kill! Congratuiation!', True, PURPLE_COLOR)
                    screen.blit(end1, (tuichu_x - 125, tuichu_y + 30))
                    if (mouse_x > tuichu_x and mouse_x < tuichu_x + tuichu_rect.width and
                            mouse_y > tuichu_y and mouse_y < tuichu_y + tuichu_rect.height):
                        if (click == 1):
                            exit()

                if (h_blood <= 0):
                    while (True):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        click, b, c = pygame.mouse.get_pressed()
                        screen.blit(tuichu, (tuichu_x, tuichu_y))
                        end1 = font.render('Try More! You Will Win Next Time  ', True, PURPLE_COLOR)
                        screen.blit(end1, (tuichu_x - 180, tuichu_y + 30))
                        if (mouse_x > tuichu_x and mouse_x < tuichu_x + tuichu_rect.width and
                                mouse_y > tuichu_y and mouse_y < tuichu_y + tuichu_rect.height):
                            if (click == 1):
                                exit()
                        pygame.display.update()
                screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))

                pygame.display.update()
            if (game_start <= 0 and mode == 2):  # 双人模式
                screen.blit(background, (0, 0))
                defen = font.render('Score: ', True, PURPLE_COLOR)
                screen.blit(defen, (10, 10))
                keys = pygame.key.get_pressed()
                keys1 = pygame.key.get_pressed()
                # pygame.key.set_repeat(100)
                if keys[pygame.K_RIGHT]:
                    h1x += 10
                elif keys[pygame.K_LEFT]:
                    h1x -= 10
                elif keys[pygame.K_UP]:
                    h1y -= 10
                elif keys[pygame.K_DOWN]:
                    h1y += 10
                if keys1[pygame.K_a]:
                    hx -= 10
                elif keys1[pygame.K_d]:
                    hx += 10
                elif keys1[pygame.K_w]:
                    hy -= 10
                elif keys1[pygame.K_s]:
                    hy += 10
                if time:  # 飞机1装填子弹
                    time -= 1
                else:
                    b_x.append(hx - b_rect.width / 2 + 2)
                    b_y.append(hy - h_height / 2 - b_rect.height)
                    time = b_v

                if time1:  # 飞机2装填子弹
                    time1 -= 1
                else:
                    b1_x.append(h1x - b_rect.width / 2 + 2)
                    b1_y.append(h1y - h_height / 2 - b_rect.height)
                    time1 = b1_v
                for i in range(len(b_x)):  # 子弹1移动
                    screen.blit(bullet1, (b_x[i], b_y[i]))
                    b_y[i] -= b_speed
                    if (b_y[i] < 0 - b_rect.height):
                        del b_y[i]
                        del b_x[i]
                        break
                    for j in range(len(enemy_y)):
                        if (b_y[i] < enemy_y[j] + e_rect.height and b_x[i] + b_rect.width > enemy_x[j]  # 子弹1碰到小敌人
                                and b_x[i] < enemy_x[j] + e_rect.width and b_y[i] + b_height > enemy_y[j]):
                            b_y[i] = -1500
                            b_x[i] = -1500
                            score += 1
                            baozha1_x.append(enemy_x[j])
                            baozha1_y.append(enemy_y[j])
                            chixushijian1.append(40)
                            del enemy_y[j]
                            del enemy_x[j]
                            del enemy_x_speed[j]
                            del enemy_y_speed[j]
                            break

                    for j in range(len(enemy1_y)):
                        if (b_y[i] < enemy1_y[j] + e_rect1.height and b_x[i] + b_rect.width > enemy1_x[j]  # 子弹1碰到中敌人
                                and b_x[i] < enemy1_x[j] + e_rect1.width and b_y[i] + b_height > enemy1_y[j]):
                            score += 1
                            b_y[i] = -1500
                            b_x[i] = -1500
                            blood_enemy1[j] = blood_enemy1[j] - 1
                            if (blood_enemy1[j] <= 0):
                                baozha2_x.append(enemy1_x[j])
                                baozha2_y.append(enemy1_y[j])
                                chixushijian2.append(40)
                                del enemy1_y[j]
                                del enemy1_x[j]
                                del blood_enemy1[j]
                                del enemy1_x_speed[j]
                                del enemy1_y_speed[j]
                                break

                    for j in range(len(enemy2_y)):
                        if (b_y[i] < enemy2_y[j] + e_rect2.height and b_x[i] + b_rect.width > enemy2_x[j]  # 子弹1碰到大敌人
                                and b_x[i] < enemy2_x[j] + e_rect2.width and b_y[i] + b_height > enemy2_y[j]):
                            b_y[i] = -1500
                            b_x[i] = -1500
                            score += 1
                            blood_enemy2[j] = blood_enemy2[j] - 1
                            if (blood_enemy2[j] <= 0):
                                baozha3_x.append(enemy2_x[j])
                                baozha3_y.append(enemy2_y[j])
                                chixushijian3.append(60)
                                del enemy2_y[j]
                                del enemy2_x[j]
                                del blood_enemy2[j]
                                del enemy2_x_speed[j]
                                del enemy2_y_speed[j]
                                break

                for i in range(len(b1_x)):  # 子弹2移动
                    screen.blit(bullet1, (b1_x[i], b1_y[i]))
                    b1_y[i] -= b1_speed
                    if (b1_y[i] < 0 - b_rect.height):
                        del b1_y[i]
                        del b1_x[i]
                        break
                    for j in range(len(enemy_y)):
                        if (b1_y[i] < enemy_y[j] + e_rect.height and b1_x[i] + b_rect.width > enemy_x[j]  # 子弹2碰到小敌人
                                and b1_x[i] < enemy_x[j] + e_rect.width and b1_y[i] + b_height > enemy_y[j]):
                            b1_y[i] = -1500
                            b1_x[i] = -1500
                            score += 1
                            baozha1_x.append(enemy_x[j])
                            baozha1_y.append(enemy_y[j])
                            chixushijian1.append(40)
                            del enemy_y[j]
                            del enemy_x[j]
                            del enemy_x_speed[j]
                            del enemy_y_speed[j]
                            break

                    for j in range(len(enemy1_y)):
                        if (b1_y[i] < enemy1_y[j] + e_rect1.height and b1_x[i] + b_rect.width > enemy1_x[j]  # 子弹2碰到中敌人
                                and b1_x[i] < enemy1_x[j] + e_rect1.width and b1_y[i] + b_height > enemy1_y[j]):
                            score += 1
                            b1_y[i] = -1500
                            b1_x[i] = -1500
                            blood_enemy1[j] = blood_enemy1[j] - 1
                            if (blood_enemy1[j] <= 0):
                                baozha2_x.append(enemy1_x[j])
                                baozha2_y.append(enemy1_y[j])
                                chixushijian2.append(40)
                                del enemy1_y[j]
                                del enemy1_x[j]
                                del blood_enemy1[j]
                                del enemy1_x_speed[j]
                                del enemy1_y_speed[j]
                                break

                    for j in range(len(enemy2_y)):
                        if (b1_y[i] < enemy2_y[j] + e_rect2.height and b1_x[i] + b_rect.width > enemy2_x[j]  # 子弹2碰到大敌人
                                and b1_x[i] < enemy2_x[j] + e_rect2.width and b1_y[i] + b_height > enemy2_y[j]):
                            b1_y[i] = -1500
                            b1_x[i] = -1500
                            score += 1
                            blood_enemy2[j] = blood_enemy2[j] - 1
                            if (blood_enemy2[j] <= 0):
                                baozha3_x.append(enemy2_x[j])
                                baozha3_y.append(enemy2_y[j])
                                chixushijian3.append(60)
                                del enemy2_y[j]
                                del enemy2_x[j]
                                del blood_enemy2[j]
                                del enemy2_x_speed[j]
                                del enemy2_y_speed[j]
                                break

                for i in range(len(buji1_x)):  # 补给1效果
                    buji1_y[i] += buji1_speed
                    screen.blit(buji1, (buji1_x[i], buji1_y[i]))
                    if (hy < buji1_y[i] + buji1_rect.height and hx + h_rect.width > buji1_x[i]
                            and hx < buji1_x[i] + buji1_rect.width and hy + h_rect.height > buji1_y[i]):
                        del buji1_x[i]
                        del buji1_y[i]
                        bullet1 = pygame.image.load(r"images\bullet2.png")
                        b_speed += 5
                        b_v -= 6
                        break
                    if (h1y < buji1_y[i] + buji1_rect.height and h1x + h_rect.width > buji1_x[i]
                            and h1x < buji1_x[i] + buji1_rect.width and h1y + h_rect.height > buji1_y[i]):
                        del buji1_x[i]
                        del buji1_y[i]
                        bullet1 = pygame.image.load(r"images\bullet2.png")
                        b1_speed += 5
                        b1_v -= 6
                        break
                for i in range(len(buji2_x)):  # 补给2效果
                    buji2_y[i] += buji2_speed
                    screen.blit(buji2, (buji2_x[i], buji2_y[i]))
                    if (hy < buji2_y[i] + buji2_rect.height and hx + h_rect.width > buji2_x[i]
                            and hx < buji2_x[i] + buji2_rect.width and hy + h_rect.height > buji2_y[i]):
                        del buji2_x[i]
                        del buji2_y[i]
                        zhadan += 1
                        break
                    if (h1y < buji2_y[i] + buji2_rect.height and h1x + h_rect.width > buji2_x[i]
                            and h1x < buji2_x[i] + buji2_rect.width and h1y + h_rect.height > buji2_y[i]):
                        del buji2_x[i]
                        del buji2_y[i]
                        zhadan += 1
                        break
                if (zhadan > 0):
                    zhadan -= 1
                    for j in range(len(enemy_y)):
                        if (0 < enemy_y[j] and enemy_y[j] < 1000):
                            score += 1
                            baozha1_x.append(enemy_x[j])
                            baozha1_y.append(enemy_y[j])
                            chixushijian1.append(40)
                            del enemy_y[j]
                            del enemy_x[j]
                            del enemy_x_speed[j]
                            del enemy_y_speed[j]
                            break
                    for j in range(len(enemy1_y)):
                        if (0 < enemy1_y[j] and enemy1_y[j] < 1000):
                            score += 1
                            baozha2_x.append(enemy1_x[j])
                            baozha2_y.append(enemy1_y[j])
                            chixushijian2.append(40)
                            del enemy1_y[j]
                            del enemy1_x[j]
                            del blood_enemy1[j]
                            del enemy1_x_speed[j]
                            del enemy1_y_speed[j]
                            break
                    for j in range(len(enemy2_y)):
                        if (0 < enemy2_y[j] and enemy2_y[j] < 1000):
                            score += 1
                            baozha3_x.append(enemy2_x[j])
                            baozha3_y.append(enemy2_y[j])
                            chixushijian3.append(60)
                            del enemy2_y[j]
                            del enemy2_x[j]
                            del blood_enemy2[j]
                            del enemy2_x_speed[j]
                            del enemy2_y_speed[j]
                            break

                protect -= protect_speed
                for i in range(len(enemy_y)):

                    if (hy < enemy_y[i] + e_rect.height and hx + h_rect.width > enemy_x[i]  # 飞机1碰撞扣血
                            and hx < enemy_x[i] + e_rect.width and hy + h_rect.height > enemy_y[i]):
                        protect_speed = 1
                        if (protect <= 0):
                            h_blood -= 1
                            protect = 50
                            protect_speed = 0

                for i in range(len(enemy1_y)):
                    if (hy < enemy1_y[i] + e_rect1.height and hx + h_rect.width > enemy1_x[i]  # 飞机1碰撞扣血
                            and hx < enemy1_x[i] + e_rect1.width and hy + h_rect.height > enemy1_y[i]):
                        protect_speed = 1
                        if (protect <= 0):
                            h_blood -= 1
                            protect = 50
                            protect_speed = 0

                for i in range(len(enemy2_y)):
                    if (hy < enemy2_y[i] + e_rect2.height and hx + h_rect.width > enemy2_x[i]  # 飞机1碰撞扣血
                            and hx < enemy2_x[i] + e_rect2.width and hy + h_rect.height > enemy2_y[i]):
                        protect_speed = 1
                        if (protect <= 0):
                            h_blood -= 1
                            protect = 50
                            protect_speed = 0

                protect1 -= protect1_speed
                for i in range(len(enemy_y)):

                    if (h1y < enemy_y[i] + e_rect.height and h1x + h_rect.width > enemy_x[i]  # 飞机2碰撞扣血
                            and h1x < enemy_x[i] + e_rect.width and h1y + h_rect.height > enemy_y[i]):
                        protect1_speed = 1
                        if (protect1 <= 0):
                            h1_blood -= 1
                            protect1 = 50
                            protect1_speed = 0

                for i in range(len(enemy1_y)):
                    if (h1y < enemy1_y[i] + e_rect1.height and h1x + h_rect.width > enemy1_x[i]  # 飞机2碰撞扣血
                            and h1x < enemy1_x[i] + e_rect1.width and h1y + h_rect.height > enemy1_y[i]):
                        protect_speed = 1
                        if (protect1 <= 0):
                            h1_blood -= 1
                            protect1 = 50
                            protect1_speed = 0

                for i in range(len(enemy2_y)):
                    if (h1y < enemy2_y[i] + e_rect2.height and h1x + h_rect.width > enemy2_x[i]  # 飞机2碰撞扣血
                            and h1x < enemy2_x[i] + e_rect2.width and h1y + h_rect.height > enemy2_y[i]):
                        protect1_speed = 1
                        if (protect1 <= 0):
                            h1_blood -= 1
                            protect1 = 50
                            protect1_speed = 0

                if (d == 1):  # 小敌人爆炸效果
                    if (len(baozha1_x) != 0):
                        for i in range(len(baozha1_x)):
                            if (41 > chixushijian1[i] > 30):
                                screen.blit(baozha1, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1
                            if (30 >= chixushijian1[i] > 20):
                                screen.blit(baozha2, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1
                            if (20 >= chixushijian1[i] > 10):
                                screen.blit(baozha3, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1
                            if (10 >= chixushijian1[i] > 0):
                                screen.blit(baozha4, (baozha1_x[i], baozha1_y[i]))
                                chixushijian1[i] -= 1

                if (d == 1):  # 中敌人爆炸效果
                    if (len(baozha2_x) != 0):
                        for i in range(len(baozha2_x)):
                            if (41 > chixushijian2[i] > 30):
                                screen.blit(baozha5, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1
                            if (30 >= chixushijian2[i] > 20):
                                screen.blit(baozha6, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1
                            if (20 >= chixushijian2[i] > 10):
                                screen.blit(baozha7, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1
                            if (10 >= chixushijian2[i] > 0):
                                screen.blit(baozha8, (baozha2_x[i], baozha2_y[i]))
                                chixushijian2[i] -= 1

                if (d == 1):  # 大敌人爆炸效果
                    if (len(baozha3_x) != 0):
                        for i in range(len(baozha3_x)):
                            if (61 > chixushijian3[i] > 50):
                                screen.blit(baozha9, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (50 >= chixushijian3[i] > 40):
                                screen.blit(baozha10, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (40 >= chixushijian3[i] > 30):
                                screen.blit(baozha11, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (30 >= chixushijian3[i] > 20):
                                screen.blit(baozha12, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (20 >= chixushijian3[i] > 10):
                                screen.blit(baozha13, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1
                            if (10 >= chixushijian3[i] > 0):
                                screen.blit(baozha14, (baozha3_x[i], baozha3_y[i]))
                                chixushijian3[i] -= 1

                defen1 = font.render(str(score), True, PURPLE_COLOR)
                screen.blit(defen1, (110, 10))
                for i in range(len(enemy_y)):  # 小敌人飞行
                    if (enemy_x[i] + e_rect.width > 600 or enemy_x[i] - e_rect.width < 0):
                        enemy_x_speed[i] = -enemy_x_speed[i]
                    if (enemy_y[i] > 1000):
                        h_blood -= 1
                        h1_blood -= 1
                        enemy_y[i] = random.randint(-100, -60)
                    enemy_y[i] += enemy_y_speed[i]
                    enemy_x[i] += enemy_x_speed[i]
                    screen.blit(enemy, (enemy_x[i], enemy_y[i]))

                for i in range(len(enemy1_y)):  # 中敌人飞行
                    if (enemy1_x[i] + e_rect1.width > 600 or enemy1_x[i] - e_rect1.width < 0):
                        enemy1_x_speed[i] = -enemy1_x_speed[i]
                    if (enemy1_y[i] > 1000):
                        h_blood -= 1
                        h1_blood -= 1
                        enemy1_y[i] = random.randint(-100, -60)
                    enemy1_y[i] += enemy1_y_speed[i]
                    enemy1_x[i] += enemy1_x_speed[i]
                    screen.blit(enemy1, (enemy1_x[i], enemy1_y[i]))

                for i in range(len(enemy2_y)):  # 大敌人飞行
                    if (enemy2_x[i] + e_rect2.width > 600 or enemy2_x[i] - e_rect2.width < 0):
                        enemy2_x_speed[i] = -enemy2_x_speed[i]
                    if (enemy2_y[i] > 1000):
                        h_blood -= 1
                        h1_blood -= 1
                        enemy2_y[i] = random.randint(-250, -150)

                    enemy2_y[i] += enemy2_y_speed[i]
                    enemy2_x[i] += enemy2_x_speed[i]
                    screen.blit(enemy2, (enemy2_x[i], enemy2_y[i]))

                for i in range(len(enemy1_x)):  # 中敌人血量显示
                    pygame.draw.line(screen, PURPLE_COLOR, (enemy1_x[i], enemy1_y[i] + e_height1 + 2),
                                     (enemy1_x[i] + blood_enemy1[i] * 10,
                                      enemy1_y[i] + e_height1 + 2), 5)
                    pygame.draw.line(screen, RED_COLOR, (enemy1_x[i] + 7 * 10, enemy1_y[i] + e_height1 + 2),
                                     (enemy1_x[i] + 7 * 10 - (7 - blood_enemy1[i]) * 10,
                                      enemy1_y[i] + e_height1 + 2), 5)

                for i in range(len(enemy2_x)):  # 大敌人血量显示
                    pygame.draw.line(screen, PURPLE_COLOR, (enemy2_x[i] + 20, enemy2_y[i] + e_height2 + 2),
                                     (enemy2_x[i] + blood_enemy2[i] * 8 + 20,
                                      enemy2_y[i] + e_height2 + 2), 5)
                    pygame.draw.line(screen, RED_COLOR, (enemy2_x[i] + 8 * 15 + 20, enemy2_y[i] + e_height2 + 2),
                                     (enemy2_x[i] + 8 * 15 - (15 - blood_enemy2[i]) * 8 + 20,
                                      enemy2_y[i] + e_height2 + 2), 5)

                pygame.draw.line(screen, PURPLE_COLOR, (hx - 55, hy + h_height - 60),  # 自己血量（第一架）
                                 (hx - 55 + h_blood * 23,
                                  hy + h_height - 60), 5)
                pygame.draw.line(screen, RED_COLOR, (hx - 55 + 5 * 23, hy + h_height - 60),
                                 (hx - 55 + 5 * 23 - (5 - h_blood) * 23,
                                  hy + h_height - 60), 5)

                pygame.draw.line(screen, PURPLE_COLOR, (h1x - 55, h1y + h_height - 60),  # 自己血量（第二架）
                                 (h1x - 55 + h1_blood * 23,
                                  h1y + h_height - 60), 5)
                pygame.draw.line(screen, RED_COLOR, (h1x - 55 + 5 * 23, h1y + h_height - 60),
                                 (h1x - 55 + 5 * 23 - (5 - h1_blood) * 23,
                                  h1y + h_height - 60), 5)

                if (len(enemy_x) == 0 and len(enemy1_x) == 0 and len(enemy2_x) == 0):  # 游戏结束条件—击杀全部
                    screen.blit(tuichu, (tuichu_x, tuichu_y))
                    end1 = font.render('Penta Kill! Congratuiation!', True, PURPLE_COLOR)
                    screen.blit(end1, (tuichu_x - 125, tuichu_y + 30))
                    if (mouse_x > tuichu_x and mouse_x < tuichu_x + tuichu_rect.width and
                            mouse_y > tuichu_y and mouse_y < tuichu_y + tuichu_rect.height):
                        if (click == 1):
                            exit()
                if (h_blood <= 0):
                    hx = 10000
                    hy = -10000

                if (h1_blood <= 0):
                    h1x = 10000
                    h1y = -10000
                if (h_blood <= 0 and h1_blood <= 0):
                    while (True):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        click, b, c = pygame.mouse.get_pressed()
                        screen.blit(tuichu, (tuichu_x, tuichu_y))
                        end1 = font.render('Try More! You Will Win Next Time  ', True, PURPLE_COLOR)
                        screen.blit(end1, (tuichu_x - 180, tuichu_y + 30))
                        if (mouse_x > tuichu_x and mouse_x < tuichu_x + tuichu_rect.width and
                                mouse_y > tuichu_y and mouse_y < tuichu_y + tuichu_rect.height):
                            if (click == 1):
                                exit()
                        pygame.display.update()
                screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))
                screen.blit(hero, (h1x - h_width / 2, h1y - h_height / 2))

                pygame.display.update()
            pygame.display.update()
    if t2.press(x, y, z):
        import pygame
        import random
        import time

        pygame.init()

        pygame.mixer.init()
        bg_music = pygame.mixer.Sound("game_music.ogg")
        bg_music.play()

        screen = pygame.display.set_mode((600, 600))
        # bg = pygame.transform.scale(pygame.image.load("xingkong.jpg"), (600, 600))
        bg = pygame.transform.scale(pygame.image.load("lvse.jpg"), (600, 600))
        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 36)
        jiemian = pygame.transform.scale(pygame.image.load("jiemian.jpg"), (600, 600))
        button1 = pygame.image.load("1.png")
        button2 = pygame.image.load("3.png")
        button3 = pygame.image.load("2.png")
        over = pygame.transform.scale(pygame.image.load("over.jpg"), (600, 600))
        suspend_button = pygame.image.load("zanting.png")
        continue_button = pygame.image.load("jixu.png")
        shengli = pygame.image.load("shengli.jpg")
        nandu1 = pygame.image.load("初级难度.png")
        nandu2 = pygame.image.load("中级难度 .png")
        nandu3 = pygame.image.load("困难难度.png")

        score = 0

        # 食物点
        r_x = random.randint(105, 495)
        r_y = random.randint(105, 495)

        time1 = 0
        time2 = 1

        # 初始化蛇位置与速度
        speed = 2
        ls_x = []
        ls_y = []
        lx = [220, 210, 200]
        ly = [300, 300, 300]

        # 存储改变方向的坐标及方向
        ji_x = []
        ji_y = []
        ji_sx = []
        ji_sy = []
        isfangxiang = False


        # 检测碰撞
        def pengzhuangceshi(x1, x2, y1, y2):
            if -10 < x1 - x2 < 10 and -10 < y1 - y2 < 10:
                return True
            else:
                return False


        class interface(object):
            def __init__(self, screen, fengmian):
                self.screen = screen
                self.fengmian = fengmian
                self.x = 0
                self.y = 0
                self.rect = self.fengmian.get_rect()

            def show(self):
                self.screen.blit(self.fengmian, (self.x, self.y))

            def move(self):
                if self.y > -self.rect.height:
                    self.y -= 3


        jiemian = interface(screen, jiemian)

        # 功能键
        # 暂停变量及按钮
        suspend = False
        suspend_button_rect = suspend_button.get_rect()

        xuanze_nandu = False
        start_game = False
        move_jiemian = False
        game_over = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == 273 and ls_y[0] != speed:  # 按键进行方向改变并且不可为反方向
                        ls_y[0] = -speed
                        ls_x[0] = 0
                        isfangxiang = True
                    if event.key == 274 and ls_y[0] != -speed:
                        ls_y[0] = speed
                        ls_x[0] = 0
                        isfangxiang = True
                    if event.key == 275 and ls_x[0] != -speed:
                        ls_y[0] = 0
                        ls_x[0] = speed
                        isfangxiang = True
                    if event.key == 276 and ls_x[0] != speed:
                        ls_y[0] = 0
                        ls_x[0] = -speed
                        isfangxiang = True
                    if isfangxiang == True:
                        ji_x.append(lx[0])
                        ji_y.append(ly[0])
                        ji_sx.append(ls_x[0])
                        ji_sy.append(ls_y[0])
                        isfangxiang = False
            # 判断蛇身的点坐标是否与改变方向点坐标相同及改变方向
            for i in range(len(lx)):
                for j in range(len(ji_x)):
                    if lx[i] == ji_x[j] and ly[i] == ji_y[j]:
                        ls_x[i] = ji_sx[j]
                        ls_y[i] = ji_sy[j]
                # 去除改变方向点
            for i in range(len(ji_x)):
                if lx[len(lx) - 1] == ji_x[i] and ly[len(lx) - 1] == ji_y[i]:
                    ji_x.pop(i)
                    ji_y.pop(i)
                    ji_sx.pop(i)
                    ji_sy.pop(i)
                    break

            # 开始界面
            if start_game == False:

                screen.blit(bg, (0, 0))
                jiemian.show()
                screen.blit(button1, (80, 130))
                screen.blit(button2, (80, 230))
                screen.blit(button3, (100, 330))

                # 获取点坐标及点击鼠标
                a, b, c = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                # print(x,y)

                # 退出游戏按钮
                if 220 < x < 360 and 480 < y < 520 and a:
                    exit()

                # 难度选择按钮
                if 220 < x < 360 and 383 < y < 417 and a:
                    xuanze_nandu = True
                if xuanze_nandu:
                    screen.blit(nandu1, (230, 200))
                    screen.blit(nandu2, (250, 240))
                    screen.blit(nandu3, (250, 300))
                    if 395 < x < 482 and 333 < y < 361 and a:
                        speed = 2
                        xuanze_nandu = False
                    if 395 < x < 482 and 385 < y < 411 and a:
                        speed = 5
                        xuanze_nandu = False
                    if 395 < x < 482 and 437 < y < 459 and a:
                        speed = 10
                        xuanze_nandu = False

                # 开始游戏按钮
                if 220 < x < 360 and 276 < y < 310 and a:
                    ls_x = [speed, speed, speed]
                    ls_y = [0, 0, 0]
                    move_jiemian = True
                if move_jiemian:
                    jiemian.move()
                    if jiemian.y <= -jiemian.rect.height:
                        start_game = True

            # 游戏开始
            if start_game:
                a, b, c = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                time2 = time.time()

                if time2 - time1 >= 0.02:

                    # 显示图标
                    screen.blit(bg, (0, 0))
                    # 食物
                    pygame.draw.circle(screen, (255, 255, 255), (r_x, r_y), 5)
                    # 边界
                    pygame.draw.line(screen, (255, 255, 255), (100, 100), (100, 500))
                    pygame.draw.line(screen, (255, 255, 255), (500, 100), (500, 500))
                    pygame.draw.line(screen, (255, 255, 255), (100, 100), (500, 100))
                    pygame.draw.line(screen, (255, 255, 255), (100, 500), (500, 500))
                    # 分数+速度
                    screen.blit(font.render("score:" + str(score), True, (255, 255, 255)), (0, 0))
                    screen.blit(font.render("speed:" + str(speed), True, (255, 255, 255)), (0, 40))

                    # 暂停与开始按钮
                    if suspend == False:
                        screen.blit(suspend_button, (30, 520))
                        # a, b, c = pygame.mouse.get_pressed()
                        # x, y = pygame.mouse.get_pos()
                        if 30 < x < 30 + suspend_button_rect.width and 520 < y < 520 + suspend_button_rect.height and a:
                            suspend = True
                    else:
                        screen.blit(continue_button, (30, 520))
                        if 30 < x < 30 + suspend_button_rect.width and 520 < y < 520 + suspend_button_rect.height and a:
                            suspend = False
                    # x+=s_x
                    # y+=s_y
                    # 坐标改变即移动
                    if suspend == False:
                        for i in range(len(ls_x)):
                            lx[i] += ls_x[i]
                            ly[i] += ls_y[i]

                    for i in range(len(lx)):
                        pygame.draw.circle(screen, (255, 255, 255), (lx[i], ly[i]), 5)
                    time1 = time.time()
                    if pengzhuangceshi(lx[0], r_x, ly[0], r_y):
                        r_x = random.randint(105, 495)
                        r_y = random.randint(105, 495)
                        score += 1
                        if ls_x[len(lx) - 1] == speed:  # 根据最后一个点的速度方向增加新的点的速度方向
                            lx.append(lx[len(lx) - 1] - 10)
                            ly.append(ly[len(ly) - 1])
                            ls_x.append(ls_x[len(ls_x) - 1])
                            ls_y.append(ls_y[len(ls_y) - 1])
                        if ls_x[len(lx) - 1] == -speed:
                            lx.append(lx[len(lx) - 1] + 10)
                            ly.append(ly[len(ly) - 1])
                            ls_x.append(ls_x[len(ls_x) - 1])
                            ls_y.append(ls_y[len(ls_y) - 1])
                        if ls_y[len(ly) - 1] == speed:
                            lx.append(lx[len(lx) - 1])
                            ly.append(ly[len(ly) - 1] - 10)
                            ls_x.append(ls_x[len(ls_x) - 1])
                            ls_y.append(ls_y[len(ls_y) - 1])
                        if ls_y[len(ly) - 1] == -speed:
                            lx.append(lx[len(lx) - 1])
                            ly.append(ly[len(ly) - 1] + 10)
                            ls_x.append(ls_x[len(ls_x) - 1])
                            ls_y.append(ls_y[len(ls_y) - 1])
                # 游戏失败结束判断
                if 495 < lx[0] or lx[0] < 105 or 495 < ly[0] or ly[0] < 105:
                    game_over = True

                for i in range(len(lx)):
                    if i != 0 and i != 1:  # 第一个点与第二个点不会发现碰撞所以无需判断
                        if pengzhuangceshi(lx[0], lx[i], ly[0], ly[i]):
                            game_over = True

            if game_over:
                screen.blit(over, (0, 0))
                screen.blit(font.render("score:" + str(score), True, (25, 25, 25)), (250, 100))
                screen.blit(button3, (100, 330))
                # a, b, c = pygame.mouse.get_pressed()
                # x, y = pygame.mouse.get_pos()
                if 220 < x < 360 and 480 < y < 520 and a:  # 结束游戏
                    exit()

            # 游戏胜利结束判断
            if suspend == 2:
                if score > 100:
                    screen.blit("shengli", (0, 0))
                    suspend = True
            elif suspend == 5:
                if score > 200:
                    screen.blit("shengli", (0, 0))
                    suspend = True
            elif suspend == 10:
                if score > 300:
                    screen.blit("shengli", (0, 0))
                    suspend = True

            pygame.display.update()
    if t3.press(x, y, z):
        import pygame
        import random
        import math

        pygame.init()
        font = pygame.font.Font("C:\Windows\Fonts\simhei.ttf", 24)
        over_font = pygame.font.Font("C:\Windows\Fonts\JOKERMAN.TTF", 72)
        over_score_font = pygame.font.Font("C:\Windows\Fonts\STXINWEI.TTF", 36)

        screen = pygame.display.set_mode((480, 852))
        background = pygame.image.load("background1.png")
        start_background = pygame.image.load("start_background.png")
        title = pygame.image.load("title.png")

        ball = pygame.image.load("ball.png")
        ball_rect = ball.get_rect()
        ball_width = ball_rect.width
        ball_height = ball_rect.height
        ball_start_x = (480 - ball_width) / 2
        ball_start_y = 50
        ball_speed_x = 0
        ball_speed_y = 0
        ball_num = 1

        add_ball = pygame.image.load("add.png")
        add_ball_rect = add_ball.get_rect()
        add_ball_width = add_ball_rect.width
        add_ball_height = add_ball_rect.height

        score = 0


        class Ball():
            def __init__(self, ball_x, ball_y, speed_x, speed_y):
                self.ball = pygame.image.load("ball.png")

                self.x = ball_x
                self.y = ball_y
                self.speed_x = speed_x
                self.speed_y = speed_y

            def show_ball(self):
                screen.blit(self.ball, (self.x, self.y))

            def after_click(self, click_x, click_y):
                self.speed_x = click_x - self.x
                self.speed_y = click_y - self.y
                # if math.sqrt(self.speed_x ** 2 + self.speed_y ** 2) < 3:
                temp_y = 8 / math.sqrt(1 + (self.speed_x / self.speed_y) ** 2)
                temp_x = self.speed_x / self.speed_y * temp_y
                self.speed_x = temp_x
                self.speed_y = temp_y

            def gravity(self, t):
                if self.y < 852 - ball_height:
                    self.speed_y = self.speed_y + 10 * t

            def move_ball(self):
                self.x += self.speed_x
                self.y += self.speed_y

            def bump_walls(self):
                if self.x < 0 or self.x > 480 - ball_width:
                    self.speed_x = -self.speed_x
                if self.y < 0:
                    self.speed_y = -self.speed_y
                if self.y > 852 - ball_height:
                    self.speed_x = 0
                    self.speed_y = 0
                    self.x = ball_start_x
                    self.y = ball_start_y


        class Line():
            def __init__(self, start_x, start_y):
                self.start_x = start_x
                self.start_y = start_y
                self.click_x, self.click_y = pygame.mouse.get_pos()

                # self.end_y = 5 / math.sqrt(1 + ((self.click_x - self.start_x) / (self.click_y - self.start_y)) ** 2)
                # self.end_x = -(self.click_x - self.start_x) / (self.click_y - self.start_y) * self.end_y

            def show_line(self):
                pygame.draw.line(screen, (255, 255, 255), (self.start_x, self.start_y), (self.click_x, self.click_y), 1)


        class Block():
            def __init__(self, block_x, block_y, color_num, blood):
                self.blocks = []
                self.blocks.append(pygame.image.load("block1.jpg"))
                self.blocks.append(pygame.image.load("block2.jpg"))
                self.blocks.append(pygame.image.load("block3.jpg"))
                self.blocks.append(pygame.image.load("block4.jpg"))
                # self.COLOR = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))
                # pygame.draw.rect(screen, self.COLOR, (random.randint(0, 480-50), 750, random.randint(0, 480-50) + 50, 800))

                self.x = block_x
                self.y = block_y
                self.num = color_num
                self.blood = blood

            def show_block(self):

                screen.blit(self.blocks[self.num], (self.x, self.y))

            def block_bumped(self, ball_list):
                for i in range(len(ball_list)):
                    if ball_list[i].x < self.x < ball_list[i].x + ball_width \
                            and self.y < ball_list[i].y + ball_height / 2 <= self.y + 60:
                        ball_list[i].speed_x = -ball_list[i].speed_x
                        self.blood -= 1
                        my_score.add_score()

                    if ball_list[i].x < self.x + 60 < ball_list[i].x + ball_width \
                            and self.y < ball_list[i].y + ball_height / 2 <= self.y + 60:
                        ball_list[i].speed_x = -ball_list[i].speed_x
                        self.blood -= 1
                        my_score.add_score()

                    if ball_list[i].y < self.y < ball_list[i].y + ball_height \
                            and self.x < ball_list[i].x + ball_height / 2 <= self.x + 60:
                        ball_list[i].speed_y = -ball_list[i].speed_y
                        self.blood -= 1
                        my_score.add_score()
                        # t_re(i)

                    if ball_list[i].y < self.y + 60 < ball_list[i].y + ball_height \
                            and self.x < ball_list[i].x + ball_height / 2 <= self.x + 60:
                        ball_list[i].speed_y = -ball_list[i].speed_y
                        self.blood -= 1
                        my_score.add_score()

            def show_blood(self):
                self.blood_str = font.render(str(self.blood), True, (0, 0, 0))
                screen.blit(self.blood_str, (self.x + 18, self.y + 18))


        class Add_ball():
            def __init__(self, add_ball_x, add_ball_y):
                self.add_ball = pygame.image.load("add.png")
                self.x = add_ball_x
                self.y = add_ball_y

            def show_add_ball(self):
                screen.blit(self.add_ball, (self.x, self.y))

            def add_ball_bumped(self, ball_list):
                for i in range(len(ball_list)):
                    if ball_list[i].x < self.x < ball_list[i].x + ball_width \
                            and self.y < ball_list[i].y + ball_height / 2 < self.y + 60:
                        ball_list[i].speed_x = -ball_list[i].speed_x
                        ball_list.append(
                            Ball(ball_list[i].x, ball_list[i].y, ball_list[i].speed_x, -ball_list[i].speed_y))
                        t.append(0.0001)
                        return 1

                    if ball_list[i].x < self.x + 60 < ball_list[i].x + ball_width \
                            and self.y < ball_list[i].y + ball_height / 2 < self.y + 60:
                        ball_list[i].speed_x = -ball_list[i].speed_x
                        ball_list.append(
                            Ball(ball_list[i].x, ball_list[i].y, ball_list[i].speed_x, -ball_list[i].speed_y))
                        t.append(0.0001)
                        return 1

                    if ball_list[i].y < self.y < ball_list[i].y + ball_height \
                            and self.x < ball_list[i].x + ball_height / 2 < self.x + 60:
                        ball_list[i].speed_y = -ball_list[i].speed_y
                        ball_list.append(
                            Ball(ball_list[i].x, ball_list[i].y, -ball_list[i].speed_x, ball_list[i].speed_y))
                        t.append(0.0001)
                        return 1

                    if ball_list[i].y < self.y + 60 < ball_list[i].y + ball_height \
                            and self.x < ball_list[i].x + ball_height / 2 < self.x + 60:
                        ball_list[i].speed_y = -ball_list[i].speed_y
                        ball_list.append(
                            Ball(ball_list[i].x, ball_list[i].y, -ball_list[i].speed_x, ball_list[i].speed_y))
                        t.append(0.0001)
                        return 1


        class Score():
            def __init__(self, score):
                self.score = score

            def show_score(self):
                self.score_display = font.render("分数：" + str(self.score), True, (255, 255, 255))
                screen.blit(self.score_display, (5, 5))

            def add_score(self):
                self.score += 1


        # class Start_interface():
        #     def __init__(self):

        # def add_ball(self):

        class Start():
            def __init__(self):
                self.button_nor = pygame.image.load("button_nor.png")
                self.button_press = pygame.image.load("button_press.png")

                self.button_rect = self.button_nor.get_rect()
                self.button_width = self.button_rect.width
                self.button_height = self.button_rect.height

            def show_button(self):
                left, right, wheel = pygame.mouse.get_pressed()
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if left == 1 and (480 - self.button_width) / 2 < mouse_x < (
                        480 - self.button_width) / 2 + self.button_width \
                        and 500 < mouse_y < 500 + self.button_height:
                    screen.blit(self.button_press, ((480 - self.button_width) / 2, 500))
                else:
                    screen.blit(self.button_nor, ((480 - self.button_width) / 2, 500))


        class End():
            def __init__(self, score):
                self.background = pygame.image.load("endbackground.png")

                self.score = score
                self.end_score = over_score_font.render("最终得分：" + str(self.score), True, (255, 255, 255))

                self.end_score_rect = self.end_score.get_rect()
                self.end_score_width = self.end_score_rect.width
                self.end_score_height = self.end_score_rect.height

            def show_end(self):
                screen.blit(self.background, (0, 0))
                while True:
                    # screen.blit(self.game_over, ((480 - self.game_over_width) / 2, 200))
                    screen.blit(self.end_score, ((480 - self.end_score_width) / 2, 400))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()

                    pygame.display.update()


        block_list = []
        for i in range(random.randint(1, 3)):
            block = Block(random.randint(0, 480 - 60), random.randint(680, 720), random.randint(0, 3),
                          random.randint(1, 3))
            block_list.append(block)

        add_ball_list = []
        add_ball_list.append(Add_ball(random.randint(0, 480 - add_ball_width), random.randint(680, 720)))

        # block_list.append(block)
        ball_list = []
        t = []
        ball_list.append(Ball(ball_start_x, ball_start_y, 0, 0))
        t.append(0)

        score = 0
        my_score = Score(score)
        my_score.show_score()


        # 初始界面
        def start():
            while True:
                whether_break = False
                screen.blit(background, (0, 0))
                my_score.show_score()

                for i in range(len(block_list)):
                    block_list[i].show_block()
                    block_list[i].show_blood()
                    if block_list[i].y < 100:
                        end = End(my_score.score)
                        end.show_end()

                for i in range(len(ball_list)):
                    ball_list[i].show_ball()

                for i in range(len(add_ball_list)):
                    add_ball_list[i].show_add_ball()

                line = Line(ball_start_x + ball_width / 2, ball_start_y + ball_height / 2)
                line.show_line()

                ball_num_display = font.render(str(ball_num), True, (255, 255, 255))
                screen.blit(ball_num_display, (235, 5))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        for i in range(len(ball_list)):
                            click_x, click_y = pygame.mouse.get_pos()
                            ball_list[i].after_click(click_x, click_y)
                            whether_break = True

                if whether_break == True:
                    break
                pygame.display.update()


        # def t_re(i):
        #     global t
        #     t[i] = 0.0001

        start_or_not = False
        while True:

            screen.blit(start_background, (0, 0))

            start_meum = Start()
            start_meum.show_button()

            for event in pygame.event.get():
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONUP \
                        and (480 - start_meum.button_width) / 2 < mouse_x < (
                        480 - start_meum.button_width) / 2 + start_meum.button_width \
                        and 500 < mouse_y < 500 + start_meum.button_height:
                    start_or_not = True
            if start_or_not == True:
                break
            screen.blit(title, (0, 200))

            # start_word = font.render("开 始 游 戏", True, (255, 255, 255))
            # start_word_rect = start_word.get_rect()
            # start_word_width = start_word_rect.width
            # screen.blit(start_word, ((480 - start_word_width)/2, 527))

            pygame.display.update()

        start()
        difficulty_a = 1
        difficulty_b = 3

        # 游戏界面
        cnt = 0
        while True:
            screen.blit(background, (0, 0))
            my_score.show_score()

            whether_show_start = True
            for i in range(len(ball_list)):
                ball_list[i].show_ball()
                ball_list[i].bump_walls()
                if ball_list[i].speed_y != 0:
                    whether_show_start = False
                if ball_list[i].speed_y == 0:
                    t[i] = 0

            if cnt // 20 < len(ball_list) - 1:
                cnt += 1

            for i in range(cnt // 20 + 1):
                ball_list[i].move_ball()
                ball_list[i].gravity(t[i])
                if ball_list[i].speed_y != 0:
                    t[i] += 0.0001

            for i in range(len(block_list)):
                block_list[i].show_block()
                block_list[i].show_blood()

            for i in range(len(add_ball_list)):
                add_ball_list[i].show_add_ball()

            for i in range(len(block_list)):
                block_list[i].block_bumped(ball_list)
            for i in range(len(block_list)):
                if block_list[i].blood < 1:
                    del block_list[i]
                    break

            for i in range(len(add_ball_list)):
                if add_ball_list[i].add_ball_bumped(ball_list) == 1:
                    ball_num += 1
                    del add_ball_list[i]
                    break

            ball_num_display = font.render(str(ball_num), True, (255, 255, 255))
            screen.blit(ball_num_display, (235, 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pass

            if whether_show_start == True:
                cnt = 0
                for i in range(len(block_list)):
                    block_list[i].y -= 80

                for i in range(random.randint(1, 3)):
                    block = Block(random.randint(0, 480 - 60), random.randint(680, 720), random.randint(0, 3),
                                  random.randint(difficulty_a, difficulty_b))
                    block_list.append(block)
                    difficulty_a += 1
                    difficulty_b += 3

                for i in range(len(add_ball_list)):
                    add_ball_list[i].y -= 80
                for i in range(random.randint(0, 1)):
                    add_ball_list.append(Add_ball(random.randint(0, 480 - add_ball_width), random.randint(680, 720)))
                start()
            pygame.display.update()
    if t4.press(x, y, z):
        pass
    pygame.display.update()