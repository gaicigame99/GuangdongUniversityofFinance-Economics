import pygame
import random
import math

# 灰机大战
# 长条形
# 鼠标操作
#
# 初始化
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((480, 700))
font = pygame.font.Font("C:\Windows\Fonts\STFANGSO.TTF", 25)
# 导入图片/背景声音
bg = pygame.image.load('background.png')
bgm = pygame.mixer.Sound('game_music.ogg')
bgm.play(True)
# 飞机
hero = pygame.image.load('hero.gif')
hero_rect = hero.get_rect()

# ==========================================敌机===============================================================
# 飞机爆炸音效
e_dwon1 = pygame.mixer.Sound('enemy1_down.wav')
e_dwon2 = pygame.mixer.Sound('enemy2_down.wav')
e_dwon3 = pygame.mixer.Sound('enemy3_down.wav')
e_dwon_m = [e_dwon1, e_dwon2, e_dwon3]
eb = pygame.image.load('e_b.png')  # 敌方子弹图片
enemy0 = pygame.image.load('enemy0.png')
enemy1 = pygame.image.load('enemy1.png')
enemy2 = pygame.image.load('enemy2.png')
enemy0_rect = enemy0.get_rect()
enemy1_rect = enemy1.get_rect()
enemy2_rect = enemy2.get_rect()
# 飞机爆炸图片
# 小飞机
e_down01 = pygame.image.load('enemy0_down1.png')
e_down02 = pygame.image.load('enemy0_down2.png')
e_down03 = pygame.image.load('enemy0_down3.png')
e_down04 = pygame.image.load('enemy0_down4.png')
e_down0 = [e_down01, e_down02, e_down03, e_down04]
# 中级敌机
e_down11 = pygame.image.load('enemy1_down1.png')
e_down12 = pygame.image.load('enemy1_down2.png')
e_down13 = pygame.image.load('enemy1_down3.png')
e_down14 = pygame.image.load('enemy1_down4.png')
e_down1 = [e_down11, e_down12, e_down13, e_down14]
# 高级敌机
e_down21 = pygame.image.load('enemy2_down1.png')
e_down22 = pygame.image.load('enemy2_down2.png')
e_down23 = pygame.image.load('enemy2_down3.png')
e_down24 = pygame.image.load('enemy2_down4.png')
e_down25 = pygame.image.load('enemy2_down5.png')
e_down26 = pygame.image.load('enemy2_down6.png')
e_down2 = [e_down21, e_down22, e_down23, e_down24, e_down25, e_down26]
e_dwon_p = [e_down0, e_down1, e_down2]
e_down = [[], [], []]
e_speed = 2
f = []  # 敌机射子弹的频率
e_b1 = []  # 一级敌机子弹的坐标列表
eb_d = []  # 敌机子弹的方向
enemy1 = []  # 敌方一级飞机列表
e_count1 = 6
f1 = []  # 敌机射子弹的频率
# enemy2 = []  # 敌方二级飞机列表
# e_count2 = 3
# e_b2 = []
# f2 = []  # 敌机射子弹的频率
# enemy3 = []  # 敌方二级飞机列表
# e_count3 = 2
# f3 = []  # 敌机射子弹的频率
# e_b3 = []


# 敌机出动
def create_enemy(enemy1, e_count, f):
    for i in range(0, e_count):
        x, y = random.randint(0, 480 - enemy0_rect.height), random.randint(-300, -enemy0_rect.width)
        enemy1.append([x, y, 6 / e_count])
        f.append(e_count * 50)


# 敌机子弹的发射和子弹移动
def e_move(enemy1, e_b1, f,enemy0_rect):
    global hero_x, hero_y, eb_d, e_speed
    for b in e_b1:
        screen.blit(eb, (b[0], b[1]))
        i = e_b1.index(b)
        b[0] += eb_d[i][0]
        b[1] += eb_d[i][1]
    i = 0
    n = len(enemy1)
    while i < n:
        x, y, *arg = enemy1[i]

        if y > 700:
            enemy1.pop(i)
            enemy1.append([random.randint(0, 480 - enemy0_rect.width), random.randint(-300, -enemy0_rect.height)])
            continue
        screen.blit(enemy0, (x, y))

        f[i] -= 1
        if f[i] <= 0:
            e_b1.append([x, y])
            eb_d.append(direct(x, y, hero_x + hero_rect.width / 2, hero_y + hero_rect.height / 2, e_speed))
            screen.blit(eb, (x, y))
            f[i] = len(enemy1) * 50
        enemy1[i][1] = y + 0.5
        i += 1


# 敌机子弹的发射方向
def direct(x1, y1, x2, y2, speed):
    x = x2 - x1
    y = y2 - y1
    k = speed / math.sqrt(x ** 2 + y ** 2)

    return [x * k, y * k]


