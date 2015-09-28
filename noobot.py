team = input()
first_row = input()
second_row = input()
third_row = input()

import random

class Board:

    def __init__(self, team, first_row, second_row, third_row):
        self.board = [first_row, second_row, third_row]
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
