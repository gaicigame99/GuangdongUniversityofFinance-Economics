import pygame
import math
import random
import time

def func():
    pygame.init()
    pygame.display.set_caption("泡泡龙")

    pygame.mixer.init()
    game_music = pygame.mixer.Sound(r"dadisou\ppl_music.ogg")
    what_play = 1

    def show_line(_screen):
        # 画分割线
        pygame.draw.line(_screen, (192, 192, 192), (617, 0), (617, 600), 4)
        for n in range(31):
            pygame.draw.line(_screen, (192, 192, 192), (0 + n * 20, 480), (10 + n * 20, 480), 2)


    class Ball(object):
        # 初始化一个空球，只给坐标
        def __init__(self, _screen, _x, _y):
            self.screen = _screen
            self.key = [r"ppl\None_ball.png", 0, 0]
            self.image = pygame.image.load(r"ppl\None_ball.png")
            self.rect = self.image.get_rect()
            self.radius = self.rect.width / 2
            self.color = 0
            self.x = _x
            self.y = _y
            self.speed_x = 0
            self.speed_y = 0
            # 初始状态，球不存在
            self.mark = 0
            # 初始状态， 遍历标记
            self.bl_mark = 0

        def make_ball(self, _key):
            self.key = _key
            self.image = pygame.image.load(self.key[0])
            self.color = self.key[1]
            self.mark = self.key[2]

        def show(self):
            self.screen.blit(self.image, (self.x, self.y))


    # 实现深度遍历的算法
    # 判断相同的颜色相连的有几颗，将bl_mark修改为mark的值，即1
    def bl_ball_color(_balls, n, m, color):
        a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
        # mark 是判断球是否存在
        if _balls[n][m].mark:
            # 球的颜色相同
            if _balls[n][m].color == color:
                # 球存在，若遍历标记为0，则将遍历标记修改为1，执行遍历
                if _balls[n][m].bl_mark == 0:
                    _balls[n][m].bl_mark = 1
                    # 判断球所在的层数，即n，为奇数或是偶数
                    if n % 2 == 0:
                        # 如果n不是第0层，的遍历
                        if 0 < n < 15:
                            # 只有从第2层开始才会遍历的
                            # 即上一层，n-1层
                            a = bl_ball_color(_balls, n-1, m, color)

                            if m - 1 >= 0:
                                b = bl_ball_color(_balls, n-1, m-1, color)

                        if 0 <= n <= 15:
                            if m - 1 >= 0:
                                c = bl_ball_color(_balls, n, m-1, color)
                                d = bl_ball_color(_balls, n+1, m-1, color)

                            # 一定会遍历的
                            e = bl_ball_color(_balls, n+1, m, color)

                            if m+1 < 20:
                                f = bl_ball_color(_balls, n, m+1, color)
                        return a + b + c + d + e + f + 1

                    else:
                        # 如果n不是第15层，即最后一层的遍历
                        if 0 < n < 15:
                            # 只有从第15层前开始才会遍历的
                            # 即下一层，n+1层
                            a = bl_ball_color(_balls, n+1, m, color)

                            if m+1 < 20:
                                b = bl_ball_color(_balls, n+1, m+1, color)

                        if 0 <= n <= 15:
                            if m+1 < 20:
                                c = bl_ball_color(_balls, n, m+1, color)
                                d = bl_ball_color(_balls, n-1, m+1, color)

                            # 一定会遍历的
                            e = bl_ball_color(_balls, n-1, m, color)

                            if m-1 >= 0:
                                f = bl_ball_color(_balls, n, m-1, color)

                        return a + b + c + d + e + f + 1

                # 有标志返回0
                return 0

            # 颜色不同返回0
            return 0
        # 球不存在返回0
        return 0


    # 实现深度遍历的算法
    # 删除颜色相同的球，且将bl_mark修改为0，用pd判断执行内容
    def bl_delete_ball(_balls, n, m, color, pd=1):
        # mark 是判断球是否存在
        if _balls[n][m].mark:
            # 球的颜色相同
            if _balls[n][m].color == color:
                # 球存在，若遍历标记为1，将标记改为0，执行遍历，将球消除，即覆盖为空球
                if _balls[n][m].bl_mark == 1:
                    if pd:
                        _balls[n][m] = Ball(_balls[n][m].screen, _balls[n][m].x, _balls[n][m].y)
                    else:
                        _balls[n][m].bl_mark = 0
                    # balls[n][m].bl_mark = 0
                    # 判断球所在的层数，即n，为奇数或是偶数
                    if n % 2 == 0:
                        # 如果n不是第0层，的遍历
                        if 0 < n < 15:
                            # 只有从第2层开始才会遍历的
                            # 即上一层，n-1层
                            bl_delete_ball(_balls, n-1, m, color, pd)

                            if m-1 >= 0:
                                bl_delete_ball(_balls, n-1, m-1, color, pd)

                        if 0 <= n <= 15:
                            if m-1 >= 0:
                                bl_delete_ball(_balls, n, m-1, color, pd)
                                bl_delete_ball(_balls, n+1, m-1, color, pd)

                            # 一定会遍历的
                            bl_delete_ball(_balls, n+1, m, color, pd)

                            if m+1 < 20:
                                bl_delete_ball(_balls, n, m+1, color, pd)

                    else:
                        # 如果n不是第15层，即最后一层的遍历
                        if 0 < n < 15:
                            # 只有从第15层前开始才会遍历的
                            # 即下一层，n+1层
                            bl_delete_ball(_balls, n+1, m, color, pd)

                            if m+1 < 20:
                                bl_delete_ball(_balls, n+1, m+1, color, pd)

                        if 0 <= n <= 15:
                            if m+1 < 20:
                                bl_delete_ball(_balls, n, m+1, color, pd)
                                bl_delete_ball(_balls, n-1, m+1, color, pd)

                            # 一定会遍历的
                            bl_delete_ball(_balls, n-1, m, color, pd)

                            if m-1 >= 0:
                                bl_delete_ball(_balls, n, m-1, color, pd)


    # 实现深度遍历的算法
    # 标记连接最顶层的球，包括最顶层
    # 判断mark0，将bl_mark修改为mark1
    # 为1，即遍历过，为0，则未遍历
    def bl_ball_hang(_balls, n, m, _mark0, _mark1):
        # mark 是判断球是否存在
        if _balls[n][m].mark:
            if _balls[n][m].bl_mark == _mark0:
                _balls[n][m].bl_mark = _mark1
                # balls[n][m].bl_mark = 0
                # 判断球所在的层数，即n，为奇数或是偶数
                if n % 2 == 0:
                    # 如果n不是第0层，的遍历
                    if 0 < n < 15:
                        # 只有从第2层开始才会遍历的
                        # 即上一层，n-1层
                        bl_ball_hang(_balls, n-1, m, _mark0, _mark1)

                        if m-1 >= 0:
                            bl_ball_hang(_balls, n-1, m-1, _mark0, _mark1)

                    if 0 <= n <= 15:
                        if m-1 >= 0:
                            bl_ball_hang(_balls, n, m-1, _mark0, _mark1)
                            bl_ball_hang(_balls, n+1, m-1, _mark0, _mark1)

                        # 一定会遍历的
                        bl_ball_hang(_balls, n+1, m, _mark0, _mark1)

                        if m+1 < 20:
                            bl_ball_hang(_balls, n, m+1, _mark0, _mark1)

                else:
                    # 如果n不是第15层，即最后一层的遍历
                    if 0 < n < 15:
                        # 只有从第15层前开始才会遍历的
                        # 即下一层，n+1层
                        bl_ball_hang(_balls, n+1, m, _mark0, _mark1)

                        if m+1 < 20:
                            bl_ball_hang(_balls, n+1, m+1, _mark0, _mark1)

                    if 0 <= n <= 15:
                        if m+1 < 20:
                            bl_ball_hang(_balls, n, m+1, _mark0, _mark1)
                            bl_ball_hang(_balls, n-1, m+1, _mark0, _mark1)

                        # 一定会遍历的
                        bl_ball_hang(_balls, n-1, m, _mark0, _mark1)

                        if m-1 >= 0:
                            bl_ball_hang(_balls, n, m-1, _mark0, _mark1)


    # 碰撞检测
    def collection(_ball, _balls):
        for n in range(len(_balls)-1):
            for m in range(len(_balls[n])):
                if _balls[n][m].mark == 1:
                    x0 = _ball.x + _ball.radius
                    y0 = _ball.y + _ball.radius
                    x1 = _balls[n][m].x + _balls[n][m].radius
                    y1 = _balls[n][m].y + _balls[n][m].radius
                    length = math.sqrt((pow(x0-x1, 2)+pow(y0-y1, 2)))
                    if length < _ball.radius + _balls[n][m].radius - 3:
                        return 1
        return 0


    # 若发生碰撞，判断小球应该所在的层数，位置，并小球加入到list_balls中
    def add_ball(_ball, _balls):
        x = round(_ball.x)
        y = round(_ball.y)
        n = y // 30
        if y % 30 >= 15:
            n += 1
        if n % 2 == 0:
            m = x // 30
            if x % 30 >= 15:
                m += 1
        else:
            m = (x + 15) // 30 - 1
            if (x + 15) % 30 >= 15:
                m += 1

        _balls[n][m].make_ball(_ball.key)
        return n, m


    def random_ball(_keys, _ball):
        n = random.randint(1, 100) / 100
        if 0 < n <= 0.25:
            _ball.make_ball(_keys[0])
        elif 0.25 < n <= 0.5:
            _ball.make_ball(_keys[1])
        elif 0.5 < n <= 0.75:
            _ball.make_ball(_keys[2])
        elif 0.75 < n <= 1:
            _ball.make_ball(_keys[3])


    def change_ball0(_hero_balls, _mark, _left, _mouse_x, _mouse_y):
        if _hero_balls[0].mark == 0:
            if _left == 1:
                _mark = 1
            else:
                if _mark == 1:
                    # 替换已出现的球
                    for n in range(4):
                        _hero_balls[n].make_ball(_hero_balls[n + 1].key)
                    random_ball(balls_key, _hero_balls[4])

                    # 让hero0的球动
                    lh = math.sqrt((pow(_mouse_x - _hero_balls[0].x, 2) + pow(_mouse_y - _hero_balls[0].y, 2)))
                    _hero_balls[0].speed_x = -(_mouse_x - _hero_balls[0].x) / lh * 8
                    _hero_balls[0].speed_y = abs((_mouse_y - _hero_balls[0].y) / lh * 8)
                    _mark = 0
        return _mark


    def change_ball0_speed(_screen, _hero_balls, _list_balls, _score_ppl):
        if _hero_balls[0].x < 0 or _hero_balls[0].x > 615 - 30:

            _hero_balls[0].speed_x = -_hero_balls[0].speed_x

        if _hero_balls[0].y < 0:
            _hero_balls[0].y = 0
            n, m = add_ball(_hero_balls[0], _list_balls)
            k = bl_ball_color(_list_balls, n, m, _hero_balls[0].color)
            if k >= 3:
                _score_ppl += k

                bl_delete_ball(_list_balls, n, m, _hero_balls[0].color)
            else:
                bl_delete_ball(_list_balls, n, m, _hero_balls[0].color, 0)
            _hero_balls[0] = Ball(_screen, 300 - 15, 500)
        else:
            if collection(_hero_balls[0], _list_balls):
                n, m = add_ball(_hero_balls[0], _list_balls)
                k = bl_ball_color(_list_balls, n, m, _hero_balls[0].color)
                if k >= 3:
                    _score_ppl += k

                    bl_delete_ball(_list_balls, n, m, _hero_balls[0].color)
                else:
                    bl_delete_ball(_list_balls, n, m, _hero_balls[0].color, 0)
                _hero_balls[0] = Ball(_screen, 300 - 15, 500)
        return _score_ppl


    def get_hang_balls(_screen, _list_balls, _score_ppl, _hang_balls):
        # 消除悬空的球
        for m in range(20):
            bl_ball_hang(_list_balls, 0, m, 0, 1)
        # 收集悬空的球
        for n in range(16):
            for m in range(20):
                if _list_balls[n][m].mark and _list_balls[n][m].bl_mark == 0:
                    _score_ppl += 1
                    _hang_balls.append(_list_balls[n][m])
                    _list_balls[n][m] = Ball(_screen, n % 2 * 15 + 30 * m, 30 * n)
        num = len(_hang_balls)
        if num:
            for n in range(len(_hang_balls)):
                _hang_balls[n].show()
                _hang_balls[n].y += 5
        n = 0
        while n < num:
            if n == num:
                break
            if _hang_balls[n].y > 800:
                _hang_balls.pop(n)
                n -= 1
                num -= 1
            n += 1
        for m in range(20):
            bl_ball_hang(_list_balls, 0, m, 1, 0)

        return _score_ppl


    def ppl(_screen, _background, _font, _score_ppl, _best_score_ppl, _mark, _hero_balls,
            _list_balls, _hang_balls, _ppl_game_mark, _button_width, _button_height, _balls_key, _start_time):

        _mouse_x, _mouse_y = pygame.mouse.get_pos()
        _left, _right, _mid = pygame.mouse.get_pressed()

        if _ppl_game_mark:
            _screen.blit(_background, (0, 0))
            show_line(_screen)
            score_font_ppl = _font.render("得分", True, (255, 255, 255))
            _screen.blit(score_font_ppl, (670, 10))

            text = str(_score_ppl)
            score_font_ppl = _font.render(text, True, (255, 255, 255))
            _screen.blit(score_font_ppl, (700 - len(text) * 7, 60))

            for n in range(16):
                for m in range(20):
                    _list_balls[n][m].show()

            for n in range(5):
                _hero_balls[n].show()

            if _ppl_game_mark == 1:
                _mark = change_ball0(_hero_balls, _mark, _left, _mouse_x, _mouse_y)

                # 加层
                if time.time() - _start_time > 10:
                    _start_time = time.time()
                    for m in range(20):
                        n = 16
                        while n > 0:
                            _list_balls[n][m].make_ball(_list_balls[n - 1][m].key)
                            n -= 1
                        random_ball(_balls_key, _list_balls[0][m])

            _hero_balls[0].x -= _hero_balls[0].speed_x
            _hero_balls[0].y -= _hero_balls[0].speed_y

            _score_ppl = change_ball0_speed(_screen, _hero_balls, _list_balls, _score_ppl)

            _score_ppl = get_hang_balls(_screen, _list_balls, _score_ppl, _hang_balls)

            # 判断是否超过界限, game over
            for m in range(20):
                if _list_balls[16][m].mark:
                    if _best_score_ppl < _score_ppl:
                        _best_score_ppl = _score_ppl
                    _ppl_game_mark = 3

            # 判断是否清空
            m = 0
            while m < 20:
                if _list_balls[0][m].mark:
                    break
                m += 1
            if m == 20:
                if _best_score_ppl < _score_ppl:
                    _best_score_ppl = _score_ppl
                _ppl_game_mark = 3

            if _ppl_game_mark == 3:

                _ppl_game_mark = over_game2(_screen, _score_ppl, _best_score_ppl,
                                            _left, _mouse_x, _mouse_y, _button_width, _button_height)
            if _ppl_game_mark == 31:
                _list_balls.clear()
                for n in range(17):
                    _balls = []
                    for m in range(20):
                        _ball = Ball(_screen, n % 2 * 15 + 30 * m, 30 * n)
                        _balls.append(_ball)
                    _list_balls.append(_balls)
                for n in range(8):
                    for m in range(20):
                        random_ball(_balls_key, _list_balls[n][m])

                _hero_balls = []
                # 运动中的玩家球
                _ball = Ball(_screen, 300 - 15, 500)
                _hero_balls.append(_ball)
                # 玩家正中间的球
                _ball = Ball(_screen, 300 - 15, 500)
                _hero_balls.append(_ball)
                for n in range(3):
                    _ball = Ball(_screen, 30 * (8 - n), 525)
                    _hero_balls.append(_ball)

                for n in range(4):
                    random_ball(_balls_key, _hero_balls[n + 1])

                # 创建一个收集悬空球的列表
                _hang_balls = []
                _mark = 0

        return _mark, _score_ppl, _best_score_ppl, _ppl_game_mark, _start_time


    screen_ppl = pygame.display.set_mode((800, 600))
    background_ppl = pygame.image.load(r"ppl\background.jpg")
    font_ppl = pygame.font.Font(r"STXINGKA.TTF", 42)
    score_ppl = 0
    # 导入本地最高纪录
    p_file = open("Score_ppl.txt", 'r')
    best_score_ppl = int(p_file.read())
    p_file.close()

    list_balls = []
    for i in range(17):
        balls = []
        for j in range(20):
            ball = Ball(screen_ppl, i % 2 * 15 + 30 * j, 30 * i)
            balls.append(ball)
        list_balls.append(balls)

    balls_key = [[r"ppl\Red_ball.png", 1, 1], [r"ppl\Yellow_ball.png", 2, 1],
                 [r"ppl\Blue_ball.png", 3, 1], [r"ppl\Green_ball.png", 4, 1]]

    for i in range(8):
        for j in range(20):
            random_ball(balls_key, list_balls[i][j])

    hero_balls = []
    # 运动中的玩家球
    ball = Ball(screen_ppl, 300-15, 500)
    hero_balls.append(ball)
    # 玩家正中间的球
    ball = Ball(screen_ppl, 300-15, 500)
    hero_balls.append(ball)
    for i in range(3):
        ball = Ball(screen_ppl, 30 * (8 - i), 525)
        hero_balls.append(ball)

    for i in range(4):
        random_ball(balls_key, hero_balls[i+1])

    # 创建一个收集悬空球的列表
    hang_balls = []
    flag = 0

    ###########################
    # 游戏开始
    ppl_game_mark = 0
    start_time = time.time()
    start_im = pygame.image.load(r"ppl\ppl_s.jpg")
    start_button = pygame.image.load(r"ppl\start_ppl.png")
    start_button_rect = start_button.get_rect()
    start_button_width = start_button_rect.width
    start_button_height = start_button_rect.height
    start_button_mark = 0

    # 泡泡龙游戏结束
    bg2 = pygame.image.load(r"ppl\background2副本.png")
    font2 = pygame.font.Font("STKAITI.TTF", 25)
    font3 = pygame.font.Font("STKAITI.TTF", 70)

    image_restart2 = pygame.image.load(r"ppl\restart2.png")  # 再来一局
    restart2_rect = image_restart2.get_rect()
    restart2_width = restart2_rect.width
    restart2_height = restart2_rect.height

    image_return2 = pygame.image.load(r"ppl\return2.png")  # 返回主界面
    return2_rect = image_return2.get_rect()
    return2_width = return2_rect.width
    return2_height = return2_rect.height

    image_exit2 = pygame.image.load(r"ppl\exit2.png")  # 退出
    exit2_rect = image_exit2.get_rect()
    exit2_width = exit2_rect.width
    exit2_height = exit2_rect.height

    button_width = [restart2_width, return2_width, exit2_width]
    button_height = [restart2_height, return2_height, exit2_height]


    def over_game2(_screen, _score_ppl, _best_score_ppl, _left, _mouse_x, _mouse_y, _button_width, _button_height):
        _screen.blit(bg2, (0, -100))
        text_end = font3.render("游戏结束！", True, (255, 255, 255))
        text_score = font2.render("本次得分：" + str(_score_ppl), True, (255, 255, 255))
        text_highest = font2.render("历史最高分：" + str(_best_score_ppl), True, (255, 255, 255))

        _screen.blit(text_end, (250, 220-100))
        _screen.blit(text_score, (300, 330-100))
        _screen.blit(text_highest, (300, 370-100))

        _screen.blit(image_restart2, (180, 446-100))
        _screen.blit(image_return2, (330, 450-100))
        _screen.blit(image_exit2, (520, 450-100))

        if _left and 180 < _mouse_x < 180 + _button_width[0] and 346 < _mouse_y < 346 + _button_height[0]:
            return 31
        if _left and 330 < _mouse_x < 330 + _button_width[1] and 350 < _mouse_y < 350 + _button_height[1]:
            _p_file = open("Score_ppl.txt", 'w')
            _p_file.write(str(_best_score_ppl))
            _p_file.close()
            return 32
        if _left and 520 < _mouse_x < 520 + _button_width[2] and 350 < _mouse_y < 350 + _button_height[2]:
            _p_file = open("Score_ppl.txt", 'w')
            _p_file.write(str(_best_score_ppl))
            _p_file.close()
            exit()
        return 3

    while True:
        if what_play==1:
            game_music.play()
            what_play=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                p_file = open("Score_ppl.txt", 'w')
                p_file.write(str(best_score_ppl))
                p_file.close()
                exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        left, right, mid = pygame.mouse.get_pressed()
        if ppl_game_mark == 0:
            start_time = time.time()
            screen_ppl.blit(start_im, (0, 0))
            screen_ppl.blit(start_button, (400-start_button_width/2, 450))
            if left == 1:
                if 400-start_button_width/2 < mouse_x < 400+start_button_width/2 and\
                        450 < mouse_y < 450 + start_button_height:
                    start_button_mark = 1
            else:
                if start_button_mark == 1:
                    ppl_game_mark = 1
                    start_button_mark = 0

        flag, score_ppl, best_score_ppl, \
        ppl_game_mark, start_time = ppl(screen_ppl, background_ppl, font_ppl, score_ppl,
                                        best_score_ppl, flag, hero_balls, list_balls, hang_balls,
                                        ppl_game_mark, button_width, button_height, balls_key, start_time)
        if ppl_game_mark == 31:
            game_music.stop()
            what_play = 1
            ppl_game_mark = 1
            start_time = time.time()
        if ppl_game_mark == 32:
            list_balls = []
            for i in range(17):
                balls = []
                for j in range(20):
                    ball = Ball(screen_ppl, i % 2 * 15 + 30 * j, 30 * i)
                    balls.append(ball)
                list_balls.append(balls)

            for i in range(8):
                for j in range(20):
                    random_ball(balls_key, list_balls[i][j])

            hero_balls = []
            # 运动中的玩家球
            ball = Ball(screen_ppl, 300 - 15, 500)
            hero_balls.append(ball)
            # 玩家正中间的球
            ball = Ball(screen_ppl, 300 - 15, 500)
            hero_balls.append(ball)
            for i in range(3):
                ball = Ball(screen_ppl, 30 * (8 - i), 525)
                hero_balls.append(ball)

            for i in range(4):
                random_ball(balls_key, hero_balls[i + 1])

            # 创建一个收集悬空球的列表
            hang_balls = []
            flag = 0
            game_music.stop()
            import 封面
            封面.func()



        pygame.display.update()
