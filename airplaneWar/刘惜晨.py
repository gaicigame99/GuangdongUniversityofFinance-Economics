import pygame
import random

def collection(a_x,a_y,a_w,a_h,b_x,b_y,b_w,b_h):
    if a_w + a_x > b_x and \
            a_x < b_w + b_x and \
            a_y <= b_h + b_y  and \
            a_h + a_y > b_y :
        return True
    else:
        return False
class bullet:
    def __init__(self,_screen):
        self.x, self.y = pygame.mouse.get_pos()
        self.image = pygame.image.load("images\\bullet1.png")
        self.screen = _screen
        self.speed = 2
        self.flag = 0
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.bgm = pygame.mixer.Sound("sound\\bullet.wav")
        self.col_bgm = pygame.mixer.Sound("sound\\use_bomb.wav")
    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y -= self.speed
        self.show()
        #如果出了屏幕或者碰撞，则将flag置0，意思是可以循环使用
        if self.y <0:
            self.flag = 0
    def play(self):
        self.bgm.play()
    def col_play(self):
        self.col_bgm.play()
    def disappear(self):
        self.flag = 0
        self.x = 0
        self.y = -50
class plane:
    def __init__(self, _screen):
        self.x, self.y = pygame.mouse.get_pos()
        self.image = pygame.image.load("images\hero1.png")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
    def show(self,_x,_y):
        self.screen.blit(self.image, (_x-self.width/2, _y-self.height/2))
class enemy:
    def __init__(self, _screen):
        self.x=random.randint(0, 350)
        self.y=-50
        self.image = pygame.image.load("images\\enemy0.png")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.flag = 0
        self.blood = 100
        self.bomb = 0
    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y += 1
        self.show()
        if self.y > 700: # or collection()
            self.flag = 0
            self.x = random.randint(0, 350)
            self.y = -36
            self.image = pygame.image.load("images\\enemy0.png")
            self.blood = 100
    def _blood(self):
        if self.blood == 50:
            self.image = bomb_1
        if self.blood == 0:
            self.disappear()

    def disappear(self):
        if self.blood == 0:
            self.flag = 0
            self.x = random.randint(0, 350)
            self.y = -50
            self.blood =100
            self.image = pygame.image.load("images\\enemy0.png")
            # return True

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 700))
bg = pygame.image.load("images\\bg.png")
bg = pygame.transform.scale(bg, (400, 700))
bgm = pygame.mixer.Sound("sound\\game_music.ogg")
bgm.play()
name_tu = pygame.image.load("images\\name.png")
start_tu = pygame.image.load("images\\game_resume_nor.png")
pause_tu = pygame.image.load("images\\game_pause_nor.png")
play1 = pygame.image.load("images\\game_loading3.png")
play2 = pygame.image.load("images\\loading.png")
play4 =  pygame.image.load("images\\btn_finish.png")
start_tu = pygame.transform.scale(start_tu, (50, 50))
name_tu =  pygame.transform.scale(name_tu, (400, 100))
pause_tu = pygame.transform.scale(pause_tu, (50, 50))
play1 = pygame.transform.scale(play1, (200, 50))
play2 = pygame.transform.scale(play2, (600, 600))
play3 = pygame.transform.flip(play1, True, False)
bomb_1 = pygame.image.load("images\\enemy0_down1.png")
bomb_2 = pygame.image.load("images\\enemy0_down2.png")
bomb_3 = pygame.image.load("images\\enemy0_down3.png")
bomb_4 = pygame.image.load("images\\enemy0_down4.png")
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)
hero = plane(screen)
score = 0
start = 0
#初始化敌机
dict_enemy={}
for i in range(10):
    dict_enemy["ene_"+str(i)] = enemy(screen)
#创建35个对象，在对象群中选择条件飞
dict_bullet={}
for i in range(35):
    dict_bullet["bu_"+str(i)] = bullet(screen)
