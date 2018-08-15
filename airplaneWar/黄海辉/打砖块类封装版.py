import pygame


# 1，让小球在屏幕上移动
# 2，让小球撞墙之后反弹
# 3, 4个墙都可以正常反弹

# 4, 把砖块放到屏幕上
# 5，碰撞检测，当小球碰撞到砖块时，砖块消失 多砖块
# 6，摆放托盘
# 7，托盘可以用鼠标移动 或者键盘移动
# 8，托盘反弹

# 9，根据撞转，得分
# 10，指定自己独特的关卡


class Ball(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("ball16.png")
        self.x = _x
        self.y = _y
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.speed_x = 1
        self.speed_y = 1
        self.width = self.x + self.rect.width
        self.height = self.x + self.rect.height

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.width = self.x + self.rect.width
        self.height = self.x + self.rect.height
        if self.y < 0 or self.y + self.rect.height > 600:  # 顶部，底部
            self.speed_y = -self.speed_y
        if self.x > 800 - 16 or self.x < 0:
            self.speed_x = -self.speed_x
        self.x += self.speed_x
        self.y += self.speed_y

    def after_collision(self, x, y, block_rect1):
        # 小球反弹
        # 简化表达式
        block_w = x + block_rect1.width
        block_h = y + block_rect1.height
        # 当碰到左边或者右边的时候x方向取反
        # 小球的右边碰到砖，要保证小球不能在砖里  ,小球的左边碰到砖，要保证小球不能在砖里,
        if (self.width >= x and self.x < x) or (self.x <= block_w and self.width > block_w):
            self.speed_x = -self.speed_x
        elif self.y < block_h or self.height > y:
            self.speed_y = -self.speed_y


class Block(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("block1.png")
        self.image = pygame.transform.scale(self.image, (90, 30))
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = _x
        self.y = _y

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))


class Tray(object):
    def __init__(self, _screen, _x, _y):
        self.image = pygame.image.load("tray1.jpg")
        self.image = pygame.transform.scale(self.image, (180, 30))
        self.rect = self.image.get_rect()

        self.screen = _screen
        self.x = _x
        self.y = _y

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))


# 碰撞检测方法
def collision(bax, bay, ball_rt, blx, bly, block_rect):
    if bax + ball_rt.width > blx and \
            bax < blx + block_rect.width and \
            bay < bly + block_rect.height and \
            bay + ball_rt.height > bly:
        print("发生碰撞")
        return True
    else:
        return False


pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("timg.jpg")


trayA = Tray(screen, 100, 530)
# 小球坐标
ballA = Ball(screen, 105, 100)

# 默认速度
y_speed = 1
x_speed = 1

# 砖块列表
list_block = []
for i in range(3):
    for j in range(7):
        x = 50 + j * 100
        y = 50 + i * 40
        blockA = Block(screen, x, y)
        list_block.append(blockA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background, (0, 0))
    ballA.show()
    ballA.move()
    trayA.show()
    # 鼠标事件
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_y > 500:
        trayA.x = mouse_x - 90
    # 画砖块
    for i in range(len(list_block)):
        block_a = list_block[i]
        block_a.show()

    # 所有砖块的碰撞检测
    for i in range(len(list_block)):
        new_block = list_block[i]
        #  小球碰撞检测
        if collision(ballA.x, ballA.y, ballA.rect, new_block.x, new_block.y, new_block.rect):
            ballA.after_collision(new_block.x, new_block.y, new_block.rect)
            list_block[i].y = -100
    # 托盘碰撞检测
    if collision(ballA.x, ballA.y, ballA.rect, trayA.x, trayA.y, trayA.rect):
        if ballA.x + ballA.rect.width > trayA.x and ballA.x < trayA.x + trayA.rect.width:
            ballA.speed_y = -ballA.speed_y


    pygame.display.update()