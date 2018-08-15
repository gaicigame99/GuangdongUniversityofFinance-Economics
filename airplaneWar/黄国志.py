import pygame
import random
import time

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((480,750),0,32)
bg=pygame.image.load(r"images\background.png")
gameover=pygame.image.load(r"images\gameover.png")
font=pygame.font.Font("C:\Windows\Fonts\Calibriz.ttf",36)
stop=pygame.image.load(r"images\game_resume_nor.png")
begin=pygame.image.load(r"images\game_pause_pressed.png")
score_str="score: "
class Plane(object):
    def __init__(self,_x,_y,_blood,_bul,_screen):
        self.screen=_screen
        self.mid_x=_x
        self.mid_y=_y
        self.hero=pygame.image.load(r"images\hero1.png")
        self.rect=self.hero.get_rect()
        self.width=self.rect.width
        self.height=self.rect.height
        self.x=self.mid_x-self.width/2
        self.y=self.mid_y-self.height/2
        self.blood=_blood
        self.bul=_bul

    def show(self):
        self.screen.blit(self.hero,(self.x,self.y))

    def show_blood(self):
        green=(255,0,0)
        white=(255,255,255)
        start_pos=(0,50)
        end_pos=(self.blood*30,50)
        pygame.draw.rect(self.screen,white,((0,45),(153,12)),1)
        pygame.draw.line(self.screen,green,start_pos,end_pos,8)


    def show_score(self):
        score=font.render(score_str+str(score_num),True,(0,0,0))
        screen.blit(score,(0,0))

    def hit(self):
        for i in enemy:
            if i.y + i.height>= self.y and self.y+self.height>i.y and i not in hited1:
                if (i.x+i.width>=self.x and i.x<=self.x)\
                        or (i.x<=self.x+self.width and i.x+i.width>=self.x):
                    self.blood-=1
                    hited1.append(i)
        for i in supply:
            if i.y + i.height>= self.y and self.y+self.height>i.y and i not in hited3:
                if (i.x+i.width>=self.x and i.x<=self.x)\
                        or (i.x<=self.x+self.width and i.x+i.width>=self.x):
                    upgrade_wav.play()
                    self.bul=20
                    i.y=1000
                    hited3.append(i)

class Bullet(object):
    def __init__(self,_x,_y,_screen):
        self.x=_x
        self.y=_y
        self.screen=_screen
        self.b_image=pygame.image.load(r"images\bullet1.png")
        self.rect = self.b_image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.speed=10
    def show(self):
        self.screen.blit(self.b_image, (self.x - self.width / 2, self.y))

class Enemy(object):
    def __init__(self,_x,_y,_screen):
        self.screen=_screen
        self.x=_x
        self.y=_y
        self.hero=pygame.image.load(r"images\enemy1.png")
        self.rect=self.hero.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.speed=2

    def show(self):
        self.screen.blit(self.hero,(self.x,self.y))

    def hit(self,score_num):
        for i in bullet:
            if i.x>=self.x and i.x<=self.x+self.width:
                if i.y>self.y and i.y<self.y+self.height and self.y+self.height>0:
                    score_num+=1
                    enemy1down_wav.play()
                    down1 = pygame.image.load(r"images\enemy1_down1.png")
                    down2 = pygame.image.load(r"images\enemy1_down2.png")
                    down3 = pygame.image.load(r"images\enemy1_down3.png")
                    down4 = pygame.image.load(r"images\enemy1_down4.png")
                    self.screen.blit(down1, (self.x, self.y))
                    self.screen.blit(down2, (self.x, self.y))
                    self.screen.blit(down3, (self.x, self.y))
                    self.screen.blit(down4, (self.x, self.y))
                    self.y=1000
                    i.y=-100
        return score_num

class Boss_Enemy(object):
    def __init__(self,_x,_y,_screen):
        self.screen=_screen
        self.x=_x
        self.y=_y
        self.blood=100
        self.hero=pygame.image.load(r"images\enemy2_n2.png")
        self.rect=self.hero.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.speed=0.1

    def show(self):
        if self.blood>0:
            self.screen.blit(self.hero,(self.x,self.y))
        else:
            enemy3down_wav.play()
            down1 = pygame.image.load(r"images\enemy2_down1.png")
            down2 = pygame.image.load(r"images\enemy2_down2.png")
            down3 = pygame.image.load(r"images\enemy2_down3.png")
            down4 = pygame.image.load(r"images\enemy2_down4.png")
            down5 = pygame.image.load(r"images\enemy2_down5.png")
            self.screen.blit(down1, (self.x, self.y))
            self.screen.blit(down2, (self.x, self.y))
            self.screen.blit(down3, (self.x, self.y))
            self.screen.blit(down4, (self.x, self.y))
            self.screen.blit(down5, (self.x, self.y))
            self.y = 1000
            self.blood=-1

    def show_blood(self):
        black=(0,0,0)
        start_pos=(0,80)
        end_pos=(self.blood*1.5,80)
        pygame.draw.rect(self.screen, (255,255,255), ((0, 45), (153, 12)), 1)
        pygame.draw.line(self.screen,black,start_pos,end_pos,10)

    def hit(self):
        for i in bullet:
            if i.x>=self.x and i.x<=self.x+self.width \
                    and i not in hited2 and self.blood>=0:
                if i.y>self.y and i.y<self.y+self.height and self.y+self.height>0:
                    down1 = pygame.image.load(r"images\enemy2_down1.png")
                    down2 = pygame.image.load(r"images\enemy2_down2.png")
                    self.screen.blit(down1, (self.x, self.y))
                    self.screen.blit(down2, (self.x, self.y))
                    self.blood-=1
                    hited2.append(i)
                    i.y = -100
                    if len(hited2)>20:
                        hited2.pop(0)

