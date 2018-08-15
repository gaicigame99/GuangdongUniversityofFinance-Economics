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


pygame.init()
pygame.mixer.init()

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",25)
back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
# ****************** 音乐 ****************************

screen = pygame.display.set_mode((495,800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (498, 800))
# **********************************子弹
bullet = pygame.image.load(r"images\bullet.png")
b_rect = bullet.get_rect()
b_w = b_rect.width
b_h = b_rect.height
b_x = []
b_y = []
b_v = 30
times = b_v
# ***********************敌方飞机
# 小型战机
enemy1 = pygame.image.load(r"images\enemy0_down1.png")
enemy2 = pygame.image.load(r"images\enemy0_down2.png")
enemy3 = pygame.image.load(r"images\enemy0_down3.png")
enemy4 = pygame.image.load(r"images\enemy0_down4.png")
enemy = pygame.image.load(r"images\enemy0.png")

list_enemy_down = []
list_enemy_down.append(enemy1)
list_enemy_down.append(enemy2)
list_enemy_down.append(enemy3)
list_enemy_down.append(enemy4)

e_rect = enemy.get_rect()
e_h = e_rect.height
e_w = e_rect.width
#中型战机
mid_enemy = pygame.image.load(r"images\enemy1.png")
mid_enemy1 = pygame.image.load(r"images\enemy1_down1.png")
mid_enemy2 = pygame.image.load(r"images\enemy1_down2.png")
mid_enemy3 = pygame.image.load(r"images\enemy1_down3.png")
mid_enemy4 = pygame.image.load(r"images\enemy1_down4.png")
mid_rect = mid_enemy.get_rect()
mid_h = mid_rect.height
mid_w = mid_rect.width
mid_ex = []
mid_ey = []

heroA = Hero(screen,100,100)

# 敌方飞机产地坐标
list_ex = []
list_ey = []
for i in range(5):
    enemyx = random.randint(50,400)
    enemyy = random.randint(-100,-50)
    list_ex.append(enemyx)
    list_ey.append(enemyy)

midx = random.randint(50, 400)
midy = random.randint(-300, -100)
def collsion(bullet_x,bullet_y,bullet_rect,p_x,p_y,p_rect):
    if bullet_x + bullet_rect.width > p_x and \
            bullet_x < p_x + p_rect.width and \
            bullet_y < p_y + p_rect.height and \
            bullet_y + bullet_rect.height > p_y:
        print("发生碰撞")
        return True
    else:
        return False

# 爆炸函数
# def boom(_screen,list_time,list_x,list_y,_flag, list_image):
#     if _flag == 1:
#         start = time.time()
#         for i in range(len(list_time)):
#             if start-list_time[i] < 0.2:
#                 _screen.blit(list_image[0], (list_x[i], list_y[i]))
#             elif 0.2 < start-list_time[i] < 0.4:
#                 _screen.blit(list_image[1], (list_x[i], list_y[i]))
#             elif 0.4 < start-list_time[i] < 0.6:
#                 _screen.blit(list_image[2], (list_x[i], list_y[i]))
#             elif 0.6 < start-list_time[i] < 0.8:
#                 _screen.blit(list_image[3], (list_x[i], list_y[i]))




shoot_speed = 5
#小型机
end = []
boom_x = []
boom_y = []
flag = 0
#中型机
mid_end = []
mid_boom_x = []
mid_boom_y = []
mid_flag = 0
# 得分
score = 0
blood = 5
#发射中型机
send = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))
    hx, hy = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    heroA.show(hx-heroA.width/2, hy-heroA.height/2)
    # 画出敌方飞机
    for i in range(5):
        screen.blit(enemy,(list_ex[i],list_ey[i]))
        if list_ey[i] < 800:
            list_ey[i] += 1
        else:
            list_ey[i] = random.randint(-100,-50)
    screen.blit(mid_enemy, (midx, midy))
    if score != 0 and score%12 == 0:
        send = score
    if send != 0 and send % 12 == 0:
        midy += 0.5
        if midy > 800:
            send = 0
            midy = random.randint(-300, -100)
    # 我方发射子弹
    if times:
        times -= 1
    else:
        b_x.append(hx - b_w/2+2)
        b_y.append(hy - heroA.height / 2- b_h)
        times = b_v
    for i in range(len(b_x)):
        screen.blit(bullet, (b_x[i], b_y[i]))
        b_y[i] -= shoot_speed
        # if b_y[i] < 0:    #假设迭代到3，出界后移除，前后面的有关i的代码就会出错
        #     b_y.pop(i)
        for j in range(len(list_ex)):
            if collsion(b_x[i], b_y[i], b_rect, list_ex[j], list_ey[j], e_rect):
                b_y[i] = -100 #子弹消失
                score += 1
                flag = 1
                end.append(time.time())
                boom_x.append(list_ex[j])
                boom_y.append(list_ey[j])

                list_ey[j] = random.randint(-100, -50)  # 飞机消失
        if collsion(b_x[i], b_y[i], b_rect, midx, midy, mid_rect):
            blood -= 1
            b_y[i] = -100  # 子弹消失
        if blood <= 0:
            mid_flag = 1
            mid_end.append(time.time())
            mid_boom_x.append(midx)
            mid_boom_y.append(midy)
            midy = random.randint(-300, -100)  # 飞机消失
            midx = random.randint(50, 400)
            score += 1
            blood = 5
    #小型飞机爆炸
    if flag == 1:
        start = time.time()
        for i in range(len(end)):
            if start-end[i] < 0.2:
                screen.blit(enemy1, (boom_x[i], boom_y[i]))
            elif 0.2 < start-end[i] < 0.4:
                screen.blit(enemy2, (boom_x[i], boom_y[i]))
            elif 0.4 < start-end[i] < 0.6:
                screen.blit(enemy3, (boom_x[i], boom_y[i]))
            elif 0.6 < start-end[i] < 0.8:
                screen.blit(enemy4, (boom_x[i], boom_y[i]))
    #中型飞机爆炸
    if mid_flag == 1:
        mid_start = time.time()
        for i in range(len(mid_end)):
            if start-end[i] < 0.2:
                screen.blit(mid_enemy1, (mid_boom_x[i], mid_boom_y[i]))
            elif 0.2 < mid_start-mid_end[i] < 0.4:
                screen.blit(mid_enemy2, (mid_boom_x[i], mid_boom_y[i]))
            elif 0.4 < mid_start-mid_end[i] < 0.6:
                screen.blit(mid_enemy3, (mid_boom_x[i], mid_boom_y[i]))
            elif 0.6 < mid_start-mid_end[i] < 0.8:
                screen.blit(mid_enemy4, (mid_boom_x[i], mid_boom_y[i]))
    # 子弹优化，节省空间
    for i in b_y:
        index = b_y.index(i)
        if i < 0:
            b_y.pop(index)
            b_x.pop(index)

    scorep = font.render("得分："+str(score),True,(255,255,255))
    screen.blit(scorep,(10,20))


    pygame.display.update()

    # if a ==0:
    #     bx = hx - h_w / 10
    #     by = hy - h_h /2
    #     a = 1
    # by -= shoot_speed
    # screen.blit(bullet, (bx, by))
    # if by < 0:
    #     a = 0
