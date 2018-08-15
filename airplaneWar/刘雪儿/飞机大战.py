import pygame
import random

class enemy(object):
    def __init__(self, _screen, _x, _y, _type):
        self.type = _type  # 敌机类型
        self.image = pygame.image.load("images/enemy"+str(self.type)+".png")
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height
        self.speed = [1, 0.7, 0.4]          # 三种敌机的速度
        self.des = [1, 3, 5]                # 三种敌机承受弹数
        self.life = [10, 30, 100]           # 三种敌机的生命值
        self.blood = self.life[self.type]   # 三种敌机的此时血量
        self.t = 30                         # 爆炸显示时间
        self.tt = self.t                    # 辅助变量

    def show(self):
        # if self.type == 2:
        #     sound_enemy3_fly.play()
        self.screen.blit(self.image, (self.x, self.y))
        pygame.draw.line(self.screen, (238, 233, 233), (self.x, self.y+self.h+10), \
                         (self.x+self.w, self.y+self.h+10), 3)
        pygame.draw.line(self.screen, (139, 126, 102), (self.x, self.y + self.h + 10), \
                         (self.x+self.blood/self.life[self.type]*self.w , self.y + self.h + 10), 3)

    def move(self):
        self.y += self.speed[self.type]

    def down(self):
        flag = False
        if self.type == 0 or self.type == 1:       # 第一二类敌机坠落
            if self.life[self.type]//2 < self.blood < self.life[self.type]:
                self.image = pygame.image.load("images/enemy"+str(self.type)+"_down1.png")
            elif 0 < self.blood <= self.life[self.type]//2:
                self.image = pygame.image.load("images/enemy"+str(self.type)+"_down2.png")
            elif self.blood <= 0:
                self.blood = 0
                self.tt -= 1
                sound_enemy[self.type].play()
                if self.tt > self.t//3:
                    self.image = pygame.image.load("images/enemy"+str(self.type)+"_down3.png")
                else:
                    self.image = pygame.image.load("images/enemy"+str(self.type)+"_down4.png")
                    if self.tt == 0:
                            flag = True
        else:                                      # 第三类敌机坠落
            if self.life[self.type]//4*3 < self.blood < self.life[self.type]:
                self.image = pygame.image.load("images/enemy"+str(self.type)+"_down1.png")
            elif self.life[self.type]//4*2 < self.blood <= self.life[self.type]//4*3:
                self.image = pygame.image.load("images/enemy"+str(self.type)+"_down2.png")
            elif self.life[self.type]//4 < self.blood <= self.life[self.type]//4*2:
                self.image = pygame.image.load("images/enemy"+str(self.type)+"_down3.png")
            elif 0 < self.blood <= self.life[self.type]//4:
                self.image = pygame.image.load("images/enemy"+str(self.type)+"_down4.png")
                sound_enemy[self.type].play()
            elif self.blood <= 0:
                self.blood = 0
                self.tt -= 1
                if self.tt > self.t//3:
                    self.image = pygame.image.load("images/enemy"+str(self.type)+"_down5.png")
                else:
                    self.image = pygame.image.load("images/enemy"+str(self.type)+"_down6.png")
                    if self.tt == 0:
                            flag = True
        return flag

    def hit(self):
        if self.type == 1 or self.type == 2:
            self.image = pygame.image.load("images/enemy"+str(self.type)+"_hit.png")
        self.blood = 0

class hero(object):
    def __init__(self, _screen):
        self.screen = _screen
        self.x = 100  # 飞机起始坐标
        self.y = 100
        self.image = pygame.image.load("images\hero.gif")
        self.rect = self.image.get_rect()
        self.w = self.rect.width  # 飞机的大小
        self.h = self.rect.height
        self.life = 100
        self.blood = 100
        self.sub_hit = 10         # 与敌机相撞减去的血量
        self.sub_skip = 20        # 敌机穿过减去的血量（待定）
        self.t = 30  # 爆炸显示时间
        self.tt = self.t  # 辅助变量

    def show(self, mouse_x, mouse_y):
        self.x = mouse_x - self.w / 2
        self.y = mouse_y - self.h / 2
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.line(self.screen, (238, 233, 233), (self.x, self.y + self.h + 10), \
                         (self.x + self.w, self.y + self.h + 10), 3)
        pygame.draw.line(self.screen, (139, 126, 102), (self.x, self.y + self.h + 10), \
                         (self.x + self.blood / self.life * self.w, self.y + self.h + 10), 3)

    def down(self):
        flag = False
        if self.life // 2 < self.blood < self.life:
            self.image = pygame.image.load("images/hero_blowup_n1.png")
        elif 0 < self.blood <= self.life // 2:
            self.image = pygame.image.load("images/hero_blowup_n2.png")
        elif self.blood <= 0:
            self.blood = 0
            self.tt -= 1
            sound_hero.play()
            if self.tt > self.t // 3:
                self.image = pygame.image.load("images/hero_blowup_n3.png")
            else:
                self.image = pygame.image.load("images/hero_blowup_n4.png")
                if self.tt == 0:
                    flag = True
        return flag

