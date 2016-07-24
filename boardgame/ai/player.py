from ..player import Player

class AiPlayer(Player):
	"""
	Extension of boardgame.player.Player containing an algorithm to play.
	"""
	def __init__(self, algorithm):
		"""
		Create an AiPlayer

		@algorithm : Algorithm to be used by the class
		"""
		super(AiPlayer, self).__init__("AI")
		self.algo = algorithm

	def play(self, state):
		return self.algo.getBestNextMove(state)
