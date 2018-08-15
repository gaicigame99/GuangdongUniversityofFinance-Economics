import pygame
import random

pygame.init()

# 游戏背景
screen = pygame.display.set_mode((495, 800))
game_background = pygame.image.load(r"images\background.png")
game_background = pygame.transform.scale(game_background, (495, 800))


move_list = {}

mv_bg = pygame.image.load("images\start_background.png")
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

# 摆放开始游戏文字
# 247   80
# 123  40
# 4 *30 /2   30/2
# 123-60    40-15
# 63     25
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
start_text = font.render("开始游戏", True, (0,0,0,150))
stx = 63+124
sty = 25+480
move_list["文字位置"] = [stx, sty]



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

# 子弹计时器
time_count = b_v

game_start = 0

# 游戏开始计时器
game_start_time = 150


def collection(bax,bay,ball_rt,blx,bly,block_rect):
    if bax + ball_rt.width > blx and \
            bax < blx + block_rect.width and \
            bay < bly + block_rect.height and \
            bay + ball_rt.height > bly:
        print("发生碰撞")
        return True
    else:
        return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(game_background, (0, 0))
    screen.blit(mv_bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
    a,b,c = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 开始游戏逻辑
    if mouse_x > btx and mouse_x < btx+blue_rect.width and mouse_y> bty and mouse_y < bty + blue_rect.height and a:
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

    if game_start and game_start_time<0:

        # 调用开始游戏逻辑
        screen.blit(enemy, (ex, ey))
        if ey < 800:
            ey += 2
        else:
            ex = random.randint(0, 495 - e_rect.width)
            ey = -e_rect.height
        if time_count:
            time_count -= 1
        else:
            # 添加子弹的位置
            b_x.append(mouse_x - b_rect.width / 2 + 2)
            b_y.append(mouse_y - h_height / 2 - b_rect.height)
            # 重置 添加频率
            time_count = b_v
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
            if collection(b_x[i], b_y[i], b_rect, ex, ey, e_rect):
                # 修改敌机的位置
                ex = random.randint(0, 495 - e_rect.width)
                ey = -e_rect.height
                # 修改子弹的位置
                b_y[i] = -100



    pygame.display.update()
