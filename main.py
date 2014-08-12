
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

    if g.is_game_over():
        g.print_result(player)
        break
    else:
        g.print_state()


