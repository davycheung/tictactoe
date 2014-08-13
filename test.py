
#!/usr/bin/python2.7

from board import Board
from game import TicTacToe
from game import MinMaxAI

g = TicTacToe()
g.print_game_instructions()

while True:
    if g.get_player() == "O":
        ai = MinMaxAI(g.get_player())
        print ai.get_move(g)

    pos = g.get_input()
    g.make_move(pos)
    g.print_state()
    g.inc_move_count()