# 判断飞机是否被毁
def ruin(e, i):
    e[i][2] -= 1
    n = len(e)
    if e[i][2] <= 0:
        e_down[6 // n - 1].append([e[i][0], e[i][1], 0])
        e.pop(i)
        e.append([random.randint(0, 480 - enemy0_rect.height), random.randint(-300, -enemy0_rect.width), 6 // n])
        e_dwon_m[6 // n - 1].play()


# 爆炸过程显示
def bomb(e_down, p_down):
    i = 0
    n1 = len(e_down)
    while i < n1:
        j = 0
        n2 = len(e_down[i])
        while j < n2:
            if e_down[i][j][2] < len(p_down[i]) * 15:
                screen.blit(p_down[i][e_down[i][j][2] // 15], (e_down[i][j][0], e_down[i][j][1]))
            e_down[i][j][2] += 1
            j += 1
        i += 1


# ==================================================我方======================================
# 子弹
bullet1 = pygame.image.load('bullet.png')  # 22*22
bm = pygame.mixer.Sound('bullet.wav')
me_down = pygame.mixer.Sound('me_down.wav')
upgrade = pygame.mixer.Sound('upgrade.wav')
bullet_rect = bullet1.get_rect()
bullet1_x, bullet1_y = 0, 0
hero_x, hero_y = 240 - bullet_rect.width / 2, 700 - bullet_rect.height  # 飞机初始位置
speed = 5  # 子弹速度
bullet = []  # 子弹列表
atk = 1  # 我方子弹攻击力


# 击中敌机
def crash(bullet, enemy1, e_rect, b_rect):
    global score
    i = 0
    bn = len(bullet)
    while i < bn:
        up_level()
        bx, by = bullet[i]
        j = 0
        en = len(list(enemy1))

        while j < en:
            ex, ey, *arg = enemy1[j]
            if ex + e_rect.width > bx > ex - b_rect.width and \
                    ey + e_rect.height > by > ey - b_rect.height and \
                    ey > -e_rect.height:
                score += 1
                ruin(enemy1, j)
                bullet.pop(i)
                i -= 1
                bn -= 1
                break
            j += 1
        i += 1


# 被敌方击中和撞中
def touched(bullet, enemy, e_rect, h_x, h_y, h_rect):
    global blood
    i = 0
    bn = len(bullet)
    while i < bn:
        bx, by = bullet[i]
        if h_x < bx < h_x + h_rect.width and h_y < by < h_y + h_rect.height:
            blood -= 1
            bullet.pop(i)
            me_down.play()
            bn -= 1
            i -= 1
            break
        j = 0
        en = len(enemy)
        while j < en:
            ex, ey, *arg = enemy[j]
            up_level()
            if h_x + h_rect.width > ex > h_x - e_rect.width and h_y + h_rect.height > ey > h_y - e_rect.height:
                ruin(enemy, j)
                blood -= 1
                me_down.play()
            j += 1
        i += 1


# 我方子弹移动
def zidan(bullet, x, y, flag):
    if flag:
        bullet.append([x + bullet_rect.width / 2, y])
        bullet.append([x + 3 * bullet_rect.width, y])
    n = len(bullet)
    i = 0
    while i < n:
        x, y = bullet[i]
        if y < -bullet_rect.width:
            bullet.remove([x, y])
            n -= 1
        else:
            screen.blit(bullet1, (x, y))
            screen.blit(bullet1, (x, y))
            bullet[i][1] = y - speed
            i += 1


# 大型飞机出动和关卡升级函数
def up_level():
    global score, e_speed,blood,level
    if score % 100 == 0 and score != 0 and level != score//100+1:
        upgrade.play()
        e_speed += 1
        blood += 10
        level = score // 100+1



# 分值和血量
score = 0
blood = 100
level =1
flag = 0
pygame.mouse.set_visible(False)

create_enemy(enemy1, e_count1, f1)
# create_enemy(enemy2, e_count2, f2)
# create_enemy(enemy3, e_count3, f3)

while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            hero_x, hero_y = pygame.mouse.get_pos()
            hero_x -= hero_rect.width / 2
            hero_y -= hero_rect.height / 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet1_x, bullet1_y = hero_x, hero_y + hero_rect.height / 2
            bm.play()
            flag = 1
    screen.blit(hero, (hero_x, hero_y))
    zidan(bullet, bullet1_x, bullet1_y, flag)
    flag = 0

    e_move(enemy1, e_b1, f1,enemy0_rect)
    # e_move(enemy2, e_b2, f2,enemy1_rect)
    # e_move(enemy3, e_b3, f3,enemy2_rect)

    crash(bullet, enemy1, enemy0_rect, bullet_rect)
    touched(e_b1, enemy1, enemy0_rect, hero_x, hero_y, hero_rect)
    # crash(bullet, enemy2, enemy1_rect, bullet_rect)
    # touched(e_b2, enemy2, enemy1_rect, hero_x, hero_y, hero_rect)
    # crash(bullet, enemy3, enemy2_rect, bullet_rect)
    # touched(e_b3, enemy3, enemy2_rect, hero_x, hero_y, hero_rect)

    bomb(e_down, e_dwon_p)
    # bomb(e_down, e_down1)
    # bomb(e_down, e_down2)

    score_txt = font.render(f'得分：{score}', True, (0, 0, 0))
    blood_txt = font.render(f'血量：{blood}', True, (0, 0, 0))
    level_txt = font.render(f'关卡：{level}', True, (0, 0, 0))
    screen.blit(score_txt, (50, 0))
    screen.blit(blood_txt, (50, 30))
    screen.blit(level_txt, (50, 670))
    pygame.display.update()
