
#!/usr/bin/python2.7

from board import Board
from game import TicTacToe
from game import GameAI

#g = TicTacToe()
#g.gameboard.set_mark(1, "X")
#g.gameboard.set_mark(2, "X")
#g.gameboard.set_mark(3, "O")
#g.gameboard.set_mark(4, "O")
#g.gameboard.set_mark(5, "O")
#g.gameboard.set_mark(9, "X")

#g.gameboard.print_board()

#ai = GameAI(g.get_player())
#ai.get_next_move(g)
#print ai.get_choice()

#g.gameboard.print_board()
#print g.get_game_copy().gameboard.get_available_pos()

#ai = GameAI(g)
#ai.get_next_move()


g = TicTacToe()
g.print_game_instructions()

while True:
    if g.get_player() == "O":
        ai = GameAI(g.get_player())
        ai.get_next_move(g)
        print ai.get_choice()

    pos = g.get_input()
    g.make_move(pos)
    g.print_state()

    
    g.inc_move_count()


