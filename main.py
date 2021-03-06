
#!/usr/bin/python2.7

from random import randrange
from game import TicTacToe
from intelligence import MinMaxAI

def pause_break():
    raw_input("Hit <enter> to continue")
    print " "

play = "Y"
while True:
    use_ai = False
    while True:
        print " "
        num_players = raw_input("How many players (1/2)? ")
        if num_players == "1" or num_players == "2":
            if num_players == "1":
                use_ai = True
            break
        else:
            print "Invalid input."

    g = TicTacToe()
    g.print_game_instructions()
    pause_break()

    first_move = True
    human_turn = True

    if use_ai:
        if randrange(2) % 2 == 0:
            human_turn = False

        if human_turn:
            print "Human is Player 1 (X)."
            print "AI is Player 2 (O)"
        else:
            print "AI is Player 1  (X)"
            print "Human is Player 2 (O)."

    pause_break()

    while True:
        if human_turn:
            pos = g.get_input()
            g.make_move(pos)
            g.print_state()
        else:
            print "==========================="
            print "One moment, I'm thinking..."
            print "==========================="

            if (first_move):
                pos = randrange(9) + 1
            else:
                computer = MinMaxAI(g.get_player())
                pos = computer.get_move(g)

            g.make_move(pos)
            print "==========================="
            print "AI plays position: " + str(pos)
            print "==========================="
            pause_break()
            g.print_state()

        if g.has_winner():
            g.print_win_msg()
            break
        elif g.is_draw():
            g.print_draw_msg()
            break

        g.inc_move_count()
        first_move = False
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


