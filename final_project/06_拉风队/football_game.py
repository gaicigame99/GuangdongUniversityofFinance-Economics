import pygame
def begin():
    pygame.init()

    screen=pygame.display.set_mode((800,600))
    bg=pygame.image.load(r"images\football.png")
    bg=pygame.transform.scale(bg,(800,600))
    zqw=pygame.image.load(r"images\zqw.png")
    zqw=pygame.transform.scale(zqw,(400,200))
    zq=pygame.image.load(r"images\zq.png")
    tp=pygame.image.load(r"images\zk.png")
    ks=pygame.image.load(r"images\start.png")
    ks=pygame.transform.scale(ks,(1000,700))
    js=pygame.image.load(r"images\end.jpg")
    js=pygame.transform.scale(js,(800,600))
    button=pygame.image.load(r"images\play3.png")
    button2=pygame.image.load(r"images\an1.png")
    button2=pygame.transform.scale(button2,(80,80))
    # bg_rect=bg.get_rect()
    zq_rect=zq.get_rect()
    tp_rect=tp.get_rect()
    zqw_rect=zqw.get_rect()
    font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",36)
    score=0

    ks_x=0
    ks_y=0

    #摆放开始按钮
    bt_x=600
    bt_y=500
    bt2_x=700
    bt2_y=100

    button_rect=button.get_rect()

    bg_y=0
    zqw_y=0

    bx=50
    by=200

    tx=100
    ty=450
    speedy=-40
    if (score//50+1)==1:
        bx_speed = 1
        by_speed = 1

    if (score // 50 + 1) == 2:
        bx_speed = 1.5
        by_speed = 1.5
    elif (score // 50 + 1) == 3:
        bx_speed = 2
        by_speed = 2
    elif (score // 50 + 1) == 4:
        bx_speed = 2.5
        by_speed = 2.5
    else:
        bx_speed = 3
        by_speed = 3

    flag=0

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        mouse_x, mouse_y = pygame.mouse.get_pos()
        a,b,c = pygame.mouse.get_pressed()
        screen.blit(bg, (0,bg_y))
        screen.blit(ks, (ks_x, ks_y))
        screen.blit(button, (bt_x, bt_y))


        if mouse_x > bt_x and mouse_x < bt_x + button_rect.width and mouse_y > bt_y and mouse_y < bt_y + button_rect.height and a:
            flag=1
        if flag==1 and ks_y>-700:
            ks_y-=20
            bt_y-=20

        if ks_y<=-700:
            screen.blit(bg,(0,0))
            text_score = font.render("分数：" + str(score), True, (255, 255, 255))
            text_level=font.render("第"+str(score//50+1)+"关",True,(255,255,255))

            screen.blit(text_score, (30, 50))
            screen.blit(text_level,(30,100))
            screen.blit(zqw,(200,zqw_y))
            screen.blit(tp,(tx,ty))
            screen.blit(button2,(bt2_x,bt2_y))

            if bx < 0 or bx + zq_rect.width > 800:
                bx_speed = -bx_speed
            if by<0:
                by_speed=-by_speed
            if (bx+zq_rect.width>200 and bx<200 and by>zqw_rect.width) or (bx<200+zqw_rect.width and bx+zq_rect.width>200+zqw_rect.width and by>zqw_rect.height):
                bx_speed=-bx_speed

            bx+=bx_speed
            by+=by_speed
            screen.blit(zq,(bx,by))
            if bx > 200 and bx < 200+ zqw_rect.width and by < zqw_rect.height-60 :   #判断小球是否进入足球网内，若进去则加分
               if by_speed<0:
                    by_speed=-by_speed
                    score+=5
            if by+zq_rect.height>600:
                score-=5
                by_speed = -by_speed
            pygame.key.get_pressed()
            pressed_keys=pygame.key.get_pressed()
            if pressed_keys[pygame.K_LEFT]:
                tx-=5
            if pressed_keys[pygame.K_RIGHT]:
                tx+=5
            if pressed_keys[pygame.K_UP]:
                ty-=5
            if pressed_keys[pygame.K_DOWN]:
                ty+=5
            if bx + zq_rect.width > tx and bx < tx + tp_rect.width and by + zq_rect.height > ty and by < ty:
                by_speed = -by_speed


        if mouse_x > bt2_x and mouse_x < bt2_x + button_rect.width and mouse_y > bt2_y and mouse_y < bt2_y + button_rect.height and a:
            flag=2
        if flag==2 and bg_y>-600:
            screen.blit(js,(0,0))
            bg_y-=20
            ty-=20
            bt_y-=20
            zqw_y-=20
        if bg_y<=-600:
            screen.blit(js, (0, 0))

        pygame.display.update()
