from ..player import HumanPlayer
from ..ai.player import AiPlayer
from ..ai.minimax import MiniMax

class TicTacToeHumanPlayer(HumanPlayer):
	def __init__(self, viewer):
		super(TicTacToeHumanPlayer, self).__init__("Human", viewer)
		
	def play(self, state):
		super(TicTacToeHumanPlayer, self).play(state)
		while True:
			try:
				played_coordinates = raw_input(
					"Choose your play move (e.g. 1 1 for top left corner):"
					).split(" ")
				x = int(played_coordinates[0])
				y = int(played_coordinates[1])
				break
			except Exception, e:
				print e
		return [x,y]

class TicTacToeAiPlayer(AiPlayer):
	def __init__(self, game_model):
		algo = MiniMax(game_model)
		super(TicTacToeAiPlayer, self).__init__(algo)