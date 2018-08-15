import pygame
import random
import math
import time


class Sun(object):
    def __init__(self, _screen):
        self.image = pygame.image.load(r"images\sun0.png")
        self.screen = _screen
        self.num = 100
        self.rect = self.image.get_rect()
        self.add_time = time.time()
        self.show_time = time.time()
        self.location = []
        self.x = []
        self.y = []
        self.speed = 2
        self.past_time = []
        self.now_time = []
        self.flag_click = []
        self.flag_remove = []

    def init(self):
        get_time = time.time()
        if get_time - self.add_time < 5:
            pass
        else:
            self.x.append(random.randint(0, 850 - self.rect.width))
            self.y.append(-100)
            self.past_time.append(time.time())
            self.now_time.append(time.time())
            self.flag_click.append(0)
            self.flag_remove.append(0)
            self.add_time = time.time()
            self.location.append(random.randint(100, 500))

    def move(self, _index):
        if self.y[_index] > self.location[_index]:
            pass
        else:
            self.y[_index] += (self.speed - 1)

    def show(self, _index):
        get_time = time.time()
        time_span = get_time - self.show_time
        if time_span < 0.2:
            screen.blit(sun0_image, (self.x[_index], self.y[_index]))
        elif time_span < 0.4:
            screen.blit(sun1_image, (self.x[_index], self.y[_index]))
        elif time_span < 0.6:
            screen.blit(sun2_image, (self.x[_index], self.y[_index]))
        elif time_span < 0.8:
            screen.blit(sun3_image, (self.x[_index], self.y[_index]))
        elif time_span < 1.0:
            screen.blit(sun4_image, (self.x[_index], self.y[_index]))
        elif time_span < 1.2:
            screen.blit(sun5_image, (self.x[_index], self.y[_index]))
        else:
            self.show_time = time.time()

    def remove(self):
        for i in self.flag_remove:
            index = self.flag_remove.index(i)
            if i == 1:
                self.x.pop(index)
                self.y.pop(index)
                self.past_time.pop(index)
                self.now_time.pop(index)
                self.flag_click.pop(index)
                self.flag_remove.pop(index)
                self.location.pop(index)

    def collect(self, _index):
        angle = math.atan(self.y[_index] / self.x[_index])
        if collection_sun(self.x[_index], self.y[_index], self.rect, 0, 0, (50, 40)):
            self.num += 50
            self.flag_remove[_index] = 1
        else:
            self.x[_index] -= (self.speed + 2) * math.cos(angle)
            self.y[_index] -= (self.speed + 2) * math.sin(angle)
            self.show(_index)

    def disappear_judge(self, _index):
        self.now_time[_index] = time.time()
        time_span = self.now_time[_index] - self.past_time[_index]
        if time_span < 16:
            self.show(_index)
        else:
            self.flag_remove[_index] = 1

    def action(self):
        for i in range(len(self.x)):
            if self.flag_remove[i] == 0:
                self.now_time[i] = time.time()
                if self.flag_click[i] == 1:
                    self.collect(i)
                else:
                    self.move(i)
                    self.disappear_judge(i)


# 标记此处是否种植
class flag(object):
    def __init__(self):
        self.flag = []
        for i in range(45):
            self.flag.append(0)


