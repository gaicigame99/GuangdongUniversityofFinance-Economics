import pygame
import random
from Bullet import Bullet
from Enemy import Enemy
from Hero import Hero
# def impactJudge(s,o):
#     if s[0] + s[2] > o[0]  and \
#         s[0] + s[2] < o[0] + o[2] + s[2] and \
#         s[1] + s[3] > o[1] and \
#         s[1] + s[3] < o[1] + o[3] + s[3]:
#         return True
pygame.init()

screen = pygame.display.set_mode((500,800))
pygame.mixer.init()
pygame.mixer.music.load("sound\game_music.ogg")
pygame.mixer.music.play(1)
# hero = pygame.image.load("images\hero.gif")
bg = pygame.image.load(r"images\background.png")
# bullet = pygame.image.load(r"images\bullet1.png")
# enemy = pygame.image.load(r"images\enemy0.png")
# bullets = []
# enemys = []
count = 1000
bg = pygame.transform.scale(bg,(500,800))
hx = 100
hy = 100
Bgroup = pygame.sprite.Group()
Egroup = pygame.sprite.Group()
hero = Hero(hx,hy,10)
while True:
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # bullets.append(Bullet(hx - 2,hy - 64,(0,-5)))
            Bgroup.add(Bullet(hx - 2,hy - 64))
    hx,hy = pygame.mouse.get_pos()
    screen.blit(bg, (0, 0))

    for i in Bgroup:
        hitSpriteList = pygame.sprite.spritecollide(i, Egroup, False, pygame.sprite.collide_mask)
        if len(hitSpriteList) > 0:
            Bgroup.remove(i)
            try:
                for each in hitSpriteList:
                    each.crash()
            except ValueError:
                pass

    Bgroup.update(ticks)
    Bgroup.draw(screen)

    Egroup.update(ticks)
    Egroup.draw(screen)

    hero.update(hx,hy,ticks,screen)

    if count >= 1000:
        count = 0
        x = random.randint(0,450)
        y = -120
        e = Enemy(x,y,(0,1),5)
        Egroup.add(e)
    count += 15
    pygame.display.update()