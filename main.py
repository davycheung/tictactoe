
#!/usr/bin/python2.7

from game import TicTacToe

g = TicTacToe()
g.print_game_instructions()

i = 0
while True:
    player = g.get_player(i)
    i += 1

    pos = raw_input("Where would you like to place " + player + " (1-9)? ")
    pos = int(pos)
    g.make_move(pos, player)
    if g.is_game_over():
        g.print_result(player)

print g.print_result()