class bullet(object):
    def __init__(self, _screen, _type):
        self.screen = _screen
        self.type = _type  #该子弹是由谁发出的 0为英雄，1为敌机
        self.x = []  # 每颗子弹当前坐标
        self.y = []
        self.v = 10  # 子弹发射的频率
        self.speed = 3  # 子弹移动的速度
        self.energy = 5
        self.image = pygame.image.load(r"images\bullet1.png")
        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height
        self.t = self.v

    def show(self):
        for i in range(len(self.x)):
            screen.blit(self.image, (self.x[i], self.y[i]))
            if self.y[i] >= -self.h:  # 没超出屏幕时才可移动，防止超出子弹打中敌机
                self.y[i] -= self.speed
            else:
                self.y[i] = -800  # 子弹移至屏幕外

    def hero_load(self, mouse_x, mouse_y, h):
        if self.t:
            self.t -= 1
        else:
            self.x.append(mouse_x - self.w / 2)
            self.y.append(mouse_y - h / 2 - self.h)
            sound_bullet.play()
            self.t = self.v

    def enemy_load(self):
        pass

    def eliminate(self):
        for i in self.y:
            index = self.y.index(i)
            if i <= -800:
                self.x.pop(index)
                self.y.pop(index)


# 屏幕信息
window_w = 500
window_h = 800

# 初始化
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((window_w, window_h))
font = pygame.font.Font("C:\Windows\Fonts\STCAIYUN.TTF", 26)

# 图片加载
bg = pygame.transform.scale(pygame.image.load(r"images\background.png"), (window_w, window_h))  # 背景

name = pygame.image.load(r"images\name.png")         # 游戏名
start1 = pygame.image.load(r"images\star.jpg")       # 开始游戏图标
start2 = pygame.transform.scale(start1, (start1.get_rect().width - 2*3, start1.get_rect().height - 2*3))

pause1 = pygame.image.load(r"images\game_pause_nor.png")       # 游戏暂停图标 & 游戏重新开始图标
pause2 = pygame.image.load(r"images\game_pause_pressed.png")
resume1 = pygame.image.load(r"images\game_resume_nor.png")
resume2 = pygame.image.load(r"images\game_resume_pressed.png")

icon_resume = pygame.image.load(r"images\resume_sel.png")     # 游戏暂停时显示文字
icon_restart = pygame.image.load(r"images\restart_sel.png")
icon_quit = pygame.image.load(r"images\quit_sel.png")

l_load = []                    # 游戏加载中显示图片
for i in range(4):
    l_load.append(pygame.image.load("images\game_loading"+str(i+1)+".png"))

# 声音加载
sound_enemy = []
sound_enemy.append(pygame.mixer.Sound(r"sound\enemy1_down.wav"))
sound_enemy.append(pygame.mixer.Sound(r"sound\enemy2_down.wav"))
sound_enemy.append(pygame.mixer.Sound(r"sound\enemy3_down.wav"))

# sound_enemy3_fly = pygame.mixer.Sound(r"sound\enemy3_flying.wav")
sound_bullet = pygame.mixer.Sound(r"sound\bullet.wav")
sound_game = pygame.mixer.Sound(r"sound\game_music.wav")

sound_hero = pygame.mixer.Sound(r"sound\me_down.wav")

# 图片信息
start1_w = start1.get_rect().width        # 开始游戏图标
start1_h = start1.get_rect().height
start1_x = window_w//2 - start1_w//2
start1_y = window_h//2 - start1_h//2

