
from board import Board
import copy

class TicTacToe(object):

    def __init__(self):
        self.instruction_b = Board(3,3)
        self.gameboard = Board(3, 3)
        self.players = ["X", "O"]
        self.move_count = 0

        for i in range(10, 0, -1):
            self.instruction_b.set_mark(i, i)

    def inc_move_count(self):
        self.move_count += 1

    def get_available_moves(self):
        return self.gameboard.get_available_pos()

    def get_game_copy(self):
        return copy.deepcopy(self)

    def get_input(self):
        player = self.get_player()
        while True:
            try:
                pos = raw_input("Where would you like to place " + player + " (1-9)? ")
                pos = int(pos)
                if pos >= 1 and pos <= 9 and self.gameboard.has_mark(pos) is False:
                    break
                else:
                    self.print_input_error()
            except ValueError:
                self.print_input_error()
        return pos

    def make_move(self, pos):
        val = self.get_player()
        self.gameboard.set_mark(pos, val)

    def get_player(self):
        i = int(self.move_count) % 2
        return self.players[i]

    def has_winner(self):
        game_over = False
        win_list = self.get_winning_pos()
        for item in win_list:
            game_over = self.gameboard.are_marks_equal(*item)
            if game_over:
                break
        return game_over

    def is_draw(self):
        return self.gameboard.is_all_marked()

    @staticmethod
    def get_winning_pos():
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

    @staticmethod
    def print_input_error():
        print "Invalid input. Please try again."

    def print_game_instructions(self):
        print " "
        print "Input your choices using the below grid:"
        self.instruction_b.print_board()
        print " "

    def print_state(self):
        print " "
        self.gameboard.print_board()
        print " "

    @staticmethod
    def print_draw():
        print " "
        print "Draw!"
        print " "

    def print_win(self):
        print "Player " + self.get_player() + " has won!"
        print " "

class GameAI(object):

    def __init__(self, player):
        self.player = player
        self.choice = None
        
    def get_next_move(self, game):
        if game.has_winner() is True:
            if game.get_player() == self.player:
                return 10
            else:
                return -10
        elif game.is_draw():
            return 0
        
        scores = []
        moves = []
        pos_available = game.get_available_moves()
        for a_move in pos_available:
            g = game.get_game_copy()
            g.make_move(a_move)
            #if len(g.get_available_moves()) > 0:
            g.inc_move_count()
            
            scores.append(self.get_next_move(g))
            moves.append(a_move)
        
        if g.get_player() == self.player:
            for index, val in enumerate(scores):
                if val == max(scores):
                    break
            self.choice = moves[index]
            return moves[index]
        else:
            for index, val in enumerate(scores):
                if val == min(scores):
                    break
            self.choice = moves[index]
            return moves[index]
        
    def get_choice(self):
        return self.choice