import pygame
import random

pygame.init()
screen = pygame.display.set_mode((480,850))
font = pygame.font.Font("C:\Windows\Fonts\BAUHS93.TTF",50)

pygame.mixer.init()
background_music = pygame.mixer.Sound("sound/game_music.ogg")
bullet_music = pygame.mixer.Sound("sound/bullet.wav")
down_music = pygame.mixer.Sound("sound/enemy1_down.wav")
background_music.play()

background = pygame.image.load("images/background.png")
begin_p = pygame.image.load("images/button_nor.png")
plane_hero = pygame.image.load("images/hero.gif")
bullet1 = pygame.image.load("images/bullet-1.gif")
bullet2 = pygame.image.load("images/bullet-3.gif")
enemy1 = pygame.image.load("images/enemy-1.gif")
enemy2 = pygame.image.load("images/enemy1.png")
enemy3 = pygame.image.load("images/enemy-3.gif")
down1 = pygame.image.load("images/enemy0_down3.png")
down2 = pygame.image.load("images/enemy1_down3.png")
down3 = pygame.image.load("images/enemy2_down5.png")
bomb1 = pygame.image.load("images/bomb-1.gif")
life = pygame.image.load("images/icon72x72.png")


hx = 200
hy = 750
list_bullet = []
list_enemy = []
speed = 10
b_t = 10
time = b_t
enemy_num = 0
hero_blood = 5
score = 0
life_num = 3
up = 0
bomb_x = random.randint(0, 420)
bomb_y = random.randint(-4000, -3000)
play_game = 0

# 子弹类，包括坐标，类型，伤害
class bullet(object):
    def __init__(self,_x,_y,_name,_halfweight,_hit):
        self.x = _x
        self.y = _y
        self.name = _name
        self.halfweight = _halfweight
        self.hit = _hit

# 敌机类，包括坐标，类型，血量，大小，击落图片
class enemy(object):
    def __init__(self,_x,_y,_name,_blood,_weight,_height,_down):
        self.x = _x
        self.y = _y
        self.name = _name
        self.weight = _weight
        self.height = _height
        self.blood = _blood
        self.first = _blood
        self.down = _down

# 小型敌机
for i in range(10):
    enemya = enemy(random.randint(0,440), random.randint(-140,-40), enemy1, 1, 50, 40,down1)
    list_enemy.append(enemya)
    enemy_num += 1

# 中型敌机
for i in range(10):
    enemya = enemy(random.randint(0, 410), random.randint(-3500, -500), enemy2, 3, 70, 90, down2)
    list_enemy.append(enemya)
    enemy_num += 1

# 大型敌机
for i in range(3):
    enemya = enemy(random.randint(0, 230), random.randint(-10000, -2000), enemy3, 10, 170, 250, down3)
    list_enemy.append(enemya)
    enemy_num += 1

