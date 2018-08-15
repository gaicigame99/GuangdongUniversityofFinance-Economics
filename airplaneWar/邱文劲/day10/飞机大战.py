import pygame
import random
import time

# 飞机大战
# 手机上的，单手操作游戏
# 长条形
# 鼠标操作

# 初始化
pygame.init()
pygame.mixer.init()
font = pygame.font.Font("C:\Windows\Fonts\SIMLI.TTF", 45)
# 添加背景音乐
background_music = pygame.mixer.Sound("sound\game_music.ogg")
background_music.play(True)
# 添加爆炸音乐
bomb_music = pygame.mixer.Sound("sound\get_bomb.wav")
# 设置屏幕大小
screen = pygame.display.set_mode((450, 700))

# 背景图片
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (450, 700))
# 子弹   #  r用来转义\b
bullet = pygame.image.load(r"images\bullet-1.gif")
hero = pygame.image.load("images\hero.gif")  # 我方飞机
enemy = pygame.image.load("images\enemy-1.gif")  # 敌方飞机1
broken_1 = pygame.image.load("images\enemy0_down1.png")  # 敌方飞机1爆炸效果1
broken_2 = pygame.image.load("images\enemy0_down2.png")  # 敌方飞机1爆炸效果2
broken_3 = pygame.image.load("images\enemy0_down3.png")  # 敌方飞机1爆炸效果3
broken_4 = pygame.image.load("images\enemy0_down4.png")  # 敌方飞机1爆炸效果4
# 我方飞机的宽高
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height
# 子弹的宽高
b_rect = bullet.get_rect()
b_width = b_rect.width
b_height = b_rect.height
# 敌方飞机的宽高
e_rect = enemy.get_rect()
e_width = e_rect.width
e_height = e_rect.height

# 子弹坐标列表
bx = []
by = []
# 子弹发射频率
flap = 20
# 敌方飞机坐标列表
ex = []
ey = []
# 敌方飞机发射频率
temp = 30

# hx = 100
# hy = 100
# 爆炸点列表
bomb_x = []
bomb_y = []
temp_bomb_y = []
# 爆炸时间列表
bomb_time = []
#分数
score = 0

move_list = {}
# 开始界面图片
start_background = pygame.image.load(r"images\start_background.png")
start_background = pygame.transform.scale(start_background, (450, 700))
bgx = 0
bgy = 0
move_list["背景位置"] = [bgx, bgy]
# 摆放开始按钮
blue_btn = pygame.image.load(r"images\blue_btn.png")
blue_btn = pygame.transform.scale(blue_btn, (220, 60))
blue_rect = blue_btn.get_rect()
btx = 120
bty = 500
move_list["按钮0位置"] = [btx, bty]

# 绿色按钮
green_btn = pygame.image.load("images\green_btn.png")
green_btn = pygame.transform.scale(green_btn, (220, 60))
gtx = 120
gty = 500
move_list["按钮1位置"] = [gtx, gty]

# "开始游戏"文字
start_text = font.render("开始游戏", True, (0, 0, 255))
stx = 143
sty = 505
move_list["文字位置"] = [stx, sty]

speed_x = 0
speed_y = 0

# 游戏开始计时器
game_start_time = 150
# 用来判断是否开始游戏，0开始界面，1游戏界面
is_start = 0


# 打印分数，分数每升高50，变一种颜色
def print_score(d_score, d_font, d_screen):
    if d_score <= 50:
        text = d_font.render("得分 " + str(d_score), True, (255, 255, 255))
    elif 50 < d_score <= 100:
        text = d_font.render("得分 " + str(d_score), True, (255, 255, 0))
    elif 100 < d_score <= 150:
        text = d_font.render("得分 " + str(d_score), True, (255, 128, 0))
    elif 150 < d_score <= 200:
        text = d_font.render("得分 " + str(d_score), True, (255, 255, 0))
    else:
        text = d_font.render("得分 " + str(d_score), True, (255, 0, 255))
    d_screen.blit(text, (0, 10))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(bg, (0, 0))

    # 开始界面
    if is_start == 0:
        screen.blit(start_background, (move_list["背景位置"][0], move_list["背景位置"][1]))
        mouse_x, mouse_y = pygame.mouse.get_pos()  # 拿到鼠标位置
        a, b, c = pygame.mouse.get_pressed()
        if mouse_x > btx and mouse_x < btx + blue_rect.width and mouse_y > bty and mouse_y < bty + blue_rect.height and a:
            screen.blit(blue_btn, (move_list["按钮1位置"][0], move_list["按钮1位置"][1]))
            speed_x = 0
            speed_y = -30
        else:
            screen.blit(green_btn, (move_list["按钮0位置"][0], move_list["按钮0位置"][1]))
        screen.blit(start_text, (move_list["文字位置"][0], move_list["文字位置"][1]))
        for i in move_list:
            move_list[i][0] += speed_x
            move_list[i][1] += speed_y

        if game_start_time == 0:
            is_start = 1
        else:
            game_start_time -= 1

        pygame.display.update()

    # 游戏界面
    if is_start == 1:
        hx, hy = pygame.mouse.get_pos()  # 拿到鼠标位置
        screen.blit(hero, (hx - h_width / 2, hy - h_rect.height / 2))
        # 显示子弹
        if flap > 0:
            flap -= 1
        else:
            bx.append(hx - b_width / 4)
            by.append(hy - h_rect.height / 2 - b_height)
            flap = 20
        num_bullet = len(bx)
        z = 0
        while z < num_bullet:
            if by[z] < 0:
                bx.pop(z)
                by.pop(z)
                num_bullet -= 1
            else:
                screen.blit(bullet, (bx[z], by[z]))
                by[z] -= 2
                z += 1
        # 显示敌方飞机1
        if temp > 0:
            temp -= 1
        else:
            ex.append(random.randint(0, 400))
            ey.append(random.randint(-300, 0))
            temp = 30
        for i in range(len(ex)):
            for j in range(len(bx)):
                # 判断碰撞
                if ey[i] > 0 and -b_width < bx[j] - ex[i] < e_width and 0 < by[j] - ey[i] < e_height:
                    bomb_x.append(ex[i])
                    bomb_y.append(ey[i])
                    temp_bomb_y.append(ey[i])
                    ey[i] = 1000
                    bomb_time.append(time.time())
                    score += 1
            screen.blit(enemy, (ex[i], ey[i]))
            ey[i] += 1

        # 取出敌机列表1中掉到屏幕外的飞机
        num_ex = len(ex)
        k = 0
        while k < num_ex:
            if ey[k] == 1000:
                ex.pop(k)
                ey.pop(k)
                num_ex -= 1
                k += 1
            else:
                k += 1

        # 显示爆炸效果
        for i in range(len(bomb_x)):
            now_tme = time.time()
            if 0 < now_tme - bomb_time[i] < 0.2:
                screen.blit(broken_1, (bomb_x[i], bomb_y[i]))
                bomb_music.play()
            elif 0.2 < now_tme - bomb_time[i] < 0.4:
                screen.blit(broken_2, (bomb_x[i], bomb_y[i]))
                bomb_music.play()
            elif 0.4 < now_tme - bomb_time[i] < 0.6:
                screen.blit(broken_3, (bomb_x[i], bomb_y[i]))
                bomb_music.play()
            elif 0.6 < now_tme - bomb_time[i] < 0.8:
                screen.blit(broken_4, (bomb_x[i], bomb_y[i]))
                bomb_music.play()
            else:
                pass
            bomb_y[i] += 1

        print_score(score, font, screen)
        pygame.display.update()
