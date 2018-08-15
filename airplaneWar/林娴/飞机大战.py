import pygame
import random

pygame.init()
# 设置BGM
# back_music = pygame.mixer.Sound("sound\\game_music.ogg")
# bullet_music = pygame.mixer.Sound("sound\\bullet.wav")
# back_music.play()
# bullet_music.play()

# 初始化所有变量
screen = pygame.display.set_mode((400,700))
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 28)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (46, 46, 46)
plane = pygame.image.load("images\life.png")
enemy = pygame.transform.scale(pygame.image.load("images\\enemy1.png"), (50, 50))
enemy_hit = pygame.transform.scale(pygame.image.load("images\\enemy1_hit.png"), (50, 50))
enemy_down1 = pygame.transform.scale(pygame.image.load("images\\enemy1_down1.png"), (50, 50))
enemy_down2 = pygame.transform.scale(pygame.image.load("images\\enemy1_down2.png"), (50, 50))
enemy_down3 = pygame.transform.scale(pygame.image.load("images\\enemy1_down3.png"), (50, 50))
h_enemy = pygame.image.load("images\\enemy1_hit.png")
d_enemy = pygame.image.load("images\\enemy1_down1.png")
background = pygame.image.load(r"images\background.png")
blood = pygame.transform.scale(pygame.image.load("images\\blood.png"),(50,10))
begin_photo = pygame.image.load("images\\begin.png")
begin_button = pygame.image.load("images\\begin_button.png")
stop = pygame.transform.scale(pygame.image.load(r"images\stop.png"), (20, 20))
return_button = pygame.transform.scale(pygame.image.load("images\\back.png"), (150, 30))
name = pygame.transform.scale(pygame.image.load("images\\name.png"), (150, 30))
loading = pygame.transform.scale(pygame.image.load("images\\loading.png"), (400, 400))
continue_button = pygame.transform.scale(pygame.image.load(r"images\return_button.png"), (108, 52))
quit = pygame.transform.scale(pygame.image.load("images\\quit_sel.png"), (100, 20))
gameover = pygame.transform.scale(pygame.image.load("images\\gameover.png"), (400, 700))
restart_button = pygame.image.load("images\\restart.png")


class bullet(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("images\\bullet.png")
        self.x = _x
        self.y = _y
        self.screen = _screen
        self.rect = self.image.get_rect()

    def show(self):
        self.screen.blit(self.image, (self.x - 10, self.y - 25))

    def move(self):
        if self.y > 0:
            self.y -= 1
        self.show()

    def explore(self, emx, emy, enemy_rect):
        if self.x + self.rect.width > self.x and \
                self.x < emx + enemy_rect.width and \
                self.y < emy + enemy_rect.height and \
                self.y + self.rect.height > self.y:
            return True
        else:
            return False

    def disappear(self):
        if self.y < 0:
            bullets.remove(self, bullet)
        self.x = -200
        self.y = -200


class enemy(object):

    def __init__(self, _screen):
        self.image = pygame.transform.scale(pygame.image.load("images\\enemy1.png"), (50,50))
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 100)
        self.screen = _screen
        self.rect = self.image.get_rect()

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 1
        if self.y > 700:
            self.y = random.randint(0, 50)
            self.x = random.randint(0, 300)
        self.show()

    def disappear(self):
        self.x = -50
        self.y = 0

    def s_ex(self, _emm):
        while True:
            _emm -= 1
            if 35 < _emm < 45:
                screen.blit(enemy_hit, (enemys[em].x, enemys[em].y))
            if 25 < _emm < 35:
                screen.blit(enemy_down1, (enemys[em].x, enemys[em].y))
            if 15 < _emm < 25:
                screen.blit(enemy_down2, (enemys[em].x, enemys[em].y))
            if 5 < _emm < 15:
                screen.blit(enemy_down3, (enemys[em].x, enemys[em].y))
            if _emm < 5:
                _emm = 45
                break


def show_first_view():
    screen.blit(begin_photo, (0, 0))
    screen.blit(begin_button, (300, 550))


def show_play_view():
    screen.blit(background, (0, 0))
    screen.blit(name, (20, 20))
    screen.blit(stop, (230, 650))
    screen.blit(quit, (280, 650))
    screen.blit(plane, (hx, hy))


def show_score():
    _score = font.render("score:" + str(score), True, BLACK_COLOR)
    screen.blit(_score, (30, 60))


def show_loading():
    screen.blit(loading, (0, 0))
    # screen.blit(return_button, (450, 500))
    screen.blit(continue_button, (150, 420))


def game_over():
    screen.blit(gameover, (0, 0))
    screen.blit(restart_button, (180, 630))
    _score = font.render(str(score), True, BLACK_COLOR)
    screen.blit(_score, (180, 480))
    scores.append(score)
    high_score = scores[0]
    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
    _high_score = font.render(str(high_score), True, BLACK_COLOR)
    screen.blit(_high_score, (180, 240))


hx, hy = 0, 0
bx, by = 350, 800
b_x = []   # 每颗子弹的位置
b_y = []

scores = []

bullets = []
enemys = []
ex_enemys = []
for i in range(10):
    enemys.append(enemy(screen))
for i in range(4):
    ex_enemys.append(enemy_hit)
    ex_enemys.append(enemy_down1)
    ex_enemys.append(enemy_down2)
    ex_enemys.append(enemy_down3)

my_time = 50
start = 0
emm = 50
score = 0

show_first_view()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # 点击开始界面开始按钮执行的操作
    if 300 < mouse_x < 300 + begin_button.get_rect().width and \
            550 < mouse_y < 550 + begin_button.get_rect().height:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = 1

    if start == 1:
        show_play_view()
        show_score()
        # 显示敌机
        for i in range(10):
            enemys[i].move()
            screen.blit(blood, (enemys[i].x, enemys[i].y + enemys[i].rect.height + 2))

        # 当鼠标位于游戏界面内时，飞机移动，发射子弹
        if pygame.mouse.get_focused():
            # 根据鼠标移动飞机
            hx = mouse_x - plane.get_rect().width / 2
            hy = mouse_y - plane.get_rect().height / 2

            # 根据my_time来调节子弹发射速度
            if my_time:
                my_time -= 1
            else:
                bullets.append(bullet(screen, mouse_x, hy))
                my_time = 50

            for i in bullets:
                i.move()
                # 让子弹移动
                for em in range(len(enemys)):
                    if i.explore(enemys[em].x, enemys[em].y, enemys[em].rect):
                        # 当子弹和敌机发生碰撞
                        score += 1
                        enemys[em].s_ex(emm)
                        enemys[em].disappear()

        # 点击暂停键执行的操作
        if 230 < mouse_x < 230 + stop.get_rect().width and \
                650 < mouse_y < 650 + stop.get_rect().height:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                start = 2
        if start == 2:
            # 展示的画面
            show_loading()

        # 点击退出游戏按钮执行的操作
        if 280 < mouse_x < 280 + quit.get_rect().width and \
                650 < mouse_y < 650 + quit.get_rect().height:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                start = 3
    # 点击重新开始按钮执行的操作
    if start == 3:
        game_over()
        if 180 < mouse_x < 180 + restart_button.get_rect().width and \
                630 < mouse_y < 630 + restart_button.get_rect().height:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                start = 5

    if start == 5:
        show_first_view()

    # 点击继续按钮时执行的操作
    if 150 < mouse_x < 150 + continue_button.get_rect().width and \
            420 < mouse_y < 420 + continue_button.get_rect().height:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = 1

    pygame.display.update()