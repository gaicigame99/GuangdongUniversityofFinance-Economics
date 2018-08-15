import pygame
import random
import time



class small_enemy(object):
    def __init__(self, _screen, _x, _y):
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.speed = 2
        self.image = pygame.image.load(r"images\enemy0.png")
        self.rect = self.image.get_rect() #获取敌人图片大
        self.width = self.rect.width
        self.height = self.rect.height
        self.blood = 5    #敌机的血量
        self.bullet_image = pygame.image.load(r"images\bullet.png")
        self.bullet_rect = self.bullet_image.get_rect()  # 获取子弹图片大小

    def bomb(self, score):
        for bullet in bullets:
            if bullet.x + self.bullet_rect.width > self.x and bullet.x < self.x + self.width:
                if bullet.y + self.bullet_rect.height > self.y and bullet.y < self.y + self.height:
                    score += 1

                    enemy_down_wav = pygame.mixer.Sound(r"sound\enemy1_down.wav")
                    enemy_down_wav.play()
                    enemy_down_wav.set_volume(0.7)

                    enemy0_down1 = pygame.image.load("images\enemy0_down1.png")
                    enemy0_down2 = pygame.image.load("images\enemy0_down2.png")
                    enemy0_down3 = pygame.image.load("images\enemy0_down3.png")
                    enemy0_down4 = pygame.image.load("images\enemy0_down4.png")
                    self.screen.blit(enemy0_down1, (self.x, self.y))
                    self.screen.blit(enemy0_down2, (self.x, self.y))
                    self.screen.blit(enemy0_down3, (self.x, self.y))
                    self.screen.blit(enemy0_down4, (self.x, self.y))

                    bomb_wav = pygame.mixer.Sound(r"sound\get_bomb.wav")
                    bomb_wav.play()
                    bomb_wav.set_volume(0.7)
                    self.y = -900
                    self.x = -100
                    bullet.y = -100
                    self.blood -= 1
        return score

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    def show_blood(self):
         start_pos=(self.x,self.y + 38)
         end_pos=(self.x+self.blood*10,self.y + 38)
         pygame.draw.line(self.screen,(255,0,0),start_pos,end_pos,3)

"""
class middle_enemy(object):
    def __init__(self, _screen, _x, _y):
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.speed = 0.5
        self.image = pygame.image.load(r"images\enemy1.png")
        self.rect = self.image.get_rect() #获取敌人图片大
        self.width = self.rect.width
        self.height = self.rect.height
        self.blood = 20    #敌机的血量
        self.bullet_image = pygame.image.load(r"images\bullet.png")
        self.bullet_rect = self.bullet_image.get_rect()  # 获取子弹图片大小

    def bomb(self, score):
        for bullet in bullets:
            if bullet.x + self.bullet_rect.width > self.x and bullet.x < self.x + self.width:
                if bullet.y + self.bullet_rect.height > self.y and bullet.y < self.y + self.height:
                    score += 1
                    enemy1_down1 = pygame.image.load("images\enemy1_down1.png")
                    enemy1_down2 = pygame.image.load("images\enemy1_down2.png")
                    enemy1_down3 = pygame.image.load("images\enemy1_down3.png")
                    enemy1_down4 = pygame.image.load("images\enemy1_down4.png")
                    self.screen.blit(enemy1_down1, (self.x, self.y))
                    self.screen.blit(enemy1_down2, (self.x, self.y))
                    self.screen.blit(enemy1_down3, (self.x, self.y))
                    self.screen.blit(enemy1_down4, (self.x, self.y))
                    self.y = 900
                    bullet.y = -100
                    self.blood -= 2
        return score

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    def show_blood(self):
         start_pos=(self.x,self.y + 38)
         end_pos=(self.x+self.blood*20,self.y + 38)
         pygame.draw.line(self.screen,(255,0,0),start_pos,end_pos,3)


class big_enemy(object):
    def __init__(self, _screen, _x, _y):
        self.screen = _screen
        self.x = _x
        self.y = _y
        # self.life = [80, 20, 100]
        self.speed = 0.1
        self.image = pygame.image.load(r"images\enemy2.png")
        self.rect = self.image.get_rect() #获取敌人图片大
        self.width = self.rect.width
        self.height = self.rect.height
        self.blood = 200    #敌机的血量
        self.bullet_image = pygame.image.load(r"images\bullet.png")
        self.bullet_rect = self.bullet_image.get_rect()  # 获取子弹图片大小

    def bomb(self, score):
        for bullet in bullets:
            if bullet.x + self.bullet_rect.width > self.x and bullet.x < self.x + self.width:
                if bullet.y + self.bullet_rect.height > self.y and bullet.y < self.y + self.height:
                    score += 1
                    enemy2_down1 = pygame.image.load("images\enemy2_down1.png")
                    enemy2_down2 = pygame.image.load("images\enemy2_down2.png")
                    enemy2_down3 = pygame.image.load("images\enemy2_down3.png")
                    enemy2_down4 = pygame.image.load("images\enemy2_down4.png")
                    self.screen.blit(enemy2_down1, (self.x, self.y))
                    self.screen.blit(enemy2_down2, (self.x, self.y))
                    self.screen.blit(enemy2_down3, (self.x, self.y))
                    self.screen.blit(enemy2_down4, (self.x, self.y))
                    self.x = 1000
                    bullet.x = -10000
                    self.blood -= 10
        return score

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    def show_blood(self):
         start_pos=(self.x,self.y + 38)
         end_pos=(self.x+self.blood*30,self.y + 38)
         pygame.draw.line(self.screen,(255,0,0),start_pos,end_pos,3)
 """

