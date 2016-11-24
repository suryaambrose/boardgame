from ..player import HumanPlayer, AiPlayer
from ..ai.randomchoice import RandomChoice
from ..ai.limited_minimax import LimitedMiniMax

class ConnectFourHumanPlayer(HumanPlayer):
	def __init__(self, viewer):
		super(ConnectFourHumanPlayer, self).__init__("Human", viewer)

	def play(self, state):
		super(ConnectFourHumanPlayer, self).play(state)
		while True:
			try:
				played_column = raw_input("Type where you wish to play (e.g. 1 for column 1):")
				c = int(played_column)
				break
			except Exception, e:
				print e
		return c

class ConnectFourAiPlayer(AiPlayer):
	def __init__(self, game_model):
		algo = LimitedMiniMax(game_model)
		super(ConnectFourAiPlayer, self).__init__("AI", algo)