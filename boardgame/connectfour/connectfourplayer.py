from ..player import HumanPlayer
from ..ai.player import AiPlayer
from ..ai.randomchoice import RandomChoice

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
		algo = RandomChoice(game_model)
		super(ConnectFourAiPlayer, self).__init__(algo)