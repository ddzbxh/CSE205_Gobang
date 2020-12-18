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
        self.term = 1
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
                self.term += 1
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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
                if self.mainList[i][j] == 255:
                    print("\033[0;35;45m ◙ \033[0m", end="")
                if self.mainList[i][j] == 128:
                    print("\033[0;30;40m ⊡ \033[0m", end="")
                elif self.mainList[i][j] == 1:
                    print(" ◌ ", end="")
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
        if self.term % 2 == 0:
            while True:
                try:
                    x, y = input('【黑棋】x,y:').split(",")
                    x = int(x) - 1
                    y = int(y) - 1
                except BaseException:
                    print("<input error, try again>")
                else:
                    if self.mainList[x][y] != 1:
                        print("<input overlap, try again>")
                    else:
                        self.mainList[x][y] = 255
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
                    if self.mainList[x][y] != 1:
                        print("<input overlap, try again>")
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


if __name__ == '__main__':
    Chess()





