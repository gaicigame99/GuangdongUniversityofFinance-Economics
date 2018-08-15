import pygame
import random
import time
pygame.init()
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
WHITE_COLOR = (255, 255, 255)


class hero(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("images\hero.gif")
        self.x = _x
        self.y = _y
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def show(self):
        screen.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))


def collection(bax,bay,ball_rt,blx,bly,block_rect):
    if bax + ball_rt.width > blx and \
            bax < blx + block_rect.width and \
            bay < bly + block_rect.height and \
            bay + ball_rt.height > bly:
        return True
    else:
        return False


def boom(screen, start, boom_x, boom_y, list_enemy_down):
    if len(start):
        end = time.time()
        for i in range(len(start)):
            if end - start[i] < 0.2:
                screen.blit(list_enemy_down[0], (boom_x[i], boom_y[i]))
            elif end - start[i] < 0.4:
                screen.blit(list_enemy_down[1], (boom_x[i], boom_y[i]))
            elif end - start[i] < 0.6:
                screen.blit(list_enemy_down[2], (boom_x[i], boom_y[i]))
            elif end - start[i] < 0.8:
                screen.blit(list_enemy_down[3], (boom_x[i], boom_y[i]))


def sum_level(level_num):  # 根据不同level，返回对应的字母个数，与速度
    if level_num == 1 or level_num < 1:
        return 1, 1
    elif level_num == 2:
        return 3, 1
    elif level_num == 3:
        return 6, 1.1
    elif level_num == 4:
        return 9, 1.1
    elif level_num == 5:
        return 15, 1.2
    elif level_num == 6:
        return 20, 1.3
    elif level_num == 7:
        return 22, 1.4
    elif level_num == 8:
        return 26, 1.5
    elif level_num == 9:
        return 10, 1.6
    elif level_num == 10:
        return 15, 1.7
    elif level_num == 11:
        return 20, 1.8
    elif level_num == 12:
        return 26, 2
    else:
        return 26, 2

screen = pygame.display.set_mode((495, 800))
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))

hero1 = pygame.image.load("images\hero.gif")
h_rect = hero1.get_rect()
h_width = h_rect.width
h_height = h_rect.height
mouse_x = 100
mouse_y = 100

b_speed = 5
bullet = pygame.image.load(r"images\bullet.png")
b_rect = bullet.get_rect()
b_x = []
b_y = []
b_v = 5
times = b_v

enemy = pygame.image.load("images\enemy0.png")
e_rect = bullet.get_rect()
b_enemy = pygame.image.load("images\enemy1.png")
b_enemy_rect = b_enemy.get_rect()

e_x = []
e_y = []
ex = 100
ey = 50
e_speed = 1
#关卡速度
speed = 1
# 大型敌机速度
be_speed = 1.5

score = 0
letter_num = 1

bomb = pygame.image.load(r"images\bomb-1.gif")

light = 750

# 按钮
button_x = 50
button_y = 700
Button_Play = pygame.image.load("Button_Play.png")
Button_Play_rect = Button_Play.get_rect()
Button_Pause = pygame.image.load("Button_Pause.png")
Button_Pause_rect = Button_Pause.get_rect()

# 敌机坐标
for i in range(3):
    x = random.randint(50, 400)
    y = random.randint(-50, 50)
    e_x.append(x)
    e_y.append(y)
e_blood = 3

be_x = []
be_y = []
be_blood = 10
# 大型敌机坐标
for i in range(3):
    x = random.randint(50, 400)
    y = random.randint(-50, 50)
    be_x.append(x)
    be_y.append(y)

# 爆炸效果
start = []
boom_x = []
boom_y = []
b_start = []
b_boom_x = []
b_boom_y = []
list_enemy0_down = []
enemy0_down1 = pygame.image.load("images\enemy0_down1.png")
enemy0_down2 = pygame.image.load("images\enemy0_down2.png")
enemy0_down3 = pygame.image.load("images\enemy0_down3.png")
enemy0_down4 = pygame.image.load("images\enemy0_down4.png")
list_enemy0_down.append(enemy0_down1)
list_enemy0_down.append(enemy0_down2)
list_enemy0_down.append(enemy0_down3)
list_enemy0_down.append(enemy0_down4)
list_enemy1_down = []
enemy1_down1 = pygame.image.load("images\enemy1_down1.png")
enemy1_down2 = pygame.image.load("images\enemy1_down2.png")
enemy1_down3 = pygame.image.load("images\enemy1_down3.png")
enemy1_down4 = pygame.image.load("images\enemy1_down4.png")
list_enemy1_down.append(enemy1_down1)
list_enemy1_down.append(enemy1_down2)
list_enemy1_down.append(enemy1_down3)
list_enemy1_down.append(enemy1_down4)

# 游戏背景
screen = pygame.display.set_mode((495, 800))
game_background = pygame.image.load(r"images\background.png")
game_background = pygame.transform.scale(game_background, (495, 800))

move_list = {}

mv_bg = pygame.image.load(r"images\timg.jpg")
mv_bg = pygame.transform.scale(mv_bg, (495, 800))
bgx = 0
bgy = 0
move_list["背景位置"] = [bgx, bgy]

# 摆放开始按钮
blue_btn = pygame.image.load(r"images\blue_btn.png")
blue_btn = pygame.transform.scale(blue_btn, (247, 80))
blue_rect = blue_btn.get_rect()
btx = 124
bty = 480
move_list["按钮0位置"] = [btx, bty]

# 绿色按钮
green_btn = pygame.image.load("images\green_btn.png")
green_btn = pygame.transform.scale(green_btn, (247, 80))
gtx = 124
gty = 480
move_list["按钮1位置"] = [gtx, gty]

