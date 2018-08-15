import pygame
import random


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, bullet_init_pos, bullet_speed=8):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_init_pos
        self.speed = bullet_speed
        # init_pos

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top <= -16:
            self.kill()


# 定义玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 10
        self.bullets = pygame.sprite.Group()
        self.hit_group = pygame.sprite.Group()
        self.explode_index = 0
        self.players = pygame.sprite.Group()

    def move(self, offset, offset_letter):
        x = self.rect.left - (offset[pygame.K_LEFT] or offset_letter[ord('a')]) + \
            (offset[pygame.K_RIGHT] or offset_letter[ord('d')])
        y = self.rect.top + (offset[pygame.K_DOWN] or offset_letter[ord('s')]) - \
            (offset[pygame.K_UP] or offset_letter[ord('w')])
        # 边界判断
        if x >= SCREEN_WIDTH - 100:    # x
            x = SCREEN_WIDTH - 100
        elif x <= 0:
            x = 0
        if y >= SCREEN_HEIGHT - 124:    # y
            y = SCREEN_HEIGHT - 124
        elif y <= 0:
            y = 0
        self.rect.left = x
        self.rect.top = y

# 发射子弹方法，参数为子弹图片
    def shoot(self, bullet_img, bullet_width=9, bullet_height=21, plane_width=100):
        # 子弹初始位置在我方飞机的上方居中位置
        bullet = Bullet(bullet_img, [self.rect.left + plane_width/2 - bullet_width/2, self.rect.top - bullet_height/2])
        # 将子弹添加到子弹组中
        self.bullets.add(bullet)


# 敌军飞机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_init_pos):
        pygame.sprite.Sprite.__init__(self)
        # self.enemies = pygame.sprite.Group()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_init_pos
        self.speed = 2
        # 敌军飞机精灵对象
        self.enemy0 = pygame.sprite.Group()
        self.enemy1 = pygame.sprite.Group()
        self.enemy2 = pygame.sprite.Group()
        # 爆炸组
        self.enemy0_hit = pygame.sprite.Group()
        self.enemy1_hit = pygame.sprite.Group()
        self.enemy2_hit = pygame.sprite.Group()
        # 爆炸索引
        self.explode0_index = 0
        self.explode1_index = 0
        self.explode2_index = 0
        # 敌军飞机血量
        self.enemy2_blood = 5
        self.enemy1_blood = 3
        self.enemy0_blood = 1
    def update(self):
        self.rect.top += self.speed
        if self.rect.top >= 800:
            self.kill()


# 补给类
class Supply(pygame.sprite.Sprite):
    def __init__(self, supply_img, supply_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = supply_img
        self.rect = self.image.get_rect()
        self.rect.topleft = supply_init_pos
        self.supplies = pygame.sprite.Group()
        self.speed_x = 1
        self.speed_y = 1

    def update(self, supply_width=60):
        self.rect.top += self.speed_y
        self.rect.left += self.speed_x
        # kill
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        # 边界判断并改变速度
        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x = -self.speed_x
        if self.rect.left >= SCREEN_WIDTH - supply_width:
            self.rect.left = SCREEN_WIDTH - supply_width
            self.speed_x = -self.speed_x


# 根据传入的飞机surface对象，将飞机对象添加到对应的飞机精灵组
def sprite_add(sprite_img, init_pos):
    # [random.randint(0, 758), random.randint(0, 100)]
    enemy_sprite = Enemy(sprite_img, init_pos)
    if sprite_img == enemy0_img:
        enemy.enemy0.add(enemy_sprite)
    elif sprite_img == enemy1_img:
        enemy.enemy1.add(enemy_sprite)
    else:
        enemy.enemy2.add(enemy_sprite)


# 显示敌军飞机爆炸函数
def show_explode(explode_items, enemy_blow_list, enemy_explode_index, ticks):
    for enemy_explode in explode_items:
        # 小飞机爆炸
        if enemy_explode_index == 'explode0_index':
            screen.blit(enemy_blow_list[enemy_explode.explode0_index], enemy_explode.rect)
            if ticks % 10 == 0:
                if enemy_explode.explode0_index < 3:
                    enemy_explode.explode0_index += 1
                else:
                    enemy.enemy0_hit.remove(enemy_explode)
        # 中飞机爆炸
        if enemy_explode_index == 'explode1_index':
            screen.blit(enemy_blow_list[enemy_explode.explode1_index], enemy_explode.rect)
            if ticks % 10 == 0:
                if enemy_explode.explode1_index < 3:
                    enemy_explode.explode1_index += 1
                else:
                    enemy.enemy1_hit.remove(enemy_explode)
        # 打飞机爆炸
        if enemy_explode_index == 'explode2_index':
            screen.blit(enemy_blow_list[enemy_explode.explode2_index], enemy_explode.rect)
            if ticks % 10 == 0:
                if enemy_explode.explode2_index < 3:
                    enemy_explode.explode2_index += 1
                else:
                    enemy.enemy2_hit.remove(enemy_explode)


def add_supply():
    x = random.randint(0, 1)
    if x == 0:
        supply.supplies.add(Supply(pygame.image.load('images/prop_type_0.png'),
                                   [random.randint(0, SCREEN_WIDTH - 60), random.randint(-60, 0)]))    # 蓝色
        return 0
    else:
        supply.supplies.add(Supply(pygame.image.load('images/prop_type_1.png'),
                                   [random.randint(0, SCREEN_WIDTH - 60), random.randint(-60, 0)]))    # 红色
        return 1


def show_supply(score):
    # x = None
    # if score == 50:
    #     if len(supply.supplies) < 1:
    #         a = add_supply()
    #         return a

    if score % 50 == 0:
        if len(supply.supplies) < 1:
            a = add_supply()
            return a


# 游戏初始化
pygame.init()
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 852
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('飞机大战')
font = pygame.font.Font(None, 36)
# 加载游戏资源
plane_img = pygame.image.load('hero1.png')
# xk = pygame.image.load('xk.jpg')
bullet_img = pygame.image.load('bullet1.png')
bullet1_img = pygame.image.load('bullet2.png')
enemy_img = pygame.image.load('enemy0.png')
bg_img = pygame.image.load('background.png')

# 创建玩家飞机 敌军飞机
player = Player(plane_img, [SCREEN_WIDTH/2.5, SCREEN_HEIGHT])
enemy = Enemy(enemy_img, [random.randint(0, SCREEN_WIDTH), random.randint(0, 200)])
supply = Supply(pygame.image.load('prop_type_0.png'),
                [random.randint(0, SCREEN_WIDTH - 60), random.randint(0, 100)])
# 玩家飞机移动、速度对象
offset = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}
offset_letter = {ord('a'): 0, ord('s'): 0, ord('d'): 0, ord('w'): 0}

