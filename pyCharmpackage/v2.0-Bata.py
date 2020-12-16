# -*- coding = utf-8 -*-
import numpy as np
from tkinter import *
from tkinter.messagebox import *

class Chess:

    def __init__(self):
        self.row, self.column = 15, 15
        self.mesh = 25
        self.ratio = 0.9
        self.board_color = "#CDBA96"
        self.header_bg = "#CDC0B0"
        self.btn_font = ("黑体", 12, "bold")
        self.step = self.mesh / 2
        self.chess_r = self.step * self.ratio
        self.point_r = self.step * 0.2
        self.matrix = [[0 for y in range(self.column)] for x in range(self.row)]
        self.is_start = False
        self.is_black = True
        self.last_p = None

        self.root = Tk()
        self.root.title("Gobang By Young")
        self.root.resizable(width=False, height=False)

        self.f_header = Frame(self.root, highlightthickness=0, bg=self.header_bg)
        self.f_header.pack(fill=BOTH, ipadx=10)

        self.b_start = Button(self.f_header, text="开始", command=self.bf_start, font=self.btn_font)
        self.b_restart = Button(self.f_header, text="重来", command=self.bf_restart, state=DISABLED, font=self.btn_font)
        self.l_info = Label(self.f_header, text="未开始", bg=self.header_bg, font=("楷体", 18, "bold"), fg="white")
        self.b_regret = Button(self.f_header, text="悔棋", command=self.bf_regret, state=DISABLED, font=self.btn_font)
        self.b_lose = Button(self.f_header, text="认输", command=self.bf_lose, state=DISABLED, font=self.btn_font)

        self.b_start.pack(side=LEFT, padx=20)
        self.b_restart.pack(side=LEFT)
        self.l_info.pack(side=LEFT, expand=YES, fill=BOTH, pady=10)
        self.b_lose.pack(side=RIGHT, padx=20)
        self.b_regret.pack(side=RIGHT)

        self.c_chess = Canvas(self.root, bg=self.board_color, width=(self.column + 1) * self.mesh,
                              height=(self.row + 1) * self.mesh, highlightthickness=0)
        self.draw_board()
        self.c_chess.bind("<Button-1>", self.cf_board)
        self.c_chess.pack()

        self.root.mainloop()

    def printBoard(self, a):
        theWinner = self.bw(a)
        if theWinner == "black win" or theWinner == "white win":
            print("----------------------")
            print("                      ")
            print("    ", theWinner)
            print("                      ")
            print("----------------------")
            return -1
        elif a != 1:
            self.clean()
        print("   1      3      5      7      9     11     13     15")
        for i in range(size):
            if i < 9:
                print(i + 1, end=" ")
            else:
                print(i + 1, end="")
            for j in range(size):
                if mainList[i][j] == 255:
                    print("\033[0;35;45m ◙ \033[0m", end="")
                if mainList[i][j] == 128:
                    print("\033[0;30;40m ⊡ \033[0m", end="")
                elif mainList[i][j] == 1:
                    print(" ◌ ", end="")
            print("\n")
        return a

    def bw(self, a):
        if a != 1:
            testWinner = self.testWin()
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
                return ""  # 【返回1.2】

    def clean(self):
        for i in range(size):
            print()

    @property
    def testWin(self):
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
                    print(end="")
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
                                if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                    i += 1
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                        if self.mainList[i][j] == 128:
                                            return "white win"
                                        if self.mainList[i][j] == 255:
                                            return "black win"
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
                                            return "white win"
                                        if self.mainList[i][j] == 255:
                                            return "black win"
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
                                            return "white win"
                                        if mainList[i][j] == 255:
                                            return "black win"
                except BaseException:
                    print(end="")
        return ""


a = 1
size = 15
mainList = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        mainList[i][j] = 1
while True:
    a = Chess.printBoard(a)
    if a == -1:
        break
    a += 1

