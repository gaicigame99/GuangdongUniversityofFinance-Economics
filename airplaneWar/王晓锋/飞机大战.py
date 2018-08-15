import pygame
import random
import time

# 飞机大战
# 手机上，单手操作
# 长条形
# 鼠标操作模拟触屏操作

pygame.init()
pygame.mixer.init()

# pygame.mixer


class Plane(object):
    # 父类飞机
    def __init__(self, _screen, _str, _bullet, _bullet_pd, _blood_pd):
        self.screen = _screen
        self.image = pygame.image.load(_str[0])
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        # 创建子弹
        self.bullets = []
        self.bullet_Hz = _bullet
        self.bullet_pd = _bullet_pd
        self.time = 0
        # 血量
        self.blood = _str[7]  # 初始血量
        self.now_blood = self.blood
        self.blood_pd = _blood_pd
        # 飞机坠毁图
        self.image1 = pygame.image.load(_str[1])
        self.image2 = pygame.image.load(_str[2])
        self.image3 = pygame.image.load(_str[3])
        self.image4 = pygame.image.load(_str[4])
        self.image5 = pygame.image.load(_str[5])
        self.image6 = pygame.image.load(_str[6])
        self.start_time = 0

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 展示血量  pd 判断，0为敌方，1为己方
    def show_blood(self):
        length = self.rect.width / self.blood
        blood_x0 = self.x + length / 10
        blood_x1 = self.x + length * 9 / 10
        blood_y = self.y + self.rect.height * self.blood_pd
        for n in range(self.now_blood):
            pygame.draw.line(self.screen, (25, 175, 25), (blood_x0, blood_y), (blood_x1, blood_y), 2)
            blood_x0 += length
            blood_x1 += length
        for n in range(self.blood - self.now_blood):
            pygame.draw.line(self.screen, (169, 169, 169), (blood_x0, blood_y), (blood_x1, blood_y), 2)
            blood_x0 += length
            blood_x1 += length

    # 添加&展示子弹 pd 判断，1为敌方，-1为己方
    def add_bullet(self):
        # 为飞机加子弹
        if self.time:
            self.time -= 1
        else:
            bullet = Bullet(self.screen, self.x, self.y, self.rect, 4, self.bullet_pd)
            self.bullets.append(bullet)
            self.time = self.bullet_Hz

        # 展示子弹
        for n in range(len(self.bullets)):
            self.bullets[n].show()
            self.bullets[n].y += self.bullets[n].speed

    # 判断子弹是否打中飞机
    # 打中飞机清除子弹，去掉对方一滴血
    def pd_bullet(self, other):
        n = 0
        while True:
            if n == len(self.bullets) or len(self.bullets) == 0:
                break
            if self.bullets[n].collection(other):
                self.bullets.pop(n)
                if other.now_blood > 0:
                    other.now_blood -= 1
                n -= 1
            n += 1

    # 清除出界的子弹 大于上界或者下界
    def delete_bullet(self):
        if len(self.bullets) > 0:
            if self.bullets[0].y < -self.bullets[0].rect.height or\
                    self.bullets[0].y > self.screen.get_height() + self.bullets[0].rect.height:
                self.bullets.pop(0)

    # 本飞机与其他飞机的 碰撞检测
    def collection(self, other):
        if self.x + self.rect.width > other.x and \
                self.x < other.x + other.rect.width and \
                self.y < other.y + other.rect.height and \
                self.y + self.rect.height > other.y:
            return True
        else:
            return False

    # 血量为零，飞机坠毁
    # 1秒播放5张图片，播放1秒
    def show_destroy(self):
        if self.now_blood == 0:
            if time.time() - self.start_time <= 0.2:
                self.screen.blit(self.image, (self.x, self.y))
            elif 0.2 < time.time() - self.start_time <= 0.4:
                self.screen.blit(self.image1, (self.x, self.y))
            elif 0.4 < time.time() - self.start_time <= 0.6:
                self.screen.blit(self.image2, (self.x, self.y))
            elif 0.6 < time.time() - self.start_time <= 0.8:
                self.screen.blit(self.image3, (self.x, self.y))
            elif 0.8 < time.time() - self.start_time <= 1.0:
                self.screen.blit(self.image4, (self.x, self.y))
            elif 1.0 < time.time() - self.start_time <= 1.2:
                self.screen.blit(self.image5, (self.x, self.y))
            elif 1.2 < time.time() - self.start_time <= 1.4:
                self.screen.blit(self.image6, (self.x, self.y))
        else:
            self.start_time = time.time()
            return 0
        return 1


