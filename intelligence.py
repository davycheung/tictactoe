
class MinMaxAI(object):

    def __init__(self, player):
        self.player = player
        self.move = None
        
    def get_next_move(self, game):
        if game.has_winner() is True:
            if game.get_player() == self.player:
                return 100
            else:
                return -100
        elif game.is_draw():
            return 0
        
        scores = []
        moves = []
        pos_available = game.get_available_moves()
        for a_move in pos_available:
            g = game.get_game_copy()
            g.make_move(a_move)
            g.inc_move_count()

            scores.append(self.get_next_move(g))
            moves.append(a_move)
        
        if g.get_player() == self.player:
            for index, val in enumerate(scores):
                if val == max(scores):
                    break
        else:
            for index, val in enumerate(scores):
                if val == min(scores):
                    break
        self.move = moves[index]
        return scores[index]
        
    def get_move(self, game):
        self.get_next_move(game)
        return self.move