# 时间对象
clock = pygame.time.Clock()
ticks = 0  # 计数器
score = 0
game_over = 0
times = 0  # 计数器
is_supply = 0  # 补给
bullet_f = 10
current_type = 0
is_supply_num = 0
reality_type = 0
player_hit = pygame.sprite.Group()
player_hit.add(player)

# 敌军爆炸列表
enemy0_img = pygame.image.load('enemy0.png')
enemy0_blow_list = [
    pygame.image.load('enemy0_down1.png'),
    pygame.image.load('enemy0_down2.png'),
    pygame.image.load('enemy0_down3.png'),
    pygame.image.load('enemy0_down4.png')
]

enemy1_img = pygame.image.load('enemy1.png')
enemy1_blow_list = [
    pygame.image.load('enemy1_down1.png'),
    pygame.image.load('enemy1_down2.png'),
    pygame.image.load('enemy1_down3.png'),
    pygame.image.load('enemy1_down4.png')
]

enemy2_img = pygame.image.load('enemy2.png')
enemy2_blow_list = [
    pygame.image.load('enemy2_down1.png'),
    pygame.image.load('enemy2_down2.png'),
    pygame.image.load('enemy2_down3.png'),
    pygame.image.load('enemy2_down4.png'),
    pygame.image.load('enemy2_down5.png'),
    pygame.image.load('enemy2_down6.png')
]