class Supply(object):
    def __init__(self,_x,_y,_screen):
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.hero = pygame.image.load(r"images\prop_type_0.png")
        self.rect = self.hero.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.speed = 2

    def show(self):
        self.screen.blit(self.hero,(self.x,self.y))
score_num=0
m_x,m_y=pygame.mouse.get_pos()
plane=Plane(m_x,m_y,5,0,screen)


bullet=[]
enemy=[]
hited1=[]
hited2=[]
hited3=[]
supply=[]

time1=0
boss_time=200
supply_time=100
# r"sound\"
bullet_wav=pygame.mixer.Sound(r"sound\bullet.wav") #filename.wav文件名
supply_wav=pygame.mixer.Sound(r"sound\supply.wav")
me_down_wav=pygame.mixer.Sound(r"sound\me_down.wav")
upgrade_wav=pygame.mixer.Sound(r"sound\upgrade.wav")
enemy1down_wav=pygame.mixer.Sound(r"sound\enemy1_down.wav")
enemy3down_wav=pygame.mixer.Sound(r"sound\enemy3_down.wav")
button_wav=pygame.mixer.Sound(r"sound\button.wav")
enemy3_wav=pygame.mixer.Sound(r"sound\enemy3_flying.wav")
game_music_ogg=pygame.mixer.Sound(r"sound\game_music.ogg")
flag=-1
screen.blit(bg,(0,0))
screen.blit(stop, (220, 300))
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        flag = -flag
        button_wav.play()
        game_music_ogg.play(100)
        screen.blit(bg, (0, 0))
        screen.blit(begin, (220, 300))
while True:

    if flag==1:
        m_x,m_y=pygame.mouse.get_pos()
        plane=Plane(m_x,m_y,plane.blood,plane.bul,screen)

        if plane.blood>0:
            screen.blit(bg,(0,0))
            plane.show()
            plane.show_score()
            plane.hit()
            plane.show_blood()

            if time1%10==0 :
                if plane.bul==0:
                    bullet.append(Bullet(plane.mid_x,plane.y,screen))
                else:
                    bullet.append(Bullet(plane.mid_x+plane.bul, plane.y, screen))
                    bullet[len(bullet) - 1].b_image = pygame.image.load(r"images\bullet2.png")
                    bullet.append(Bullet(plane.mid_x-plane.bul, plane.y, screen))
                    bullet[len(bullet)-1].b_image=pygame.image.load(r"images\bullet2.png")
                bullet_wav.play()
            if time1%50==0:
               enemy.append(Enemy(random.randint(0,480-69),random.randint(-500,-100),screen))

            if time1==supply_time:
                supply.append(Supply(random.randint(50,400),random.randint(-400,-50),screen))
                supply_wav.play()

            if time1==boss_time:
                boss_enemy =Boss_Enemy(200, -200, screen)
            if time1>boss_time:
                if boss_enemy.blood>=0:
                    enemy3_wav.play()
                    boss_enemy.y += boss_enemy.speed
                    boss_enemy.show()
                    boss_enemy.hit()
                    boss_enemy.show_blood()
                if boss_enemy.y + boss_enemy.height >= plane.y and plane.y + plane.height > boss_enemy.y:
                    if (boss_enemy.x + boss_enemy.width >= plane.x and boss_enemy.x <= plane.x) \
                            or (boss_enemy.x <= plane.x + plane.width and
                                boss_enemy.x + boss_enemy.width >= plane.x):
                        plane.blood -= 5
                elif boss_enemy.y > 750 and boss_enemy.y<1000:
                    plane.blood -= 5

            for i in bullet:
                i.show()
                i.y-=i.speed
                if i.y<-100:
                    bullet.pop(0)

            for i in enemy:
                score_num=i.hit(score_num)
                i.show()
                i.y+=i.speed
                if i.y>1000:
                    max=0
                    index=0
                    th=0
                    for i in enemy:
                        if i.y>max:
                            max=i.y
                            index=th
                        th+=1
                    enemy.pop(index)

            for i in supply:
                if i.y<800:
                    i.show()
                    i.y+=i.speed
        else:
            me_down_wav.play()
            screen.blit(gameover,(0,0))
            font = pygame.font.Font("C:\Windows\Fonts\Calibriz.ttf", 48)
            final_score=font.render(str(score_num),True,(255,0,0))
            screen.blit(final_score,(230,600))
            flag=-flag
        time1+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = -flag
            button_wav.play()
            if flag==-1:
                game_music_ogg.stop()
            else:
                game_music_ogg.play()
            screen.blit(stop, (220, 300))
    pygame.display.update()
