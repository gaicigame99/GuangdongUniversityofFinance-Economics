import pygame
import random
import time

pygame.init()
# 屏幕
screen = pygame.display.set_mode((400,800))
screen_rect = screen.get_rect()
font = pygame.font.Font(r'C:\Windows\Fonts\Arial.ttf', 25)
WHILE_COLOR = (255, 255, 255)
s = 0
score = font.render(u'score:%d'%(s),True,(255, 255, 255))


# 玩家
hero = pygame.image.load('hero.gif')
hero = pygame.transform.scale(hero, (35, 50))
hx = 250
hy = 800
h_rect = hero.get_rect()
h_width = h_rect.width
h_height = h_rect.height

# 背景
background = pygame.image.load('background.png')

class bullrtl(pygame.sprite.Sprite):
    def __init__(self, bullet_surface, bullet_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_pos
        self.speed = 1

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()
# 子弹
bullrt1 = pygame.image.load('bullet1.png')
# b_rect = bullrt1.get_rect()
# b_width = bullrt1.width
# b_height = bullrt1.height
# 敌军1



enemy = pygame.image.load('enemy1.png')
e_rect = enemy.get_rect()
e_width = e_rect.width
e_height = e_rect.height
# 敌军2
enemy_2 = pygame.image.load('enemy2.png')
e_2_rect = enemy.get_rect()
e_2_width = e_rect.width
e_2_height = e_rect.height
# 敌军爆炸
enemy1 = pygame.image.load('enemy1_down1.png')
enemy2 = pygame.image.load('enemy1_down2.png')
enemy3 = pygame.image.load('enemy1_down3.png')
enemy4 = pygame.image.load('enemy1_down4.png')
# 爆炸图片显示间隔时间初始
boom_time = 1

# 背景音乐
b_music = pygame.mixer.Sound('sound\game_music.ogg')
b_music.play()
#爆炸音效
boom_music = pygame.mixer.Sound(r'sound\button.wav')

# 子弹速度
speed = 5
bx_x = []
bx_y = []
# 上弹速度
htime = 10
e_time = 15
e_x = []
e_y = []
# 敌军血量
blood = []

# 精灵
# class player(pygame.sprite.Sprite):
#     def __init__(self, initial_position):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface([10, 10])
#         self.image.fill((0, 0, 0))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = initial_position
#
# #         self.speed = 1
#
#     def update(self):
#         self.rect.left += self.speed
#         if self.rect.left > screen_rect.width:
#             self.kill()

group = pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    hx, hy = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    screen.blit(hero, (hx, hy))
    screen.blit(score, (50, 700))


    # 子弹频率
    if htime:
        htime -= 1
    else:
        bx_x.append(hx + 15)
        bx_y.append(hy)
        htime = 20
    # 子弹速度
    for i in range(len(bx_x)):
        screen.blit(bullrt1, (bx_x[i], bx_y[i]))
        bx_y[i] -= speed

    #敌人出现频率
    ex = random.randint(0, 350)
    ey = -30
    xue = 5
    if e_time:
        e_time -= 0.5
    else:
        e_x.append(ex)
        e_y.append(ey)
        blood.append(xue)
        e_time = 15
    # 敌人速度
    for i in range(len(e_x)):
        screen.blit(enemy, (e_x[i], e_y[i]))
        e_y[i] += 1
    # 清除屏幕外子弹、敌机
    for i in bx_x:
        index = bx_x.index(i)
        if i < 0:
            bx_x.pop(index)
            bx_y.pop(index)
    for i in e_x:
        index = e_x.index(i)
        if i > 800:
            e_x.pop(index)
            e_y.pop(index)

    # 击中判定
    for i in range(len(e_x)):
        for j in range(len(bx_x)):
            if e_x[i] < bx_x[j] < e_x[i] + e_width and e_y[i] < bx_y[j] < e_y[i] + e_height:
                # blood[i] -= 1
            # if blood[i] <= 0:
                #播放敌军爆炸图片
                s += 1
                if boom_time % 400 <= 100:
                    screen.blit(enemy1, (e_x[i], e_y[i]))
                elif 100 < boom_time % 400 <= 200:
                    screen.blit(enemy2, (e_x[i], e_y[i]))
                elif 200 < boom_time % 400 <= 300:
                    screen.blit(enemy3, (e_x[i], e_y[i]))
                else:
                    screen.blit(enemy4, (e_x[i], e_y[i]))
                boom_time += 0.01
                e_y[i] = 900
                e_x[i] = 900
                bx_x[j] = -900
                bx_y[j] = -900
                boom_music.play()


    # group.add(player((random.randint(0,screen_rect.width),random.randint(0, screen_rect.height))))

    # group.update()
    # group.draw(screen)
    pygame.display.update()
