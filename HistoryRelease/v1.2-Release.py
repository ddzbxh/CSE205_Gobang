# -*- coding = utf-8 -*-
import numpy as np

# 全局变量：
a = 1  # 在主函数内迭代，bw(a)通过对a的奇偶进行判断来分别棋色
size = 15  # 棋盘大小，通过修改可以生成不同大小的棋盘

# 初始化棋盘：
mainList = np.zeros((size, size))  # 用numpy生成二维矩阵，参考【https://blog.csdn.net/qq_25436597/article/details/79334240】

# 初始化棋盘：
for i in range(size):
    for j in range(size):  # 遍历棋盘所有坐标，(i,j)即棋盘坐标系的(x,y)值
        mainList[i][j] = 1  # 棋盘所有棋位赋值为1，黑旗值255，白棋值128
# *注：根据书写逻辑，y轴从上向下，即起点在上，Y↓，X→

def bw(a):
    if a != 1:  # a为1时表示初始棋盘，此时需要先打印一个空棋盘，因此首次调用bw(a)时实际上不应执行
        testWinner = testWin()  # 调用testWin()用以判定是否有一方胜出，如有胜出将会返回"black win"或"white win"
        if testWinner == "black win" or testWinner == "white win":  # 如果有一方已经胜出将直接结束
            return testWinner  # 【返回1.1】
        else:  # 如果还没有胜出者，将会input新棋子
            if a % 2 == 0:  # 通过判定a迭代的值是奇或偶数，选择input黑方或白方
                while True:                                            # 【1.1】若输入不合法，将重新执行输入
                    try:                                               # 【1.2】用try拦截不合法时的报错，防止程序中断
                        x, y = input('【黑棋】x,y:').split(",")
                        x = int(x) - 1
                        y = int(y) - 1                                 # 【1.3】矫正，实际棋盘坐标起始为(0,0)，输入值起始为(1,1)
                    except BaseException:
                        print("<input error, try again>")
                    else:
                        if mainList[x][y] != 1:                        # 【1.4】如果该坐标的值不为1，则表示已经落子，需要重新执行while，选择其他坐标
                            print("<input overlap, try again>")
                        else:                                          # 【1.5】如果是空位，执行落子，break while
                            mainList[x][y] = 255
                            break
            else:
                while True:                                            # 【同1.1】
                    try:                                               # 【同1.2】
                        x, y = input('【白棋】x,y:').split(",")
                        x = int(x) - 1
                        y = int(y) - 1  # 【同1.3】
                    except BaseException:
                        print("<input error, try again>")
                    else:
                        if mainList[x][y] != 1:  # 【同1.4】
                            print("<input overlap, try again>")
                        else:                                          # 【同1.5】
                            mainList[x][y] = 128
                            break
            return ""  # 【返回1.2】

def clean():  # 打印与棋盘等大的换行
    for i in range(size):
        print()

def printBoard(a):  # 主体function
    theWinner = bw(a)  # 调用bw(a)，返回值决定是否有胜者出现，根据【返回1.1】判断胜利归属，无胜出时则返回值来自【返回1.2】
    if theWinner == "black win" or theWinner == "white win":  # 如有胜出，宣布胜利归属
        print("----------------------")
        print("                      ")
        print("    ", theWinner)
        print("                      ")
        print("----------------------")
        return -1  # 返回-1将使主函数中的a停止迭代，结束函数
    elif a != 1:  # 如不是a的第一次迭代，将调用clean()清空窗口
        clean()
    # 打印棋盘：
    print("   1      3      5      7      9     11     13     15")  # 横向坐标
    for i in range(size):  # 遍历棋盘Y轴
        if i < 9:  # 判断，横坐标为一位数时退一格，两位数时不退格
            print(i + 1, end=" ")
        else:
            print(i + 1, end="")
        for j in range(size):  # 遍历棋盘X轴，判断棋值，如果为255打印黑棋符号，128打印白棋符号，1打印空符号
            if mainList[i][j] == 255:
                print("\033[0;35;45m ◙ \033[0m", end="")
            if mainList[i][j] == 128:
                print("\033[0;30;40m ⊡ \033[0m", end="")
            elif mainList[i][j] == 1:
                print(" ◌ ", end="")
        print("\n")  # 换行
    return a  # 结束，返回主函数，迭代下一个a

