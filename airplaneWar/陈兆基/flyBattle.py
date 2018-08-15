import pygame
import random
import time

# 飞机大战
# 键盘操作

pygame.init()

# 设置窗口标题
pygame.display.set_caption("飞机大战")
pygame.mixer.init()  # 声音初始化
screen = pygame.display.set_mode((480, 852))
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 72)
font2 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 24)

back_music = pygame.mixer.Sound('sound/game_music.ogg')
back_music.play()
background = pygame.image.load('images/background.png')
back_game = pygame.image.load('images/btn_finish.png')


# 开始界面
class start_main():
    def __init__(self, _screen):
        self.name = pygame.image.load('images/name.png')  # 最上面飞机大战的字
        self.quit_sel = pygame.image.load('images/quit_sel.png')  # 退出游戏（还没实现）
        self.restart_sel = pygame.image.load('images/restart_sel.png')  # 重新开始（还没实现）
        self.resume_sel = pygame.image.load('images/resume_sel.png')  # 继续（还没实现）
        self.loading = pygame.image.load('images/loading.png')  # 等待界面
        self.screen = _screen
        self.name_x = 20
        self.name_y = 0
        self.quit_sel_x = 195     # 设置图片的初始位置x与y
        self.quit_sel_y = 500
        self.restart_sel_x = 195
        self.restart_sel_y = 400
        self.resume_sel_x = 220
        self.resume_sel_y = 300
        self.start_text_x = 150
        self.start_text_y = 800
        self.screen.blit(self.name, (self.name_x, self.name_y))  # 加载图片
        self.screen.blit(self.quit_sel, (self.quit_sel_x, self.quit_sel_y))
        self.screen.blit(self.restart_sel, (self.restart_sel_x, self.restart_sel_y))
        self.screen.blit(self.resume_sel, (self.resume_sel_x, self.resume_sel_y))
        self.game_start_time = 10000000  # 游戏计时器

    def start(self):
        start_text = font2.render('点击空白部分开始', True, (0, 0, 0, 0))
        self.screen.blit(start_text, (self.start_text_x, self.start_text_y))
        start_text2 = font2.render('方向盘进行游戏', True, (0, 0, 0, 0))
        self.screen.blit(start_text2, (self.start_text_x+10, self.start_text_y-50))
        self.screen.blit(self.name, (self.name_x, self.name_y))
        self.screen.blit(self.quit_sel, (self.quit_sel_x, self.quit_sel_y))
        self.screen.blit(self.restart_sel, (self.restart_sel_x, self.restart_sel_y))
        self.screen.blit(self.resume_sel, (self.resume_sel_x, self.resume_sel_y))
        self.x, self.y, self.z = pygame.mouse.get_pressed()  # 获得鼠标的点击建
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()  # 获得鼠标当前位置
        if ((0 <= self.mouse_x <= 195 and 0 <= self.mouse_y <= 852)\
                or (0 <= self.mouse_x <= 480 and (0 <= self.mouse_y <= 300 or 550 <= self.mouse_y <= 852)) \
                    or (305 <= self.mouse_x <= 480 and 0 <= self.mouse_y <= 852))\
                    and self.x:  # 当鼠标停在空白处，并且单击左键时，移除开始界面，进入游戏界面
            self.name_x, self.name_y = 10000, 10000
            self.restart_sel_x, self.restart_sel_y = 10000, 10000
            self.resume_sel_x, self.resume_sel_y = 10000, 10000
            self.quit_sel_x, self.quit_sel_y = 10000, 10000
            self.start_text_x, self.start_text_y = 10000, 10000
            while self.game_start_time >= 0:
                self.game_start_time -= 1


