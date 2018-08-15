import pygame
import random
import time

pygame.init()
pygame.mixer.init()
back_music = pygame.mixer.Sound("sound\game_music.ogg")
back_music.play()
screen = pygame.display.set_mode((480, 852))
background1 = pygame.image.load(r"images\background.png")
background2 = pygame.image.load(r"images\background.png")
move_list = {}

mv_bg = pygame.image.load("images\start_background.jpg")
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
font = pygame.font.Font("C:\Windows\Fonts\STXINGKA.TTF", 24)

speedx = 0
speedy = 0

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
start_text = font.render("开始游戏", True, (0,0,0,150))
stx = 63+124
sty = 25+480
move_list["文字位置"] = [stx, sty]

enemy0_down1 = pygame.image.load("images\enemy0_down1.png")
enemy0_down2 = pygame.image.load("images\enemy0_down2.png")
enemy0_down3 = pygame.image.load("images\enemy0_down3.png")
enemy0_down4 = pygame.image.load("images\enemy0_down4.png")

# 飞机宽高
hero = pygame.image.load("images\hero1.png")
h_rect = hero.get_rect()
h_height = h_rect.height
h_width = h_rect.width
# 敌机宽高
enemy0 = pygame.image.load("images\enemy0.png")
e_rect = enemy0.get_rect()
e_height = e_rect.height
e_width = e_rect.width
# 弹夹
bullet = pygame.image.load(r"images\bullet.png")
l_clip = []
r_clip = []

s_time = time.time()    # 开始时间
# 敌机位置
e_x = []
e_y = []

score = 0
b_x = []
b_y = []
st_time=[]

y1 = 0
y2 = -852

game_start = 0
game_start_time = 150

for i in range(5):
    e_x.append(random.randint(0, 400))
    e_y.append(random.randint(-30, -10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    hx, hy = pygame.mouse.get_pos()
    screen.blit(background1, (0, y1))
    screen.blit(background2, (0, y2))
    if len(move_list):
        screen.blit(mv_bg, (move_list["背景位置"][0], move_list["背景位置"][1]))
        a, b, c = pygame.mouse.get_pressed()
        # 开始游戏逻辑
        if hx > btx and hx < btx + blue_rect.width and hy > bty and hy < bty + blue_rect.height and a:
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
        move_list.clear()
        screen.blit(hero, (hx-h_width/2, hy-h_height/2))
        y1 += 5
        y2 += 5
        if y1 >= 852:
            y1 = 0
        if y2 >= 0:
            y2 = -852
        for i in range(5):
            screen.blit(enemy0, (e_x[i], e_y[i]))
            e_y[i] += 1
        c_time = time.time()
        u_b = []
        if c_time-s_time >= 0.5:
            s_time = c_time
            l_clip_x = hx-42
            l_clip_y = hy-37
            l_clip.append((l_clip_x, l_clip_y))
            r_clip_x = hx+22
            r_clip_y = hy-37
            r_clip.append((r_clip_x, r_clip_y))
        for i in range(len(l_clip)):
            screen.blit(bullet, l_clip[i])
            screen.blit(bullet, r_clip[i])
            l_clip[i] = (l_clip[i][0], l_clip[i][1]-10)
            r_clip[i] = (r_clip[i][0], r_clip[i][1]-10)
            if l_clip[i][1] < -20:
                u_b.append(i)
            for j in range(5):
                screen.blit(font.render("得分: %d" % score, True, (0, 0, 0)), (10, 10))
                if 0<e_y[j]<=852:
                    if (e_x[j]<l_clip[i][0]<e_x[j]+e_width and e_y[j]<=l_clip[i][1]<=e_y[j]+e_height) or (e_x[j]<r_clip[i][0]<e_x[j]+e_width and e_y[j]<=r_clip[i][1]<=e_y[j]+e_height):
                        score += 1
                        st_time.append(time.time())
                        # cu_time.append(time.time())
                        b_x.append(e_x[j])
                        b_y.append(e_y[j])
                        e_x[j] = random.randint(0, 400)
                        e_y[j] = random.randint(-30, -10)

                if e_y[j]>852:
                    e_x[j] = random.randint(0, 400)
                    e_y[j] = random.randint(-30, -10)
                    score -= 1
        for i in range(len(u_b)-1,-1,-1):
            del l_clip[u_b[i]]
            del r_clip[u_b[i]]
        u_b.clear()
        if len(st_time):
            for i in st_time:
                index = st_time.index(i)
                cu_time=time.time()
                if cu_time-i<=0.2:
                    screen.blit(enemy0_down1, (b_x[index], b_y[index]))
                elif cu_time - i <= 0.4:
                    screen.blit(enemy0_down2, (b_x[index], b_y[index]))
                elif cu_time-i <= 0.6:
                    screen.blit(enemy0_down3, (b_x[index], b_y[index]))
                elif cu_time - i <= 0.8:
                    screen.blit(enemy0_down4, (b_x[index], b_y[index]))
                else:
                    st_time.pop(index)
                    b_x.pop(index)
                    b_y.pop(index)
    pygame.display.update()