class Hero(Plane):
    # 玩家飞机
    def __init__(self, _screen, _str, _bullet):
        Plane.__init__(self, _screen, _str, _bullet, -1, 1)
        self.screen = _screen
        self.image = pygame.image.load(r"images\hero.gif")
        self.rect = self.image.get_rect()

    def move(self, _x, _y):
        self.x = _x - self.rect.width / 2
        if _y - self.rect.height / 2 >= self.screen.get_height() / 2:
            self.y = _y - self.rect.height / 2

    # 判断是否与敌机相撞
    # 是，血量都归零
    # # 未完善
    # def pd_impact(self, other):
    #     n = 0
    #     while True:
    #         if len(other) == 0:
    #             break
    #         for m in
    #         if self.collection(other[n]):
    #             other[n].now_blood = 0
    #             self.now_blood = 0
    #             n -= 1
    #         n += 1


class Enemy(Plane):
    # 敌人飞机
    def __init__(self, _screen, _str, _bullet):
        Plane.__init__(self, _screen, _str, _bullet, 1, 0)
        self.x = random.randint(self.rect.width, _screen.get_width() - self.rect.width)
        self.y = -self.rect.height
        self.speed = _str[8]


class Bullet(object):
    def __init__(self, _screen, _x, _y, plane_rect, _speed, _dir=1):  # x,y要传入飞机的坐标，而不是鼠标的
        self.screen = _screen
        self.image = pygame.image.load(r"images\bullet1.png")
        self.rect = self.image.get_rect()
        self.x = _x - self.rect.width / 2 + plane_rect.width / 2
        if _dir == 1:
            self.y = _y + _dir * plane_rect.height
        elif _dir == -1:
            self.y = _y + _dir * self.rect.height
        self.speed = _speed * _dir

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    def collection(self, other):
        if self.x + self.rect.width > other.x and \
                self.x < other.x + other.rect.width and \
                self.y < other.y + other.rect.height and \
                self.y + self.rect.height > other.y:
            return True
        else:
            return False


class Button(object):
    def __init__(self, _screen, _str, _x_dir=1.0, _y_dir=1.0):
        self.screen = _screen
        self.image_nor = pygame.image.load(_str[0])
        self.image_pressed = pygame.image.load(_str[1])
        self.rect = self.image_nor.get_rect()
        self.x = (self.screen.get_width() - self.rect.width) * _x_dir
        self.y = (self.screen.get_height() - self.rect.height) * _y_dir
        self.mark = 0

    # 展示按钮，并判断按钮是否被点击，点击返回1
    def pd_button_show(self, _mouse_x, _mouse_y):
        if self.x < _mouse_x < self.x + self.rect.width and\
                self.y < _mouse_y < self.y + self.rect.height and a:
            screen.blit(self.image_pressed, (self.x, self.y))
            self.mark = 1
        else:
            if self.mark == 1:
                # self.mark = 0
                return 1
            else:
                screen.blit(self.image_nor, (self.x, self.y))
        return 0


screen = pygame.display.set_mode((500, 800))

background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (500, 800))

# 初始化 玩家飞机
hero_key = list()
hero_key.append([r"images\hero.png", r"images\hero_blowup1.png",
                 r"images\hero_blowup2.png", r"images\hero_blowup3.png",
                 r"images\hero_blowup4.png", r"images\hero_blowup5_6.png",
                 r"images\hero_blowup5_6.png", 5])
hero = Hero(screen, hero_key[0],  15)

# 初始化 敌方飞机
enemy_key = list()
enemy_key.append([r"images\enemy0.png", r"images\enemy0_down1.png",
                  r"images\enemy0_down2.png", r"images\enemy0_down3.png",
                  r"images\enemy0_down4.png", r"images\enemy0_down5_6.png",
                  r"images\enemy0_down5_6.png", 1, 1])
