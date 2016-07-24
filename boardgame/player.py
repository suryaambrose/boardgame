
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
