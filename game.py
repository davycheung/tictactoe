
#!/usr/bin/python2.7

from board import Board

class TicTacToe(object):

    def __init__(self):
        self.instruction_b = Board(3,3)
        self.gameboard = Board(3, 3)
        self.players = ["X", "O"]

        for i in range(10, 0, -1):
            self.instruction_b.set_mark(i, i)

    def get_input(self, player):
        while True:
            try:
                pos = raw_input("Where would you like to place " + player + " (1-9)? ")
                pos = int(pos)
                if pos >= 1 and pos <= 9:
                    break
                else:
                    self.print_input_error()
            except ValueError:
                self.print_input_error()
        return pos

    def make_move(self, pos, val):
        self.gameboard.set_mark(pos, val)

    def get_player(self, i):
        return self.players[i]

    def is_game_over(self):
        game_over = False
        win_list = self.get_winning_pos()
        for item in win_list:
            game_over = self.gameboard.are_marks_equal(*item)
            if game_over:
                break
        return game_over

    @staticmethod
    def get_winning_pos():
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

    @staticmethod
    def print_input_error():
        print "Invalid input. Please try again."

    def print_game_instructions(self):
        print " "
        print "Input your choices using the below grid:"
        self.instruction_b.print_board()
        print " "

    def print_state(self):
        self.gameboard.print_board()

    def print_result(self, player):
        print " "
        self.gameboard.print_board()
        print " "
        print "Player " + player + " has won!"
        print " "
