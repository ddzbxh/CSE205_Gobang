# -*- coding = utf-8 -*-

import numpy as np
import time
import os
import random

class Chess:

    @staticmethod
    def getTime():
        return str(time.time())

    def __init__(self):
        self.a = 1
        self.b = 1
        self.c = 1
        self.x = 7
        self.y = 7
        self.theTime = self.getTime()
        self.syn = open("data0.syn", "w", encoding='utf-8')
        self.syn.close()
        self.data = open("data1.syn", "w", encoding='utf-8')
        self.data.close()
        self.data1 = open("data2.syn", "w", encoding='utf-8')
        self.data1.close()
        self.size = 15
        self.mainList = np.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                self.mainList[i][j] = 1
        self.winner = ""
        self.space = " "
        self.term = 2
        self.checkHelp = True
        self.PBMode = True
        self.language = 1
        self.XLine = 2
        self.YLine = 2
        self.InpStr = ","
        self.InpMod = 1
        self.InpTerm = 1
        self.askLanguage()
        self.direction()
        self.main()

    def writeListA(self):
        self.data = open("data1.syn", "w", encoding='utf-8')
        self.data.write("")
        self.data.close()
        self.data = open("data1.syn", "a", encoding='utf-8')
        for i in range(self.size):
            for j in range(self.size):
                self.data.write(str(int(self.mainList[i][j]))+"\n")
        self.data.close()

    def readListA(self):
        readList = []
        self.data = open("data1.syn", "r", encoding='utf-8')
        for i in self.data.readlines():
            i = i.strip("\n")
            readList.append(i)
        self.data.close()
        x = self.size
        for i in range(x):
            for j in range(x):
                self.mainList[i][j] = readList[(i*x+j)]

    def writeListB(self):
        self.data = open("data2.syn", "w", encoding='utf-8')
        self.data.write("")
        self.data.close()
        self.data = open("data2.syn", "a", encoding='utf-8')
        for i in range(self.size):
            for j in range(self.size):
                self.data.write(str(int(self.mainList[i][j]))+"\n")
        self.data.close()

    def readListB(self):
        readList = []
        self.data = open("data2.syn", "r", encoding='utf-8')
        for i in self.data.readlines():
            i = i.strip("\n")
            readList.append(i)
        self.data.close()
        x = self.size
        for i in range(x):
            for j in range(x):
                self.mainList[i][j] = readList[(i*x+j)]

    def saveFile(self):
        a = open("data0.syn", "r", encoding="ISO-8859-1")
        b = a.readlines()
        c = []
        for i in range(self.size+2, len(b)):
            c.append(b[i])
        a.close()
        d = open(self.getTime()+".txt", "w", encoding='utf-8')
        for i in c:
            d.write(i)
        d.close()
        print(os.path.dirname(os.path.abspath(__file__)))

    def main(self):
        while True:
            if self.language == 1:
                inp = input("A.双人模式\nB.人机模式\n>>>")
            else:
                inp = input("A.PVP\nB.BOT\n>>>")
            if inp == "A" or inp == "a":
                self.mainPVP()
                return True
            elif inp == "B" or inp == "b":
                self.mainBOT()
                return True
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def mainS(self):
        self.checkHelp = True
        self.mainList = np.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                self.mainList[i][j] = 1
        self.winner = ""
        self.space = " "
        self.term = 2
        while True:
            if self.language == 1:
                inp = input("A.双人模式\nB.人机模式\n>>>")
            else:
                inp = input("A.PVP\nB.BOT\n>>>")
            if inp == "A" or inp == "a":
                self.mainPVP()
                return True
            elif inp == "B" or inp == "b":
                self.mainBOT()
                return True
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def mainPVP(self):
        while self.term != -1:
            self.testWin()
            if self.winner == "black win" or self.winner == "white win":
                self.printTheWinner()
                self.syn = open("data0.syn", "w", encoding='utf-8')
                self.syn.write("")
                self.syn.close()
            else:
                if self.XLine == 1:
                    self.printXNums()
                    self.printBoard()
                else:
                    self.printBoard()
                    self.printXNums()
                if self.term % 2 == 1:
                    self.writeListA()
                else:
                    self.writeListB()
                self.playOneStep()
                if self.checkHelp:
                    self.term += 1
                    if not self.PBMode:
                        print("\n"*self.size*2)
                    else:
                        print("-"*60)
                else:
                    self.askHelp()

    def mainBOT(self):
        while self.term != -1:
            self.testWin()
            if self.winner == "black win" or self.winner == "white win":
                self.printTheWinner()
                self.syn = open("data0.syn", "w", encoding='utf-8')
                self.syn.write("-"*self.size + "\n" + self.winner)
                self.syn.close()
            else:
                if self.XLine == 1:
                    self.printXNums()
                    self.printBoard()
                else:
                    self.printBoard()
                    self.printXNums()
                if self.term % 2 == 1:
                    self.writeListA()
                else:
                    self.writeListB()
                self.BOT()
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
        if self.YLine == 1:
            for i in range(self.size):
                if i < 9:
                    print(i + 1, end=" ")
                else:
                    print(i + 1, end="")
                for j in range(self.size):
                    print(self.space, end="")
                    self.syn = open("data0.syn", "a", encoding='utf-8')
                    self.syn.write(" ")
                    self.syn.close()
                    if self.mainList[i][j] == 255:
                        print("\033[0;35;45m◙\033[0m", end="")
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("W")
                        self.syn.close()
                    if self.mainList[i][j] == 128:
                        print("\033[0;30;40m⊡\033[0m", end="")
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("M")
                        self.syn.close()
                    elif self.mainList[i][j] == 1:
                        print("◌", end="")
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("  ")
                        self.syn.close()
                    print(self.space, end="")
                    self.syn = open("data0.syn", "a", encoding='utf-8')
                    self.syn.write(" ")
                    self.syn.close()
                print("\n")
                self.syn = open("data0.syn", "a", encoding='utf-8')
                self.syn.write("\n")
                self.syn.close()
            self.syn = open("data0.syn", "a", encoding='utf-8')
            self.syn.write("\n"+"-"*60+"\n")
            self.syn.close()
        else:
            for i in range(self.size - 1, -1, -1):
                if i < 9:
                    print(i + 1, end=" ")
                else:
                    print(i + 1, end="")
                for j in range(self.size):
                    print(self.space, end="")
                    self.syn = open("data0.syn", "a", encoding='utf-8')
                    self.syn.write(" ")
                    self.syn.close()
                    if self.mainList[i][j] == 255:
                        print("\033[0;35;45m◙\033[0m", end="")
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("W")
                        self.syn.close()
                    if self.mainList[i][j] == 128:
                        print("\033[0;30;40m⊡\033[0m", end="")
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("M")
                        self.syn.close()
                    elif self.mainList[i][j] == 1:
                        print("◌", end="")
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("  ")
                        self.syn.close()
                    print(self.space, end="")
                    self.syn = open("data0.syn", "a", encoding='utf-8')
                    self.syn.write(" ")
                    self.syn.close()
                print("\n")
                self.syn = open("data0.syn", "a", encoding='utf-8')
                self.syn.write("\n")
                self.syn.close()
            self.syn = open("data0.syn", "a", encoding='utf-8')
            self.syn.write("\n"+"-"*60+"\n")
            self.syn.close()

    def printTheWinner(self):
        if self.winner == "black win" or self.winner == "white win":
            self.printXNums()
            self.printBoard()
            print("-" * 30, "\n", "*" * 30, sep="")
            print(" " * 10, self.winner, "\n", "*" * 30, sep="")
            print("-" * 30)
            self.syn = open("data0.syn", "a", encoding='utf-8')
            self.syn.write("-" * 30+"\n"+"*" * 30+"\n"+" " * 10+self.winner+"\n"+"*" * 30+"-" * 30)
            self.syn.close()
            self.askWin()

    def playOneStep(self):
        while True:
            if self.term % 2 == 0:
                if self.InpMod == 1:
                    if self.language == 1:
                        xy = input('【黑棋】x,y:')
                    else:
                        xy = input('[black]x,y:')
                else:
                    if self.language == 1:
                        x = input('【黑棋】\nx:')
                        y = input('y:')
                        xy = x + self.InpStr + y
                    else:
                        x = input('[black]\nx:')
                        y = input('y:')
                        xy = x + self.InpStr + y
            else:
                if self.InpMod == 1:
                    if self.language == 1:
                        xy = input('【白棋】x,y:')
                    else:
                        xy = input('[white]x,y:')
                else:
                    if self.language == 1:
                        x = input('【白棋】\nx:')
                        y = input('y:')
                        xy = x + self.InpStr + y
                    else:
                        x = input('[white]\nx:')
                        y = input('y:')
                        xy = x + self.InpStr + y
            try:
                if self.InpTerm == 1:
                    y, x = xy.split(self.InpStr)
                else:
                    x, y = xy.split(self.InpStr)
                x = int(x) - 1
                y = int(y) - 1
            except BaseException:
                a = "help" in xy
                b = "?" in xy
                c = "？" in xy
                d = "Help" in xy
                e = "what" in xy
                if a or b or c or d or e:
                    self.checkHelp = False
                    break
                if self.language == 1:
                    print("<无法识别的输入，重试或输入“help”寻求帮助>")
                elif self.language == 2:
                    print("<input error, try again, or type 'help'>")
            else:
                try:
                    if self.mainList[x][y] != 1:
                        if self.language == 1:
                            print("<此处已经落子，重试或输入“help”寻求帮助>")
                        elif self.language == 2:
                            print("<input overlap, try again, or type 'help'>")
                    else:
                        if self.term % 2 == 0:
                            self.mainList[x][y] = 255
                            self.syn = open("data0.syn", "a", encoding='utf-8')
                            self.syn.write("[black]x,y:" + xy + "\n")
                            self.syn.close()
                        else:
                            self.mainList[x][y] = 128
                            self.syn = open("data0.syn", "a", encoding='utf-8')
                            self.syn.write("[white]x,y:" + xy + "\n")
                            self.syn.close()
                        break
                except BaseException:
                    if self.language == 1:
                        print("<输入需在坐标范围内，重试或输入“help”寻求帮助>")
                    elif self.language == 2:
                        print("<input should be within the range of coordinates, try again, or type 'help'>")

    def BOT(self):
        if self.term % 2 == 0:
            while True:
                for i in range(self.size):
                    for j in range(self.size):
                        try:
                            if self.mainList[i][j] == 128:
                                if self.mainList[i][j + 1] == 128:
                                    if self.mainList[i][j + 2] == 128:
                                        if self.mainList[i][j + 3] == 1 and self.c == 1:
                                            self.mainList[i][j + 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i][j - 1] == 1 and self.c == 1:
                                            self.mainList[i][j - 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 128:
                                if self.mainList[i + 1][j] == 128:
                                    if self.mainList[i + 2][j] == 128:
                                        if self.mainList[i + 3][j] == 1 and self.c == 1:
                                            self.mainList[i + 3][j] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i - 1][j] == 1 and self.c == 1:
                                            self.mainList[i - 1][j] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 128:
                                if self.mainList[i + 1][j + 1] == 128:
                                    if self.mainList[i + 2][j + 2] == 128:
                                        if self.mainList[i + 3][j + 3] == 1 and self.c == 1:
                                            self.mainList[i + 3][j + 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i - 1][j - 1] == 1 and self.c == 1:
                                            self.mainList[i - 1][j - 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 128:
                                if self.mainList[i + 1][j - 1] == 128:
                                    if self.mainList[i + 2][j - 2] == 128:
                                        if self.mainList[i + 3][j - 3] == 1 and self.c == 1:
                                            self.mainList[i + 3][j - 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i - 1][j + 1] == 1 and self.c == 1:
                                            self.mainList[i - 1][j + 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 128:
                                if self.mainList[i - 1][j + 1] == 128:
                                    if self.mainList[i - 2][j + 2] == 128:
                                        if self.mainList[i - 3][j + 3] == 1 and self.c == 1:
                                            self.mainList[i - 3][j + 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i + 1][j - 1] == 1 and self.c == 1:
                                            self.mainList[i + 1][j - 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 128:
                                if self.mainList[i - 1][j - 1] == 128:
                                    if self.mainList[i - 2][j - 2] == 128:
                                        if self.mainList[i - 3][j - 3] == 1 and self.c == 1:
                                            self.mainList[i - 3][j - 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i + 1][j + 1] == 1 and self.c == 1:
                                            self.mainList[i + 1][j + 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 255:
                                if self.mainList[i][j + 1] == 255:
                                    if self.mainList[i][j + 2] == 255:
                                        if self.mainList[i][j + 3] == 1 and self.c == 1:
                                            self.mainList[i][j + 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i][j - 1] == 1 and self.c == 1:
                                            self.mainList[i][j - 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 255:
                                if self.mainList[i + 1][j] == 255:
                                    if self.mainList[i + 2][j] == 255:
                                        if self.mainList[i + 3][j] == 1 and self.c == 1:
                                            self.mainList[i + 3][j] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i - 1][j] == 1 and self.c == 1:
                                            self.mainList[i - 1][j] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 255:
                                if self.mainList[i + 1][j + 1] == 255:
                                    if self.mainList[i + 2][j + 2] == 255:
                                        if self.mainList[i + 3][j + 3] == 1 and self.c == 1:
                                            self.mainList[i + 3][j + 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i - 1][j - 1] == 1 and self.c == 1:
                                            self.mainList[i - 1][j - 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 255:
                                if self.mainList[i + 1][j - 1] == 255:
                                    if self.mainList[i + 2][j - 2] == 255:
                                        if self.mainList[i + 3][j - 3] == 1 and self.c == 1:
                                            self.mainList[i + 3][j - 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i - 1][j + 1] == 1 and self.c == 1:
                                            self.mainList[i - 1][j + 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 255:
                                if self.mainList[i - 1][j + 1] == 255:
                                    if self.mainList[i - 2][j + 2] == 255:
                                        if self.mainList[i - 3][j + 3] == 1 and self.c == 1:
                                            self.mainList[i - 3][j + 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i + 1][j - 1] == 1 and self.c == 1:
                                            self.mainList[i + 1][j - 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                        try:
                            if self.mainList[i][j] == 255:
                                if self.mainList[i - 1][j - 1] == 255:
                                    if self.mainList[i - 2][j - 2] == 255:
                                        if self.mainList[i - 3][j - 3] == 1 and self.c == 1:
                                            self.mainList[i - 3][j - 3] = 255
                                            self.c = 0
                                            break
                                        elif self.mainList[i + 1][j + 1] == 1 and self.c == 1:
                                            self.mainList[i + 1][j + 1] = 255
                                            self.c = 0
                                            break
                        except BaseException:
                            print(end="")
                break

        if self.term % 2 == 0 and self.c == 1:
            while True:
                try:
                    a = self.a
                    if a > 75:
                        if self.mainList[self.x][self.y] != 1:
                            self.x += 1
                            self.y += 1
                            self.b += 1
                    elif a > 50:
                        if self.mainList[self.x][self.y] != 1:
                            self.x -= 1
                            self.y -= 1
                            self.b += 1
                    elif a > 25:
                        if self.mainList[self.x][self.y] != 1:
                            self.x += 1
                            self.y -= 1
                            self.b += 1
                    else:
                        if self.mainList[self.x][self.y] != 1:
                            self.x -= 1
                            self.y += 1
                            self.b += 1
                except BaseException:
                    if self.b % 3 != 0:
                        self.x = random.randint(3, 13)
                        self.y = random.randint(3, 13)
                        self.a = random.randint(0, 100)
                try:
                    if self.mainList[self.x][self.y] == 1:
                        self.mainList[self.x][self.y] = 255
                        self.syn = open("data0.syn", "a", encoding='utf-8')
                        self.syn.write("[black]x,y:" + str(self.x + 1) + "," + str(self.y + 1) + "\n")
                        self.syn.close()
                        break
                    else:
                        self.x = random.randint(3, 13)
                        self.y = random.randint(3, 13)
                        self.a = random.randint(0, 100)
                except BaseException:
                    self.x = random.randint(3, 13)
                    self.y = random.randint(3, 13)
                    self.a = random.randint(0, 100)

        if self.c == 0:
            self.c = 1

        if self.term % 2 == 1:
            while True:
                if self.InpMod == 1:
                    if self.language == 1:
                        xy = input('【白棋】x,y:')
                    else:
                        xy = input('[white]x,y:')
                else:
                    if self.language == 1:
                        x = input('【白棋】\nx:')
                        y = input('y:')
                        xy = x + self.InpStr + y
                    else:
                        x = input('[white]\nx:')
                        y = input('y:')
                        xy = x + self.InpStr + y
                try:
                    if self.InpTerm == 1:
                        y, x = xy.split(self.InpStr)
                    else:
                        x, y = xy.split(self.InpStr)
                    x = int(x) - 1
                    y = int(y) - 1
                except BaseException:
                    a = "help" in xy
                    b = "?" in xy
                    c = "？" in xy
                    d = "Help" in xy
                    e = "what" in xy
                    if a or b or c or d or e:
                        self.checkHelp = False
                        break
                    if self.language == 1:
                        print("<无法识别的输入，重试或输入“help”寻求帮助>")
                    elif self.language == 2:
                        print("<input error, try again, or type 'help'>")
                else:
                    try:
                        if self.mainList[x][y] != 1:
                            if self.language == 1:
                                print("<此处已经落子，重试或输入“help”寻求帮助>")
                            elif self.language == 2:
                                print("<input overlap, try again, or type 'help'>")
                        else:
                            self.mainList[x][y] = 128
                            self.syn = open("data0.syn", "a", encoding='utf-8')
                            self.syn.write("[white]x,y:" + xy + "\n")
                            self.syn.close()
                            break
                    except BaseException:
                        if self.language == 1:
                            print("<输入需在坐标范围内，重试或输入“help”寻求帮助>")
                        elif self.language == 2:
                            print("<input should be within the range of coordinates, try again, or type 'help'>")

    def testWin(self):
        for i in range(self.size):
            for j in range(self.size):
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i][j + 1]:
                            j += 1
                            if self.mainList[i][j] == self.mainList[i][j + 1]:
                                j += 1
                                if self.mainList[i][j] == self.mainList[i][j + 1]:
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i][j + 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i + 1][j]:
                            i += 1
                            if self.mainList[i][j] == self.mainList[i + 1][j]:
                                i += 1
                                if self.mainList[i][j] == self.mainList[i + 1][j]:
                                    i += 1
                                    if self.mainList[i][j] == self.mainList[i + 1][j]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")
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
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                            i += 1
                            j -= 1
                            if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                i += 1
                                j -= 1
                                if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                    i += 1
                                    j -= 1
                                    if self.mainList[i][j] == self.mainList[i + 1][j - 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                            i -= 1
                            j += 1
                            if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                                i -= 1
                                j += 1
                                if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                                    i -= 1
                                    j += 1
                                    if self.mainList[i][j] == self.mainList[i - 1][j + 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")
                try:
                    if self.mainList[i][j] != 1:
                        if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                            i -= 1
                            j -= 1
                            if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                                i -= 1
                                j -= 1
                                if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                                    i -= 1
                                    j -= 1
                                    if self.mainList[i][j] == self.mainList[i - 1][j - 1]:
                                        if self.mainList[i][j] == 128:
                                            self.winner = "white win"
                                        if self.mainList[i][j] == 255:
                                            self.winner = "black win"
                except BaseException:
                    print(end="")

    def askWin(self):
        while True:
            if self.language == 1:
                inp = input("A.直接重新开始\nB.保存棋谱并重新开始\nC.退出\nD.保存棋谱并退出\n>>>")
            else:
                inp = input('A.Restart\nB.Save chess board than Restart\nC.EXIT\nD.Save chess board than EXIT\n>>>')
            if inp == "A" or inp == "a":
                self.mainList = np.zeros((self.size, self.size))
                for i in range(self.size):
                    for j in range(self.size):
                        self.mainList[i][j] = 1
                self.winner = ""
                self.space = " "
                self.term = 1
                break
            elif inp == "B" or inp == "b":
                self.saveFile()
                self.mainList = np.zeros((self.size, self.size))
                for i in range(self.size):
                    for j in range(self.size):
                        self.mainList[i][j] = 1
                self.winner = ""
                self.space = " "
                self.term = 1
                break
            elif inp == "C" or inp == "c":
                self.term = -1
                break
            elif inp == "D" or inp == "d":
                self.saveFile()
                self.term = -1
                break
            else:
                print("Please give your choose by letter as A, B, etc.\n请输入选项以选择，如大写A、B等")
        if not self.PBMode:
            print("\n" * self.size * 2)
        else:
            print("-" * 60)

    def askHelp(self):
        while not self.checkHelp:
            print("-" * 30)
            while True:
                if self.language == 1:
                    inp = input("A.游戏\nB.界面参数\nC.切换输入方式\nD.保存棋谱\nE.Language\nF.退出\nG.返回\n>>>")
                else:
                    inp = input('A.About game\nB.Change parameter\nC.Change input function\nD.Save chess board\nE.调整语言\nF.EXIT\nG.Back\n>>>')
                check = False
                if inp == "A" or inp == "a":
                    check = self.askGame()
                elif inp == "B" or inp == "b":
                    check = self.askPara()
                elif inp == "C" or inp == "c":
                    check = self.askInpFunction()
                elif inp == "D" or inp == "d":
                    self.saveFile()
                    check = True
                elif inp == "E" or inp == "e":
                    self.askLanguage()
                    check = True
                elif inp == "F" or inp == "f":
                    self.term = -1
                    check = True
                elif inp == "G" or inp == "g":
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

    def askInpFunction(self):
        while True:
            if self.language == 1:
                inp = input("*注：分隔符默认为英文逗号\nA.单行分隔符模式\nB.换行输入模式\nC.XY反转\nD.返回上级\n>>>")
            else:
                inp = input("*PS:The delimiter defaults to English comma\nA.Single-line delimiter mode\nB.Line feed input mode\nC.XY inversion\nD.Back\n>>>")
            if inp == "A" or inp == "a":
                self.InpMod = 1
                if self.language == 1:
                    self.InpStr = input("输入分隔符号：")
                else:
                    self.InpStr = input("Enter the separator:")
                return True
            elif inp == "B" or inp == "b":
                self.InpMod = 2
                return True
            elif inp == "C" or inp == "c":
                if self.InpTerm == 1:
                    self.InpTerm = 2
                else:
                    self.InpTerm = 1
                return True
            elif inp == "D" or inp == "d":
                return False
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def askGame(self):
        while True:
            if self.language == 1:
                inp = input("A.重新开始\nB.悔棋\nC.切换模式\nD.返回上级\n>>>")
            else:
                inp = input("A.Restart\nB.Retract a False Move\nC.Switch game mode\nD.Back\n>>>")
            if inp == "A" or inp == "a":
                self.mainList = np.zeros((self.size, self.size))
                for i in range(self.size):
                    for j in range(self.size):
                        self.mainList[i][j] = 1
                self.winner = ""
                self.space = " "
                self.term = 1
                self.syn = open("data0.syn", "w")
                self.syn.write("")
                self.syn.close()
                return True
            elif inp == "B" or inp == "b":
                if self.term % 2 != 1:
                    self.readListA()
                else:
                    self.readListB()
                self.term -= 1
                return True
            elif inp == "C" or inp == "c":
                self.mainS()
                return True
            elif inp == "D" or inp == "d":
                return False
            else:
                if self.language == 1:
                    print("<无法识别的输入，请输入选项以选择，如大写A、B等")
                elif self.language == 2:
                    print("<input error, try again, give your choose as A, B, etc.>")

    def askPara(self):
        while True:
            if self.language == 1:
                inp = input("A.调整间隔字符\nB.棋盘刷新方式\nC.调整XY轴形式\nD.调整棋盘大小并重新开始\nE.恢复默认并重新开始\nF.返回上级\n>>>")
            else:
                inp = input("A.Change the space letter\nB.Checkerboard refresh mode\nC.Change Xy-axis mode\nD.Resize board and restart\nE.Restore default Settings and restart\nF.Back\n>>>")
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
                self.askXL()
                return True
            elif inp == "D" or inp == "d":
                if self.language == 1:
                    self.size = int(input("边长(默认15):"))
                else:
                    self.size = int(input("Side length (default 15):"))
                self.mainList = np.zeros((self.size, self.size))
                for i in range(self.size):
                    for j in range(self.size):
                        self.mainList[i][j] = 1
                self.winner = ""
                self.space = " "
                self.term = 1
                return True
            elif inp == "E" or inp == "e":
                self.XLine = 2
                self.YLine = 2
                self.size = 15
                self.space = " "
                self.PBMode = True
                self.mainList = np.zeros((self.size, self.size))
                for i in range(self.size):
                    for j in range(self.size):
                        self.mainList[i][j] = 1
                self.winner = ""
                self.space = " "
                self.term = 1
                self.syn = open("data0.syn", "w")
                self.syn.write("")
                self.syn.close()
                return True
            elif inp == "F" or inp == "f":
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

    def askXL(self):
        while True:
            if self.language == 1:
                inp = input("A.X坐标在上\nB.X坐标在下\nC.Y轴反转\n>>>")
            else:
                inp = input("A.X-axis on top\nB.X-axis down below\nC.Inversion Y-axis\n>>>")
            if inp == "A" or inp == "a":
                self.XLine = 1
                return True
            elif inp == "B" or inp == "b":
                self.XLine = 2
                return True
            elif inp == "C" or inp == "c":
                if self.YLine == 1:
                    self.YLine = 2
                else:
                    self.YLine = 1
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
                  "1.有“双人模式”和“人机”两种选择\n"
                  "2.不规范的输入将被驳回\n"
                  "3.在已经落子的棋位下棋将被驳回\n"
                  "4.当有一方胜出，将会自动结束\n"
                  "5.输入\"help\"或双语问号调整设置\n"
                  "6.选项以字母序号为反馈,不区分大小写\n"
                  "7.仅双人模式可以悔棋，且只能回溯一步\n"
                  "https://github.com/ddzbxh/CSE205_Project3\n"
                  , end="")
            print("-" * 30)
        elif self.language == 2:
            print("-" * 30)
            print("project3, Gobang\n"
                  "1. There are two choices: \"two-person mode\" and \"man-machine mode\"\n"
                  "2. Non-standard input will be rejected\n"
                  "3. Playing in a position that has been played will be rejected\n"
                  "4. When one side wins, it automatically ends\n"
                  "5. Enter \"help\" or bilingual question mark to adjust Settings\n"
                  "6. Options respond to alphabetic and are case-insensitive\n"
                  "7. The regret function is only one step back and Only two-player mode can\n"
                  "https://github.com/ddzbxh/CSE205_Project3\n"
                  , end="")
            print("-" * 30)


if __name__ == '__main__':
    Chess()