# 英雄机类
class hero(object):
    def __init__(self, _screen, _hero_png, _x, _y):  # 初始化战机的初始位置xy，血量和血量图片
        self.x = _x
        self.y = _y
        self.hero = pygame.image.load(_hero_png)
        self.screen = _screen
        self.life = 5
        self.life_png = []

    def show(self, enemy):  # 显示战机方法
        hero_rect = self.hero.get_rect()  # 得到战机的宽和高
        hero_width = hero_rect.width
        hero_height = hero_rect.height
        # self.x, self.y = pygame.mouse.get_pos()  # 鼠标控制
        press_keys = pygame.key.get_pressed()
        if press_keys[pygame.K_LEFT]:
            if self.x >= hero_width//2:
                self.x -= 10
        if press_keys[pygame.K_RIGHT]:
            if self.x <= 480-hero_width // 2:
                self.x += 10
        if press_keys[pygame.K_UP]:
            if self.y >= hero_height:
                self.y -= 10
        if press_keys[pygame.K_DOWN]:
            if self.y <= 852-hero_height//2:
                self.y += 10
        if self.life >= 0:  # 如果战机的血量大于0则会显示战机
            self.screen.blit(self.hero, (self.x - hero_width//2, self.y - hero_height//2))
        else:
            pass

        for i in range(self.life):  # 显示战机的血量
            self.life_png.append(pygame.image.load('images/life.png'))
            self.screen.blit(self.life_png[i], (434-i*50, 0))

        enemy_rect = enemy.enemy.get_rect()
        enemy_width = enemy_rect.width
        enemy_height = enemy_rect.height
        for j in range(len(enemy.x)):  # 如果战机与敌机碰撞，则战机的血量-1(还不完善)
            if enemy.x[j] <= self.x <= enemy.x[j] + enemy_width and \
                    enemy.y[j] <= self.y <= enemy.y[j] + enemy_height:
                self.life -= 1


# 敌机类
class enemy(object):
    def __init__(self, _screen, _enemy_png, _enemy_down1_png, _enemy_down2_png,
                 _enemy_down3_png, _enemy_down4_png, _speed, _time, _blood):  # 初始化敌机
        self.enemy = pygame.image.load(_enemy_png)
        self.x = []
        self.y = []
        self.speed = _speed
        self.time = _time
        self.tmp_time = _time
        self.screen = _screen
        self.enemy_down1 = pygame.image.load(_enemy_down1_png)  # 敌机销毁图片
        self.enemy_down2 = pygame.image.load(_enemy_down2_png)
        self.enemy_down3 = pygame.image.load(_enemy_down3_png)
        self.enemy_down4 = pygame.image.load(_enemy_down4_png)
        self.boom_action = []
        self.boom_action.append(self.enemy_down1)
        self.boom_action.append(self.enemy_down2)
        self.boom_action.append(self.enemy_down3)
        self.boom_action.append(self.enemy_down4)
        self.blood = _blood  # 敌机血量
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_width = self.enemy_rect.width
        self.enemy_height = self.enemy_rect.height
        if _blood == 1:  # 按照不同的敌机血量，将血量放入不同的临时血量组
            self.tmp_blood1 = []
        if _blood == 5:
            self.tmp_blood2 = []
        if _blood == 10:
            self.tmp_blood3 = []

    def num_enemy(self):  # 生产敌机方法
        if self.time:  # 生产敌机的频率
            self.time -= 1
        else:
            self.x.append(random.randint(0, 480-self.enemy_width))
            self.y.append(random.randint(-self.enemy_height-300, -self.enemy_height))
            if self.blood == 1:  # 根据一开始初始化敌机的血量按照对应关系放入
                self.tmp_blood1.append(1)
            if self.blood == 5:
                self.tmp_blood2.append(5)
            if self.blood == 10:
                self.tmp_blood3.append(10)
            self.time = self.tmp_time  # 重置频率

    def show(self):  # 显示敌机
        for i in range(len(self.x)):  # 根据初始化的时候敌机出现的频率出现敌机
            self.y[i] += self.speed
            self.screen.blit(self.enemy, (self.x[i], self.y[i]))
            # 根据血量不同在敌机下方显示血条，并根据临时血量控制血条长度
            if self.blood == 1:
                pygame.draw.line(self.screen, (255, 0, 0), (self.x[i], self.y[i] + self.enemy_height + 3),
                                 (self.x[i] + self.tmp_blood1[i]*self.enemy_width//self.blood, self.y[i] + self.enemy_height + 3), 3)
            if self.blood == 5:
                pygame.draw.line(self.screen, (255, 0, 0), (self.x[i], self.y[i] + self.enemy_height + 3),
                                 (self.x[i] + self.tmp_blood2[i]*self.enemy_width//self.blood, self.y[i] + self.enemy_height + 3), 3)
            if self.blood == 10:
                pygame.draw.line(self.screen, (255, 0, 0), (self.x[i], self.y[i] + self.enemy_height + 3),
                                 (self.x[i] + self.tmp_blood3[i]*self.enemy_width//self.blood, self.y[i] + self.enemy_height + 3), 3)

    def boom(self):  # 敌机爆炸方法（还没实现）
        for i in range(len(self.x)):
            for j in range(len(enemy.x)):
                if (self.blood == 1 and self.tmp_blood1[j] == 1) or \
                (enemy.blood == 5 and enemy.tmp_blood2[j] == 1) or \
                (enemy.blood == 10 and enemy.tmp_blood3[j] == 1):
                    pass


# 子弹类
class bullet(object):
    def __init__(self, _screen, _speed, _time):  # 初始化子弹
        self.bullet = pygame.image.load('images/bullet.png')
        self.x = []
        self.y = []
        self.speed = _speed
        self.time = _time
        self.tmp_time = _time
        self.screen = _screen
        self.boom_time = 0
        self.score = 0
        self.score_image = pygame.image.load('images/score.png')  # 得到分数的图片
        self.font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 26)  # 得到分数的字体
        self.score_text = self.font.render(str(self.score), True, (0, 0, 0, 0))

    def show(self):  # 显示子弹和分数
        for i in range(len(self.x)):
            self.y[i] -= self.speed
            self.screen.blit(self.bullet, (self.x[i] - 11, self.y[i] - 73))
            self.screen.blit(self.score_image, (0, 0))
            self.score_text = self.font.render(str(self.score), True, (0, 0, 0, 0))
            self.screen.blit(self.score_text, (51, 0))

    def collision(self, enemy):  # 碰撞检测
        enemy_rect = enemy.enemy.get_rect()  # 得到敌机的宽和高
        enemy_width = enemy_rect.width
        enemy_height = enemy_rect.height
        for i in range(len(self.x)):  # 检验每一颗子弹与每一架敌机是否发生碰撞
            for j in range(len(enemy.x)):
                if enemy.x[j] <= self.x[i] <= enemy.x[j] + enemy_width and \
                        enemy.y[j] <= self.y[i] <= enemy.y[j]+enemy_height:
                    self.x[i], self.y[i] = 10000, 10000
                    # 如果是，根据血量得到击败哪种类型的敌机并增加分数
                    if (enemy.blood == 1 and enemy.tmp_blood1[j] == 1) or \
                            (enemy.blood == 5 and enemy.tmp_blood2[j] == 1) or\
                            (enemy.blood == 10 and enemy.tmp_blood3[j] == 1):
                        if enemy.blood == 1:
                            self.score += 1
                        elif enemy.blood == 5:
                            self.score += 2
                        else:
                            self.score += 3
                        # 爆炸特效（没有实现）
                        if time.time() - self.boom_time >= 0.2:
                            self.screen.blit(enemy.enemy_down1, (enemy.x[j], enemy.y[j]))
                        elif time.time() - self.boom_time >= 0.4:
                            self.screen.blit(enemy.enemy_down2, (enemy.x[j], enemy.y[j]))
                        elif time.time() - self.boom_time >= 0.6:
                            self.screen.blit(enemy.enemy_down3, (enemy.x[j], enemy.y[j]))
                        else:
                            self.screen.blit(enemy.enemy_down4, (enemy.x[j], enemy.y[j]))
                        enemy.x[j], enemy.y[j] = 10000, 10000
                    # 如果不是，将敌机的血量降低
                    else:
                        if enemy.blood == 1:
                            enemy.tmp_blood1[j] -= 1
                        if enemy.blood == 5:
                            enemy.tmp_blood2[j] -= 1
                        if enemy.blood == 10:
                            enemy.tmp_blood3[j] -= 1

    def shot(self, hero):  # 生产子弹方法
        if self.time:
            self.time -= 1
        else:
            self.x.append(hero.x)
            self.y.append(hero.y)
            self.time = self.tmp_time


# 清理生产出来的子弹和敌机，防止卡屏
def clear_list(bullet, enemy):
    if len(bullet.x) > 100:
        del bullet.x[1:50]
        del bullet.y[1:50]

    if len(enemy.y) > 100:
        del enemy.x[1:50]
        del enemy.y[1:50]


# 初始化
main = start_main(screen)
hero1 = hero(screen, 'images/hero.gif', 200, 700)
bullet1 = bullet(screen, 10, 5)
enemy0 = enemy(screen, 'images/enemy0.png', 'images/enemy0_down1.png',
               'images/enemy0_down2.png', 'images/enemy0_down3.png', 'images/enemy0_down4.png', 5, 40, 1)
enemy1 = enemy(screen, 'images/enemy1.png', 'images/enemy1_down1.png',
               'images/enemy1_down2.png', 'images/enemy1_down3.png', 'images/enemy1_down4.png', 3, 100, 5)
enemy2 = enemy(screen, 'images/enemy2.png', 'images/enemy2_down1.png',
               'images/enemy2_down2.png', 'images/enemy2_down3.png', 'images/enemy2_down4.png', 1, 400, 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))

    main.start()
    # 进入游戏界面
    if main.game_start_time <= 0 and hero1.life != 0:
        hero1.show(enemy0)
        hero1.show(enemy1)
        hero1.show(enemy2)

        bullet1.show()

        enemy0.num_enemy()
        enemy0.show()

        enemy1.num_enemy()
        enemy1.show()

        enemy2.num_enemy()
        enemy2.show()

        bullet1.shot(hero1)
        bullet1.collision(enemy0)
        bullet1.collision(enemy1)
        bullet1.collision(enemy2)

        clear_list(bullet1, enemy0)
        clear_list(bullet1, enemy1)
        clear_list(bullet1, enemy2)
    # 游戏结束界面
    elif hero1.life == 0:
        screen.blit(pygame.image.load('images/gameover.png'), (0, 0))
        score_text = font.render(str(bullet1.score), True, (0, 0, 0, 0))
        screen.blit(score_text, (214, 600))

    pygame.display.update()