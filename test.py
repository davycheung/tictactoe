
#!/usr/bin/python2.7

from board import Board
from game import TicTacToe


#instruction_b = Board(3,3)
#for i in range(1, 10):
#    instruction_b.set_mark(i, i)
#
#instruction_b.print_board()




#b = Board(3,3)
#b.set_mark(1, "X")
#b.set_mark(2, "X")
#b.set_mark(3, "X")
#b.set_mark(4, "O")
#
#print b.b
#b.print_board()
#print ' '
#

g = TicTacToe()
g.gameboard.set_mark(1, "X")
g.gameboard.set_mark(2, "X")
g.gameboard.set_mark(3, "O")
g.gameboard.set_mark(4, "O")
g.gameboard.set_mark(5, "O")
g.gameboard.set_mark(9, "X")

g.gameboard.print_board()
print g.is_game_over()