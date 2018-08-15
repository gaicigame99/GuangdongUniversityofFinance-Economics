import time
import pygame
import random
from pygame.locals import *


# 我方飞机精灵
class MyPlane(pygame.sprite.Sprite):
    def __init__(self, str_images):
        super(MyPlane, self).__init__()
        self.image = pygame.image.load(str_images).convert()
        self.rect = self.image.get_rect(center=(random.randint(0, 495), random.randint(600, 800)))  # 获取rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


# 敌方飞机精灵
class EmPlane(pygame.sprite.Sprite):
    def __init__(self, str_images):
        super(EmPlane, self).__init__()
        self.image = pygame.image.load(str_images).convert()
        self.rect = self.image.get_rect(center=(random.randint(0, 495), random.randint(-5, 0)))  # 获取rect()

        self.x_speed = 0
        self.y_speed = 1

    # 飞机随机下落
    def update(self):
        self.rect.y += self.y_speed

        if self.rect.y > 800:  # 跑出屏幕杀掉
            self.kill()


class MyBullet(pygame.sprite.Sprite):
    def __init__(self, str_images, x, y):
        super(MyBullet, self).__init__()
        self.image = pygame.image.load(str_images).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(5, 8)

    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:  # 跑出屏幕杀掉
            self.kill()


class EmBullet(pygame.sprite.Sprite):
    def __init__(self, str_images, x, y):
        super(EmBullet, self).__init__()
        self.image = pygame.image.load(str_images).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(5, 8)

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 800:  # 跑出屏幕杀掉
            self.kill()


class BloodStrip():#传入颜色，长度画血条,掉血加血，只是把传入的blood_x做改变就行,如果blood_x==0的话屏幕调到游戏结束的画面
    def __init__(self,screen,g,r,b,blood_x):
        pygame.draw.line(screen,(g,r,b),(400,785),(400+blood_x,785),5)

class BloodPackage(pygame.sprite.Sprite):
    def __init__(self,str_images):
        # super(Plane, self).__init__()
        self.image = pygame.image.load(str_images).convert()
        self.rect = self.image.get_rect(center=(random.randint(0, 495), random.randint(-5, 0)))#获取rect()

    def update(self):
        self.rect.y += 10
        # if self.rect.y > 800:  # 跑出屏幕杀掉
        #     self.kill()


# 初始化 pygame
pygame.init()
pygame.mixer.init()
font = pygame.font.Font("C:\Windows\Fonts\STKAITI.TTF", 36)
screen = pygame.display.set_mode((495, 800))
pygame.display.set_caption("飞机大战")
bm = pygame.mixer.Sound("sound\game_music.ogg")
bm.play()

bg = pygame.image.load(r"images\background.png")
bg = pygame.transform.scale(bg, (495, 800))

#我机
myPlane = MyPlane("images\hero.gif")
all_myPlane = pygame.sprite.Group()
all_myPlane.add(myPlane)

#加入空投
blood_p = BloodPackage(r"images\bomb-2.gif")
all_bloodPackage = pygame.sprite.Group()
all_bloodPackage.add(all_bloodPackage)

# 我方子弹精灵组
all_myBullet = pygame.sprite.Group()

# 敌机精灵组
enemies = pygame.sprite.Group()

# 所有精灵组
all_sprites = pygame.sprite.Group()
# 敌机子弹精灵组
all_emBullet = pygame.sprite.Group()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)  # 敌机产生的速度

ADDBULLET = pygame.USEREVENT + 2
pygame.time.set_timer(ADDBULLET, 250)  # 我机子弹发射速度