# 植物类
class wandou(object):
    def __init__(self, _screen):
        self.x = -100   # 设置初始的xy坐标
        self.y = -100
        self.screen = _screen
        self.wandou = pygame.image.load("images/shot-0.png")    # 加载豌豆植物的动态图片
        self.image2 = pygame.image.load("images/plant_02.png")
        self.image4 = pygame.image.load("images/plant_04.png")
        self.image6 = pygame.image.load("images/plant_06.png")
        self.image8 = pygame.image.load("images/plant_08.png")
        self.image10 = pygame.image.load("images/plant_10.png")
        self.image12 = pygame.image.load("images/plant_12.png")
        self.image14 = pygame.image.load("images/plant_14.png")
        self.wandou_rect = self.wandou.get_rect()   # 得到植物的宽和高
        self.wandou_width = self.wandou_rect.width
        self.wandou_height = self.wandou_rect.height

    # 放置植物的方法
    def put(self, _l, w_x, w_y, flag):  # 传进的参数是是否点击了豌豆图标_l，放置植物的xy坐标以及该位置是否存在植物
        if _l:
            # 判断植物放置在哪一行，是在哪一列，将放置豌豆的坐标赋给self.x,self.y，并将flag从0变为1，表示在该地方已经有植物
            if 80 <= w_y <= 180:
                ww_y = 120
                if 50 <= w_x <= 140 and flag[0] == 0:
                    ww_x = 100
                    flag_.flag[0] = 1
                elif 140 < w_x <= 220 and flag[1] == 0:
                    ww_x = 170
                    flag_.flag[1] = 1
                elif 220 < w_x <= 300 and flag[2] == 0:
                    ww_x = 250
                    flag_.flag[2] = 1
                elif 300 < w_x <= 380 and flag[3] == 0:
                    ww_x = 340
                    flag[3] = 1
                elif 380 < w_x <= 460 and flag[4] == 0:
                    ww_x = 420
                    flag[4] = 1
                elif 460 < w_x <= 540 and flag[5] == 0:
                    ww_x = 500
                    flag[5] = 1
                elif 540 < w_x <= 620 and flag[6] == 0:
                    ww_x = 580
                    flag[6] = 1
                elif 620 < w_x <= 700 and flag[7] == 0:
                    ww_x = 660
                    flag[7] = 1
                elif 700 < w_x <= 780 and flag[8] == 0:
                    ww_x = 740
                    flag[8] = 1
                else:
                    ww_x = self.x
                    ww_y = self.y
            elif 180 < w_y <= 280:
                ww_y = 220
                if 50 <= w_x <= 140 and flag[9] == 0:
                    ww_x = 100
                    flag[9] = 1
                elif 140 < w_x <= 220 and flag[10] == 0:
                    ww_x = 170
                    flag[10] = 1
                elif 220 < w_x <= 300 and flag[11] == 0:
                    ww_x = 250
                    flag[11] = 1
                elif 300 < w_x <= 380 and flag[12] == 0:
                    ww_x = 340
                    flag[12] = 1
                elif 380 < w_x <= 460 and flag[13] == 0:
                    ww_x = 420
                    flag[13] = 1
                elif 460 < w_x <= 540 and flag[14] == 0:
                    ww_x = 500
                    flag[14] = 1
                elif 540 < w_x <= 620 and flag[15] == 0:
                    ww_x = 580
                    flag[15] = 1
                elif 620 < w_x <= 700 and flag[16] == 0:
                    ww_x = 660
                    flag[16] = 1
                elif 700 < w_x <= 780 and flag[17] == 0:
                    ww_x = 740
                    flag[17] = 1
                else:
                    ww_x = self.x
                    ww_y = self.y
            elif 280 < w_y <= 380:
                ww_y = 320
                if 50 <= w_x <= 140 and flag[18] == 0:
                    ww_x = 100
                    flag[18] = 1
                elif 140 < w_x <= 220 and flag[19] == 0:
                    ww_x = 170
                    flag[19] = 1
                elif 220 < w_x <= 300 and flag[20] == 0:
                    ww_x = 250
                    flag[20] = 1
                elif 300 < w_x <= 380 and flag[21] == 0:
                    ww_x = 340
                    flag[21] = 1
                elif 380 < w_x <= 460 and flag[22] == 0:
                    ww_x = 420
                    flag[22] = 1
                elif 460 < w_x <= 540 and flag[23] == 0:
                    ww_x = 500
                    flag[23] = 1
                elif 540 < w_x <= 620 and flag[24] == 0:
                    ww_x = 580
                    flag[24] = 1
                elif 620 < w_x <= 700 and flag[25] == 0:
                    ww_x = 660
                    flag[25] = 1
                elif 700 < w_x <= 780 and flag[26] == 0:
                    ww_x = 740
                    flag[26] = 1
                else:
                    ww_x = self.x
                    ww_y = self.y
            elif 380 < w_y <= 480:
                ww_y = 420
                if 50 <= w_x <= 140 and flag[27] == 0:
                    ww_x = 100
                    flag[27] = 1
                elif 140 < w_x <= 220 and flag[28] == 0:
                    ww_x = 170
                    flag[28] = 1
                elif 220 < w_x <= 300 and flag[29] == 0:
                    ww_x = 250
                    flag[29] = 1
                elif 300 < w_x <= 380 and flag[30] == 0:
                    ww_x = 340
                    flag[30] = 1
                elif 380 < w_x <= 460 and flag[31] == 0:
                    ww_x = 420
                    flag[31] = 1
                elif 460 < w_x <= 540 and flag[32] == 0:
                    ww_x = 500
                    flag[32] = 1
                elif 540 < w_x <= 620 and flag[33] == 0:
                    ww_x = 580
                    flag[33] = 1
                elif 620 < w_x <= 700 and flag[34] == 0:
                    ww_x = 660
                    flag[34] = 1
                elif 700 < w_x <= 780 and flag[35] == 0:
                    ww_x = 740
                    flag[35] = 1
                else:
                    ww_x = self.x
                    ww_y = self.y
            elif 480 < w_y <= 580:
                ww_y = 520
                if 50 <= w_x <= 140 and flag[36] == 0:
                    ww_x = 100
                    flag[36] = 1
                elif 140 < w_x <= 220 and flag[37] == 0:
                    ww_x = 170
                    flag[37] = 1
                elif 220 < w_x <= 300 and flag[38] == 0:
                    ww_x = 250
                    flag[38] = 1
                elif 300 < w_x <= 380 and flag[39] == 0:
                    ww_x = 340
                    flag[39] = 1
                elif 380 < w_x <= 460 and flag[40] == 0:
                    ww_x = 420
                    flag[40] = 1
                elif 460 < w_x <= 540 and flag[41] == 0:
                    ww_x = 500
                    flag[41] = 1
                elif 540 < w_x <= 620 and flag[42] == 0:
                    ww_x = 580
                    flag[42] = 1
                elif 620 < w_x <= 700 and flag[43] == 0:
                    ww_x = 660
                    flag[43] = 1
                elif 700 < w_x <= 780 and flag[44] == 0:
                    ww_x = 740
                    flag[44] = 1
                else:
                    ww_x = self.x
                    ww_y = self.y
            self.x = ww_x
            self.y = ww_y

    # 显示豌豆的方法
    def draw(self,tick):
        if tick in range(0,20):
            screen.blit(self.image2, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))
        elif tick in range(20,40):
            screen.blit(self.image4, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))
        elif tick in range(40,60):
            screen.blit(self.image6, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))
        elif tick in range(60,80):
            screen.blit(self.image8, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))
        elif tick in range(80,100):
            screen.blit(self.image10, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))
        elif tick in range(100,120):
            screen.blit(self.image12, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))
        elif tick in range(120,140):
            screen.blit(self.image14, (self.x- self.wandou_width//2,self.y- self.wandou_height//2))

    # 清除豌豆
    def del_wandou(self, w_x, w_y, flag):
        # 判断植物放置在哪一行，是在哪一列，将放置豌豆的坐标赋给self.x,self.y，并将flag从0变为1，表示在该地方已经有植物
        if 80 <= w_y <= 180:
            ww_y = 120
            if 50 <= w_x <= 140 and flag[0] == 1:
                ww_x = 100
                flag[0] = 0
            elif 140 < w_x <= 220 and flag[1] == 1:
                ww_x = 1700
                flag[1] = 0
            elif 220 < w_x <= 300 and flag[2] == 1:
                ww_x = 2500
                flag[2] = 0
            elif 300 < w_x <= 380 and flag[3] == 1:
                ww_x = 3400
                flag[3] = 0
            elif 380 < w_x <= 460 and flag[4] == 1:
                ww_x = 420
                flag[4] = 0
            elif 460 < w_x <= 540 and flag[5] == 1:
                ww_x = 500
                flag[5] = 0
            elif 540 < w_x <= 620 and flag[6] == 1:
                ww_x = 580
                flag[6] = 0
            elif 620 < w_x <= 700 and flag[7] == 1:
                ww_x = 660
                flag[7] = 0
            elif 700 < w_x <= 780 and flag[8] == 1:
                ww_x = 740
                flag[8] = 0
            else:
                ww_x = self.x
                ww_y = self.y
        elif 180 < w_y <= 280:
            ww_y = 220
            if 50 <= w_x <= 140 and flag[9] == 1:
                ww_x = 100
                flag[9] = 0
            elif 140 < w_x <= 220 and flag[10] == 1:
                ww_x = 170
                flag[10] = 0
            elif 220 < w_x <= 300 and flag[11] == 1:
                ww_x = 250
                flag[11] = 0
            elif 300 < w_x <= 380 and flag[12] == 1:
                ww_x = 340
                flag[12] = 0
            elif 380 < w_x <= 460 and flag[13] == 1:
                ww_x = 420
                flag[13] = 0
            elif 460 < w_x <= 540 and flag[14] == 1:
                ww_x = 500
                flag[14] = 0
            elif 540 < w_x <= 620 and flag[15] == 1:
                ww_x = 580
                flag[15] = 0
            elif 620 < w_x <= 700 and flag[16] == 1:
                ww_x = 660
                flag[16] = 0
            elif 700 < w_x <= 780 and flag[17] == 1:
                ww_x = 740
                flag[17] = 0
            else:
                ww_x = self.x
                ww_y = self.y
        elif 280 < w_y <= 380:
            ww_y = 320
            if 50 <= w_x <= 140 and flag[18] == 1:
                ww_x = 100
                flag[18] = 0
            elif 140 < w_x <= 220 and flag[19] == 1:
                ww_x = 170
                flag[19] = 0
            elif 220 < w_x <= 300 and flag[20] == 1:
                ww_x = 250
                flag[20] = 0
            elif 300 < w_x <= 380 and flag[21] == 1:
                ww_x = 340
                flag[21] = 0
            elif 380 < w_x <= 460 and flag[22] == 1:
                ww_x = 420
                flag[22] = 0
            elif 460 < w_x <= 540 and flag[23] == 1:
                ww_x = 500
                flag[23] = 0
            elif 540 < w_x <= 620 and flag[24] == 1:
                ww_x = 580
                flag[24] = 0
            elif 620 < w_x <= 700 and flag[25] == 1:
                ww_x = 660
                flag[25] = 0
            elif 700 < w_x <= 780 and flag[26] == 1:
                ww_x = 740
                flag[26] = 0
            else:
                ww_x = self.x
                ww_y = self.y
        elif 380 < w_y <= 480:
            ww_y = 420
            if 50 <= w_x <= 140 and flag[27] == 1:
                ww_x = 100
                flag[27] = 0
            elif 140 < w_x <= 220 and flag[28] == 1:
                ww_x = 170
                flag[28] = 0
            elif 220 < w_x <= 300 and flag[29] == 1:
                ww_x = 250
                flag[29] = 0
            elif 300 < w_x <= 380 and flag[30] == 1:
                ww_x = 340
                flag[30] = 0
            elif 380 < w_x <= 460 and flag[31] == 1:
                ww_x = 420
                flag[31] = 0
            elif 460 < w_x <= 540 and flag[32] == 1:
                ww_x = 500
                flag[32] = 0
            elif 540 < w_x <= 620 and flag[33] == 1:
                ww_x = 580
                flag[33] = 0
            elif 620 < w_x <= 700 and flag[34] == 1:
                ww_x = 660
                flag[34] = 0
            elif 700 < w_x <= 780 and flag[35] == 1:
                ww_x = 740
                flag[35] = 0
            else:
                ww_x = self.x
                ww_y = self.y
        elif 480 < w_y <= 580:
            ww_y = 520
            if 50 <= w_x <= 140 and flag[36] == 1:
                ww_x = 100
                flag[36] = 0
            elif 140 < w_x <= 220 and flag[37] == 1:
                ww_x = 170
                flag[37] = 0
            elif 220 < w_x <= 300 and flag[38] == 1:
                ww_x = 250
                flag[38] = 0
            elif 300 < w_x <= 380 and flag[39] == 1:
                ww_x = 340
                flag[39] = 0
            elif 380 < w_x <= 460 and flag[40] == 1:
                ww_x = 420
                flag[40] = 0
            elif 460 < w_x <= 540 and flag[41] == 1:
                ww_x = 500
                flag[41] = 0
            elif 540 < w_x <= 620 and flag[42] == 1:
                ww_x = 580
                flag[42] = 0
            elif 620 < w_x <= 700 and flag[43] == 1:
                ww_x = 660
                flag[43] = 0
            elif 700 < w_x <= 780 and flag[44] == 1:
                ww_x = 740
                flag[44] = 0
            else:
                ww_x = self.x
                ww_y = self.y
        self.x = ww_x
        self.y = ww_y


# 子弹类
class bullet (object):
    def __init__(self,_screen):
        self.btype={'1':"images/bullet.png",'2':"images/bullet1.png"}
        self.image=pygame.image.load(self.btype['1'])
        self.score = 0
        self.x=[]
        self.y=[]
        self.screen=_screen
        #子弹移动速度
        self.speed=3
        # 发射频率
        self.v=200
        self.time=20
        # 获得子弹图片的宽高
        self.rect=self.image.get_rect()
        self.width=self.rect.width
        self.height=self.rect.height

    # 子弹移动
    def move(self):
        for i in range(len(self.x)):
            self.screen.blit(self.image, (self.x[i], self.y[i]))
            self.x[i] += self.speed
        # 删除子弹优化
        for i in self.x:
            index = self.x.index(i)
            if i > 848:
                self.y.pop(index)
                self.x.pop(index)

    # 子弹位置确定
    def addbullet(self,wandou):
        if self.time:
            self.time -= 1
        else:
            # 添加子弹位置
            self.x.append(wandou.x +wandou.wandou_width/2)
            self.y.append(wandou.y -28)
            self.time = self.v

    # 子弹与僵尸碰撞
    def collection(self,corpse,score):
        for i in range(len(self.x)):
            for j in range(len(corpse.x)):
                if self.x[i] + self.width > corpse.x[j] and corpse.y[j] < self.y[i] < corpse.y[j] + corpse.height:
                    corpse.x[j] = random.randint(1000, 1200)
                    self.y[i] = 1000
                    self.x[i] = 1000
                    score[0] += 10
                if self.x[i] + self.width > 850:
                    self.x[i] = 1000

    # # 子弹与僵尸碰撞
    # def collection(self, corpse):
    #     for i in range(len(self.x)):
    #         for j in range(len(corpse.x)):
    #             if self.x[i] + self.width > corpse.x[j] and corpse.y[j] < self.y[i] < corpse.y[j] + corpse.height:
    #                 corpse.x[j] = random.randint(1000, 1200)
    #                 self.y[i] = 1000
    #                 self.x[i] = 1000
    #             if self.x[i] + self.width > 850:
    #                 self.x[i] = 1000


# 僵尸类
class Hero(object):
    def __init__(self):
        self.image1 = pygame.image.load("images\僵尸01.png")
        self.image2 = pygame.image.load("images\僵尸02.png")
        self.image3 = pygame.image.load("images\僵尸03.png")
        self.image4 = pygame.image.load("images\僵尸04.png")
        self.image5 = pygame.image.load("images\僵尸05.png")
        self.image6 = pygame.image.load("images\僵尸06.png")
        self.image7 = pygame.image.load("images\僵尸07.png")
        self.image8 = pygame.image.load("images\僵尸08.png")
        self.image9 = pygame.image.load("images\僵尸09.png")
        self.image10 = pygame.image.load("images\僵尸10.png")
        self.image11 = pygame.image.load("images\僵尸11.png")
        self.x = []
        self.y= []
        self.blood=[]
        self.z=[40,142,240,340,440]

        self.rect = self.image1.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        for i in range(50):
            self.x.append(random.randint(772,1100))
            self.y.append(self.z[random.randint(0,4)])
    def show(self,tick):
        for i in range(len(self.x)):
            if tick in range(0,20):
                screen.blit(self.image1, (self.x[i],self.y[i]))
            elif tick in range(20,40):
                screen.blit(self.image2, (self.x[i], self.y[i]))
            elif tick in range(40,60):
                screen.blit(self.image3, (self.x[i], self.y[i]))
            elif tick in range(60,80):
                screen.blit(self.image4, (self.x[i], self.y[i]))
            if tick in range(80,100):
                screen.blit(self.image5, (self.x[i],self.y[i]))
            elif tick in range(100,120):
                screen.blit(self.image6, (self.x[i], self.y[i]))
            elif tick in range(120,140):
                screen.blit(self.image7, (self.x[i], self.y[i]))
            elif tick in range(140,160):
                screen.blit(self.image8, (self.x[i], self.y[i]))
            elif tick in range(160,180):
                screen.blit(self.image9, (self.x[i], self.y[i]))


# 碰撞检测方法
def collection_sun(b_x, b_y, b_rect, e_x, e_y, e_rect):
    if b_x + b_rect.width > e_x and \
            b_x < e_x + e_rect[0] and \
            b_y < e_y + e_rect[1] and \
            b_y + b_rect.height > e_y:
        return True
    else:
        return False


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((850, 600))
move_list = {}
btn_speedy = 0

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 25)

#界面音乐

back_music = pygame.mixer.music.load(r"sound\bgm.mp3")

# 背景图片1
bg1 = pygame.image.load(r"images\bg.png")
bg1 = pygame.transform.scale(bg1, (850, 600))
bg1x = 0
bg1y = 0
move_list["背景位置"] = [bg1x, bg1y]

# 发光开始按钮
start_btn = pygame.image.load(r"images\btn3.png")
start_btn = pygame.transform.scale(start_btn, (250, 50))
sbtn_rect = start_btn.get_rect()
sbtn_x = 285
sbtn_y = 470
move_list["按钮0位置"] = [sbtn_x, sbtn_y]

# 灰色按钮
start_btn1 = pygame.image.load(r"images\btn2.png")
start_btn1 = pygame.transform.scale(start_btn1, (250, 50))
sbtn1_rect = start_btn1.get_rect()
sbtn1_x = 285
sbtn1_y = 470
move_list["按钮1位置"] = [sbtn1_x, sbtn1_y]

start_text = font.render("点击进入游戏", True, (0, 0, 0, 150))
text_x = 335
text_y = 480
move_list["文字位置"] = [text_x, text_y]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    butt = pygame.mouse.get_pressed()
    m_x, m_y = pygame.mouse.get_pos()

    screen.blit(bg1, (move_list["背景位置"][0], move_list["背景位置"][1]))

    # 鼠标移入按钮内发亮，点击后开始游戏
    if m_x > sbtn1_x and m_x < sbtn1_x + sbtn1_rect.width and m_y> sbtn1_y and m_y < sbtn1_y + sbtn1_rect.height :

        screen.blit(start_btn, (move_list["按钮0位置"][0], move_list["按钮0位置"][1]))
        if butt[0]:
            break
    else:
        screen.blit(start_btn1, (move_list["按钮1位置"][0], move_list["按钮1位置"][1]))

    screen.blit(start_text, (move_list["文字位置"][0], move_list["文字位置"][1]))

    pygame.display.update()

move_list1 = {}

mv_bg = pygame.image.load(r"images\bg1.png")
mv_bg = pygame.transform.scale(mv_bg, (850, 600))
bgx = 0
bgy = 0
move_list1["背景位置"] = [bgx, bgy]

# 摆放按钮
# 冒险模式
star1_btn = pygame.image.load("images\star1.png")
star1_btn = pygame.transform.scale(star1_btn, (267, 80))
star1_rect = star1_btn.get_rect()
# 点击变亮
star2_btn = pygame.image.load("images\star2.png")
star2_btn = pygame.transform.scale(star2_btn, (267, 80))
star2_rect = star2_btn.get_rect()
# 退出按钮
game_quit_btn = pygame.image.load("images\quit_sel.png")
game_quit_rect = game_quit_btn.get_rect()

# 迷你模式
star3_btn = pygame.image.load("images\star3.png")
star3_btn = pygame.transform.scale(star3_btn, (267, 80))
star3_rect = star3_btn.get_rect()
# 点击变亮
star4_btn = pygame.image.load("images\star4.png")
star4_btn = pygame.transform.scale(star4_btn, (267, 80))
star4_rect = star4_btn.get_rect()
# 生存模式
star5_btn = pygame.image.load("images\star5.png")
star5_btn = pygame.transform.scale(star5_btn, (267, 80))
star5_rect = star5_btn.get_rect()
# 点击变亮
star6_btn = pygame.image.load("images\star6.png")
star6_btn = pygame.transform.scale(star6_btn, (267, 80))
star6_rect = star6_btn.get_rect()

# 按钮1的位置
btx1 = 488
bty1 = 85
move_list1["按钮1位置"] = [btx1, bty1]

# 按钮2的位置
btx2 = 488
bty2 = 85
move_list1["按钮2位置"] = [btx2, bty2]

# 按钮3的位置
btx3 = 488
bty3 = bty1 + star1_rect.height
move_list["按钮3位置"] = [btx3, bty3]

# 按钮4的位置
btx4 = 488
bty4 = bty1 + star1_rect.height
move_list["按钮4位置"] = [btx4, bty4]

# 按钮5的位置
btx5 = 488
bty5 = bty3 + star3_rect.height
move_list["按钮5位置"] = [btx5, bty5]

# 按钮6的位置
btx6 = 488
bty6 = bty3 + star3_rect.height
move_list["按钮6位置"] = [btx6, bty6]

# 退出按钮的位置
btx7 = 700
bty7 = 520
move_list1["退出按钮位置"] = [btx7, bty7]
pygame.mixer.music.play()

# 奖杯按钮的位置
cup_x = 10
cup_y = 20
move_list["奖杯按钮位置"] = [cup_x, cup_y]

# 钱袋按钮的位置
money_x = cup_x + 150
money_y = 20
move_list["钱袋按钮位置"] = [money_x, money_y]

# 锁按钮的位置
lock_x = money_x + 150
lock_y = 20
move_list["锁按钮位置"] = [lock_x, lock_y]

# 奖杯，锁，商店
cup1 = pygame.image.load("images\奖杯.png")
cup2 = pygame.image.load("images\奖杯喜.png")
cup1_rect = cup1.get_rect()
money1 = pygame.image.load("images\钱袋.png")
money2 = pygame.image.load("images\钱袋嗨.png")
money1_rect = money1.get_rect()
lock1 = pygame.image.load("images\锁.png")
lock2 = pygame.image.load("images\锁扣打开.png")
lock1_rect = lock1.get_rect()

# 僵尸动图
dead1 = pygame.image.load("images\僵尸1.png")
dead2 = pygame.image.load("images\僵尸2.png")
dead3 = pygame.image.load("images\僵尸3.png")
dead4 = pygame.image.load("images\僵尸4.png")
dead5 = pygame.image.load("images\僵尸5.png")
dead_head = pygame.image.load("images\僵尸头.gif")

flag1 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(mv_bg, (move_list1["背景位置"][0], move_list1["背景位置"][1]))
    butt = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.blit(game_quit_btn, (move_list1["退出按钮位置"][0], move_list1["退出按钮位置"][1]))
    # 点击退出游戏
    if mouse_x > btx3 and mouse_x < btx3 + game_quit_rect.width and mouse_y > bty3 and mouse_y < bty3 + game_quit_rect.height and butt[0]:
        print("退出游戏")
        exit()

    # 点击按钮开始进入下一界面
    if mouse_x > btx1 and mouse_x < btx1+star1_rect.width and mouse_y> bty1 and mouse_y < bty1 + star1_rect.height:
        screen.blit(star2_btn, (move_list1["按钮2位置"][0], move_list1["按钮2位置"][1]))
        if butt[0]:
            start_time = time.time()
            flag1 = 1
    else:
        screen.blit(star1_btn, (move_list1["按钮1位置"][0], move_list1["按钮1位置"][1]))
    if flag1:
        end_time = time.time()
        if end_time - start_time < 0.2:
            screen.blit(dead1, (250, 400))
            #screen.blit(dead_head, (250, 500))
        elif 0.2 < end_time - start_time < 0.4:
            screen.blit(dead2, (250, 400))
            screen.blit(dead_head, (280, 420))
        elif 0.4 < end_time - start_time < 0.6:
            screen.blit(dead3, (250, 400))
            screen.blit(dead_head, (260, 440))
        elif 0.6 < end_time - start_time < 0.8:
            screen.blit(dead4, (250, 400))
            screen.blit(dead_head, (240, 460))
        elif 0.8 < end_time - start_time < 1.5:
            screen.blit(dead5, (250, 400))
            screen.blit(dead_head, (200, 500))
        else:
            break
    # 迷你模式
    if btx4 < mouse_x < btx4 + star4_rect.width and bty4 < mouse_y < bty4 + star4_rect.height:
        screen.blit(star4_btn, (move_list["按钮4位置"][0], move_list["按钮4位置"][1]))
    else:
        screen.blit(star3_btn, (move_list["按钮3位置"][0], move_list["按钮3位置"][1]))

    # 生存模式
    if btx6 < mouse_x < btx6 + star6_rect.width and bty6 < mouse_y < bty6 + star6_rect.height:
        screen.blit(star6_btn, (move_list["按钮6位置"][0], move_list["按钮6位置"][1]))
    else:
        screen.blit(star5_btn, (move_list["按钮5位置"][0], move_list["按钮5位置"][1]))

    # 奖杯按钮
    if cup_x < mouse_x < cup_x + cup1_rect.width and cup_y < mouse_y < cup_y + cup1_rect.height:
        screen.blit(cup2, (move_list["奖杯按钮位置"][0], move_list["奖杯按钮位置"][1]))
    else:
        screen.blit(cup1, (move_list["奖杯按钮位置"][0], move_list["奖杯按钮位置"][1]))

    # 钱袋按钮
    if money_x < mouse_x < money_x + money1_rect.width and money_y < mouse_y < money_y + money1_rect.height:
        screen.blit(money2, (move_list["钱袋按钮位置"][0], move_list["钱袋按钮位置"][1]))
    else:
        screen.blit(money1, (move_list["钱袋按钮位置"][0], move_list["钱袋按钮位置"][1]))

    # 锁按钮
    if lock_x < mouse_x < lock_x + lock1_rect.width and lock_y < mouse_y < lock_y + lock1_rect.height:
        screen.blit(lock2, (move_list["锁按钮位置"][0], move_list["锁按钮位置"][1]))
    else:
        screen.blit(lock1, (move_list["锁按钮位置"][0], move_list["锁按钮位置"][1]))

    pygame.display.update()

# 游戏变量初始化
background = pygame.image.load(r"images\background.jpg")
a1 = pygame.image.load("images\亮豌豆.png")
a2 = pygame.image.load("images\暗豌豆.png")
b = pygame.image.load("images\阳光.png")
c = pygame.image.load("images\横条.png")
d = pygame.image.load("images\图标框.png")
wandou_pircture = pygame.image.load("images/shot-0.png")
sun0_image = pygame.image.load("images\sun0.png")
sun1_image = pygame.image.load("images\sun1.png")
sun2_image = pygame.image.load("images\sun2.png")
sun3_image = pygame.image.load("images\sun3.png")
sun4_image = pygame.image.load("images\sun4.png")
sun5_image = pygame.image.load("images\sun5.png")
a1 = pygame.transform.scale(a1, (40, 55))
a2 = pygame.transform.scale(a2, (40, 55))
b = pygame.transform.scale(b, (35, 35))
d = pygame.transform.scale(d, (280, 70))
font_small = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
bx = 0
by = 0
flag_tuodong = 0
sun = Sun(screen)
tub_rest = wandou_pircture.get_rect()
flag_su = 0
flag_fa = 0
score_num = []
score_num.append(0)

# 子弹列表
bullet1=[]

# 豌豆列表
wandou1 = []
flag_ = flag()

hero=Hero()
tick = 0
ticks = 0
m_x = []
m_y = []
l_y = []
# 僵尸数量
for i in range(10):
    j = random.randint(0, 4)
    l_y.append(j)

while True:
    screen.blit(background, (bx, by))
    bx -= 2
    if bx <= -550:
        time.sleep(1)
        while True:
            screen.blit(background, (bx, by))
            bx += 2
            if bx >= -200:
                break
            pygame.display.update()
        break
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # 判断是否发生了鼠标拖动事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 获得鼠标点击三个按钮的点击情况(1,0,0)
            # 如果第一个参数为1,表示左键被按下
            # 如果第二个参数为1,表示滚轮被按下
            # 如果第三个参数为1,表示右键被按下
            buttons = pygame.mouse.get_pressed()
            # 我们只处理左键被按下的情况

            if buttons[0]:
                # 获得拖动鼠标的拖动位置
                mou_x, mou_y = pygame.mouse.get_pos()
                print(mou_x, mou_y)
                if 60<mou_x<60+tub_rest.width and 5<mou_y<5+tub_rest.height and sun.num >= 100:
                    flag_tuodong = 1

                for i in range(len(sun.x)):
                    if sun.x[i] < mou_x < sun.x[i] + sun.rect.width and sun.y[i] < mou_y < sun.y[i] + sun.rect.height:
                        sun.flag_click[i] = 1
    screen.blit(background, (bx, by))
    sun_num = font_small.render(f"{sun.num}", True, (0, 0, 0))
    te_score = font_small.render(f"score:{score_num[0]}", True, (0, 0, 0))
    screen.blit(d, (0, 0))
    if sun.num >= 100:
        screen.blit(a1, (60, 5))
    else:
        screen.blit(a2, (60, 5))
    screen.blit(b, (13, 5))
    screen.blit(c, (12, 40))
    screen.blit(sun_num, (15, 40))
    screen.blit(te_score, (700, 10))
    sun.init()
    sun.action()
    sun.remove()
    if flag_tuodong:
        w_x, w_y = pygame.mouse.get_pos()  # 得到鼠标的位置
        screen.blit(wandou_pircture, (w_x - tub_rest.width / 2, w_y - tub_rest.height/2))
        l, m, r = pygame.mouse.get_pressed()  # 得到鼠标的按键
        if r and 50 <= w_x <= 780 and 80 <= w_y <= 580 and w_x not in m_x:
            m_x.append(w_x)
            m_y.append(w_y)
            for i in range(45):
                if flag_.flag[i] == 0:
                    wandou1.append(wandou(screen))
                    bullet1.append(bullet(screen))
        if r:
            for i in range(len(m_x)):
                wandou1[i].put(1, m_x[i], m_y[i], flag_.flag)
                flag_tuodong = 0
            if flag_.flag[i] == 0:
                sun.num -= 100

    for i in range(len(m_x)):
        wandou1[i].draw(tick)
        bullet1[i].addbullet(wandou1[i])
        bullet1[i].move()
        bullet.collection(bullet1[i], hero, score_num)
        if score_num[0] > 300:
            flag_su = 1

    if ticks > 140:
        ticks = 0
    ticks += 1

    hero.show(ticks)
    for i in range(50):
        hero.x[i] -= 0.2
        if hero.x[i] < 0:
            flag_fa = 1

    if tick > 140:
        tick = 0
    tick += 1
    if flag_su or flag_fa:
        break
    pygame.display.update()

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 25)
bg = pygame.transform.scale(pygame.image.load(r"images\bg4.png"), (850, 600))

