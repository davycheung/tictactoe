
#!/usr/bin/python2.7

from board import Board

class TicTacToe(object):

    def __init__(self):
        self.instruction_b = Board(3,3)
        self.gameboard = Board(3, 3)

        for i in range(1, 10):
            instruction_b.set_mark(i, i)



