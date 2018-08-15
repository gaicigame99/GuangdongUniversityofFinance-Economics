import copy
class computer:
    def __init__(self):
        size = 14
        self.chess_Value = [[0 for i in range(size + 1)] for i in range(size + 1)]
        self.chess_Value2 = [[0 for i in range(size + 1)] for i in range(size + 1)]
        #  code用来提取空棋点八个方向的棋型，并获得相应的权值，比如上面是三个黑棋，则对应着"111"
        self.code = ""
        #  chess_color 用来保存某一位置的棋的颜色，用于获取棋型
        self.chess_color = 0
    def count2(self,chess):
        size = 14
        dic2 = {"0": 0, "1": 10, "2": 8, "11": 1000, "22": 1000, "111": 2600, "222": 2500, "1111": 10000, "2222": 5000,
                "21": 2, "12": 4, "211": 20, "122": 25, "11112": 10000, "112": 500, "1112": 4000, "221": 6, "2221": 500,
                "22221": 3000}
        for i in range(15):
            for j in range(15):
                if chess[i][j] == 0:
                    for x in range(j + 1, size + 1):
                        # 如果向右的第一位置为空就跳出循环
                        if chess[i][x] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[i][x])  # 记录它的颜色
                                self.chess_color = chess[i][x]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[i][x]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[i][x])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[i][x])  # 获去获取棋型
                                    break  # 结束本次循环
                        # 取出对应的权值，此处对齐第一个for，有不懂的请往下看
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x in range(j - 1, 0, -1):
                        if chess[i][x] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[i][x])  # 记录它的颜色
                                self.chess_color = chess[i][x]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[i][x]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[i][x])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[i][x])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x in range(i + 1, size + 1):
                        if chess[x][j] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][j])  # 记录它的颜色
                                self.chess_color = chess[x][j]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][j])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][j])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x in range(i - 1, 0, -1):
                        if chess[x][j] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][j])  # 记录它的颜色
                                self.chess_color = chess[x][j]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][j])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][j])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i - 1, 0, -1), range(j + 1, size + 1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i + 1, size + 1), range(j - 1, 0, -1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i - 1, 0, -1), range(j - 1, 0, -1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i + 1, size + 1), range(j + 1, size + 1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic2.get(self.code)
                    if value:
                        self.chess_Value2[i][j] += value
                    self.code = ""
                    self.chess_color = 0
    def count(self,chess):
        size = 14
        dic = {"0": 0, "1": 8, "2": 10, "11": 1000, "22": 1000, "111": 2500, "222": 2600, "1111": 1000, "2222": 10000,
               "21": 4, "12": 2, "211": 25, "122": 20, "11112": 3000, "112": 6, "1112": 500, "221": 500, "2221": 4000,
               "22221": 10000, "11111":20000}
        dic2 = {"0": 0, "1": 10, "2": 8, "11": 1000, "22": 1000, "111": 2600, "222": 2500, "1111": 10000, "2222": 5000,
               "21": 2, "12": 4, "211": 20, "122": 25, "11112": 10000, "112": 500, "1112": 4000, "221": 6, "2221": 500,
               "22221": 3000}
        for i in range(15):
            for j in range(15):
                if chess[i][j] == 0:
                    for x in range(j + 1, size + 1):
                        # 如果向右的第一位置为空就跳出循环
                        if chess[i][x] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[i][x])  # 记录它的颜色
                                self.chess_color = chess[i][x]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[i][x]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[i][x])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[i][x])  # 获去获取棋型
                                    break  # 结束本次循环
                        # 取出对应的权值，此处对齐第一个for，有不懂的请往下看
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x in range(j - 1,0,-1):
                        if chess[i][x] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[i][x])  # 记录它的颜色
                                self.chess_color = chess[i][x]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[i][x]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[i][x])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[i][x])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x in range(i + 1,size + 1):
                        if chess[x][j] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][j])  # 记录它的颜色
                                self.chess_color = chess[x][j]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][j])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][j])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x in range(i - 1, 0, -1):
                        if chess[x][j] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][j])  # 记录它的颜色
                                self.chess_color = chess[x][j]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][j])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][j])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i - 1, 0, -1), range(j + 1, size + 1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i + 1, size + 1), range(j - 1 ,0, -1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i - 1, 0, -1), range(j - 1,0, -1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0
                    for x, y in zip(range(i + 1, size + 1), range(j + 1, size + 1)):
                        if chess[x][y] == 0:
                            break  # 结束本次循环
                        else:
                            #  向右搜索的第一个是特例，用来保存棋子的颜色
                            if self.chess_color == 0:  # 这是右边第一颗棋子
                                self.code += str(chess[x][y])  # 记录它的颜色
                                self.chess_color = chess[x][y]  # 保存它的颜色
                            else:
                                if self.chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                    self.code += str(chess[x][y])  # 获取棋型，进入下一次循环，并再继续向右搜索
                                else:  # 右边找到一颗不同颜色的棋子
                                    self.code += str(chess[x][y])  # 获去获取棋型
                                    break  # 结束本次循环
                    value = dic.get(self.code)
                    if value:
                        self.chess_Value[i][j] += value
                    self.code = ""
                    self.chess_color = 0

    def get_result(self,chess):
        chess_in = copy.deepcopy(chess)
        size = 14
        self.chess_Value = [[0 for i in range(size + 1)] for i in range(size + 1)]
        self.chess_Value2 = [[0 for i in range(size + 1)] for i in range(size + 1)]
        self.count(chess_in)
        xxx = 0
        yyy = 0
        xxx1 = 0
        yyy1 = 0
        choicevalue = []
        choiceXY = []

        mymax1 = self.chess_Value[0][0]
        mycenter = self.chess_Value[0][0]
        mymin = self.chess_Value[0][0]
        #  遍历棋盘
        for a in range(0, size + 1):
            for b in range(0, size + 1):
                if self.chess_Value[a][b] > mymax1 and chess[a][b] == 0:
                    mymax1 = self.chess_Value[a][b]  # 获得权值最大点，xxx，yyy保存最大点位置
                    xxx = a
                    yyy = b
        chess_in[xxx][yyy] = 2

        self.count2(chess_in)
        mymax2 = self.chess_Value2[0][0]
        #  遍历棋盘
        for a in range(0, size + 1):
            for b in range(0, size + 1):
                if self.chess_Value2[a][b] > mymax2 and chess[a][b] == 0:
                    mymax2 = self.chess_Value2[a][b]  # 获得权值最大点，xxx，yyy保存最大点位置
                    xxx1 = a
                    yyy1 = b
        chess_in[xxx][yyy] = 1

        self.chess_Value = [[0 for i in range(size + 1)] for i in range(size + 1)]
        self.count(chess_in)
        mymax3 = self.chess_Value[0][0]
        #  遍历棋盘
        for a in range(0, size + 1):
            for b in range(0, size + 1):
                if self.chess_Value[a][b] > mymax3 and chess[a][b] == 0:
                    mymax3 = self.chess_Value[a][b]  # 获得权值最大点，xxx，yyy保存最大点位置
                    xxx1 = a
                    yyy1 = b
        if mymax3 - 2500> mymax1:
            return[xxx1,yyy1]
        return [xxx,yyy]
        # chess[xxx][yyy] = 2