# 胜利
victory = pygame.transform.scale(pygame.image.load(r"images\cg1.png"), (425, 300))

# 失败
defeat = pygame.image.load(r"images\sb1.png")
defeat0 = pygame.transform.scale(pygame.image.load(r"images\sb2.png"), (425, 300))
ex_btn = pygame.transform.scale(pygame.image.load(r"images\quitg.png"), (200, 80))
de_rect = defeat.get_rect()
de0_rect = defeat0.get_rect()
btn_rect = ex_btn.get_rect()
btn_x = 300
btn_y = 400
print(de0_rect)
defeat1 = pygame.transform.scale(defeat,(398,339))
defeat2 = pygame.transform.scale(defeat,(298,239))
# 列表存储图片
list_def = []
list_def.append(defeat)
list_def.append(defeat1)
list_def.append(defeat2)
list_def.append(defeat0)

# 列表存储位置
list_dex = [176, 226, 276, 200]
list_dey = [81, 131, 181, 100]
# xy是测试僵尸的坐标，times存储判定胜负的时间播放结束动画
x = 850
y = 400
flag1 = 0
flag2 = 0
times = []

# 结束文本
victory_text = font.render("氪金使我变快乐！", True, (0, 0, 0, 150))
vtext_x = 325
vtext_y = 280

