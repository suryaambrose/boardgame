class Player(object):
	"""
	Base class for players
	"""
	def __init__(self, name):
		"""
		:param name: player's name (str)
		"""
		self.name = name

	def play(self, state):
		"""
		Human player is asked to choose a move, AI player
		decides which move to play.

		:param state: Current state of the game (GameState)
		"""
		raise NotImplementedError()


class HumanPlayer(Player):
	"""
	Base class for human players
	"""
	def __init__(self, name, game_viewer):
		"""
		:param name: player's name (str)
		:param game_viewer: Game displayer class (GameViewer)
		"""
		Player.__init__(self, name)
		self.game_viewer = game_viewer

	def play(self, state):
		self.game_viewer.showState(state)
		return self.game_viewer.waitForAMove()

class AiPlayer(Player):
	"""
	Base class for AI Player containing an algorithm to play.
	"""
	def __init__(self, name, algorithm):
		"""
		Create an AiPlayer

		@algorithm : Algorithm to be used by the class
		"""
		Player.__init__(self, name)
		self.algo = algorithm

	def play(self, state):
		return self.algo.getBestNextMove(state)
