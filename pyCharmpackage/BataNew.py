# -*- coding = utf-8 -*-

import numpy as np

class Chess:

    def __init__(self):
        self.size = 15
        self.mainList = np.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                self.mainList[i][j] = 1
        self.winner = ""
        self.space = " "
        self.term = 1
        self.checkHelp = True
        self.language = 1
        self.direction()
        self.language = 2
        self.direction()
        self.main()

    def main(self):
        while self.term != -1:
            self.testWin()
            if self.winner == "black win" or self.winner == "white win":
                self.printTheWinner()
            else:
                self.printXNums()
                self.printBoard()
                self.playOneStep()
                if self.checkHelp:
                    self.term += 1
                    print("\n"*self.size)
                else:
                    self.askHelp()

    def printXNums(self):
        if self.size <= 10:
            print("   ", end="")
            for i in range(self.size + 1):
                if i % 2 == 1:
                    print(i, end="      ")
            print("\n")
        else:
            print("   1      3      5      7      9     ", end="")
            for i in range(11, (self.size + 1)):
                if i % 2 == 1:
                    print(i, end="     ")
            print("\n")

    def printBoard(self):
        for i in range(self.size):
            if i < 9:
                print(i + 1, end=" ")
            else:
                print(i + 1, end="")
            for j in range(self.size):
                print(self.space, end="")
                if self.mainList[i][j] == 255:
                    print("\033[0;35;45m◙\033[0m", end="")
                if self.mainList[i][j] == 128:
                    print("\033[0;30;40m⊡\033[0m", end="")
                elif self.mainList[i][j] == 1:
                    print("◌", end="")
                print(self.space, end="")
            print("\n")

    def printTheWinner(self):
        if self.winner == "black win" or self.winner == "white win":
            print("----------------------")
            print("                      ")
            print("    ", self.winner)
            print("                      ")
            print("----------------------")
            self.term = -1

    def playOneStep(self):
        while True:
            if self.term % 2 == 0:
                xy = input('【黑棋】x,y:')
            else:
                xy = input('【白棋】x,y:')
            try:
                x, y = xy.split(",")
            except BaseException:
                if xy == "help" or xy == "?" or xy == "？" or xy == "Help":
                    self.checkHelp = False
                    break
                print("<input error, try again, or type 'help'>")
            else:
                x = int(x) - 1
                y = int(y) - 1
                if self.mainList[x][y] != 1:
                    print("<input overlap, try again, or type 'help'>")
                else:
                    if self.term % 2 == 0:
                        self.mainList[x][y] = 255
                    else:
                        self.mainList[x][y] = 128
                    break

    def testWin(self):
        xBlack = []
        yBlack = []
        xWhite = []
        yWhite = []
        for i in range(self.size):
            for j in range(self.size):
                if self.mainList[i][j] == 255:
                    xBlack.append(i)
                    yBlack.append(j)
                if self.mainList[i][j] == 128:
                    xWhite.append(i)
                    yWhite.append(j)
        xB = set(xBlack)
        for i in xB:
            countXB = 0
            for j in xBlack:
                if i == j:
                    countXB += 1
                if countXB >= 5:
                    self.winner = "black win"
        yB = set(yBlack)
        for i in yB:
            countYB = 0
            for j in yBlack:
                if i == j:
                    countYB += 1
                if countYB >= 5:
                    self.winner = "black win"
        xW = set(xWhite)
        for i in xW:
            countXW = 0
            for j in xWhite:
                if i == j:
                    countXW += 1
                if countXW >= 5:
                    self.winner = "white win"
        yW = set(yWhite)
        for i in yW:
            countYW = 0
            for j in yWhite:
                if i == j:
                    countYW += 1
                if countYW >= 5:
                    self.winner = "white win"

        for i in range(self.size):
            for j in range(self.size):
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i + 1][j + 1]:
                            i += 1
                            j += 1
                            if self.mainList[i][j] == self.mainList[i + 1][j + 1]:
                                i += 1
                                j += 1
                                if self.mainList[i][j] == self.mainList[i + 1][j + 1]:
                                    i += 1
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i + 1][j + 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")

        for i in range(self.size):
            for j in range(self.size):
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                            i += 1
                            j += 1
                            if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                i += 1
                                j += 1
                                if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                    i += 1
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")

        for i in range(self.size):
            for j in range(self.size):
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                            i += 1
                            j += 1
                            if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                                i += 1
                                j += 1
                                if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                                    i += 1
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")

        for i in range(self.size):
            for j in range(self.size):
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                            i += 1
                            j += 1
                            if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                                i += 1
                                j += 1
                                if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                                    i += 1
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")

    def askHelp(self):
        self.checkHelp = True
        while True:
            q1 = input()


    def direction(self):
        if self.language == 1:
            print("--------------------------------------------------------\n"
                  "project3，《五子棋》\n"
                  "1.此为双人模式，两名玩家轮流走棋\n"
                  "2.可识别的输入格式为【行】【英文逗号】【列】，不规范的输入将被驳回\n"
                  "3.在已经落子的棋位下棋将被驳回\n"
                  "4.当有一方胜出，将会自动结束\n"
                  "5.输入\"help\"或双语问号调整设置\n"
                  "--------------------------------------------------------")
        elif self.language == 2:
            print("--------------------------------------------------------\n"
                  "project3, Gobang\n"
                  "1. This is a two-player mode, with two players playing chess in turn\n"
                  "2. The recognizable input format is [row] [English comma] [column], and non-standard input will be rejected\n"
                  "3. Playing in a position that has been played will be rejected\n"
                  "4. When one side wins, it automatically ends\n"
                  "5. Enter \"help\" or bilingual question mark to adjust Settings\n"
                  "--------------------------------------------------------")

if __name__ == '__main__':
    Chess()





