import os
import pyautogui
import numpy as np
import time

# 全局变量：
a = 1
size = 15

# 初始化棋盘：
# 【https://blog.csdn.net/qq_25436597/article/details/79334240】
mainList = np.zeros((size, size))

# 初始化棋盘：
for i in range(size):
    for j in range(size):
        mainList[i][j] = 1

def bw(a):
    if a % 2 == 1:
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
        testWin(x, y, mainList[x][y])
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
        testWin(x, y, mainList[x][y])

def clean():
    for i in range(size):
        print()

def printBoard(a):
    # 打印棋盘主体：
    print("   1      3      5      7      9     11     13     15")
    for i in range(size):
        if i < 9:
            print(i + 1, end=" ")
        else:
            print(i + 1, end="")
        for j in range(size):
            if mainList[i][j] == 255:
                print(" ◙ ", end="")
            if mainList[i][j] == 128:
                print(" ⊡ ", end="")
            elif mainList[i][j] == 1:
                print(" ◌ ", end="")
        print("\n")

    bw(a)
    clean()

def testWin(xIn, yIn, numIn):
    print(xIn, yIn, numIn)
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
                print("you win XB")
    yB = set(yBlack)
    for i in yB:
        countYB = 0
        for j in yBlack:
            if i == j:
                countYB += 1
            if countYB >= 5:
                print("you win YB")
    xW = set(xWhite)
    for i in xW:
        countXW = 0
        for j in xWhite:
            if i == j:
                countXW += 1
            if countXW >= 5:
                print("you win XW")
    yW = set(yWhite)
    for i in yW:
        countYW = 0
        for j in yWhite:
            if i == j:
                countYW += 1
            if countYW >= 5:
                print("you win YW")

# 主体：l
while True:
    printBoard(a)
    a += 1



