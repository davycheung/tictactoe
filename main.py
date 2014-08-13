
#!/usr/bin/python2.7

from game import TicTacToe

play = "Y"
while True:
    g = TicTacToe()
    g.print_game_instructions()

    while True:
        pos = g.get_input()
        g.make_move(pos)

        if g.has_winner():
            g.print_state()
            g.print_win_msg()
            break
        elif g.is_draw():
            g.print_state()
            g.print_draw_msg()
            break
        else:
            g.print_state()

        g.inc_move_count()

    while True:
        play = raw_input("Would you like to play again (Y/N)? ")
        play = play.strip().upper()
        if play == "Y" or play == "N":
            break

    if play == "N":
        break
