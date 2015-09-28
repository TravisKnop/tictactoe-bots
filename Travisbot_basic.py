team = input()
first_row = input()
second_row = input()
third_row = input()

#print("{} {}".format(1, A))


BOARD = [
    ['A1', 'B1', 'C1'],
    ['A2', 'B2', 'C2'],
    ['A3', 'B3', 'C3'],
]

A1 = ' _'
B1 = ' _'
C1 = ' _'
A2 = ' _'
B2 = ' _'
C2 = ' _'
A3 = ' _'
B3 = ' _'
C3 = ' _'
all_spaces = [A1, A2, A3, B1, B2, B3, C1, C2, C3]

#print('   A  B  C')
#print('1  {} {} {}'.format(A1, B1, C1))
#print('2  {} {} {}'.format(A2, B2, C2))
#print('3  {} {} {}'.format(A3, B3, C3))

class Prioritize:
    def __init__(self, team=input(), first_row=input(), second_row=input(), third_row=input()):
        self.team = team
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row

    @property
    def winning_sets(self):
        self.winning_sets = [
        [A1, B1, C1],
        [A2, B2, C2],
        [A3, B3, C3],
        [A1, B2, C3],
        [A3, B2, C1],
        [A1, A2, A3],
        [B1, B2, B3],
        [C1, C2, C3],
        ]
        return self.winning_sets

    def elim_win_sets(self):
        for a in all_spaces:
            a.count()

    def check_board(self, X, O):
        BOARD.count(X)

    def 


#calculate value of each, A1 =
Prioritize