speedx = 0
speedy = 0

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
start_text = font.render("开始游戏", True, (0, 0, 0, 150))
stx = 63+124
sty = 25+480
move_list["文字位置"] = [stx, sty]

# 子弹计时器
time_count = b_v

game_start = 0

# 游戏开始计时器
game_start_time = 150


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(game_background, (0, 0))
    screen.blit(mv_bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
    a, b, c = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 开始游戏逻辑
    if mouse_x > btx and mouse_x < btx + blue_rect.width and mouse_y > bty and mouse_y < bty + blue_rect.height and a:
        screen.blit(blue_btn, (move_list["按钮1位置"][0], move_list["按钮1位置"][1]))
        speedx = 0
        speedy = -30
        game_start = 1
    else:
        screen.blit(green_btn, (move_list["按钮0位置"][0], move_list["按钮0位置"][1]))

    for i in move_list:
        move_list[i][0] += speedx
        move_list[i][1] += speedy

    # 开始按钮文字
    screen.blit(start_text, (move_list["文字位置"][0], move_list["文字位置"][1]))

    if game_start:
        game_start_time -= 1

    if game_start and game_start_time < 0:

        #screen.blit(bg, (0, 0))
        text_score = font.render("得分:" + str(score), True, WHITE_COLOR)
        screen.blit(text_score, (20, 10))
        text_level = font.render("关卡:" + str(letter_num), True, WHITE_COLOR)
        screen.blit(text_level, (20, 10 + 36))

        # 发射大小型敌机
        for i in range(3):
            screen.blit(enemy, (e_x[i], e_y[i]))
            screen.blit(b_enemy, (be_x[i], be_y[i]))
            if e_y[i] < 800:
                e_y[i] += speed
            else:
                e_x[i] = random.randint(0, 495 - e_rect.width)
                e_y[i] = - e_rect.height

            if be_y[i] < 800:
                be_y[i] += speed * 1.5
            else:
                be_x[i] = random.randint(0, 495 - b_enemy_rect.width)
                be_y[i] = - b_enemy_rect.height

        # 获取鼠标位置
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # 大招（激光）
        screen.blit(Button_Play, (button_x, button_y))
        text_big = font.render("大招:", True, WHITE_COLOR)
        screen.blit(text_big, (0, 715))

        # 点按钮发射大招
        a, b, c = pygame.mouse.get_pressed()
        if mouse_x > button_x and mouse_x < button_x + Button_Play_rect.width and \
                mouse_y > button_y and mouse_y < button_y + Button_Play_rect.height and a:
            screen.blit(Button_Pause, (button_x, button_y))

            pygame.draw.line(screen, WHITE_COLOR, (0, light), (495, light), 5)
            light -= 1
            if light < 0:
                light = 750

        # 发射英雄机
        heroA = hero(screen, mouse_x, mouse_y)
        heroA.show()

        # 子弹模块
        if time_count:
            time_count -= 1
        else:
            b_x.append(mouse_x - b_rect.width/2+2)
            b_y.append(mouse_y - heroA.height/2 - b_rect.height)
            time_count = b_v

        # 激光命中，敌机消失
        for i in range(len(e_x)):
            if e_y[i] < light < e_y[i] + e_rect.height:
                e_x[i] = random.randint(0, 495 - e_rect.width)
                e_y[i] = - e_rect.height
                score += 1

            if be_y[i] < light < be_y[i] + b_enemy_rect.height:
                be_x[i] = random.randint(0, 495 - b_enemy_rect.width)
                be_y[i] = - b_enemy_rect.height
                score += 2

        for i in range(len(b_x)):
            screen.blit(bullet, (b_x[i], b_y[i]))
            b_y[i] -= b_speed

            for j in range(len(e_x)):
                # 碰撞检测
                if collection(b_x[i], b_y[i], b_rect, e_x[j], e_y[j], e_rect):
                    e_blood -= 1

                    if e_blood == 0:
                        # 得分（小敌机一分）
                        score += 1
                        e_blood = 3
                        # 记录爆炸的坐标
                        start.append(time.time())
                        boom_x.append(e_x[j])
                        boom_y.append(e_y[j])
                        # 修改敌机的位置
                        e_x[j] = random.randint(0, 495 - e_rect.width)
                        e_y[j] = - e_rect.height
                    # 修改子弹的位置
                    b_x[i] = random.randint(0, 495 - e_rect.width)
                    b_y[i] = - e_rect.height
                # 大型敌机碰撞检测
                if collection(b_x[i], b_y[i], b_rect, be_x[j], be_y[j], b_enemy_rect):
                    be_blood -= 1
                    if be_blood == 0:
                        # 大型敌机两分
                        score += 2
                        be_blood = 10
                        # 记录爆炸的坐标
                        b_start.append(time.time())
                        b_boom_x.append(be_x[j])
                        b_boom_y.append(be_y[j])
                        # 修改敌机的位置
                        be_x[j] = random.randint(0, 495 - b_enemy_rect.width)
                        be_y[j] = - b_enemy_rect.height
                    # 修改子弹的位置
                    b_x[i] = random.randint(0, 495 - e_rect.width)
                    b_y[i] = - e_rect.height
        # 爆炸效果
        boom(screen, start, boom_x, boom_y, list_enemy0_down)
        boom(screen, b_start, b_boom_x, b_boom_y, list_enemy1_down)

        level = score // 20 + 1
        # 用方法获得对应等级的速度
        letter_num, speed = sum_level(level)

    pygame.display.update()