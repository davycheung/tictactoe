
#!/usr/bin/python2.7

from game import TicTacToe

g = TicTacToe()
g.print_game_instructions()

i = 0
while True:
    player = g.get_player(i % 2)
    i += 1

    pos = g.get_input(player)
    g.make_move(pos, player)

    if g.is_win():
        g.print_state()
        g.print_win(player)
        break
    elif g.is_draw():
        g.print_state()
        g.print_draw()
        break
    else:
        g.print_state()