#初始化子弹，敌机频率
time_bu =0
time_ene = 0
time = 0
#初始化按钮
start_tu_x = 170
start_tu_y = 350
start_tu_rect = start_tu.get_rect()
pause_tu_x = 340
pause_tu_y = 0
pause_tu_rect = pause_tu.get_rect()
load_flag = 1 #初始化开始界面标志
botton_flag = 1 #初始化按钮操作标志
def loading():
    if load_flag == 1:
        screen.blit(start_tu, (start_tu_x, start_tu_y))
        screen.blit(name_tu, (0, 180))
        screen.blit(play1, (100, 60))
        screen.blit(play2, (-105, 70))
        screen.blit(play3, (100, 530))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bg, (0, 0))
    loading()
    #开始界面
    if botton_flag == 1:

        screen.blit(start_tu, (start_tu_x, start_tu_y))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        a,b,c = pygame.mouse.get_pressed()
        if mouse_x > start_tu_x and mouse_x < start_tu_x + start_tu_rect.width and \
            mouse_y >start_tu_y and mouse_y < start_tu_y + start_tu_rect.height and a:
            start = 1  #开始游戏界面
            load_flag = 0  #关闭开始界面
            botton_flag = 0  #关闭开始按钮
    #游戏界面
    if start == 1:
        # 飞机的运动
        hero.x, hero.y = pygame.mouse.get_pos() #飞机的坐标来自于鼠标
        hero.show(hero.x, hero.y)
        screen.blit(pause_tu, (340, 0))
        a, b, c = pygame.mouse.get_pressed()
        if hero.x > pause_tu_x and hero.x < pause_tu_x + pause_tu_rect.width and \
                hero.y > pause_tu_y and hero.y < pause_tu_y + pause_tu_rect.height and a:
            start = 0
            botton_flag = 1


        # 每50次就初始化一颗子弹，如果找到一个满足flag=0的，就break
        if time_bu == 50:
            for i in range(35):
                if dict_bullet["bu_" + str(i)].flag == 0:
                    dict_bullet["bu_" + str(i)].flag = 1
                    dict_bullet["bu_" + str(i)].x = hero.x-2  #子弹的坐标初始化来自于飞机
                    dict_bullet["bu_" + str(i)].y = hero.y - hero.height / 2-18
                    dict_bullet["bu_" + str(i)].show()
                    dict_bullet["bu_" + str(i)].play()
                    break
            time_bu = 0
        else:
            time_bu += 1

        #每100次就初始化一架敌机
        if time_ene == 100:
            for i in range(10):
                if dict_enemy["ene_" + str(i)].flag == 0:
                    dict_enemy["ene_" + str(i)].flag = 1
                    dict_enemy["ene_" + str(j)].bomb = 0
                    dict_enemy["ene_" + str(i)].show()
                    dict_enemy["ene_" + str(i)]._blood()
                    break

            time_ene = 0
        else:
            time_ene += 1

        #让屏幕上所有的子弹飞
        for i in range(35):
            if dict_bullet["bu_"+str(i)].flag == 1:
                dict_bullet["bu_" + str(i)].move()
            # 子弹碰撞敌机
            for j in range(10):
                if collection(dict_bullet["bu_"+str(i)].x,dict_bullet["bu_"+str(i)].y,\
                    dict_bullet["bu_"+str(i)].width,dict_bullet["bu_"+str(i)].height, \
                        dict_enemy["ene_" + str(j)].x,dict_enemy["ene_"+str(j)].y, \
                              dict_enemy["ene_" + str(j)].width,dict_enemy["ene_"+str(j)].height-10):
                    dict_enemy["ene_" + str(j)].blood -= 50
                    dict_enemy["ene_" + str(j)].bomb = 1
                    dict_enemy["ene_" + str(j)]._blood()
                    score += 1
                    dict_bullet["bu_" + str(i)].disappear()
                    dict_bullet["bu_" + str(i)].col_play()
        p_sc = font.render("score:" + str(int(score/2)), True, (255, 255, 255))
        screen.blit(p_sc, (1, 1))
        #让屏幕上所有的敌机飞
        for i in range(10):
            if dict_enemy["ene_"+str(i)].flag == 1:
                dict_enemy["ene_" + str(i)].move()

            # 敌机碰撞飞机
            if collection(dict_enemy["ene_" + str(i)].x,dict_enemy["ene_" + str(i)].y, \
                          dict_enemy["ene_" + str(i)].width,dict_enemy["ene_" + str(i)].height,\
                          hero.x,hero.y,hero.width,hero.height ):
                pass #结束游戏

    pygame.display.update()