# 玩家飞机爆炸列表
player_blow_list = [
    pygame.image.load('hero_blowup_n1.png'),
    pygame.image.load('hero_blowup_n2.png'),
    pygame.image.load('hero_blowup_n3.png'),
    pygame.image.load('hero_blowup_n4.png')
]
blood = 5
flags1 = 0
flags2 = 0
while 1:
    clock.tick(60)
    pygame.display.update()
    if not game_over:
        ticks += 1
        if ticks >= 60:
            ticks = 0
        # 按频率添加子弹对象到精灵组 并 更新精灵组
        if ticks % bullet_f == 0:
            if not is_supply:
                player.shoot(bullet1_img)    # 蓝色
            if is_supply and reality_type == 0:
                player.shoot(bullet1_img)    # 蓝色
            if is_supply and reality_type == 1:
                player.shoot(bullet_img)   # 红色

        player.bullets.update()
        # 按频率添加敌军飞机对象到精灵组 并 更新精灵组
        if ticks % 60 == 0:
            num = random.randint(0, 2)
            if num == 0:
                sprite_add(enemy0_img, [random.randint(0, SCREEN_WIDTH - 51), random.randint(-SCREEN_HEIGHT, 0)])
            elif num == 1:
                sprite_add(enemy1_img, [random.randint(0, SCREEN_WIDTH - 69), random.randint(-SCREEN_HEIGHT, 0)])
            else:
                sprite_add(enemy2_img, [random.randint(0, SCREEN_WIDTH - 165), random.randint(-SCREEN_HEIGHT, 0)])

        enemy.enemy0.update()
        enemy.enemy1.update()
        enemy.enemy2.update()
        # 绘制背景
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (0, SCREEN_HEIGHT), 1600)
        # screen.blit(bg_img, [0, 0])

        screen.blit(player.image, player.rect)
        player.bullets.draw(screen)

        enemy.enemy0.draw(screen)
        enemy.enemy1.draw(screen)
        enemy.enemy2.draw(screen)

        # 绘制敌军爆炸图
        show_explode(enemy.enemy0_hit, enemy0_blow_list, 'explode0_index', ticks)
        show_explode(enemy.enemy1_hit, enemy1_blow_list, 'explode1_index', ticks)
        show_explode(enemy.enemy2_hit, enemy2_blow_list, 'explode2_index', ticks)

        # 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                # 如果是上下左右箭头事件，则修改字典
                if event.key in offset or event.key in offset_letter:
                    offset[event.key] = 10
                    offset_letter[event.key] = 10
            elif event.type == pygame.KEYUP:
                if event.key in offset or event.key in offset_letter:
                    offset[event.key] = 0
                    offset_letter[event.key] = 0
        # 玩家飞机移动
        player.move(offset, offset_letter)
        # 判断子弹与敌军飞机 与 玩家飞机与敌法飞机是否发生碰撞
        enemy_down0 = pygame.sprite.groupcollide(enemy.enemy0, player.bullets, True, True)
        enemy_down1 = pygame.sprite.groupcollide(enemy.enemy1, player.bullets, flags1, True)
        enemy_down2 = pygame.sprite.groupcollide(enemy.enemy2, player.bullets, flags2, True)
        # 给飞机添加血量，大飞机 5血，中飞机 3血，小飞机一碰就炸
        if enemy_down0:
            enemy.enemy0_hit.add(enemy_down0)      # 爆炸小飞机
        if enemy.enemy2_blood == 0:
            enemy.enemy2_hit.add(enemy_down2)      # 爆炸中飞机
        if enemy.enemy1_blood == 0:
            enemy.enemy1_hit.add(enemy_down1)      # 爆炸大飞机

        # 判断血量
        if len(enemy_down2):
            enemy.enemy2_blood -= 1
            if enemy.enemy2_blood == 0:
                flags2 = 1
            if enemy.enemy2_blood < 0:
                enemy.enemy2_blood = 5
                flags2 = 0
        if len(enemy_down1):
            enemy.enemy1_blood -= 1
            if enemy.enemy1_blood == 0:
                flags1 = 1
            if enemy.enemy1_blood < 0:
                enemy.enemy1_blood = 3
                flags1 = 0

        # 玩家飞机与敌军飞机碰撞
        was_hit0 = pygame.sprite.groupcollide(player_hit, enemy.enemy0, True, True)
        player.hit_group.add(was_hit0)       # add
        was_hit1 = pygame.sprite.groupcollide(player_hit, enemy.enemy1, True, True)
        player.hit_group.add(was_hit1)       # add
        was_hit2 = pygame.sprite.groupcollide(player_hit, enemy.enemy2, True, True)
        player.hit_group.add(was_hit2)       # add

        # 在当前屏幕显示成绩
        if enemy_down0:
            score += 10
        if enemy_down1:
            score += 10
        if enemy_down2:
            score += 10

        # 补给出现
        if len(supply.supplies) < 1:
            type_num = show_supply(score)
            if type_num == 0 or type_num == 1:
                # 当前的补给子弹颜色 0、蓝色 1、红色
                current_type = type_num

        supply.supplies.draw(screen)
        supply.supplies.update()

        screen.blit(font.render('score:' + str(score), 1, (120, 120, 60)), [SCREEN_WIDTH - 150, 100])
        pygame.display.update()

        # 玩家吃到补给 改变子弹颜色与频率
        supply_hit = pygame.sprite.groupcollide(player_hit, supply.supplies, 1, 1)
        if len(supply_hit):
            score += 100
            player_hit.add(player)
            is_supply = 1
            is_supply_num += 1
            # 判断是否吃的同一类型的补给
            if reality_type == current_type:
                bullet_f -= 3
                if bullet_f < 1:
                    bullet_f = 1
            else:
                bullet_f = 15
            reality_type = current_type

        # 玩家飞机毁坏
        if player.hit_group:
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                # 绘制玩家飞机爆炸图
                for player_explode in player.hit_group:
                    screen.blit(bg_img, [0, 0])
                    screen.blit(player_blow_list[player_explode.explode_index], player_explode.rect)
                    if times % 20 == 0:
                        if player_explode.explode_index < 3:
                            player_explode.explode_index += 1
                        else:
                            player.hit_group.remove(player_explode)
                            screen.blit(bg_img, [0, 0])
                            screen.blit(font.render
                                        ('game over', 1, (120, 120, 60)), [SCREEN_WIDTH/2.5, SCREEN_HEIGHT/2 + 50])
                            screen.blit(font.render
                                        ('score:' + str(score), 1, (120, 120, 60)), [SCREEN_WIDTH/2.5, SCREEN_HEIGHT/2])
                pygame.display.update()
                times += 1
