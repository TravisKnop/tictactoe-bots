team = input()
first_row = input()
second_row = input()
third_row = input()

import random
import sys
def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)


class Board:

    def __init__(self, team, first_row, second_row, third_row):
        self.team = team
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row
        self.board = [self.first_row, self.second_row, self.third_row]
        self.A1 = self.board[0][0]
        self.B1 = self.board[0][1]
        self.C1 = self.board[0][2]
        self.A2 = self.board[1][0]
        self.B2 = self.board[1][1]
        self.C2 = self.board[1][2]
        self.A3 = self.board[2][0]
        self.B3 = self.board[2][1]
        self.C3 = self.board[2][2]
        self.all_spaces = [self.A1, self.B1, self.C1, self.A2, self.B2, self.C2, self.A3, self.B3, self.C3]
        self.corners = [self.A1, self.C1, self.A3, self.C3]
        self.edges = [self.B1, self.A2, self.C2, self.B3]
        self.center = [self.B2]
        self.winning_sets = [[self.A1, self.B1, self.C1],
                             [self.A2, self.B2, self.C2],
                             [self.A3, self.B3, self.C3],
                             [self.A1, self.A2, self.A3],
                             [self.B1, self.B2, self.B3],
                             [self.C1, self.C2, self.C3],
                             [self.A1, self.B2, self.C3],
                             [self.C1, self.B2, self.A3]]

    def locateX(self):
        self.X_spaces = []
        for a, b in enumerate(self.all_spaces):
            if b == "X":
                self.X_spaces.append(a)
        return self.X_spaces

    def locateO(self):
        self.O_spaces = []
        for a, b in enumerate(self.all_spaces):
            if b == "O":
                self.O_spaces.append(a)
        return self.O_spaces

    def locate_(self):
        self._spaces = []
        for a, b in enumerate(self.all_spaces):
            if b == "_":
                self._spaces.append(a)
        return self._spaces

    def spaces_taken(self):
        return len(self.locateX()) + len(self.locateO())



class FirstTurn(Board):
    def play(self):
        if Board.spaces_taken(self) == 0:
            print("{} {}".format(1, 1))


class SecondTurn(Board):
    def play(self):
        if Board.spaces_taken(self) == 1:
            if Board.locateX(self) != [4]:
                print("1 1")
            else:
                print("2 0")


class ThirdTurn(Board):
    def play(self):
        if Board.spaces_taken(self) == 2:
            if Board.locateO(self) == [1]:
                print("2 0")
            if Board.locateO(self) == [2]:
                print("2 0")
            if Board.locateO(self) == [5]:
                print("2 0")
            elif Board.locateO(self) == [3]:
                print("0 2")
            elif Board.locateO(self) == [6]:
                print("0 2")
            elif Board.locateO(self) == [7]:
                print("0 2")
            elif Board.locateO(self) == [0]:
                print("2 2")
            elif Board.locateO(self) == [8]:
                print("0 0")


class FourthTurn(Board):
    def play(self):
        if Board.spaces_taken(self) == 3:
             if Board.locateO(self) == [6]:
                    if Board.locateX(self) == [4, 8]:
                        print("0 0")
                    elif Board.locateX(self) == [4, 7]:
                        print("0 1")
                    elif Board.locateX(self) == [4, 5]:
                        print("1 0")
                    elif Board.locateX(self) == [3, 4]:
                        print("1 2")
                    elif Board.locateX(self) == [2, 4]:
                        print("2 1")
                    elif Board.locateX(self) == [1, 4]:
                        print("2 1")
                    elif Board.locateX(self) == [0, 4]:
                        print("2 2")


class SeventhTurn(Board):
    def play(self):
        if Board.spaces_taken(self) >= 4:
            x = random.choice(Board.locate_(self))
            if x == 0:
                print("0 0")
            elif x == 1:
                print("0 1")
            elif x == 2:
                print("0 2")
            elif x == 3:
                print("1 0")
            elif x == 5:
                print("1 2")
            elif x == 6:
                print("2 0")
            elif x == 7:
                print("2 1")
            elif x == 8:
                print("2 2")



a = Board(team, first_row, second_row, third_row)
b = FirstTurn(team, first_row, second_row, third_row)
c = SecondTurn(team, first_row, second_row, third_row)
d = ThirdTurn(team, first_row, second_row, third_row)
e = FourthTurn(team, first_row, second_row, third_row)
f = SeventhTurn(team, first_row, second_row, third_row)
a
b.play()
c.play()
d.play()
e.play()
f.play()
