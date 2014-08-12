
#!/usr/bin/python2.7

from board import Board

class TicTacToe(object):

    def __init__(self):
        self.instruction_b = Board(3,3)
        self.gameboard = Board(3, 3)

        for i in range(10, 1, -1):
            self.instruction_b.set_mark(i, i)

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