defeat_text = font.render("不充钱不配赢！", True, (0, 0, 0, 150))
dtext_x = 335
dtext_y = 280

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    a, b, c = pygame.mouse.get_pressed()
    m_x, m_y = pygame.mouse.get_pos()
    screen.blit(bg, (0, 0))

    if flag_fa == 1:
        start = time.time()
        times.append(start)
        end = time.time()
        for i in range(len(times)):
            if end - times[i] < 0.2:
                screen.blit(list_def[2], (list_dex[2], list_dey[2]))
            elif 0.2 < end - times[i] < 0.4:
                list_dey[2] = -800
                screen.blit(list_def[1], (list_dex[1], list_dey[1]))
            elif 0. < end - times[i] < 0.6:
                list_dey[1] = -800
                screen.blit(list_def[0], (list_dex[0], list_dey[0]))
            elif 1.2 < end - times[i]:
                list_dey[0] = -800
                screen.blit(list_def[3], (list_dex[3], list_dey[3]))
                screen.blit(defeat_text, (dtext_x, dtext_y))
                screen.blit(ex_btn, (btn_x, btn_y))
                # 点击后退出游戏
                if btn_x < m_x < btn_x + btn_rect.width and btn_y < m_y < btn_y + btn_rect.height and a:
                    btn_y = -800
                    list_dey[3] = -800
                    print("点我了")
                    exit()
    # 僵尸被打死，游戏胜利
    # if条件句需要修改
    elif flag_su == 1:
        screen.blit(victory, (list_dex[3], list_dey[3]))
        screen.blit(victory_text, (vtext_x, vtext_y))
        screen.blit(ex_btn, (btn_x, btn_y))

    if btn_x < m_x < btn_x + btn_rect.width and btn_y < m_y < btn_y + btn_rect.height and a:
        btn_y = -800
        list_dey[3] = -800
        print("点我了")
        exit()
    pygame.display.update()