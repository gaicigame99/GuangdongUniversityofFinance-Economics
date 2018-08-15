def tanyitan():
    import pygame
    import random
    import math

    pygame.init()
    font = pygame.font.Font("C:\Windows\Fonts\simhei.ttf", 24)
    over_font = pygame.font.Font("C:\Windows\Fonts\JOKERMAN.TTF", 72)
    over_score_font = pygame.font.Font("C:\Windows\Fonts\STXINWEI.TTF", 36)

    screen = pygame.display.set_mode((480, 852))
    background = pygame.image.load("background1.png")
    start_background = pygame.image.load("start_background.png")
    title = pygame.image.load("title.png")

    ball = pygame.image.load("ball.png")
    ball_rect = ball.get_rect()
    ball_width = ball_rect.width
    ball_height = ball_rect.height
    ball_start_x = (480 - ball_width) / 2
    ball_start_y = 50
    ball_speed_x = 0
    ball_speed_y = 0
    ball_num = 1

    add_ball = pygame.image.load("add.png")
    add_ball_rect = add_ball.get_rect()
    add_ball_width = add_ball_rect.width
    add_ball_height = add_ball_rect.height

    score = 0

    class Ball():
        def __init__(self, ball_x, ball_y, speed_x, speed_y):
            self.ball = pygame.image.load("ball.png")

            self.x = ball_x
            self.y = ball_y
            self.speed_x = speed_x
            self.speed_y = speed_y

        def show_ball(self):
            screen.blit(self.ball, (self.x, self.y))

        def after_click(self, click_x, click_y):
            self.speed_x = click_x - self.x
            self.speed_y = click_y - self.y
            # if math.sqrt(self.speed_x ** 2 + self.speed_y ** 2) < 3:
            temp_y = 8 / math.sqrt(1 + (self.speed_x / self.speed_y) ** 2)
            temp_x = self.speed_x / self.speed_y * temp_y
            self.speed_x = temp_x
            self.speed_y = temp_y

        def gravity(self, t):
            if self.y < 852 - ball_height:
                self.speed_y = self.speed_y + 10 * t

        def move_ball(self):
            self.x += self.speed_x
            self.y += self.speed_y

        def bump_walls(self):
            if self.x < 0 or self.x > 480 - ball_width:
                self.speed_x = -self.speed_x
            if self.y < 0:
                self.speed_y = -self.speed_y
            if self.y > 852 - ball_height:
                self.speed_x = 0
                self.speed_y = 0
                self.x = ball_start_x
                self.y = ball_start_y

    class Line():
        def __init__(self, start_x, start_y):
            self.start_x = start_x
            self.start_y = start_y
            self.click_x, self.click_y = pygame.mouse.get_pos()

            # self.end_y = 5 / math.sqrt(1 + ((self.click_x - self.start_x) / (self.click_y - self.start_y)) ** 2)
            # self.end_x = -(self.click_x - self.start_x) / (self.click_y - self.start_y) * self.end_y

        def show_line(self):
            pygame.draw.line(screen, (255, 255, 255), (self.start_x, self.start_y), (self.click_x, self.click_y), 1)

    class Block():
        def __init__(self, block_x, block_y, color_num, blood):
            self.blocks = []
            self.blocks.append(pygame.image.load("block1.jpg"))
            self.blocks.append(pygame.image.load("block2.jpg"))
            self.blocks.append(pygame.image.load("block3.jpg"))
            self.blocks.append(pygame.image.load("block4.jpg"))
            # self.COLOR = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))
            # pygame.draw.rect(screen, self.COLOR, (random.randint(0, 480-50), 750, random.randint(0, 480-50) + 50, 800))

            self.x = block_x
            self.y = block_y
            self.num = color_num
            self.blood = blood

        def show_block(self):

            screen.blit(self.blocks[self.num], (self.x, self.y))

        def block_bumped(self, ball_list):
            for i in range(len(ball_list)):
                if ball_list[i].x < self.x < ball_list[i].x + ball_width \
                        and self.y < ball_list[i].y + ball_height / 2 <= self.y + 60:
                    ball_list[i].speed_x = -ball_list[i].speed_x
                    self.blood -= 1
                    my_score.add_score()

                if ball_list[i].x < self.x + 60 < ball_list[i].x + ball_width \
                        and self.y < ball_list[i].y + ball_height / 2 <= self.y + 60:
                    ball_list[i].speed_x = -ball_list[i].speed_x
                    self.blood -= 1
                    my_score.add_score()

                if ball_list[i].y < self.y < ball_list[i].y + ball_height \
                        and self.x < ball_list[i].x + ball_height / 2 <= self.x + 60:
                    ball_list[i].speed_y = -ball_list[i].speed_y
                    self.blood -= 1
                    my_score.add_score()
                    # t_re(i)

                if ball_list[i].y < self.y + 60 < ball_list[i].y + ball_height \
                        and self.x < ball_list[i].x + ball_height / 2 <= self.x + 60:
                    ball_list[i].speed_y = -ball_list[i].speed_y
                    self.blood -= 1
                    my_score.add_score()

        def show_blood(self):
            self.blood_str = font.render(str(self.blood), True, (0, 0, 0))
            screen.blit(self.blood_str, (self.x + 18, self.y + 18))

    class Add_ball():
        def __init__(self, add_ball_x, add_ball_y):
            self.add_ball = pygame.image.load("add.png")
            self.x = add_ball_x
            self.y = add_ball_y

        def show_add_ball(self):
            screen.blit(self.add_ball, (self.x, self.y))

        def add_ball_bumped(self, ball_list):
            for i in range(len(ball_list)):
                if ball_list[i].x < self.x < ball_list[i].x + ball_width \
                        and self.y < ball_list[i].y + ball_height / 2 < self.y + 60:
                    ball_list[i].speed_x = -ball_list[i].speed_x
                    ball_list.append(Ball(ball_list[i].x, ball_list[i].y, ball_list[i].speed_x, -ball_list[i].speed_y))
                    t.append(0.0001)
                    return 1

                if ball_list[i].x < self.x + 60 < ball_list[i].x + ball_width \
                        and self.y < ball_list[i].y + ball_height / 2 < self.y + 60:
                    ball_list[i].speed_x = -ball_list[i].speed_x
                    ball_list.append(Ball(ball_list[i].x, ball_list[i].y, ball_list[i].speed_x, -ball_list[i].speed_y))
                    t.append(0.0001)
                    return 1

                if ball_list[i].y < self.y < ball_list[i].y + ball_height \
                        and self.x < ball_list[i].x + ball_height / 2 < self.x + 60:
                    ball_list[i].speed_y = -ball_list[i].speed_y
                    ball_list.append(Ball(ball_list[i].x, ball_list[i].y, -ball_list[i].speed_x, ball_list[i].speed_y))
                    t.append(0.0001)
                    return 1

                if ball_list[i].y < self.y + 60 < ball_list[i].y + ball_height \
                        and self.x < ball_list[i].x + ball_height / 2 < self.x + 60:
                    ball_list[i].speed_y = -ball_list[i].speed_y
                    ball_list.append(Ball(ball_list[i].x, ball_list[i].y, -ball_list[i].speed_x, ball_list[i].speed_y))
                    t.append(0.0001)
                    return 1

    class Score():
        def __init__(self, score):
            self.score = score

        def show_score(self):
            self.score_display = font.render("分数：" + str(self.score), True, (255, 255, 255))
            screen.blit(self.score_display, (5, 5))

        def add_score(self):
            self.score += 1

    # class Start_interface():
    #     def __init__(self):

    # def add_ball(self):

    class Start():
        def __init__(self):
            self.button_nor = pygame.image.load("button_nor.png")
            self.button_press = pygame.image.load("button_press.png")

            self.button_rect = self.button_nor.get_rect()
            self.button_width = self.button_rect.width
            self.button_height = self.button_rect.height

        def show_button(self):
            left, right, wheel = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if left == 1 and (480 - self.button_width) / 2 < mouse_x < (480 - self.button_width) / 2 + self.button_width \
                    and 500 < mouse_y < 500 + self.button_height:
                screen.blit(self.button_press, ((480 - self.button_width) / 2, 500))
            else:
                screen.blit(self.button_nor, ((480 - self.button_width) / 2, 500))

    class End():
        def __init__(self, score):
            self.background = pygame.image.load("endbackground.png")

            self.score = score
            self.end_score = over_score_font.render("最终得分：" + str(self.score), True, (255, 255, 255))

            self.end_score_rect = self.end_score.get_rect()
            self.end_score_width = self.end_score_rect.width
            self.end_score_height = self.end_score_rect.height

        def show_end(self):
            screen.blit(self.background, (0, 0))
            while True:
                # screen.blit(self.game_over, ((480 - self.game_over_width) / 2, 200))
                screen.blit(self.end_score, ((480 - self.end_score_width) / 2, 400))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                pygame.display.update()

    block_list = []
    for i in range(random.randint(1, 3)):
        block = Block(random.randint(0, 480 - 60), random.randint(680, 720), random.randint(0, 3), random.randint(1, 3))
        block_list.append(block)

    add_ball_list = []
    add_ball_list.append(Add_ball(random.randint(0, 480 - add_ball_width), random.randint(680, 720)))

    # block_list.append(block)
    ball_list = []
    t = []
    ball_list.append(Ball(ball_start_x, ball_start_y, 0, 0))
    t.append(0)

    score = 0
    my_score = Score(score)
    my_score.show_score()

    # 初始界面
    def start():
        while True:
            whether_break = False
            screen.blit(background, (0, 0))
            my_score.show_score()

            for i in range(len(block_list)):
                block_list[i].show_block()
                block_list[i].show_blood()
                if block_list[i].y < 100:
                    end = End(my_score.score)
                    end.show_end()

            for i in range(len(ball_list)):
                ball_list[i].show_ball()

            for i in range(len(add_ball_list)):
                add_ball_list[i].show_add_ball()

            line = Line(ball_start_x + ball_width / 2, ball_start_y + ball_height / 2)
            line.show_line()

            ball_num_display = font.render(str(ball_num), True, (255, 255, 255))
            screen.blit(ball_num_display, (235, 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in range(len(ball_list)):
                        click_x, click_y = pygame.mouse.get_pos()
                        ball_list[i].after_click(click_x, click_y)
                        whether_break = True

            if whether_break == True:
                break
            pygame.display.update()

    # def t_re(i):
    #     global t
    #     t[i] = 0.0001

    start_or_not = False
    while True:

        screen.blit(start_background, (0, 0))

        start_meum = Start()
        start_meum.show_button()

        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP \
                    and (480 - start_meum.button_width) / 2 < mouse_x < (
                    480 - start_meum.button_width) / 2 + start_meum.button_width \
                    and 500 < mouse_y < 500 + start_meum.button_height:
                start_or_not = True
        if start_or_not == True:
            break
        screen.blit(title, (0, 200))

        # start_word = font.render("开 始 游 戏", True, (255, 255, 255))
        # start_word_rect = start_word.get_rect()
        # start_word_width = start_word_rect.width
        # screen.blit(start_word, ((480 - start_word_width)/2, 527))

        pygame.display.update()

    start()
    difficulty_a = 1
    difficulty_b = 3

    # 游戏界面
    cnt = 0
    while True:
        screen.blit(background, (0, 0))
        my_score.show_score()

        whether_show_start = True
        for i in range(len(ball_list)):
            ball_list[i].show_ball()
            ball_list[i].bump_walls()
            if ball_list[i].speed_y != 0:
                whether_show_start = False
            if ball_list[i].speed_y == 0:
                t[i] = 0

        if cnt // 20 < len(ball_list) - 1:
            cnt += 1

        for i in range(cnt // 20 + 1):
            ball_list[i].move_ball()
            ball_list[i].gravity(t[i])
            if ball_list[i].speed_y != 0:
                t[i] += 0.0001

        for i in range(len(block_list)):
            block_list[i].show_block()
            block_list[i].show_blood()

        for i in range(len(add_ball_list)):
            add_ball_list[i].show_add_ball()

        for i in range(len(block_list)):
            block_list[i].block_bumped(ball_list)
        for i in range(len(block_list)):
            if block_list[i].blood < 1:
                del block_list[i]
                break

        for i in range(len(add_ball_list)):
            if add_ball_list[i].add_ball_bumped(ball_list) == 1:
                ball_num += 1
                del add_ball_list[i]
                break

        ball_num_display = font.render(str(ball_num), True, (255, 255, 255))
        screen.blit(ball_num_display, (235, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        if whether_show_start == True:
            cnt = 0
            for i in range(len(block_list)):
                block_list[i].y -= 80

            for i in range(random.randint(1, 3)):
                block = Block(random.randint(0, 480 - 60), random.randint(680, 720), random.randint(0, 3),
                              random.randint(difficulty_a, difficulty_b))
                block_list.append(block)
                difficulty_a += 1
                difficulty_b += 3

            for i in range(len(add_ball_list)):
                add_ball_list[i].y -= 80
            for i in range(random.randint(0, 1)):
                add_ball_list.append(Add_ball(random.randint(0, 480 - add_ball_width), random.randint(680, 720)))
            start()
        pygame.display.update()
tanyitan()