pause_x = 10                              # 暂停游戏图标
pause_y = 10
pause_w = pause1.get_rect().width
pause_h = pause1.get_rect().height

icon_resume_w = icon_resume.get_rect().width   # 继续游戏文字
icon_resume_h = icon_resume.get_rect().height
icon_resume_x = window_w//2 - icon_resume_w//2
icon_resume_y = window_h//3

icon_restart_w = icon_restart.get_rect().width   # 重新开始文字
icon_restart_h = icon_restart.get_rect().height
icon_restart_x = window_w//2 - icon_restart_w//2
icon_restart_y = icon_resume_y + 90

icon_quit_w = icon_quit.get_rect().width   # 退出游戏文字
icon_quit_h = icon_quit.get_rect().height
icon_quit_x = window_w//2 - icon_quit_w//2
icon_quit_y = icon_restart_y + 90

# 对象初始化
l_e = []
l_e.append(enemy(screen, random.randint(0, window_w-100), -300, 0))  # 0为敌机型号
hero1 = hero(screen)
bullet1 = bullet(screen, 0)
enemy_bullet = []

# 辅助变量
game_wait_flag = True   # 等待游戏开始界面标志
game_start_flag = False  # 游戏开始标志
game_stop_flag = False  # 游戏暂停标志

b_v = bullet1.v         # 子弹出现频率
e_v = 200               # 敌机出现频率

start_t = 200           # 游戏等待开始时间
game_over_time = 500    # 输时相应时间
hero_die_flag = False   # 英雄死亡标志
score = 0               # 记录分数
start_tt = start_t      # 辅助变量
time_e = e_v            # 辅助变量，计算敌机出来时间