while 1:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 开始界面（尚未完成）
    if play_game == 0:
        screen.blit(begin_p, (170, 400))
        play_inf = font.render(u"PLAY", True, (255, 255, 255))
        screen.blit(play_inf, (180, 395))
        if event.type == pygame.MOUSEBUTTONDOWN:
            xp, yp = pygame.mouse.get_pos()
            if xp > 170 and xp < 170 + 132 and yp > 400 and yp < 400 + 48:
                play_game = 1

    if play_game == 3:
        dead_inf = font.render(u"Game Over!", True, (255, 255, 255))
        screen.blit(dead_inf, (130, 300))
        screen.blit(begin_p, (170, 400))
        play_inf = font.render(u"PLAY", True, (255, 255, 255))
        screen.blit(play_inf, (180, 395))
        if event.type == pygame.MOUSEBUTTONDOWN:
            xp, yp = pygame.mouse.get_pos()
            if xp > 170 and xp < 170 + 132 and yp > 400 and yp < 400 + 48:
                play_game = 1

    if play_game == 1:
        hx, hy =pygame.mouse.get_pos()
        screen.blit(plane_hero, (hx-50, hy-60))

        # 空投
        screen.blit(bomb1, (bomb_x, bomb_y))
        bomb_y += 3
        if bomb_y > 900:
            bomb_y = random.randint(-4000, -3000)
        # 空投碰撞检测
        if (bomb_x-5<=hx<=bomb_x+60 and bomb_y-5<=hy-60<=bomb_y+90) or \
                (bomb_x-5<=hx<=bomb_x+60 and bomb_y-5<=hy-60<=bomb_y+90):
                up = 1
                bomb_y = random.randint(-4000, -3000)


        if time:
            time -= 1
        else:
            if up == 1:
                list_bullet.append(bullet(hx, hy, bullet2,10, 5))
            else:
                list_bullet.append(bullet(hx,hy,bullet1,4,1))
            time = b_t

        # 发射子弹
        for i in range(len(list_bullet)):
            screen.blit(list_bullet[i].name, (list_bullet[i].x-list_bullet[i].halfweight, list_bullet[i].y-85))
            bullet_music.play()
            list_bullet[i].y-=speed



            for j in range(enemy_num):
                if (list_enemy[j].x <= hx - 50 <= list_enemy[j].x + list_enemy[j].weight and \
                    list_enemy[j].y <= hy - 60 <= list_enemy[j].y + list_enemy[j].height) or \
                        (list_enemy[j].x <= hx + 50 <= list_enemy[j].x + list_enemy[j].weight and \
                         list_enemy[j].y <= hy - 60 <= list_enemy[j].y + list_enemy[j].height):
                    life_num -= 1


                # 击中判定
                if list_enemy[j].x<=list_bullet[i].x-list_bullet[i].halfweight<=list_enemy[j].x+list_enemy[j].weight and \
                        0<list_enemy[j].y<=list_bullet[i].y-70<=list_enemy[j].y+list_enemy[j].height:
                    list_bullet[i].x = -10
                    list_bullet[i].y = -40
                    list_enemy[j].blood -= list_bullet[i].hit
                    # 敌机血量为0，重新分配位置及血量
                    if list_enemy[j].blood <= 0:
                        screen.blit(list_enemy[j].down, (list_enemy[j].x, list_enemy[j].y))
                        down_music.play()
                        list_enemy[j].x = random.randint(0, 480-list_enemy[j].weight)
                        list_enemy[j].y = random.randint(-list_enemy[j].height-500, -list_enemy[j].height)
                        list_enemy[j].blood = list_enemy[j].first
                        score += list_enemy[j].first*100

        # 清理飞出屏幕的子弹
        for i in range(len(list_bullet)):
            if list_bullet[i].y<-30:
                list_bullet.pop(i)
                break

        # 敌机向下移动
        for j in range(enemy_num):
            screen.blit(list_enemy[j].name, (list_enemy[j].x, list_enemy[j].y))
            list_enemy[j].y += 1
            # 敌机飞出屏幕后重新分配位置
            if list_enemy[j].y > 850:
                list_enemy[j].x = random.randint(0, 480 - list_enemy[j].weight)
                list_enemy[j].y = random.randint(-list_enemy[j].height-500, -list_enemy[j].height)

        # 飞机碰撞检测(尚未完成)
        for j in range(enemy_num):
            if (list_enemy[j].x <= hx - 50 <= list_enemy[j].x + list_enemy[j].weight and \
                list_enemy[j].y <= hy - 60 <= list_enemy[j].y + list_enemy[j].height) or \
                    (list_enemy[j].x <= hx + 50 <= list_enemy[j].x + list_enemy[j].weight and \
                     list_enemy[j].y <= hy - 60 <= list_enemy[j].y + list_enemy[j].height):
                life_num -= 1
                up = 0
                break
        # 飞机剩余血量显示
        if life_num > 0:
            screen.blit(life, (400, 770))
            if life_num > 1:
                screen.blit(life, (328, 770))
                if life_num == 3:
                    screen.blit(life, (256, 770))
        else:
            play_game = 3
            life_num = 3



        # 输出分数
        inf = font.render(u"Score:", True, (255, 255, 255))
        value = font.render(u"%d" % (score), True, (0, 255, 0))
        screen.blit(inf, (10, 755))
        screen.blit(value, (10, 800))

    pygame.display.update()
