
#!/usr/bin/python2.7

from game import TicTacToe
from intelligence import MinMaxAI

play = "Y"
while True:
    use_ai = False
    while True:
        num_players = raw_input("How many players (1/2)? ")
        if num_players == "1" or num_players == "2":
            if num_players == "1":
                use_ai = True
            break
        else:
            print "Invalid input."

    g = TicTacToe()
    g.print_game_instructions()
    human_turn = True

    while True:
        if human_turn:
            pos = g.get_input()
            g.make_move(pos)
            g.print_state()
        else:
            print "==========================="
            print "One moment, I'm thinking..."
            print "==========================="
            computer = MinMaxAI(g.get_player())
            pos = computer.get_move(g)
            g.make_move(pos)
            print "==========================="
            print "AI plays position: " + str(pos)
            print "==========================="
            g.print_state()

        if g.has_winner():
            g.print_win_msg()
            break
        elif g.is_draw():
            g.print_draw_msg()
            break

        g.inc_move_count()
        if use_ai is True:
            human_turn = not human_turn

    while True:
        play = raw_input("Would you like to play again (Y/N)? ")
        play = play.strip().upper()
        if play == "Y" or play == "N":
            break
        else:
            print "Invalid input."

    if play == "N":
        break
