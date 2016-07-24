
class Player(object):
	"""
	Player handling

	This class should be inherited, and the method `play` must be overridden.
	"""
	def __init__(self, name):
		self.name = name
		
	def play(self, state):
		"""
		Human player is asked to choose a move, AI player
		decides which move to play.

		@state : Current state of the game (GameState)
		"""
		raise NotImplementedError()

class HumanPlayer(Player):
	"""
	Base class for human players

	@name         : player's name (str)
	@game_viewer  : Game displayer class (GameViewer)
	"""
	def __init__(self, name, game_viewer):
		super(HumanPlayer, self).__init__(name)
		self.game_viewer = game_viewer

	def play(self, state):
		self.game_viewer.showState(state)
