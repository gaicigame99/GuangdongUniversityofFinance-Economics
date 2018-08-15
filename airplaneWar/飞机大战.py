import pygame
import random

# 飞机大战，
# 手机上的，单手操作游戏
# 长条形
# 鼠标操作

# 摆放背景
# 摆放飞机
# 飞机跟随鼠标移动
# 发射子弹
# 敌机出现
# 碰撞检测
pygame.init()
pygame.mixer.init()

back_mousic= pygame.mixer.Sound("sound\game_music.ogg")
back_mousic.play()

screen = pygame.display.set_mode((495, 800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))

bullet = pygame.image.load(r"images\bullet.png")
b_rect = bullet.get_rect()
b_x = []   # 每颗子弹的位置
b_y = []
b_speed = 3
b_v = 50

hero = pygame.image.load("images\hero.gif")
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height
hx = 100
hy = 100

enemy = pygame.image.load(r"images\enemy0.png")
e_rect = enemy.get_rect()
ex = 100
ey = 0

time = b_v

green = pygame.image.load(r"images\green_button.png")
red = pygame.image.load(r"images\red_button.png")

g_rect = green.get_rect()
r_rect = red.get_rect()
button_x = 200
button_y = 400



def collection(bax,bay,ball_rt,blx,bly,block_rect):
    if bax + ball_rt.width > blx and \
            bax < blx + block_rect.width and \
            bay < bly + block_rect.height and \
            bay + ball_rt.height > bly:
        print("发生碰撞")
        return True
    else:
        return False

# 把一堆要播放的图片，放到一个容器中，

# 发生碰撞flag =

# tupianbofangcount =0
# time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))
    screen.blit(enemy, (ex, ey))

    screen.blit(green, (button_x,button_y))




    if ey< 800:
        ey += 2
    else:
        ex = random.randint(0, 495-e_rect.width)
        ey = -e_rect.height

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # #
    a,b,c = pygame.mouse.get_pressed()
    # print(pygame.mouse.get_focused())
    if mouse_x > button_x and mouse_x < button_x + g_rect.width and \
        mouse_y >button_y and mouse_y < button_y + g_rect.height and a:
        screen.blit(red, (button_x, button_y))
        # 开始按钮，
        # 。。。。
        # 暂停
        # 。。。。

    # 根据自己设置的时间变量，设置当前子弹的添加频率
    if time:
        time -= 1
    else:
        # 添加子弹的位置
        b_x.append(mouse_x - b_rect.width/2+2)
        b_y.append(mouse_y - h_height / 2 - b_rect.height)
        # 重置 添加频率
        time = b_v

    ## 所有移出屏幕的子弹，删除掉
    for i in b_y:
        index = b_y.index(i)
        if i < 0:
            b_y.pop(index)
            b_x.pop(index)


    screen.blit(hero, (mouse_x - h_width / 2, mouse_y - h_height / 2))
    # 子弹绘制
    for i in range(len(b_x)):
        # 子弹绘制
        screen.blit(bullet, (b_x[i], b_y[i]))
        # 子弹移动
        b_y[i] -= b_speed

        # 碰撞检测
        if collection(b_x[i],b_y[i],b_rect,ex, ey, e_rect):
            # 修改敌机的位置
            ex = random.randint(0, 495 - e_rect.width)
            ey = -e_rect.height
            # 修改子弹的位置
            b_y[i] = -100
            # 发生碰撞之后，
            # list_flag = 1
    #         time.time()
    #
    # # 1 60Hz  一秒有60个画面
    # # 1 24帧   24Hz
    # # 1 5 0.2
    # time.time()
    # <0.4
    # # 1 秒播5张图片
    # if flag:
    #     # for i in range(len(list _suoyoutu)):
    #         screen.blit(bullet, (b_x[i], b_y[i]))

    # 子弹列表优化

    # 爆炸效果

    # 添加游戏得分

    # 增加中型敌机
    # 增加大型敌机

    # 中型敌机血量 5  给敌机添加血条
    # 大型敌机血量 10

    # 增加道具
    # 添加英雄生命   英雄飞机生命小图标加上
    # 添加对应音效

    # 制作游戏关卡

    pygame.display.update()