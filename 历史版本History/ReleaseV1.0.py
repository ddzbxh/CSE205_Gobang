import os
import pyautogui
import numpy as np
import time

# 全局变量：
a = 1
size = 15
x, y = 1, 1

# 初始化棋盘：
# 【https://blog.csdn.net/qq_25436597/article/details/79334240】
mainList = np.zeros((size, size))

# 初始化棋盘：
for i in range(size):
    for j in range(size):
        mainList[i][j] = 1

def bw(a):
    if a != 1:
        testWinner = testWin()
        if testWinner == "black win" or testWinner == "white win":
            return testWinner
        else:
            if a % 2 == 0:
                while True:
                    try:
                        x, y = input('【黑棋】x,y:').split(",")
                        x = int(x) - 1
                        y = int(y) - 1
                    except BaseException:
                        print("<input error, try again>")
                    else:
                        if mainList[x][y] != 1:
                            print("<input overlap, try again>")
                        else:
                            mainList[x][y] = 255
                            break
            else:
                while True:
                    try:
                        x, y = input('【白棋】x,y:').split(",")
                        x = int(x) - 1
                        y = int(y) - 1
                    except BaseException:
                        print("<input error, try again>")
                    else:
                        if mainList[x][y] != 1:
                            print("<input overlap, try again>")
                        else:
                            mainList[x][y] = 128
                            break
            return ""

def clean():
    for i in range(size):
        print()

def printBoard(a):
    theWinner = bw(a)
    if theWinner == "black win" or theWinner == "white win":
        print("----------------------")
        print("                      ")
        print("    ", theWinner)
        print("                      ")
        print("----------------------")
        return -1
    elif a == 1:
        # 打印棋盘主体：
        print("   1      3      5      7      9     11     13     15")
        for i in range(size):
            if i < 9:
                print(i + 1, end=" ")
            else:
                print(i + 1, end="")
            for j in range(size):
                if mainList[i][j] == 255:
                    print(" ⊡ ", end="")
                if mainList[i][j] == 128:
                    print(" ◙ ", end="")
                elif mainList[i][j] == 1:
                    print(" ◌ ", end="")
            print("\n")
        return a
    else:
        clean()
        # 打印棋盘主体：
        print("   1      3      5      7      9     11     13     15")
        for i in range(size):
            if i < 9:
                print(i + 1, end=" ")
            else:
                print(i + 1, end="")
            for j in range(size):
                if mainList[i][j] == 255:
                    print(" ⊡ ", end="")
                if mainList[i][j] == 128:
                    print(" ◙ ", end="")
                elif mainList[i][j] == 1:
                    print(" ◌ ", end="")
            print("\n")
        return a

def testWin():
    xBlack = []
    yBlack = []
    xWhite = []
    yWhite = []
    for i in range(size):
        for j in range(size):
            if mainList[i][j] == 255:
                xBlack.append(i)
                yBlack.append(j)
            if mainList[i][j] == 128:
                xWhite.append(i)
                yWhite.append(j)
    xB = set(xBlack)
    for i in xB:
        countXB = 0
        for j in xBlack:
            if i == j:
                countXB += 1
            if countXB >= 5:
                return "black win"
    yB = set(yBlack)
    for i in yB:
        countYB = 0
        for j in yBlack:
            if i == j:
                countYB += 1
            if countYB >= 5:
                return "black win"
    xW = set(xWhite)
    for i in xW:
        countXW = 0
        for j in xWhite:
            if i == j:
                countXW += 1
            if countXW >= 5:
                return "white win"
    yW = set(yWhite)
    for i in yW:
        countYW = 0
        for j in yWhite:
            if i == j:
                countYW += 1
            if countYW >= 5:
                return "white win"

    for i in range(size):
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
    for i in range(size):
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
    for i in range(size):
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
    for i in range(size):
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
    return ""
# 主体：l
while True:
    a = printBoard(a)
    if a == -1:
        break
    a += 1