def testWin():
    xBlack = []
    yBlack = []
    xWhite = []
    yWhite = []
    for i in range(size):                # 遍历，将所有落子的坐标值存入单独的list
        for j in range(size):
            if mainList[i][j] == 255:
                xBlack.append(i)
                yBlack.append(j)
            if mainList[i][j] == 128:
                xWhite.append(i)
                yWhite.append(j)
    xB = set(xBlack)                     # 检测黑棋是否有5连的横向坐标
    for i in xB:
        countXB = 0
        for j in xBlack:
            if i == j:
                countXB += 1
            if countXB >= 5:
                return "black win"
    yB = set(yBlack)                     # 检测黑棋是否有5连的纵向坐标
    for i in yB:
        countYB = 0
        for j in yBlack:
            if i == j:
                countYB += 1
            if countYB >= 5:
                return "black win"
    xW = set(xWhite)                     # 检测白棋是否有5连的横向坐标
    for i in xW:
        countXW = 0
        for j in xWhite:
            if i == j:
                countXW += 1
            if countXW >= 5:
                return "white win"
    yW = set(yWhite)                     # 检测白棋是否有5连的纵向坐标
    for i in yW:
        countYW = 0
        for j in yWhite:
            if i == j:
                countYW += 1
            if countYW >= 5:
                return "white win"

    for i in range(size):                # 检测右下方向是否有5连坐标
        for j in range(size):
            try:
                if mainList[i][j] != 1:
                    if mainList[i][j] == mainList[i + 1][j + 1]:
                        i += 1
                        j += 1
                        if mainList[i][j] == mainList[i + 1][j + 1]:
                            i += 1
                            j += 1
                            if mainList[i][j] == mainList[i + 1][j + 1]:
                                i += 1
                                j += 1
                                if mainList[i][j] == mainList[i + 1][j + 1]:
                                    if mainList[i][j] == 128:
                                        return "white win"
                                    if mainList[i][j] == 255:
                                        return "black win"
            except BaseException:
                error = 1
    for i in range(size):                # 检测左下方向是否有5连坐标
        for j in range(size):
            try:
                if mainList[i][j] != 1:
                    if mainList[i][j] == mainList[i + 1][j - 1]:
                        i += 1
                        j += 1
                        if mainList[i][j] == mainList[i + 1][j - 1]:
                            i += 1
                            j += 1
                            if mainList[i][j] == mainList[i + 1][j - 1]:
                                i += 1
                                j += 1
                                if mainList[i][j] == mainList[i + 1][j - 1]:
                                    if mainList[i][j] == 128:
                                        return "white win"
                                    if mainList[i][j] == 255:
                                        return "black win"
            except BaseException:
                error = 1
    for i in range(size):                # 检测右上方向是否有5连坐标
        for j in range(size):
            try:
                if mainList[i][j] != 1:
                    if mainList[i][j] == mainList[i - 1][j + 1]:
                        i += 1
                        j += 1
                        if mainList[i][j] == mainList[i - 1][j + 1]:
                            i += 1
                            j += 1
                            if mainList[i][j] == mainList[i - 1][j + 1]:
                                i += 1
                                j += 1
                                if mainList[i][j] == mainList[i - 1][j + 1]:
                                    if mainList[i][j] == 128:
                                        return "white win"
                                    if mainList[i][j] == 255:
                                        return "black win"
            except BaseException:
                error = 1
    for i in range(size):                # 检测左上方向是否有5连坐标
        for j in range(size):
            try:
                if mainList[i][j] != 1:
                    if mainList[i][j] == mainList[i - 1][j - 1]:
                        i += 1
                        j += 1
                        if mainList[i][j] == mainList[i - 1][j - 1]:
                            i += 1
                            j += 1
                            if mainList[i][j] == mainList[i - 1][j - 1]:
                                i += 1
                                j += 1
                                if mainList[i][j] == mainList[i - 1][j - 1]:
                                    if mainList[i][j] == 128:
                                        return "white win"
                                    if mainList[i][j] == 255:
                                        return "black win"
            except BaseException:
                error = 1
    return ""  # 无胜利者
# 主体：
while True:
    a = printBoard(a)  # 调用主体function，其他function由printBoard(a)使用，每次参数a与返回a相同，若返回a变为-1，则出现胜者，结束程序
    if a == -1:  # 若有胜者产生，a在printBoard(a)内被改变为-1
        break
    a += 1  # a的迭代




