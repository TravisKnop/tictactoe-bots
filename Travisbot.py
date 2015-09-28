import sys
import itertools
import collections

def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)


class Board:
    def __init__(self, team=input(), first_row=input(), second_row=input(), third_row=input()):
        self.team = team
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row
        self.all_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def get_board(self):
        self.stringer = str(self.first_row) + str(self.second_row) + str(self.third_row)
        self.board = list(self.first_row + self.second_row + self.third_row)
        return self.board

    def locateX(self):
        self.X_spaces = []
        for key, value in enumerate(self.board):
            if value == "X":
                self.X_spaces.append(key)
        return self.X_spaces

    def locateO(self):
        self.O_spaces = []
        for key, value in enumerate(self.board):
            if value == "O":
                self.O_spaces.append(key)
        return self.O_spaces

    def offlimitsX(self):
        return [x for x in self.all_spaces if x not in self.locateO()]

    def offlimitsO(self):
        return [x for x in self.all_spaces if x not in self.locateX()]

    def spaces_taken(self):
        return len(self.locateX()) + len(self.locateO())

    def remaining_spaces(self):
        return [x for x in self.all_spaces if x not in self.locateO() or self.locateX()]

#def possible_winsX(self):
#""" for b in all_spaces:
#        for a in winning_sets:
#            return {x:b.count(x) for x in all_spaces}"""
#    pass
#debug_print(X_spaces(board))
#debug_print(Board())
#debug_print(remaining_spaces(board))
#debug_print(remaining_spaces(board))
#debug_print(len(X_spaces(board)) + len(O_spaces(board)))
#debug_print(offlimitsO(board))
#debug_print(possible_winsX(board))
#print("{} {}".format(2, 1))


class FirstTurn(Board):

    def turn(self, spaces_taken):
        if Board.spaces_taken == 0:
            return "{} {}".format(1, 1)
        else:
            pass

class SecondTurn(Board):
    def __init__(self, spaces_taken=1):
        self.spaces_taken = spaces_taken

    def locate(self):
        self.O_spaces = []
        for key, value in enumerate(self):
            if value == "X":
                self.O_spaces.append(key)
        debug_print(self.O_spaces)
        return self.O_spaces

    def first_choice(self, O_spaces):
        if self.O_spaces != 4:
            print("{} {}".format(1, 1))
        else:
            print("{} {}".format(2, 2))

x = FirstTurn(Board("X"))
x.turn()
#print(SecondTurn(Board()))
