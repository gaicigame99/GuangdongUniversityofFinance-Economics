import pygame
import random
import time
def func():
    pygame.init()
    pygame.mixer.init()
    game_music=pygame.mixer.Sound(r"dadisou\game_back.ogg")
    what_play=1

    pygame.display.set_caption("打地鼠")
    screen0=pygame.image.load(r"dadisu\screen0.jpg")
    screen0=pygame.transform.scale(screen0,(1000,550))

    screen3=pygame.image.load(r"dadisu\screen3.png")
    screen3=pygame.transform.scale(screen3,(1000,550))
    gameover=pygame.image.load(r"dadisu\gameover.png")
    again=pygame.image.load(r"dadisu\again.png")
    again=pygame.transform.scale(again,(200,70))
    goto=pygame.image.load(r"dadisu\goto.png")
    goto=pygame.transform.scale(goto,(205,70))

    def pain_screen3():
        screen.blit(screen3, (0, 0))
        screen.blit(gameover, (200, 20))
        screen.blit(font.render("总得分:" + str(score) + "分", True, (0, 0, 0)), (400, 200))
        screen.blit(again, (400, 300))
        screen.blit(goto, (400, 400))
        screen.blit(font.render("退出", True, (0, 0, 0)), (460, 416))
    font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",36)
    screen=pygame.display.set_mode((1000,550))
    back=pygame.image.load(r"dadisu\back.png")
    back=pygame.transform.scale(back,(800,400))
    score_back=pygame.image.load(r"dadisu\score_back.png")
    score_back=pygame.transform.scale(score_back,(200,400))
    game_back=pygame.image.load(r"dadisu\game_back.png")
    game_back=pygame.transform.scale(game_back,(1000,150))

    bi_time=0
    score=0
    aim_score=30
    level=1
    what_screen=0
    def paint_score_back():
        screen.blit(font.render("时间:" + str(times) + "s", True, (0, 0, 0)), (800, 80))
        screen.blit(font.render("得分:" + str(score) + "分", True, (0, 0, 0)), (800, 120))
        screen.blit(font.render("目标得分:", True, (0, 0, 0)), (800, 160))
        screen.blit(font.render(str(aim_score) + "分", True, (0, 0, 0)), (860, 200))
        screen.blit(font.render("第"+str(level)+"关", True, (0, 0, 0)), (800, 240))
    def paint_game_back():
        screen.blit(font.render("游戏规则：", True, (0, 0, 0)), (0,400))
        screen.blit(font.render("在规定时间内达到目标分数，进入下一关，否则游戏结束", True, (0, 0, 0)), (20, 440))
        screen.blit(font.render("通过点击鼠标进行游戏 ", True, (0, 0, 0)), (20, 480))
    def know_level(times,score,aim_score,level,bi_time,what_screen,what_play):
        if times==0:
            if score>=aim_score:
                level+=1
                aim_score=aim_score*2
                bi_time = time.time()
                what_play=1
            else:
                what_screen=3
        return aim_score,level,bi_time,what_screen,what_play
    def pain():
        screen.blit(back, (0, 0))
        screen.blit(score_back, (800, 0))
        screen.blit(game_back, (0, 400))
        paint_game_back()
        paint_score_back()

    mouse=pygame.image.load(r"dadisu\mouse.png")
    mouse2=pygame.image.load(r"dadisu\mouse2.png")
    mouse=pygame.transform.scale(mouse,(100,100))
    mouse2=pygame.transform.scale(mouse2,(100,100))
    mouse_x=[140,325,525,110,325,525,100,330,550]
    mouse_y=[80,80,80,160,160,160,240,240,240]
    i=random.randint(0,8)
    j=random.randint(0,8)

    bun=pygame.image.load(r"dadisu\bun.png")
    def updata(what_screen,bi_time,score,level,aim_score):
        what_screen = 1
        bi_time = time.time()
        score = 0
        level = 1
        aim_score = 30
        return what_screen,bi_time,score,level,aim_score

    while True:
        if what_play==1:
            game_music.play()
            what_play=0
        if what_screen==0:
            screen.blit(screen0,(0,0))
        elif what_screen==1:
            en_time=time.time()
            times=int(20-(en_time-bi_time))
            pain()
            time.sleep(0.27)
            aim_score, level,bi_time,what_screen,what_play\
                =know_level(times,score,aim_score,level,bi_time,what_screen,what_play)
            screen.blit(mouse, (mouse_x[i], mouse_y[i]))
            screen.blit(mouse, (mouse_x[j], mouse_y[j]))
        else:
            pain_screen3()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if mouse_x[i]<=x<=mouse_x[i]+100 and mouse_y[i]<=y<=mouse_y[i]+100 and what_screen==1:
                    screen.blit(mouse2, (mouse_x[i], mouse_y[i]))
                    screen.blit(bun,(x-20,y-150))
                    i = random.randint(0, 8)
                    score+=1
                if mouse_x[j]<=x<=mouse_x[j]+100 and mouse_y[j]<=y<=mouse_y[j]+100 and what_screen==1:
                    screen.blit(mouse2, (mouse_x[j], mouse_y[j]))
                    screen.blit(bun,(x-20,y-150))
                    j = random.randint(0, 8)
                    score+=1
                if 310<=x<=700 and 410<=y<=510 and what_screen==0:
                    what_screen, bi_time, score, level, aim_score=updata(what_screen,bi_time,score,level,aim_score)
                if 400<=x<=600 and 300<=y<=370 and what_screen==3:
                    game_music.stop()
                    what_play=1
                    what_screen, bi_time, score, level, aim_score = updata(what_screen, bi_time, score, level, aim_score)
                if 400 <= x <= 605 and 400 <= y <= 470 and what_screen == 3:
                    game_music.stop()
                    what_screen =0
                    import 封面
                    封面.func()
        pygame.display.update()


