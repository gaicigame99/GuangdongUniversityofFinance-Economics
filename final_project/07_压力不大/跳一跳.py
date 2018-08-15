import time
import pygame
import random
from pygame.locals import *

def tyt():
    pygame.mixer.init()
    game_music = pygame.mixer.Sound(r"dadisou\tyt.ogg")
    #板块精灵和针刺精灵（传入不同的图片即可，把大小改为相同）对象
    class PlateAndBarrier(pygame.sprite.Sprite):
        def __init__(self, str_images,y_speed,x,y):#传入图片和y轴移动速度  x和y坐标
            super(PlateAndBarrier, self).__init__()
            self.image = pygame.image.load(str_images).convert()
            self.image = pygame.transform.scale(self.image,(100,20))
            self.rect = self.image.get_rect(center=(x, y))  # 随机出现在获取rect()
            self.y_speed = y_speed

        # 板块和障碍物下落
        def update(self):
            self.rect.y += self.y_speed
            if self.rect.y > 800:  # #跑出屏幕回去
                self.rect.x = random.randint(0,500)
                self.rect.y = random.randint(-5,0)

    #小熊精灵
    class Bear(pygame.sprite.Sprite):
        def __init__(self, x,y):
            super(Bear, self).__init__()
            self.image = pygame.image.load("images\lili.png")
            self.image = pygame.transform.scale(self.image, (30, 60))
            self.rect = self.image.get_rect(center=(x, y))  # 获取rect()
            self.y_speed = 2
            self.x_speed = 0

    #礼物精灵
    class Gift(pygame.sprite.Sprite):
        def __init__(self,y_speed):
            super(Gift, self).__init__()
            self.image = pygame.image.load("images\liwu.png").convert()
            self.image = pygame.transform.scale(self.image,(40,40))
            self.rect = self.image.get_rect(center=(random.randint(0,500),random.randint(-5,0)))  # 获取rect()里面有x,y属性和width 和heigth
            self.y_speed = y_speed


        def update(self):
            self.rect.y += self.y_speed
            if self.rect.left < 0:#跑出屏幕回去
                self.rect.left = 0
            elif self.rect.right > 500:
                self.rect.right = 500
            elif self.rect.y > 800:
                self.rect.x = random.randint(0,500)
                self.rect.y = random.randint(-5,0)

    # 初始化 pygame
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((500, 800))
    pygame.display.set_caption("欢乐跳一跳")#游戏名称

    # bm = pygame.mixer.Sound("sound\game_music.ogg")#背景音乐
    # bm.play()

    #实例化小熊精灵
    bear = Bear(175,660)

    #先实例化几个板块
    plate1 = PlateAndBarrier(r"images\bankuai.jpg",1,175,700)
    plate2 = PlateAndBarrier(r"images\bankuai.jpg",1,50,500)
    plate3 = PlateAndBarrier(r"images\bankuai.jpg",1,400,200)

    plate_group = pygame.sprite.Group()
    plate_group.add(plate1)
    plate_group.add(plate2)
    plate_group.add(plate3)

    #实例化礼物精灵
    gift = Gift(1)

    #实例化障碍物
    barrier = PlateAndBarrier(r"images\zhenci.jpg",1,random.randint(0,500),random.randint(-5,0))
    barrier_group = pygame.sprite.Group()
    barrier_group.add(barrier)

    #初始化结束页面参数
    end_bg1 = pygame.image.load(r"kk\background.jpg")  # 背景图
    end_bg1 = pygame.transform.scale(end_bg1, (500, 800))
    image_restart1 = pygame.image.load(r"kk\restart.png")  # 再来一局
    restart1_rect = image_restart1.get_rect()
    image_return1 = pygame.image.load(r"kk\return.png")  # 返回主界面
    return1_rect = image_return1.get_rect()
    image_exit1 = pygame.image.load(r"kk\exit.png")  # 退出
    exit1_rect = image_exit1.get_rect()
    font = pygame.font.Font("C:\Windows\Fonts\STKAITI.TTF", 36)  # 字体样式
    font1 = pygame.font.Font("C:\Windows\Fonts\STKAITI.TTF", 80)  # “游戏失败”的字体（大一点）
    text_end = font1.render("游戏失败！", True, (85, 170, 255))
    role_y = 460 - 72
    speed = 6

    # 欢乐跳一跳暂停页面
    def pause(mark,role_y, speed):
        pause_cover = pygame.image.load(r"kk\背景.jpg")
        pause_cover = pygame.transform.scale(pause_cover, (500, 1600))
        screen.blit(pause_cover, (0, 0))
        stone = pygame.image.load(r"kk\砖块.jpg")
        stone = pygame.transform.scale(stone, (100, 20))
        screen.blit(stone, (200, 460))
        button_continue = pygame.image.load(r"kk\button_continue.png")
        screen.blit(button_continue, (390, 600))
        role = pygame.image.load("kk\hhhhh.png")
        screen.blit(role, (200 + 18, role_y))
        role_y -= speed
        if role_y >= 460 - 72 or role_y <= 250:
            speed = -speed

        font_0 = pygame.font.Font("C:\windows\Fonts\SimHei.ttf", 36)  # 文字
        f_0 = font_0.render("欢乐跳一跳，游戏暂停中...", True, (255, 153, 18))
        screen.blit(f_0, (30, 150))
        f_1 = font_0.render("返回游戏", True, (255, 153, 18))
        screen.blit(f_1, (350, 650))

        x, y = pygame.mouse.get_pos()  # 获取鼠标位置
        pressed_array = pygame.mouse.get_pressed()
        for index in range(len(pressed_array)):
            if pressed_array[index]:
                if index == 0:
                    if x >= 390 and x <= 390 + 32 and y >= 600 and y <= 600 + 32:  # 返回游戏
                        mark = 1
        return mark,role_y, speed
    #显示开始游戏封面
    def start_cover(screen):

        screen.blit()

    def isHit(bear,everyentity):
        if everyentity.rect.y+5 > bear.rect.bottom > everyentity.rect.y and everyentity.rect.left - bear.rect.width/2 < bear.rect.left < everyentity.rect.right- bear.rect.width/2:
            return True
        return False

    # 判断小熊是否撞击到板块或者障碍物的底部
    def isTLR(bear,everyentity):
        if everyentity.rect.bottom>= bear.rect.top >= everyentity.rect.bottom-5  and everyentity.rect.left - bear.rect.width < bear.rect.left < everyentity.rect.right:
            return True
        return False
    #判断小熊和礼物是否碰撞
    def isbl(bear,gift):
        if gift.rect.bottom >= bear.rect.top >= gift.rect.bottom - 5 and gift.rect.left - bear.rect.width < bear.rect.left < gift.rect.right:
            return True
        elif  gift.rect.y+5 >= bear.rect.bottom >= gift.rect.y and gift.rect.left - bear.rect.width < bear.rect.left < gift.rect.right:
                return True
        return False


    #游戏过程中screen,bear,plate_group,mouse_x,mouse_y,gb_y,pressed_keys,0
    def start_game(screen,bear,plate_group,gb_y,scorce,mark,gift,barrier,barrier_group):
        # 获取鼠标点击
        pressed_keys = pygame.mouse.get_pressed()
        # 获取鼠标焦点
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #显示背景
        gb_y = pain_game_back(gb_y)
        plate_group.update()#板块移动

        #显示板块精灵组
        for every_plate in plate_group:
            if every_plate.rect.left < 0:
                every_plate.rect.left = 0
            elif every_plate.rect.right > 500:
                every_plate.rect.right = 500
            screen.blit(every_plate.image,(every_plate.rect.x,every_plate.rect.y))

        #判断小熊是否与板块组碰撞并且在板块上面使其速度与板块一致
        for everyentity in plate_group:
            if isHit(bear,everyentity):
                bear.rect.bottom = everyentity.rect.y
                scorce += 1
                bear.y_speed = 1
                bear.x_speed = 0

        #判断小熊是否与板块底部碰撞
        for everyentity in plate_group:
            if isTLR(bear,everyentity):
                bear.rect.y = everyentity.rect.y + bear.rect.height
                bear.y_speed = 5
                bear.x_speed = 0

        # 判断小熊是否与礼物碰撞
        if isbl(bear,gift):
            scorce += 10
            gift.rect.x = random.randint(0, 500)
            gift.rect.y = random.randint(-500, -400)

        #判断小熊是否与障碍物顶部碰撞,跳出游戏
        for everyentity in barrier_group:
            if isHit(bear,everyentity):
                mark = 0
            elif isTLR(bear, everyentity):#底部碰撞
                bear.rect.y = everyentity.rect.y+bear.rect.height
                bear.y_speed = 5
                bear.x_speed = 0
            #判断礼物是否与障碍物碰撞
            if isHit(gift,everyentity) or isTLR(gift, everyentity):
                gift.rect.x = random.randint(0, 500)
                gift.rect.y = random.randint(-500, -400)
        #

        #点击鼠标 小熊向上跳
        if pressed_keys[0]:
            if mouse_x >= 390 and mouse_x <= 390 + 32 and mouse_y >= 700 and mouse_y <= 700 + 32:  # 暂停游戏
                mark = 2
            else:
                bear.y_speed = -5
                if bear.rect.x+bear.rect.width/2 > mouse_x:
                    bear.x_speed = -1
                elif bear.rect.x+bear.rect.width/2 <= mouse_x:
                    bear.x_speed = 1

        #如果小熊的顶部高于上次鼠标点击的位置，则让其下落
        if bear.rect.top < mouse_y:
            bear.y_speed = 5

        #防止小熊跳出左右边和上边屏幕
        if bear.rect.left < 0:
            bear.rect.left = 1
            bear.y_speed = 5
            bear.x_speed = 0
        elif bear.rect.right > 500:
            bear.rect.right = 500
            bear.y_speed = 5
            bear.x_speed = 0
        elif bear.rect.top < 0:
            bear.rect.top = 1
            bear.y_speed = 5
            bear.x_speed = 0
        elif bear.rect.top >800:#游戏结束
            mark = 0

        if barrier.rect.left < 0:  # 跑出屏幕回去
            barrier.rect.left = 0
        elif barrier.rect.right > 500:
            barrier.rect.right = 500
        elif barrier.rect.y > 800:
            barrier.rect.x = random.randint(0, 500)
            barrier.rect.y = random.randint(-5, 0)

        #显示暂停按钮
        button_stop = pygame.image.load(r"kk\button_stop.png")
        screen.blit(button_stop, (390, 700))
        #显示礼物
        screen.blit(gift.image,(gift.rect.x,gift.rect.y))
        gift.update()

        #显示障碍物
        screen.blit(barrier.image,(barrier.rect.x,barrier.rect.y))
        barrier.update()

        # 显示小熊
        screen.blit(bear.image,(bear.rect.x,bear.rect.y))
        bear.rect.y += bear.y_speed
        bear.rect.x += bear.x_speed
        return gb_y,mark,scorce

    #
    # 结束游戏封面
    # def over_game(bear,plate_group,mark,screen, scorce,list_scorce,end_bg1,image_restart1,restart1_rect,image_return1,return1_rect,image_exit1,exit1_rect,font,font1,text_end):
    #     # 欢乐跳一跳结束游戏封面
    #     #
    #     pressed_keys = pygame.mouse.get_pressed()
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #
    #     list_scorce.append(scorce)
    #
    #     text_score = font.render("本次得分：" + str(scorce), True, (85, 170, 255))
    #     # text_highest = font.render("历史最高分：" + str(max(list_scorce)), True, (85, 170, 255))
    #
    #     screen.blit(end_bg1, (0, 0))
    #     screen.blit(text_end, (80, 150))
    #     screen.blit(text_score, (140, 400))
    #     # screen.blit(text_highest, (140, 450))
    #     screen.blit(image_restart1, (180, 550))
    #     screen.blit(image_return1, (180, 600))
    #     screen.blit(image_exit1, (180, 650))
    #
    #     # 跳一跳按钮位置
    #     if pressed_keys[0] and 180 < mouse_x < 180 + restart1_rect.width and 550 < mouse_y < 550 + restart1_rect.height:
    #         mark = 1
    #         #初始化数据
    #         bear.rect.x = 175
    #         bear.rect.y = 660
    #         for palte in plate_group:
    #             palte.kill()
    #         plate1 = PlateAndBarrier(r"images\bankuai.jpg", 1, 175, 700)
    #         plate2 = PlateAndBarrier(r"images\bankuai.jpg", 1, 50, 500)
    #         plate3 = PlateAndBarrier(r"images\bankuai.jpg", 1, 400, 200)
    #         plate_group.add(plate1)
    #         plate_group.add(plate2)
    #         plate_group.add(plate3)
    #         game_music.stop()
    #
    #     if pressed_keys[0] and 180 < mouse_x < 180 + return1_rect.width and 600 < mouse_y < 600 + return1_rect.height:
    #         game_music.stop()
    #         import 封面
    #         封面.func()
    #     if pressed_keys[0] and 180 < mouse_x < 180 + exit1_rect.width and 650 < mouse_y < 650 + exit1_rect.height:
    #         exit()
    #     return list_scorce,bear,plate_group,mark
        # 结束游戏封面
    def over_game(scorce_mark, bear, plate_group, mark, screen, scorce, list_scorce, end_bg1, image_restart1,
                  restart1_rect, image_return1, return1_rect, image_exit1, exit1_rect, font, font1, text_end):
        # 欢乐跳一跳结束游戏封面
        #
        pressed_keys = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        list_scorce.append(scorce)

        text_score = font.render("本次得分：" + str(scorce), True, (85, 170, 255))
        # text_highest = font.render("历史最高分：" + str(max(list_scorce)), True, (85, 170, 255))

        screen.blit(end_bg1, (0, 0))
        screen.blit(text_end, (80, 150))
        screen.blit(text_score, (140, 400))
        # screen.blit(text_highest, (140, 450))
        screen.blit(image_restart1, (180, 550))
        screen.blit(image_return1, (180, 600))
        screen.blit(image_exit1, (180, 650))

        # 跳一跳按钮位置
        if pressed_keys[
            0] and 180 < mouse_x < 180 + restart1_rect.width and 550 < mouse_y < 550 + restart1_rect.height:
            mark = 1
            # 初始化数据
            bear.rect.x = 175
            bear.rect.y = 660
            for palte in plate_group:
                palte.kill()
            plate1 = PlateAndBarrier(r"images\bankuai.jpg", 1, 175, 700)
            plate2 = PlateAndBarrier(r"images\bankuai.jpg", 1, 50, 500)
            plate3 = PlateAndBarrier(r"images\bankuai.jpg", 1, 400, 200)
            plate_group.add(plate1)
            plate_group.add(plate2)
            plate_group.add(plate3)
            scorce_mark = 1
            game_music.stop()
            return scorce_mark, 0, list_scorce, bear, plate_group, mark
        if pressed_keys[0] and 180 < mouse_x < 180 + return1_rect.width and 600 < mouse_y < 600 + return1_rect.height:
            game_music.stop()
            import 封面
            封面.func()
        if pressed_keys[0] and 180 < mouse_x < 180 + exit1_rect.width and 650 < mouse_y < 650 + exit1_rect.height:
            exit()
        return scorce_mark, scorce, list_scorce, bear, plate_group, mark

    #背景移动
    game_back=pygame.image.load(r"images\bg.jpg")
    game_back=pygame.transform.scale(game_back,(500,1600))
    gb_y=-800#图片纵坐标
    def pain_game_back(gb_y):
        if gb_y==0:
            gb_y=-800
        screen.blit(game_back,(0,gb_y))
        gb_y+= 0.1
        return  gb_y

    list_scorce = []
    scorce = 0
    mark = 1
    scorce_mark = 0
    game_music.play()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
        #游戏中
        if mark == 1:
            # 调用游戏过程的方法
            gb_y,mark,scorce = start_game(screen,bear,plate_group,gb_y,scorce,mark,gift,barrier,barrier_group)
            game_music.play()
        #结束页面
        if mark == 0:
            if scorce_mark == 0:
                scorce_mark,scorce,list_scorce,bear,plate_group,mark = over_game(scorce_mark,bear,plate_group,mark,screen, scorce,list_scorce,end_bg1,image_restart1,restart1_rect,image_return1,return1_rect,image_exit1,exit1_rect,font,font1,text_end)
            elif scorce_mark == 1:
                scorce_mark,scorce,list_scorce,bear,plate_group,mark = over_game(scorce_mark,bear,plate_group,mark,screen, scorce,list_scorce,end_bg1,image_restart1,restart1_rect,image_return1,return1_rect,image_exit1,exit1_rect,font,font1,text_end)
            # list_scorce,bear,plate_group,mark = over_game(bear,plate_group,mark,screen, scorce-1,list_scorce,end_bg1,image_restart1,restart1_rect,image_return1,return1_rect,image_exit1,exit1_rect,font,font1,text_end)
        if mark == 2:
            mark,role_y, speed = pause(mark,role_y, speed)  # 欢乐跳一跳暂停页面
        pygame.display.flip()












