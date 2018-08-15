import pygame
import random
import math

# conn = pymysql.connect(host='localhost', port=3306, user='root',
#                        passwd='150202', db='rank', charset='utf8')
# cur = conn.cursor()
stronger = []  # 分数最高三个分数
cla = 0  # 等级
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('瓜皮战机')
screen = pygame.display.set_mode((500, 800))

blue_button = pygame.image.load('blue.png')  # 开始游戏
blue_button = pygame.transform.scale(blue_button, (200, 48))
blue_rect = blue_button.get_rect()
font2 = pygame.font.Font("C:\Windows\Fonts\STFANGSO.TTF", 30)
font3 = pygame.font.Font("C:\Windows\Fonts\STZHONGS.TTF", 50)
buttonm = pygame.mixer.Sound(r"sound\button.wav")
start_surface = pygame.image.load('bg.jpg')  # 开始界面背景
start_surface = pygame.transform.scale(start_surface, (500, 854))
rank_frame = pygame.image.load('rank.png')  # 排行榜框
return_button = pygame.image.load('return.png')  # 返回按钮
start_button = pygame.image.load('1.png')  # 开始游戏
rank_button = pygame.image.load('2.png')  # 排行榜
set_button = pygame.image.load('3.png')  # 设置
exit_button = pygame.image.load('4.png')  # 退出游戏
guangquan_button = pygame.image.load('5.png')  # 退出游戏
easy_button = pygame.image.load('简单.png')  # 简单
mid_button = pygame.image.load('中等.png')  # 中等
dif_button = pygame.image.load('困难.png')  # 困难
# 按钮的尺寸
return_rect = return_button.get_rect()
start_rect = start_button.get_rect()
rank_rect = rank_button.get_rect()
set_rect = set_button.get_rect()
exit_rect = exit_button.get_rect()
easy_rect = easy_button.get_rect()
mid_rect = mid_button.get_rect()
dif_rect = dif_button.get_rect()
# 按钮坐标
return_x, return_y = 300, 700
start_x, start_y = 100, 200
rank_x, rank_y = 100, 300
set_x, set_y = 100, 400
exit_x, exit_y = 100, 500
easy_x, easy_y = 200, 300
mid_x, mid_y = 200, 400
dif_x, dif_y = 200, 500
guangquan_x, guangquan_y = 100, 280
fa = 0