enemy_key.append([r"images\enemy1.png", r"images\enemy1_down1.png",
                  r"images\enemy1_down2.png", r"images\enemy1_down3.png",
                  r"images\enemy1_down4.png", r"images\enemy1_down5_6.png",
                  r"images\enemy1_down5_6.png", 3, 0.75])
enemy_key.append([r"images\enemy2.png", r"images\enemy2_down1.png",
                  r"images\enemy2_down2.png", r"images\enemy2_down3.png",
                  r"images\enemy2_down4.png", r"images\enemy2_down5.png",
                  r"images\enemy2_down6.png", 5, 0.5])
enemy = list()

# 开始界面
# 游戏名称
game_name = pygame.image.load(r"images\name.png")
name_rect = game_name.get_rect()
name_x = (screen.get_width() - name_rect.width)/2
name_y = 100

# 游戏按钮
# 开始时的开始按钮
start_key = [r"images\game_start_nor.png", r"images\game_start_pressed.png"]
start_button = Button(screen, start_key, 0.5, 0.5)
# 游戏中的暂停按钮
pause_key = [r"images\game_pause_nor.png", r"images\game_pause_pressed.png"]
pause_button = Button(screen, pause_key)

# 暂停后出现的按钮
# 继续
resume_key = [r"images\resume_nor.png", r"images\resume_sel.png"]
resume_button = Button(screen, resume_key, 0.5, 0.4)
# 重新开始
restart_key = [r"images\restart_nor.png", r"images\restart_sel.png"]
restart_button = Button(screen, restart_key, 0.5, 0.5)
# 退出游戏
quit_key = [r"images\quit_nor.png", r"images\quit_sel.png"]
quit_button = Button(screen, quit_key, 0.5, 0.6)

# 判断游戏是否开始
game_start = 0
game_start_time = 60

# 结束界面
game_over = pygame.image.load(r"images\gameover.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pressed_mouse = pygame.mouse.get_pressed()
        #     if pressed_mouse[0]:
        #         x, y = pygame.mouse.get_pos()
        #         bullet_x.append(x)
        #         bullet_y.append(y)

    screen.blit(background, (0, 0))

    a, b, c = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 开始游戏逻辑
    if game_start == 0:
        # 游戏未开始，刷新敌我飞机，刷新开始界面
        name_y = 100
        enemy = list()
        for i in range(3):
            for j in range(3-i):
                enemy.append(Enemy(screen, enemy_key[i], 80))
        hero = Hero(screen, hero_key[0], 15)
        game_start = start_button.pd_button_show(mouse_x, mouse_y)

    if game_start:
        game_start_time -= 1
        if name_y > -name_rect.height:
            name_y -= 3

    if game_start and game_start_time < 0:
        # 暂停后的界面
        if pause_button.pd_button_show(mouse_x, mouse_y):
            if resume_button.pd_button_show(mouse_x, mouse_y):
                pause_button.mark = 0
                resume_button.mark = 0
            if restart_button.pd_button_show(mouse_x, mouse_y):
                game_start = 0
                game_start_time = 60
                start_button.mark = 0
                restart_button.mark = 0
                pause_button.mark = 0
            if quit_button.pd_button_show(mouse_x, mouse_y):
                exit()
        else:
            # 游戏进程
            # 判断飞机是否坠毁
            if hero.show_destroy():
                pass
            else:
                hero.move(mouse_x, mouse_y)
                hero.show()
                hero.add_bullet()  # 玩家　加&射出子弹
                if len(enemy):
                    for i in range(len(enemy)):
                        hero.pd_bullet(enemy[i])    # 判断子弹是否打中飞机
                    # hero.pd_impact(enemy)
                hero.delete_bullet()    # 清除出界的子弹
                hero.show_blood()    # 展示血量

            if len(enemy):
                for i in range(len(enemy)):
                    if enemy[i].show_destroy():
                        pass
                    else:
                        enemy[i].show()
                        enemy[i].add_bullet()  # 敌方　加&射出子弹
                        enemy[i].pd_bullet(hero)  # 判断子弹是否打中飞机
                        enemy[i].delete_bullet()  # 清除出界的子弹
                        enemy[i].show_blood()    # 展示血量
                        enemy[i].y += enemy[i].speed
    else:
        screen.blit(game_name, (name_x, name_y))

    pygame.display.update()
