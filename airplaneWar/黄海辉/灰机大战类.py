import pygame
import random
import time
#飞机大战
#手机上单手操作游戏
#屏幕长方形

# **************************我方飞机
class Hero(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("images\hero.gif")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y
    def show(self, _x, _y):
        self.x = _x
        self.y = _y
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen.blit(self.image, (self.x, self.y))

class senemy_plane(object):
    def __init__(self, _screen, _x, _y):
        self.enemy = pygame.image.load(r"images\enemy0.png")
        self.down = []
        self.enemy1 = pygame.image.load(r"images\enemy0_down1.png")
        self.enemy2 = pygame.image.load(r"images\enemy0_down2.png")
        self.enemy3 = pygame.image.load(r"images\enemy0_down3.png")
        self.enemy4 = pygame.image.load(r"images\enemy0_down4.png")
        self.down.append(self.enemy1)
        self.down.append(self.enemy2)
        self.down.append(self.enemy3)
        self.down.append(self.enemy4)
        self.rect = self.enemy.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.list_senemy = []
    def show(self):
        self.screen.blit(self.enemy, (self.x, self.y))

class menemy_plane(object):
    def __init__(self, _screen, _x, _y):
        self.menemy = pygame.image.load(r"images\enemy1.png")
        self.mdown = []
        self.menemy1 = pygame.image.load(r"images\enemy1_down1.png")
        self.menemy2 = pygame.image.load(r"images\enemy1_down2.png")
        self.menemy3 = pygame.image.load(r"images\enemy1_down3.png")
        self.menemy4 = pygame.image.load(r"images\enemy1_down4.png")
        self.mdown.append(self.menemy1)
        self.mdown.append(self.menemy2)
        self.mdown.append(self.menemy3)
        self.mdown.append(self.menemy4)
        self.rect = self.menemy.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y

    def show(self):
        self.screen.blit(self.menemy, (self.x, self.y))

class bullet(object):
    def __init__(self, _screen, _x, _y, _times):
        self.image = pygame.image.load(r"images\bullet.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.times = _times
        self.b_x = []
        self.b_y = []
        self.times = 0
        self.speed = 0
    def show(self,plane_x,plane_y, _times, shoot_speed):
        if self.times:
            self.times -= 1
        else:
            self.b_x.append(plane_x- self.width/2+2)
            self.b_y.append(plane_y- heroA.height / 2 - self.height)
            self.times = _times
        for i in range(len(self.b_x)):
            self.screen.blit(self.image, (self.b_x[i], self.b_y[i]))
            self.b_y[i] -= shoot_speed
        for i in self.b_y:
            index = self.b_y.index(i)
            if i < 0:
                self.b_y.pop(index)
                self.b_x.pop(index)

pygame.init()
pygame.mixer.init()

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",25)
back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
# ****************** 音乐 ****************************
btn_speedx = 0
btn_speedy = 0
#游戏开始背景图
move_list = {}
start_bg = pygame.image.load("sbg.png")
start_bg = pygame.transform.scale(start_bg, (498, 800))
sbg_x = 0
sbg_y = 0
move_list["背景位置"] = [sbg_x, sbg_y]
# 摆放开始按钮
s_btn = pygame.image.load("blue.png")
s_btn = pygame.transform.scale(s_btn, (150, 80))
s_rect = s_btn.get_rect()
s_btnx = 180
s_btny = 650
move_list["按钮0位置"] = [s_btnx, s_btny]
# 红色按钮
red_btn = pygame.image.load("red.png")
red_btn = pygame.transform.scale(red_btn, (150, 80))
r_rect = red_btn.get_rect()
r_btnx = 180
r_btny = 650
move_list["按钮1位置"] = [r_btnx, r_btny]
screen = pygame.display.set_mode((495,800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (498, 800))

# 频率和射击速度
b_v = 30
shoot_speed = 5

# hero
hx = 100
hy = 100
heroA = Hero(screen,hx,hy)
bulletA = bullet(screen, hx, hy, b_v)

# 小型机爆炸
end = []
boom_x = []
boom_y = []
flag = 0
# 中型机爆炸
mid_end = []
mid_boom_x = []
mid_boom_y = []
mid_flag = 0
# 得分
score = 0

#发射中型机
send = 0

# 敌方小飞机产地坐标
list_senemy = []
for i in range(5):
    enemyx = random.randint(50,400)
    enemyy = random.randint(-100,-50)
    senemy_planeA = senemy_plane(screen, enemyx, enemyy)
    list_senemy.append(senemy_planeA)

# 中型机生产
blood = 5
list_menemy = []
midx = random.randint(50, 400)
midy = random.randint(-300, -100)
menemy_planeA = menemy_plane(screen, midx, midy)
list_menemy.append(menemy_planeA)

gsart = 0
def colision(bullet_x,bullet_y,bullet_rect,p_x,p_y,p_rect):
    if bullet_x + bullet_rect.width > p_x and \
            bullet_x < p_x + p_rect.width and \
            bullet_y < p_y + p_rect.height and \
            bullet_y + bullet_rect.height > p_y:
        print("发生碰撞")
        return True
    else:
        return False

def boom(_screen,list_time,list_x,list_y,_flag, list_image):
    if _flag == 1:
        start = time.time()
        for i in range(len(list_time)):
            if start-list_time[i] < 0.2:
                _screen.blit(list_image[0], (list_x[i], list_y[i]))
            elif 0.2 < start-list_time[i] < 0.4:
                _screen.blit(list_image[1], (list_x[i], list_y[i]))
            elif 0.4 < start-list_time[i] < 0.6:
                _screen.blit(list_image[2], (list_x[i], list_y[i]))
            elif 0.6 < start-list_time[i] < 0.8:
                _screen.blit(list_image[3], (list_x[i], list_y[i]))

# def after_colision(blood,bullet_y,p_x,p_y):
#     flag = 0
#     bullet_y = -100
#     blood -= 1
#     if blood <= 0:
#         flag = 1
#         mid_end.append(time.time())
#         mid_boom_x.append(p_x)
#         mid_boom_y.append(p_y)
#         p_y = random.randint(-300, -100)  # 飞机消失
#         p_x = random.randint(50, 400)
#     return flag,p_y,p_x

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
start_text = font.render("开始游戏", True, (0,0,0,150))
stx = 15+180
sty = 25+650
move_list["文字位置"] = [stx, sty]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))
    screen.blit(start_bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
    a,b,c = pygame.mouse.get_pressed()
    hx, hy = pygame.mouse.get_pos()

    if hx > s_btnx and hx < s_btnx + s_rect.width and hy> r_btny and hy < r_btny + s_rect.height and a:

        screen.blit(red_btn, (move_list["按钮1位置"][0], move_list["按钮1位置"][1]))
        btn_speedx = 0
        btn_speedy = -30
        gsart = 1
    else:
        screen.blit(s_btn, (move_list["按钮0位置"][0], move_list["按钮0位置"][1]))

    for i in move_list:
        move_list[i][0] += btn_speedx
        move_list[i][1] += btn_speedy
        # 开始按钮文字
    if move_list[i][1] < -800:
        btn_speedy = 0
    screen.blit(start_text, (move_list["文字位置"][0], move_list["文字位置"][1]))
    if gsart:

        heroA.show(hx-heroA.width/2, hy-heroA.height/2)
        # 画出敌方小飞机
        for i in range(len(list_senemy)):
            list_senemy[i].show()
            if list_senemy[i].y < 800:
                list_senemy[i].y += 1
            else:
                list_senemy[i].y = random.randint(-100, -50)
        # 画出中飞机
        list_menemy[0].show()
        if score != 0 and score%12 == 0:
            send = score
        if send != 0 and send % 12 == 0:
            list_menemy[0].y += 0.5
            if list_menemy[0].y > 800:
                send = 0
                list_menemy[0].y = random.randint(-300, -100)
        # 我方发射子弹
        bulletA.show(hx,hy,b_v,shoot_speed)
        for i in range(len(bulletA.b_x)):
            # 小型机碰撞检测
            for j in range(len(list_senemy)):
                if colision(bulletA.b_x[i], bulletA.b_y[i], bulletA.rect, list_senemy[j].x, list_senemy[j].y, list_senemy[j].rect):
                    bulletA.b_y[i] = -100 # 子弹消失
                    score += 1
                    flag = 1
                    end.append(time.time())
                    boom_x.append(list_senemy[j].x)
                    boom_y.append(list_senemy[j].y)
                    list_senemy[j].y = random.randint(-100, -50)  # 飞机消失
            # 中型机碰撞检测
            if colision(bulletA.b_x[i], bulletA.b_y[i], bulletA.rect, list_menemy[0].x, list_menemy[0].y, list_menemy[0].rect):
                blood -= 1
                bulletA.b_y[i] = -100  # 子弹消失
            if blood <= 0:
                mid_flag = 1
                mid_end.append(time.time())
                mid_boom_x.append(list_menemy[0].x)
                mid_boom_y.append(list_menemy[0].y)
                list_menemy[0].y = random.randint(-300, -100)  # 飞机消失
                list_menemy[0].x = random.randint(50, 400)
                score += 3
                blood = 5
        #小型飞机爆炸
        boom(screen, end, boom_x, boom_y, flag,senemy_planeA.down)
        #中型飞机爆炸
        boom(screen, mid_end, mid_boom_x, mid_boom_y, mid_flag,menemy_planeA.mdown)
        print(len(bulletA.b_x))
        scorep = font.render("得分："+str(score),True,(255,255,255))
        screen.blit(scorep,(10,20))



    pygame.display.update()