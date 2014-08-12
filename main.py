
#!/usr/bin/python2.7

from game import TicTacToe

g = TicTacToe()
g.print_game_instructions()

while True:
    pos = g.get_input()
    g.make_move(pos)

    if g.has_winner():
        g.print_state()
        g.print_win()
        break
    elif g.is_draw():
        g.print_state()
        g.print_draw()
        break
    else:
        g.print_state()
    
    g.inc_move_count()