# 爆炸特效的敌机
# emPlane_tx = EmPlane(r"images\enemy0_down1.png")
# start_time = 0
myBullet_stop = False  # 我机子弹与飞机同步
blood_x = 80
start_game = 0
scorce = 0
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
        elif event.type == QUIT:
            exit()
        elif event.type == ADDENEMY:  # 隔一定的时间加入敌机
            emPlane = EmPlane(r"images\enemy-1.gif")
            max_emPlane = EmPlane(r"images\enemy1.png")
            enemies.add(emPlane)
            all_sprites.add(emPlane)
            enemies.add(max_emPlane)
            all_sprites.add(max_emPlane)
            emBullet = EmBullet(r"images\bullet-1.gif", emPlane.rect.x, emPlane.rect.y)
            all_emBullet.add(emBullet)
            max_emBullet = EmBullet(r"images\bullet-2.gif", max_emPlane.rect.x, max_emPlane.rect.y)
            all_emBullet.add(max_emBullet)
        elif event.type == ADDBULLET:#隔一定的时间加入子弹
            if myBullet_stop == False:
                myBullet = MyBullet(r"images\bullet.png", myPlane.rect.x, myPlane.rect.y)
                all_myBullet.add(myBullet)
        elif event.type == pygame.MOUSEBUTTONDOWN:#鼠标事件控制页面跳转
            pressed_keys = pygame.mouse.get_pressed()
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if pressed_keys[0] and 250-64 < mouse_x <250-64+128 and 400-64 < mouse_y < 400-64+128:#开始游戏
                start_game = 1

    if start_game == 1:
        # 背景
        screen.blit(bg,(0, 0))

        # 设置飞机坐标为鼠标坐标
        myPlane.rect.x, myPlane.rect.y = pygame.mouse.get_pos()
        for enemie in enemies:  # 遍历所有敌机，如果和我方子弹碰撞，则消失
            enemie.update()
            screen.blit(enemie.image, (enemie.rect.x - enemie.rect.width / 2, enemie.rect.y - enemie.rect.height / 2))
            if pygame.sprite.spritecollideany(enemie, all_myBullet):
                scorce += 1
                enemie.kill()
                # start_time = time.time()
                # tx_x = enemie.rect.x
                # tx_y = enemie.rect.y
            # # if str((time.time()-start_time))[0:3] == "0.3":#显示敌机爆炸效果
            #     screen.blit(emPlane_tx.image,(tx_x - enemie.rect.width / 2, tx_y - enemie.rect.height / 2))
            # #     screen.blit(emPlane_tx.image,(-1, -500))
            # # if str((time.time()-start_time))[0:3] == "0.３":
            # #     enemie.kill()
        for em_b in all_emBullet:
            if pygame.sprite.spritecollideany(myPlane, all_emBullet):  # 我方战机被碰撞掉血，子弹消失
                blood_x -= 2

                em_b.kill()#子弹消失
                if blood_x == 0:#如果血量为0跳到游戏结束页面
                    myPlane.kill()
                    myBullet_stop = True
                    start_game = 2

        #显示空投
        for b_p in all_bloodPackage:
            b_p.update()
            screen.blit(b_p.image,(b_p.rect.x - b_p.rect.width / 2, b_p.rect.y - b_p.rect.height))

            if pygame.sprite.spritecollideany(b_p, all_myPlane) or b_p.rect.y > 800:#被我机吃掉
                b_p.kill()
                blood_p = BloodPackage(r"images\bomb-2.gif")#再次加入一个空投
                all_bloodPackage.add(blood_p)

        for my_plane in all_myPlane:  # 显示我机
            screen.blit(myPlane.image,(myPlane.rect.x - myPlane.rect.width / 2, myPlane.rect.y - myPlane.rect.height / 2))  # 显示我方飞机


        for everybullet in all_myBullet:  # 显示所有我机子弹
            everybullet.update()
            screen.blit(everybullet.image,(everybullet.rect.x - everybullet.rect.width / 2, everybullet.rect.y - everybullet.rect.height))

        for embullet in all_emBullet:  # 显示所有敌机子弹
            embullet.update()
            screen.blit(embullet.image, (embullet.rect.x - embullet.rect.width / 2, embullet.rect.y - embullet.rect.height))
        #显示血条
        font_tip = font.render("血量:" ,True ,(0, 0, 0))
        screen.blit(font_tip , (400,730))
        boold = BloodStrip(screen,0,0,0,80)#血槽
        boold = BloodStrip(screen,255,0,0,blood_x)#血条

        #显示得分
        show_scorce = font.render("得分:"+str(scorce) ,True ,(0, 0, 0))
        screen.blit(show_scorce, (0, 0))

    elif start_game == 0:#显示开始封面
        cover = pygame.image.load(r"images\cover.jpg")
        cover = pygame.transform.scale(cover,(495,800))
        screen.blit(cover,(0,0))
        start_button = pygame.image.load(r"images\start_button.jpg")
        start_button = pygame.transform.scale(start_button, (128, 128))
        screen.blit(start_button,(250-64,400-64))
    else:#显示结束封面
        over = pygame.image.load(r"images\gameover.png")
        over = pygame.transform.scale(over, (495, 800))
        screen.blit(over, (0, 0))
        sc = font.render(str(scorce), True, (0, 0, 0))
        screen.blit(sc, (245, 230))

        sc = font.render(str(scorce) ,True ,(0, 0, 0))
        screen.blit(sc , (245,530))
    pygame.display.flip()















