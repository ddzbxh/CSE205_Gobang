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
        self.PBMode = True
        self.language = 1
        self.askLanguage()
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
                    if not self.PBMode:
                        print("\n"*self.size*2)
                    else:
                        print("-"*60)
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
            print("-" * 30, "\n", "*" * 30)
            print(" " * 10, self.winner, " win!!!\n", "*" * 30)
            print("-" * 30)
            self.term = -1

    def playOneStep(self):
        while True:
            if self.term % 2 == 0:
                if self.language == 1:
                    xy = input('【黑棋】x,y:')
                else:
                    xy = input('[black]x,y:')
            else:
                if self.language == 1:
                    xy = input('【白棋】x,y:')
                else:
                    xy = input('[white]x,y:')
            try:
                x, y = xy.split(",")
                x = int(x) - 1
                y = int(y) - 1
            except BaseException:
                if xy == "help" or xy == "?" or xy == "？" or xy == "Help":
                    self.checkHelp = False
                    break
                if self.language == 1:
                    print("<无法识别的输入，重试或输入“help”寻求帮助>")
                elif self.language == 2:
                    print("<input error, try again, or type 'help'>")
            else:
                if self.mainList[x][y] != 1:
                    if self.language == 1:
                        print("<此处已经落子，重试或输入“help”寻求帮助>")
                    elif self.language == 2:
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
        while not self.checkHelp:
            print("-" * 30)
            while True:
                if self.language == 1:
                    inp = input("A.游戏\nB.界面参数\nC.Language\nD.退出\n>>>")
                else:
                    inp = input('A.About game\nB.Change parameter\nC.调整语言\nD.EXIT\n>>>')
                check = False
                if inp == "A" or inp == "a":
                    check = self.askGame()
                elif inp == "B" or inp == "b":
                    check = self.askPara()
                elif inp == "C" or inp == "c":
                    self.askLanguage()
                    check = True
                elif inp == "D" or inp == "d":
                    check = True
                else:
                    if self.language == 1:
                        print("<无法识别的输入，请输入选项以选择，如大写A、B等>")
                    elif self.language == 2:
                        print("<input error, try again, give your choose as A, B, etc.>")
                if not check:
                    print("-" * 30)
                else:
                    self.checkHelp = True
                    break
        print("-" * 30)

    def askGame(self):
        while True:
            if self.language == 1:
                inp = input("A.重新开始\nB.返回上级\n>>>")
            else:
                inp = input("A.Restart\nB.Back\n>>>")
            if inp == "A" or inp == "a":
                self.mainList = np.zeros((self.size, self.size))
                for i in range(self.size):
                    for j in range(self.size):
                        self.mainList[i][j] = 1
                self.winner = ""
                self.space = " "
                self.term = 1
                return True
            elif inp == "B" or inp == "b":
                return False
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def askPara(self):
        while True:
            if self.language == 1:
                inp = input("A.调整间隔字符\nB.棋盘刷新方式\nC.返回上级\n>>>")
            else:
                inp = input("A.Change the space letter\nB.Checkerboard refresh mode\nC.Back\n>>>")
            if inp == "A" or inp == "a":
                if self.language == 1:
                    self.space = input("间隔字符:")
                elif self.language == 2:
                    self.space = input("the space letter:")
                return True
            elif inp == "B" or inp == "b":
                self.askPB()
                return True
            elif inp == "C" or inp == "c":
                return False
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def askPB(self):
        while True:
            if self.language == 1:
                inp = input("A.横线分割模式\nB.换行模式\n>>>")
            else:
                inp = input("A.Horizontal division mode\nB.Multiple newline mode\n>>>")
            if inp == "A" or inp == "a":
                self.PBMode = True
                return True
            elif inp == "B" or inp == "b":
                self.PBMode = False
                return True
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def askLanguage(self):
        while True:
            language = input("A.简体中文\nB.English\n>>>")
            if language == "A" or language == "a":
                self.language = 1
                break
            elif language == "B" or language == "b":
                self.language = 2
                break
            else:
                print("Please give your choose by letter as A, B, etc.\n请输入选项以选择，如大写A、B等")

    def direction(self):
        if self.language == 1:
            print("-" * 30)
            print("project3，《五子棋》\n"
                  "1.此为双人模式，两名玩家轮流走棋\n"
                  "2.可识别的输入格式为【行】【英文逗号】【列】，不规范的输入将被驳回\n"
                  "3.在已经落子的棋位下棋将被驳回\n"
                  "4.当有一方胜出，将会自动结束\n"
                  "5.输入\"help\"或双语问号调整设置\n"
                  , end="")
            print("-" * 30)
        elif self.language == 2:
            print("-" * 30)
            print("project3, Gobang\n"
                  "1. This is a two-player mode, with two players playing chess in turn\n"
                  "2. The recognizable input format is [row] [English comma] [column],\n"
                  "\tand non-standard input will be rejected\n"
                  "3. Playing in a position that has been played will be rejected\n"
                  "4. When one side wins, it automatically ends\n"
                  "5. Enter \"help\" or bilingual question mark to adjust Settings\n"
                  , end="")
            print("-" * 30)


if __name__ == '__main__':
    Chess()