# 打印开始界面的按钮
def buttons():
    screen.blit(start_surface, (0, 0))

    screen.blit(start_button, (start_x, start_y))
    start_txt = font2.render('开始游戏', True, (0, 0, 0))
    screen.blit(start_txt, (start_x + start_rect.width // 4, start_y + start_rect.height // 4))

    screen.blit(rank_button, (rank_x, rank_y))
    rank_txt = font2.render('排行榜', True, (0, 0, 0))
    screen.blit(rank_txt, (rank_x + rank_rect.width // 3, rank_y + rank_rect.height // 4))

    screen.blit(set_button, (set_x, set_y))
    set_txt = font2.render('设置', True, (0, 0, 0))
    screen.blit(set_txt, (set_x + set_rect.width // 3, set_y + set_rect.height // 4))

    screen.blit(exit_button, (exit_x, exit_y))
    exit_txt = font2.render('退出游戏', True, (0, 0, 0))
    screen.blit(exit_txt, (exit_x + exit_rect.width // 4, exit_y + exit_rect.height // 4))


# 开始界面——按钮检测
def click():
    global fa
    x, y = pygame.mouse.get_pos()
    if start_x < x < start_x + start_rect.width and start_y < y < start_y + start_rect.height:
        buttonm.play()
        fa = 1
    elif rank_x < x < rank_x + rank_rect.width and rank_y < y < rank_y + rank_rect.height:
        buttonm.play()
        rank()
    elif exit_x < x < exit_x + exit_rect.width and exit_y < y < exit_y + exit_rect.height:
        buttonm.play()
        exit()
    elif set_x < x < set_x + set_rect.width and set_y < y < set_y + set_rect.height:
        buttonm.play()
        class_()


# 设置——等级选择
def class_():
    global cla, guangquan_x, guangquan_y
    flag = 1
    while flag:

        screen.blit(start_surface, (0, 0))
        screen.blit(easy_button, (easy_x, easy_y))
        screen.blit(mid_button, (mid_x, mid_y))
        screen.blit(dif_button, (dif_x, dif_y))
        screen.blit(return_button, (return_x, return_y))  # 返回按钮
        screen.blit(guangquan_button, (guangquan_x, guangquan_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if easy_x < x < easy_x + easy_rect.width and easy_y < y < easy_y + easy_rect.height:
                    buttonm.play()
                    guangquan_x, guangquan_y = easy_x - 100, easy_y - 20
                    cla = 0.5
                elif mid_x < x < mid_x + mid_rect.width and mid_y < y < mid_y + mid_rect.height:
                    buttonm.play()
                    guangquan_x, guangquan_y = mid_x - 100, mid_y - 20
                    cla = 1
                elif dif_x < x < dif_x + dif_rect.width and dif_y < y < dif_y + dif_rect.height:
                    buttonm.play()
                    guangquan_x, guangquan_y = dif_x - 100, dif_y - 20
                    cla = 1.5
                elif return_x < x < return_x + return_rect.width and return_y < y < return_y + return_rect.height:
                    buttonm.play()
                    flag = 0

            pygame.display.update()


# 排行榜——打印
def rank():
    stronger.sort(reverse=True)
    screen.blit(start_surface, (0, 0))
    screen.blit(rank_frame, (50, 200))
    txt = font3.render('排行榜', True, (43, 130, 255))
    screen.blit(txt, (170, 200))

    screen.blit(return_button, (return_x, return_y))  # 返回按钮

    n = 0
    for s in stronger:
        txt = font2.render('第' + str(n + 1) + '名\t\t\t' + str(s), True, (43, 130, 255))
        screen.blit(txt, (100, 330 + 60 * n))
        n += 1
        if n == 3:
            break
    pygame.display.update()

    flag = 1
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if return_x < x < return_x + return_rect.width and return_y < y < return_y + return_rect.height:
                    buttonm.play()
                    flag = 0


# ===================================================================================================
# =====================================================================================================

# 飞机大战
# 游戏规则：
# 鼠标操作，点击开始游戏，开始游戏。击毁小中大型敌机飞机，获得（1，5，10）分，假如小中大型飞机安全离开界面，
# 减少我方敌机（1，5，8）血量。每500分一关，随着关数的增加，敌机的速度会增加，道具的频率也会增加。拿一个
# 道具，子弹会变强，伤害加1。假如长时间没有拿道具，子弹会变为最弱的。
# 爆炸效果          get
# 添加游戏得分      get
# 小，中，大型战机  血量1，10，80       get
# 增加道具           get
# 添加英雄生命值      get
# 添加音效            get
# 开始界面            get
# 结束界面            get
# 制作游戏关卡        get
# 大型飞机放弹        get
back_mousic = pygame.mixer.Sound("sound\game_music.ogg")
back_mousic1 = pygame.mixer.Sound("sound\enemy1_down.wav")
back_mousic2 = pygame.mixer.Sound("sound\enemy2_down.wav")
back_mousic3 = pygame.mixer.Sound("sound\enemy3_down.wav")
bulletm = pygame.mixer.Sound(r"sound\bullet.wav")
font = pygame.font.Font("C:\Windows\Fonts\STFANGSO.TTF", 20)
font1 = pygame.font.Font("C:\Windows\Fonts\STFANGSO.TTF", 36)
bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (500, 800))
enemy0_down1 = pygame.image.load(r"images\enemy0_down1.png")
enemy0_down2 = pygame.image.load(r"images\enemy0_down2.png")
enemy0_down3 = pygame.image.load(r"images\enemy0_down3.png")
enemy0_down4 = pygame.image.load(r"images\enemy0_down4.png")
enemy1_down1 = pygame.image.load(r"images\enemy1_down1.png")
enemy1_down2 = pygame.image.load(r"images\enemy1_down2.png")
enemy1_down3 = pygame.image.load(r"images\enemy1_down3.png")
enemy1_down4 = pygame.image.load(r"images\enemy1_down4.png")
enemy2_down1 = pygame.image.load(r"images\enemy2_down1.png")
enemy2_down2 = pygame.image.load(r"images\enemy2_down2.png")
enemy2_down3 = pygame.image.load(r"images\enemy2_down3.png")
enemy2_down4 = pygame.image.load(r"images\enemy2_down4.png")

Key = pygame.image.load(r"images\button_nor.png")
Key2 = pygame.transform.scale(Key, (200, 48))
bg3 = pygame.image.load(r"bg3.jpg")
bg3 = pygame.transform.scale(bg3, (500, 800))
bg4 = pygame.image.load(r"bg4.jpg")
bg4 = pygame.transform.scale(bg4, (500, 800))
bg5 = pygame.image.load(r"bg5.jpg")
bg5 = pygame.transform.scale(bg5, (500, 800))
bomb1 = pygame.image.load(r"images\bomb-1.gif")
bomb2 = pygame.image.load(r"images\bomb-2.gif")
bomb3 = pygame.image.load(r"images\plane.png")

bullet = pygame.image.load(r"p-f03.png")
bullet1 = pygame.image.load(r"p-f02.png")
bullet2 = pygame.image.load(r"p-f01.png")
jizhong = pygame.image.load(r"jizhong1.png")
jizhong = pygame.transform.scale(jizhong, (40, 60))


Enemy = pygame.image.load("a4-2.png")
Enemy = pygame.transform.scale(Enemy, (51, 39))
hero = pygame.image.load("a4-1.png")
hero = pygame.transform.scale(hero, (100, 122))

# 我方战机
h_rect = hero.get_rect()  # 获得飞机的模型
h_width = h_rect.width  # 获得飞机宽度
h_height = h_rect.height  # 获得飞机高度
hx = 100  # 我方飞机开始的位置
hy = 100
# 子弹
bx = []  # 子弹的的坐标
by = []
vis = []  # 标记子弹是否显示
times = 0  # 标记出现子弹相隔的时间

# 小型战机
Enemy_x = []  # 敌机的坐标
Enemy_y = []
Enemy_times = []  # 标记战机毁灭后的情景
vise = []  # 标记敌机是否显示
times2 = 0  # 标记出现敌机相隔的时间

# 中型敌机
Enemy_mid = pygame.image.load("a4-3.png")
Enemy_mid = pygame.transform.scale(Enemy_mid, (69, 89))
med_x = []
med_y = []
med_Q = []
med_times = []  # 标记中型战机毁灭后的情景
times3 = 0  # 标记出现中型敌机相隔的时间
vism2 = []  # 标记中型敌机是否显示

# 大型敌机
Enemy_max = pygame.image.load("a4-6.png")
Enemy_max = pygame.transform.scale(Enemy_max, (165, 264))
max_x = []
max_y = []
max_Q = []
max_times = []  # 标记大型战机毁灭后的情景
times4 = 0  # 标记出现大型敌机相隔的时间
vism4 = []  # 标记大型敌机是否显示
max_speed = 5

# 道具1
bomb1_x = 0
bomb1_y = 0
bomb1_vis = False
bomb1_times = 0

# 道具2
bomb2_x = 0
bomb2_y = 0
bomb2_vis = False
bomb2_times = 0

# 道具3
bomb3_x = 0
bomb3_y = 0
bomb3_vis = False
bomb3_times = 0

for i in range(200):  # 初始化变量
    bx.append(0)  # 子弹
    by.append(0)

    Enemy_x.append(0)  # 小型战机
    Enemy_y.append(0)
    vis.append(False)
    vise.append(False)
    Enemy_times.append(500)

    med_x.append(0)  # 中型战机
    med_y.append(0)
    med_Q.append(10)
    med_times.append(500)
    vism2.append(False)

    max_x.append(0)  # 大型战机
    max_y.append(0)
    max_Q.append(160)
    max_times.append(500)
    vism4.append(False)

grade = 0  # 分数，小型敌机（1分），中型敌机（5分），大型敌机（10分）
bullet_vis = 0  # 0(buttet号子弹)，1（buttet1号子弹），>2（buttet1号子弹）     三种子弹对应的伤害是（1，2，3）
bulletkk_vis = 0
kkk = 0
kkk2 = 0
my_Q = 10  # 如果小型战机安全离开（-1），中型（-5），大型（-8）
gu = 1
back_mousic.play(-1)

screen_times = 0


###########################################################################################################################

# 敌机子弹的发射方向
def direct(x1, y1, x2, y2, speed):  # speed敌机子弹的速度
    x = x2 - x1
    y = y2 - y1
    k = speed / math.sqrt(x ** 2 + y ** 2)
    return x * k, y * k


##############################################################################################################################
# 敌机子弹的初始化，大boos会发弹
ebx = []
eby = []
eb_speedx = []
eb_speedy = []
eb_falg = []
eb_times = 0
gu_times = 0
for i in range(100):  # 初始化
    ebx.append(0)
    eby.append(0)
    eb_speedx.append(0)
    eb_speedy.append(0)
    eb_falg.append(False)
###############################################################################################################################
while True:
    # 开始界面
    if fa == 0:
        buttons()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click()
    ###########################################################################################################################
    # 结束界面
    if fa == 3:
        str1 = "游戏结束！ "
        t = font1.render(str1, True, (255, 0, 0))
        screen.blit(t, (170, 300))
        # 继续游戏按钮
        screen.blit(blue_button, (140, 600))
        str2 = "继续游戏"
        t = font.render(str2, True, (0, 0, 0))
        screen.blit(t, (200, 610))
        # 退出游戏按钮
        screen.blit(blue_button, (140, 700))
        str3 = "退出游戏"
        t = font.render(str3, True, (0, 0, 0))
        screen.blit(t, (200, 710))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                if x1 > 180 and x1 < 180 + 132 and y1 > 600 and y1 < 600 + 48:
                    fa = 1
                    my_Q = 10
                elif 140 < x1 < 140 + blue_rect.width and 700 < y1 < 700 + blue_rect.width:
                    stronger.append(grade)
                    fa = 0
                    ##################################################################
                    # 初始化
                    hx = 100  # 我方飞机开始的位置
                    hy = 100
                    # 子弹
                    bx = []  # 子弹的的坐标
                    by = []
                    vis = []  # 标记子弹是否显示
                    times = 0  # 标记出现子弹相隔的时间

                    # 小型战机
                    Enemy_x = []  # 敌机的坐标
                    Enemy_y = []
                    Enemy_times = []  # 标记战机毁灭后的情景
                    vise = []  # 标记敌机是否显示
                    times2 = 0  # 标记出现敌机相隔的时间

                    # 中型敌机
                    med_x = []
                    med_y = []
                    med_Q = []
                    med_times = []  # 标记中型战机毁灭后的情景
                    times3 = 0  # 标记出现中型敌机相隔的时间
                    vism2 = []  # 标记中型敌机是否显示

                    # 大型敌机
                    max_x = []
                    max_y = []
                    max_Q = []
                    max_times = []  # 标记大型战机毁灭后的情景
                    times4 = 0  # 标记出现大型敌机相隔的时间
                    vism4 = []  # 标记大型敌机是否显示
                    max_speed = 5

                    # 道具1
                    bomb1_x = 0
                    bomb1_y = 0
                    bomb1_vis = False
                    bomb1_times = 0

                    # 道具2
                    bomb2_x = 0
                    bomb2_y = 0
                    bomb2_vis = False
                    bomb2_times = 0

                    # 道具3
                    bomb3_x = 0
                    bomb3_y = 0
                    bomb3_vis = False
                    bomb3_times = 0

                    for i in range(200):  # 初始化变量
                        bx.append(0)  # 子弹
                        by.append(0)

                        Enemy_x.append(0)  # 小型战机
                        Enemy_y.append(0)
                        vis.append(False)
                        vise.append(False)
                        Enemy_times.append(500)

                        med_x.append(0)  # 中型战机
                        med_y.append(0)
                        med_Q.append(10)
                        med_times.append(500)
                        vism2.append(False)

                        max_x.append(0)  # 大型战机
                        max_y.append(0)
                        max_Q.append(160)
                        max_times.append(500)
                        vism4.append(False)

                    grade = 0  # 分数，小型敌机（1分），中型敌机（5分），大型敌机（10分）
                    bullet_vis = 0  # 0(buttet号子弹)，1（buttet1号子弹），>2（buttet1号子弹）     三种子弹对应的伤害是（1，2，3）
                    bulletkk_vis = 0
                    kkk = 0
                    kkk2 = 0
                    my_Q = 10  # 如果小型战机安全离开（-1），中型（-5），大型（-8）
                    gu = 1
                    screen_times = 0
                    break
    ################################################################################################################################
    # 按空格后的暂停界面
    if fa == 4:
        # 继续游戏按钮
        screen.blit(blue_button, (140, 600))
        str2 = "继续游戏"
        t = font.render(str2, True, (0, 0, 0))
        screen.blit(t, (200, 610))
        # 退出游戏按钮
        screen.blit(blue_button, (140, 700))
        str3 = "退出游戏"
        t = font.render(str3, True, (0, 0, 0))
        screen.blit(t, (200, 710))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    fa = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                if x1 > 180 and x1 < 180 + 132 and y1 > 600 and y1 < 600 + 48:
                    fa = 1
                elif 140 < x1 < 140 + blue_rect.width and 700 < y1 < 700 + blue_rect.width:
                    fa = 0
                    stronger.append(grade)
                    # 我方战机
                    ##################################################################
                    # 初始化
                    hx = 100  # 我方飞机开始的位置
                    hy = 100
                    # 子弹
                    bx = []  # 子弹的的坐标
                    by = []
                    vis = []  # 标记子弹是否显示
                    times = 0  # 标记出现子弹相隔的时间

                    # 小型战机
                    Enemy_x = []  # 敌机的坐标
                    Enemy_y = []
                    Enemy_times = []  # 标记战机毁灭后的情景
                    vise = []  # 标记敌机是否显示
                    times2 = 0  # 标记出现敌机相隔的时间

                    # 中型敌机
                    med_x = []
                    med_y = []
                    med_Q = []
                    med_times = []  # 标记中型战机毁灭后的情景
                    times3 = 0  # 标记出现中型敌机相隔的时间
                    vism2 = []  # 标记中型敌机是否显示

                    # 大型敌机
                    max_x = []
                    max_y = []
                    max_Q = []
                    max_times = []  # 标记大型战机毁灭后的情景
                    times4 = 0  # 标记出现大型敌机相隔的时间
                    vism4 = []  # 标记大型敌机是否显示
                    max_speed = 5

                    # 道具1
                    bomb1_x = 0
                    bomb1_y = 0
                    bomb1_vis = False
                    bomb1_times = 0

                    # 道具2
                    bomb2_x = 0
                    bomb2_y = 0
                    bomb2_vis = False
                    bomb2_times = 0

                    # 道具3
                    bomb3_x = 0
                    bomb3_y = 0
                    bomb3_vis = False
                    bomb3_times = 0

                    for i in range(200):  # 初始化变量
                        bx.append(0)  # 子弹
                        by.append(0)

                        Enemy_x.append(0)  # 小型战机
                        Enemy_y.append(0)
                        vis.append(False)
                        vise.append(False)
                        Enemy_times.append(500)

                        med_x.append(0)  # 中型战机
                        med_y.append(0)
                        med_Q.append(10)
                        med_times.append(500)
                        vism2.append(False)

                        max_x.append(0)  # 大型战机
                        max_y.append(0)
                        max_Q.append(160)
                        max_times.append(500)
                        vism4.append(False)

                    grade = 0  # 分数，小型敌机（1分），中型敌机（5分），大型敌机（10分）
                    bullet_vis = 0  # 0(buttet号子弹)，1（buttet1号子弹），>2（buttet1号子弹）     三种子弹对应的伤害是（1，2，3）
                    bulletkk_vis = 0
                    kkk = 0
                    kkk2 = 0
                    my_Q = 10  # 如果小型战机安全离开（-1），中型（-5），大型（-8）
                    gu = 1
                    screen_times = 0
    ################################################################################################################################
    # 游戏界面
    if fa == 1:
        if gu == 1:
            screen.blit(bg3, (0, screen_times))
            screen.blit(bg3, (0, screen_times - 800))
            if gu_times < 200:
                str1 = "第 " + str(gu) + " 关 "
                text = font1.render(str1, True, (255, 255, 255))
                screen.blit(text, (300, 300))
                gu_times += 1
        if gu == 2:
            screen.blit(bg4, (0, screen_times))
            screen.blit(bg4, (0, screen_times - 800))
            if gu_times < 200:
                str1 = "第 " + str(gu) + " 关 "
                text = font1.render(str1, True, (255, 255, 255))
                screen.blit(text, (300, 300))
                gu_times += 1
        if gu >= 3:
            screen.blit(bg5, (0, screen_times))
            screen.blit(bg5, (0, screen_times - 800))
            if gu_times < 200:
                str1 = "第 " + str(gu) + " 关 "
                text = font1.render(str1, True, (255, 255, 255))
                screen.blit(text, (300, 300))
                gu_times += 1

        str1 = str(gu)  # 显示关卡
        text = font2.render(str1, True, (255, 0, 0))
        screen.blit(text, (420, 2))
        str1 = "第      关 "
        text = font2.render(str1, True, (255, 255, 255))
        screen.blit(text, (370, 2))

        str1 = str(grade)  # 显示得分
        text = font2.render(str1, True, (255, 0, 0))
        screen.blit(text, (450, 40))
        str1 = "得分: "
        text = font2.render(str1, True, (255, 255, 255))
        screen.blit(text, (370, 40))
        times += 1  # 这些变量只是一个时间上的一个辅助
        times2 += 1
        times3 += 1
        times4 += 1
        eb_times += 1
        bomb1_times += 1
        bomb2_times += 1
        kkk += 1
        kkk2 += 1
        screen_times += 0.6
        if screen_times > 800:
            screen_times = 0

        if kkk > 950:  # kkk控制1，2号子弹的时间，假如长时间没有吃道具，会变成0号子弹
            if bullet_vis > 0:
                bullet_vis -= 1
                kkk = 0
        if kkk > 10000:
            kkk = 1000
        if kkk2 > 850:  # kkk控制1，2号子弹的时间，假如长时间没有吃道具，会变成0号子弹
            if bulletkk_vis > 0:
                bulletkk_vis -= 1
                kkk2 = 0
        if kkk2 > 10000:
            kkk2 = 1000
        hx, hy = pygame.mouse.get_pos()  # 获取鼠标的坐标
        ###################################################################################################################################
        # 子弹的显示与碰撞检测
        for i in range(200):  # 子弹的位置小于0，置False
            if by[i] < 0:
                vis[i] = False

        if times == 1 or times > 14:  # 两个子弹出现的相隔时间
            for i in range(200):
                if vis[i]:
                    pass
                else:
                    bx[i] = hx - 10
                    by[i] = hy
                    buttonm.play()
                    vis[i] = True  # 加子弹
                    times = 2
                    break

        for i in range(200):
            if vis[i]:
                pp = 10
                if bullet_vis == 0:
                    if bulletkk_vis == 0:
                        screen.blit(bullet, (bx[i] - pp, by[i] - pp))  # 显示子弹
                    if bulletkk_vis == 1:
                        screen.blit(bullet, (bx[i] + 10 - pp, by[i] - pp))  # 双
                        screen.blit(bullet, (bx[i] - 10 - 8, by[i] - 2))
                    if bulletkk_vis > 1:
                        screen.blit(bullet, (bx[i] - 20 - pp, by[i] - pp))  # 三
                        screen.blit(bullet, (bx[i] - pp, by[i] - pp))
                        screen.blit(bullet, (bx[i] - pp + 20, by[i] - pp))
                if bullet_vis == 1:
                    if bulletkk_vis == 0:
                        screen.blit(bullet1, (bx[i] - pp, by[i] - pp))  # 显示子弹
                    if bulletkk_vis == 1:
                        screen.blit(bullet1, (bx[i] + 10 - pp, by[i] - pp))  # 双
                        screen.blit(bullet1, (bx[i] - 10 - pp, by[i] - pp))
                    if bulletkk_vis > 1:
                        screen.blit(bullet1, (bx[i] - 20 - pp, by[i] - pp))  # 三
                        screen.blit(bullet1, (bx[i] - pp, by[i] - pp))
                        screen.blit(bullet1, (bx[i] + 20 - pp, by[i] - pp))
                if bullet_vis >= 2:
                    if bulletkk_vis == 0:
                        screen.blit(bullet2, (bx[i] - pp, by[i] - pp))  # 显示子弹
                    if bulletkk_vis == 1:
                        screen.blit(bullet2, (bx[i] + 10 - pp, by[i] - pp))  # 双
                        screen.blit(bullet2, (bx[i] - 10 - pp, by[i] - pp))
                    if bulletkk_vis > 1:
                        screen.blit(bullet2, (bx[i] - 20 - pp, by[i] - pp))  # 三
                        screen.blit(bullet2, (bx[i] - pp, by[i] - pp))
                        screen.blit(bullet2, (bx[i] + 20 - pp, by[i] - pp))
                by[i] -= 4.5  # 子弹速度
                for j in range(200):
                    if vise[j]:
                        if bx[i] + 22 > Enemy_x[j] and bx[i] < Enemy_x[j] + 51 and by[i] < Enemy_y[j] + 39 and by[
                            i] + 22 > Enemy_y[j]:  # 碰撞检测
                            back_mousic1.play()
                            vise[j] = False
                            grade += 1
                            Enemy_times[j] = 0
                            vis[i] = False

                    if vism2[j]:  # 中型敌机的拼撞检测
                        if bx[i] + 22 > med_x[j] and bx[i] < med_x[j] + 69 and by[i] < med_y[j] + 89 and by[i] + 22 > \
                                med_y[j]:  # 中型敌机拼撞检测
                            if bullet_vis <= 2:
                                med_Q[j] -= (1 + bullet_vis)
                            else:
                                med_Q[j] -= (1 + 2)
                            vis[i] = False
                            if med_Q[j] < 0:
                                back_mousic2.play()
                                med_times[j] = 0
                                grade += 5
                                vism2[j] = False
                                med_Q[j] = 10

                    if vism4[j]:  # 大型敌机的拼撞检测
                        if bx[i] + 22 > max_x[j] and bx[i] < max_x[j] + 165 and by[i] < max_y[j] + 246 and by[i] + 22 > \
                                max_y[j]:  # 大型敌机拼撞检测
                            if bullet_vis <= 2:
                                max_Q[j] -= (1 + bullet_vis)
                            else:
                                max_Q[j] -= (1 + 2)
                            vis[i] = False
                            if max_Q[j] < 0:
                                back_mousic3.play()
                                max_times[j] = 0
                                grade += 10
                                vism4[j] = False
                                max_Q[j] = 160

                                bomb3_vis = True  # 道具3的添加
                                bomb3_x = max_x[j]
                                bomb3_y = max_y[j]
                                gu += 1
                                gu_times = 0
                                times4 = 2

        ##############################################################################################################################
        # 小型战机
        if times2 == 1 or times2 > 50:  # 小型机出现的相隔时间
            for i in range(200):
                if vise[i]:
                    pass
                elif Enemy_times[i] < -2:
                    Enemy_x[i] = random.randint(50, 450)
                    Enemy_y[i] = -50
                    vise[i] = True
                    times2 = 2
                    break

        for i in range(200):  # 显示小型战机毁灭
            if vise[i]:
                pass
            elif Enemy_times[i] > -2 and Enemy_times[i] < 35:
                if Enemy_times[i] < 5:
                    screen.blit(enemy0_down1, (Enemy_x[i], Enemy_y[i]))
                if Enemy_times[i] < 13 and Enemy_times[i] > 5:
                    screen.blit(enemy0_down2, (Enemy_x[i], Enemy_y[i]))
                if Enemy_times[i] < 21 and Enemy_times[i] > 13:
                    screen.blit(enemy0_down3, (Enemy_x[i], Enemy_y[i]))
                if Enemy_times[i] < 29 and Enemy_times[i] > 21:
                    screen.blit(enemy0_down4, (Enemy_x[i], Enemy_y[i]))
                Enemy_times[i] += 1
            if Enemy_times[i] > 29:
                Enemy_times[i] = -3

        for i in range(200):  # 小型敌机的显示
            if vise[i]:
                if Enemy_y[i] > 800:
                    my_Q -= 1
                    vise[i] = False
                else:
                    screen.blit(Enemy, (Enemy_x[i], Enemy_y[i]))
                    Enemy_y[i] += 1.2 + (gu - 1) * 0.5 + cla  # 小型敌机的速度

        ##############################################################################################################################
        # 中型敌机
        if times3 == 1 or times3 > 250:  # 中型敌机出现的相隔时间
            for i in range(200):
                if vise[i]:
                    pass
                elif med_times[i] < -2:
                    med_x[i] = random.randint(50, 450)
                    med_y[i] = -50
                    vism2[i] = True
                    times3 = 2
                    break

        for i in range(200):  # 显示中型战机毁灭
            if vism2[i]:
                pass
            elif med_times[i] > -2 and med_times[i] < 35:
                if med_times[i] < 5:
                    screen.blit(enemy1_down1, (med_x[i], med_y[i]))
                if med_times[i] < 13 and med_times[i] > 5:
                    screen.blit(enemy1_down2, (med_x[i], med_y[i]))
                if med_times[i] < 21 and med_times[i] > 13:
                    screen.blit(enemy1_down3, (med_x[i], med_y[i]))
                if med_times[i] < 29 and med_times[i] > 21:
                    screen.blit(enemy1_down4, (med_x[i], med_y[i]))
                med_times[i] += 1
            if med_times[i] > 29:
                med_times[i] = -3

        for i in range(200):  # 中型敌机的显示
            if vism2[i]:
                if med_y[i] > 800:
                    my_Q -= 5
                    vism2[i] = False
                else:
                    screen.blit(Enemy_mid, (med_x[i], med_y[i]))
                    pygame.draw.line(screen, (144, 144, 144), (med_x[i], med_y[i]), (med_x[i] + 69, med_y[i]), 6)
                    if med_Q[i] > 2:
                        pygame.draw.line(screen, (205, 186, 150), (med_x[i], med_y[i]),
                                         (med_x[i] + (69 / 10) * med_Q[i], med_y[i]), 6)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (med_x[i], med_y[i]),
                                         (med_x[i] + (69 / 10) * med_Q[i], med_y[i]), 6)
                    med_y[i] += 1.2 + (gu - 1) * 0.5 + cla  # 敌机的速度
        ################################################################################################################################
        # 大型敌机，大型敌机左右移动
        if times4 == 1 or times4 > 4000:  # 大型敌机出现的相隔时间
            for i in range(200):
                if vise[i]:
                    pass
                elif max_times[i] < -2:
                    max_x[i] = 300
                    max_y[i] = 10
                    vism4[i] = True
                    times4 = 2
                    break

        for i in range(200):  # 显示大型战机毁灭
            if vism4[i]:
                pass
            elif max_times[i] > -2 and max_times[i] < 35:
                if max_times[i] < 18:
                    screen.blit(enemy2_down2, (max_x[i], max_y[i]))
                if max_times[i] < 38 and max_times[i] > 18:
                    screen.blit(enemy2_down3, (max_x[i], max_y[i]))
                if max_times[i] < 55 and max_times[i] > 38:
                    screen.blit(enemy2_down4, (max_x[i], max_y[i]))
                max_times[i] += 1
            if max_times[i] > 55:
                max_times[i] = -3

        for i in range(200):  # 大型敌机的显示
            if vism4[i]:
                if max_y[i] > 800:
                    my_Q -= 8
                    vism4[i] = False
                else:
                    screen.blit(Enemy_max, (max_x[i], max_y[i]))
                    pygame.draw.line(screen, (144, 144, 144), (max_x[i], max_y[i]), (max_x[i] + 165, max_y[i]), 10)
                    if max_Q[i] > 20:
                        pygame.draw.line(screen, (255, 165, 79), (max_x[i], max_y[i]),
                                         (max_x[i] + (165 / 160) * max_Q[i], max_y[i]), 10)
                    else:
                        pygame.draw.line(screen, (255, 0, 0), (max_x[i], max_y[i]),
                                         (max_x[i] + (165 / 160) * max_Q[i], max_y[i]), 10)
                    max_x[i] += max_speed * 0.1
                    if max_x[i] > 500 - 165 or max_x[i] < 0:
                        max_speed = -max_speed

                    if eb_times > 50:  # 加敌机子弹
                        for k in range(100):
                            if eb_falg[k]:
                                pass
                            else:
                                eb_falg[k] = True
                                eb_times = 0
                                ebx[k] = max_x[i] + 82
                                eby[k] = max_y[i] + 246
                                xs = hx - ebx[k]
                                ys = hy - eby[k]
                                ks = 4 / math.sqrt(xs ** 2 + ys ** 2)
                                eb_speedx[k], eb_speedy[k] = xs * ks, ys * ks
                                break
        ###############################################################################################################################
        # 子弹的移动
        for i in range(100):
            if eb_falg[i]:
                screen.blit(jizhong, (ebx[i], eby[i]))
                ebx[i] += eb_speedx[i]
                eby[i] += eb_speedy[i]
                if eby[i] < 0 or ebx[i] > 500 or eby[i] > 800:
                    eb_falg[i] = False

                if hx + 100 > ebx[i] and hx < ebx[i] + 22 and hy + 45 < eby[i] + 22 and hy + 80 > eby[i]:  # 拼撞检测
                    eb_falg[i] = False
                    my_Q -= 1

        ################################################################################################################################
        # 道具1,变子弹的颜色
        if bomb1_times > 900 - (gu - 1) * 50:
            bomb1_x = random.randint(50, 450)
            bomb1_y = -50
            bomb1_times = 0
            bomb1_vis = True
        if bomb1_vis:
            if hx + 100 > bomb1_x and hx < bomb1_x + 58 and hy < bomb1_y + 88 and hy + 124 > bomb1_y:  # 拼撞检测
                bulletm.play()
                bomb1_vis = False
                bullet_vis += 1
                if bullet_vis > 2:
                    bullet_vis = 2
                kkk = 0
        if bomb1_vis:
            bomb1_y += 2
            screen.blit(bomb2, (bomb1_x, bomb1_y))
            if bomb1_y > 800 - (gu - 1) * 50 * 0.7:
                bomb1_vis = False

        # 道具2,双弹
        if bomb2_times > 750 - (gu - 1) * 50:
            bomb2_x = random.randint(50, 450)
            bomb2_y = -50
            bomb2_times = 0
            bomb2_vis = True
        if bomb2_vis:
            if hx + 100 > bomb2_x and hx < bomb2_x + 58 and hy < bomb2_y + 88 and hy + 124 > bomb2_y:  # 拼撞检测
                bulletm.play()
                bomb2_vis = False
                bulletkk_vis += 1
                if bulletkk_vis > 2:
                    bulletkk_vis = 2
                kkk2 = 0
        if bomb2_vis:
            bomb2_y += 2
            screen.blit(bomb1, (bomb2_x, bomb2_y))
            if bomb2_y > 800 - (gu - 1) * 50 * 0.7:
                bomb2_vis = False

        # 道具3，大型飞机毁坏后加血道具
        if bomb3_vis:
            screen.blit(bomb3, (bomb3_x, bomb3_y))
            if hx + 100 > bomb3_x and hx < bomb3_x + 38 and hy < bomb3_y + 38 and hy + 124 > bomb3_y:  # 拼撞检测
                bomb3_vis = False
                my_Q = 10
            if bomb3_vis > 800:
                bomb3_vis = False
            bomb3_y += 3

        ################################################################################################################################
        # 结束界面
        if my_Q <= 0:
            my_Q = -1
            fa = 3
        str1 = " Blood "
        t = font.render(str1, True, (255, 255, 255))
        screen.blit(t, (10, 2))
        pygame.draw.line(screen, (144, 144, 144), (10, 35), (150, 35), 12)
        if my_Q > 5:
            pygame.draw.line(screen, (84, 255, 159), (10, 35), (((150 - 10) / 10) * my_Q + 10, 35), 10)
        elif my_Q > 0:
            pygame.draw.line(screen, (255, 0, 0), (10, 35), (((150 - 10) / 10) * my_Q + 10, 35), 10)
        ################################################################################################################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    fa = 4
        screen.blit(hero, (hx - h_width / 2, hy - h_height / 2))  # 我方的战机的显示
        pygame.display.update()