sound_game.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.blit(bg, (0, 0))

    # 当按下暂停键时改变游戏状态
    if pause_x <= mouse_x <= pause_x+pause_w and pause_y <= mouse_y <= pause_y+pause_h \
            and pygame.mouse.get_pressed() == (1, 0, 0):
        screen.blit(pause1, (pause_x, pause_y))
        game_start_flag = False
        game_wait_flag = False
        game_stop_flag = True

    # 当游戏暂停时显示的页面
    if game_stop_flag:
        screen.blit(resume1, (pause_x, pause_y))
        screen.blit(icon_resume, (icon_resume_x, icon_resume_y))
        screen.blit(icon_restart, (icon_restart_x, icon_restart_y))
        screen.blit(icon_quit, (icon_quit_x, icon_quit_y))

    # 位于暂停页面时
    if game_stop_flag and pygame.mouse.get_pressed() == (1, 0, 0):
        # 按下继续按钮
        if icon_resume_x <= mouse_x <= icon_resume_x+icon_resume_w and \
                icon_resume_y <= mouse_y <= icon_resume_y+icon_resume_h:
            game_stop_flag = False
            game_start_flag = True
        # 按下重新开始按钮
        elif icon_restart_x <= mouse_x <= icon_restart_x+icon_restart_w and \
                icon_restart_y <= mouse_y <= icon_restart_y+icon_restart_h:
            game_stop_flag = False
            game_wait_flag = True
        # 按下退出游戏按钮
        elif icon_quit_x <= mouse_x <= icon_quit_x+icon_quit_w and \
                icon_quit_y <= mouse_y <= icon_quit_y+icon_quit_h:
            exit()

    # 当游戏没正式开始
    if game_wait_flag:
        # 对象重新初始化
        l_e = []
        l_e.append(enemy(screen, random.randint(0, window_w - 100), -300, 0))  # 0为敌机型号
        hero1 = hero(screen)
        bullet1 = bullet(screen, 0)
        enemy_bullet = []
        # 辅助变量重新初始化
        score = 0
        game_over_time = 500
        hero_die_flag = False
        start_tt = start_t  # 辅助变量
        time_e = e_v        # 辅助变量，计算敌机出来时间

        # 页面显示
        screen.blit(name, (30, 100))
        if start1_x <= mouse_x <= start1_x+start1_w and \
                start1_y <= mouse_y <= start1_y+start1_h and \
                pygame.mouse.get_pressed() == (1, 0, 0):
            screen.blit(start2, (start1_x+3, start1_y+3))
            game_start_flag = True
            game_wait_flag = False
        else:
            screen.blit(start1, (start1_x, start1_y))

    # 当游戏正式开始
    if game_start_flag:
        if start_tt:                   # 游戏加载页面
            if start_t//4*3 < start_tt <= start_t:
                screen.blit(l_load[0], (window_w//3, window_h//3))
            elif start_t//4*2 < start_tt <= start_t//4*3:
                screen.blit(l_load[1], (window_w//3+5, window_h // 3))
            elif start_t // 4*1 < start_tt <= start_t // 4*2:
                screen.blit(l_load[2], (window_w//3+10, window_h // 3))
            else:
                screen.blit(l_load[3], (window_w//3+15, window_h // 3))
            start_tt -= 1
        elif hero_die_flag:        # 当敌机死了
            if game_over_time:
                game_over_text = font.render("you lose!", True, (28, 28, 28))
                score_text = font.render("你的分数为："+str(score), True, (28, 28, 28))
                screen.blit(game_over_text, (window_w//3+25, window_h//3))
                screen.blit(score_text, (window_w//3, window_h//3+50))
                game_over_time -= 1
            else:
                game_start_flag = False
                game_wait_flag = True
        else:                        # 游戏加载完成
            hero_die_flag = hero1.down()
            # 英雄显示
            hero1.show(mouse_x, mouse_y)
            # 暂停键显示
            screen.blit(pause1, (pause_x, pause_y))
            # 分数显示
            score_text = font.render("分数:"+str(score), True, (28, 28, 28))
            screen.blit(score_text, (pause_x, pause_y+50))

            # 子弹装载
            bullet1.hero_load(mouse_x, mouse_y, hero1.h)

            # 敌机装载
            if time_e:
                time_e -= 1
            else:
                type = random.randint(0, 2)
                e = enemy(screen, random.randint(0, window_w - 100), -300, type)
                l_e.append(e)
                # if type == 1 or type == 2:  # 敌机类型为1和2的会发出子弹
                #     enemy_bullet.append(bullet(screen, 1, len(l_e)))
                time_e = e_v

            # 清除子弹
            bullet1.eliminate()                         # 清除英雄超屏的子弹
            # for i in range(len(enemy_bullet)):          # 清除敌机超屏的子弹
            #     for j in enemy_bullet[i].x:
            #         index = enemy_bullet[i].x.index(j)
            #         if j>=window_h:
            #             enemy_bullet[i].x.pop(index)
            #             enemy_bullet[i].y.pop(index)

            # 清除敌机
            for i in l_e:
                index = l_e.index(i)
                if i.y <= -700 or i.y > window_h:
                    l_e.pop(index)

            # 子弹显示
            bullet1.show()

            # 敌机显示 & 敌机穿过判定 & 飞机与敌机碰撞判定
            for i in range(len(l_e)):  # 敌机显示
                if l_e[i].down():  # 只有炸毁完毕敌机才能放置在屏幕外
                    l_e[i].y = -800
                    score += 1
                l_e[i].show()
                l_e[i].move()

                if l_e[i].y >= window_h:  # 敌机穿过判定
                    hero1.blood -= hero1.sub_skip

                # 飞机与敌机碰撞判定
                if (hero1.x >= l_e[i].x and hero1.y >= l_e[i].y and \
                    hero1.x + hero1.w <= l_e[i].x + l_e[i].w and hero1.y + hero1.h <= l_e[i].y + l_e[i].h) or \
                        (l_e[i].x >= hero1.x and l_e[i].y >= hero1.y and \
                         l_e[i].x + l_e[i].w <= hero1.x + hero1.w and l_e[i].h + l_e[i].y <= hero1.y + hero1.h):
                    l_e[i].hit()
                    hero1.blood -= hero1.sub_hit

            # 子弹与敌机碰撞判定
            for i in range(len(bullet1.x)):
                for j in range(len(l_e)):
                    if l_e[j].x <= bullet1.x[i] <= l_e[j].x + l_e[j].w and \
                            l_e[j].y <= bullet1.y[i] <= l_e[j].y + l_e[j].h:
                        l_e[j].blood -= bullet1.energy  # 敌机血量减少
                        if l_e[j].blood < 0:
                            l_e[j].blood = 0
                        bullet1.y[i] = -800  # 子弹移至屏幕外

    pygame.display.update()