class Bullet(object):
    def __init__(self,_screen, _x, _y):
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.image = pygame.image.load(r"images\bullet.png")
        self.rect = self.image.get_rect()  # 获取子弹图片大小
        self.width = self.rect.width
        self.height = self.rect.height
        self.speed = 30

    def show(self):
        self.screen.blit(self.image, (self.x + self.width+16, self.y-18))

class Plane(object):
    def __init__(self, _screen, _x, _y, _blood, _bul):
        self.screen = _screen
        self.hero = pygame.image.load("images\hero.gif")
        self.rect = self.hero.get_rect()  # 获取敌人图片大小
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = _x - self.width/2
        self.y = _y - self.height/2
        self.blood = _blood
        self.bul = _bul

    def show(self):
        self.screen.blit(self.hero, (self.x, self.y))

    def show_blood(self):
         start_pos=(self.x,self.y - 20)
         end_pos=(self.x+self.blood*10,self.y - 20)
         pygame.draw.line(self.screen,(255,0,0),start_pos,end_pos,3)

    def hit(self,score):
            for enemy in enemys:
                if enemy.y + enemy.height > self.y and self.y+self.height > enemy.y and \
                        enemy.x+enemy.width > self.x and enemy.x < self.x + self.width and \
                        enemy not in hit_1:
                    self.blood -= 1
                    hit_1.append(enemy)
            return score

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((495, 800))
background = pygame.image.load(r"images\background.png")
background = pygame.transform.scale(background, (495, 800))

bullets = []   #子弹
enemys = []    #敌机
hit_1 = []     #被子弹击中的敌机
# hit_2 = []
# hit_3 = []
score = 0




pygame.init()

# 游戏背景
screen = pygame.display.set_mode((495, 800))

font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 24)
font1 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)

m_x, m_y = pygame.mouse.get_pos()
plane=Plane(screen, m_x, m_y, 10, 0)

UI = 1     #界面1~4标志

grade = 0  #关卡

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if UI == 1:   #开始界面
        start_bg = pygame.image.load(r"images\start_bg.jpg") #开始背景
        start_bg = pygame.transform.scale(start_bg, (495, 900))
        game_name = pygame.image.load(r"images\name.png")

        screen.blit(start_bg, (0, 0))           #游戏名字
        game_name_x, game_name_y = 10, 90
        screen.blit(game_name, (game_name_x, game_name_y))

        start_letter = font.render("开始游戏", True, (0, 0, 0))      #游戏开始文字
        start_letter_x, start_letter_y = 110, 650
        screen.blit(start_letter, (start_letter_x, start_letter_y))

        start_button = pygame.image.load(r"images\button_p.png")    #游戏开始按钮
        start_button_rect = start_button.get_rect()  #获取按钮图片大小
        start_button_x, start_button_y = 90, 640
        screen.blit(start_button, (start_button_x, start_button_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #鼠标左键
                m_x, m_y = pygame.mouse.get_pos()  #鼠标位置
                if m_x > start_button_x and m_x < start_button_x + start_button_rect.width and \
                    m_y> start_button_y and m_y < start_button_y + start_button_rect.height:
                    button_wav = pygame.mixer.Sound(r"sound\button.wav")
                    button_wav.play()
                    UI = 2
        pygame.display.update()

    if UI == 2:   #加载界面
        t = time.time()
        loading_bg = pygame.image.load(r"images\background.png")     #加载背景
        loading_bg = pygame.transform.scale(loading_bg, (495, 800))
        screen.blit(loading_bg, (0, 0))

        loading_letter = font.render("等待或点鼠标左键开始游戏", True, (0, 0, 0))
        loading_letter_x, loading_letter_y = 130, 600
        screen.blit(loading_letter, (loading_letter_x, loading_letter_y))   #加载游戏提示文字

        loading_photo = pygame.image.load(r"images\game_loading3.png")  #加载图片
        loading_photo_x, loading_photo_y = 160, 400
        screen.blit(loading_photo, (loading_photo_x, loading_photo_y))
        if 0.07 < time.time() - t < 0.09:     #加载等待时间
             UI = 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #鼠标左键
                UI = 3
        pygame.display.update()

    if UI == 3:
        game_background = pygame.image.load(r"images\background.png")          #游戏背景
        game_background = pygame.transform.scale(game_background, (495, 800))
        screen.blit(game_background, (0, 0))

        m_x, m_y = pygame.mouse.get_pos()
        plane = Plane(screen, m_x, m_y, plane.blood, plane.bul)

        bullet_wav = pygame.mixer.Sound(r"sound\bullet.wav")
        bullet_wav.play()

        game_music = pygame.mixer.Sound(r"sound\game_music.ogg")
        game_music.play()
        game_music.set_volume(0.3)

        for bullet in bullets:     #显示子弹
            bullet.show()
            bullet.y -= bullet.speed
            if bullet.y < 0:
                bullets.pop(0)
        for enemy in enemys:       #显示敌机
            score = enemy.bomb(score)
            enemy.show()
            enemy.show_blood()
            enemy.y += enemy.speed

        if plane.blood > 0 and score >= 0:
            plane.show()
            score = plane.hit(score)
            plane.show_blood()
            if plane.bul == 0:
                bullets.append(Bullet(screen, plane.x, plane.y))
            else:
                bullets.append(Bullet(screen, plane.x+plane.bul, plane.y))
            enemys.append(small_enemy(screen, random.randint(0, 480-20), random.randint(-10000, -10)))

            grade = score // 100 + 1   #关卡显示
            score_show = font1.render("score: "+str(score), True, (0, 0, 0))
            screen.blit(score_show, (320, 10))

            grade_show = font.render("关卡： "+str(grade), True, (0, 0, 0))  #得分显示
            screen.blit(grade_show, (320, 50))

        if plane.blood < 0:
            plane.blood = 0
        if plane.blood == 0:

            game_music.stop()
            me_down_wav = pygame.mixer.Sound(r"sound\me_down.wav")
            me_down_wav.play()

            UI = 4
        pygame.display.update()

    if UI == 4:  #结束得分界面
        end_background = pygame.image.load(r"images\background.png")
        end_background = pygame.transform.scale(game_background, (495, 800))
        screen.blit(end_background, (0, 0))

        end_score = font1.render("最终得分 ", True, (0, 0, 0))
        end_score_x, end_score_y = 180, 250
        screen.blit(end_score, (end_score_x, end_score_y))   #游戏得分

        show_score = font1.render(str(score), True, (0, 0, 0))
        show_score_x, show_score_y = 205, 300
        screen.blit(show_score, (show_score_x, show_score_y))   #游戏得分

        restart = pygame.image.load(r"images\restart_nor.png")
        restart_x, restart_y = 200, 500
        screen.blit(restart, (restart_x, restart_y))

        restart_button = pygame.image.load(r"images\button_p.png")
        restart_button_rect = restart_button.get_rect()  #获取按钮图片大小
        restart_button_x, restart_button_y = 190, 490
        screen.blit(restart_button, (restart_button_x, restart_button_y))

        quit_game = pygame.image.load(r"images\quit_nor.png")
        quit_game_x, quit_game_y = 200, 600
        screen.blit(quit_game, (quit_game_x, quit_game_y))

        quit_button = pygame.image.load(r"images\button_p.png")
        quit_button_rect = quit_button.get_rect()
        quit_button_x, quit_button_y = 190, 590
        screen.blit(quit_button, (quit_button_x, quit_button_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  #鼠标左键
                m_x, m_y = pygame.mouse.get_pos()  #鼠标位置
                if m_x > restart_button_x and m_x < restart_button_x + restart_button_rect.width and \
                    m_y> restart_button_y and m_y < restart_button_y + restart_button_rect.height:
                    score = 0                      #重新开始游戏
                    UI = 3
                    m_x, m_y = pygame.mouse.get_pos()
                    plane = Plane(screen, m_x, m_y, 10, 0)
                    bullets = []
                    enemys = [] 
                    hit_1 = []  
                    hit_2 = []  
                    hit_3 = []

                if m_x > quit_button_x and m_x < quit_button_x + quit_button_rect.width and \
                    m_y> quit_button_y and m_y < quit_button_y + quit_button_rect.height:
                    exit()                                     #退出出游戏
        pygame.display.update()