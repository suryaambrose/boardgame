
class GameController(object):
	"""
	Handles the game, the different player turns and the display.

	This class should be inherited, but only the constructor needs to be
	overwritten
	"""

	def __init__(self, game_model,
		               game_state):
		"""
		Create GameController

		:param game_model: Class handling the game behavior (GameModel)
		:param game_state: Initial state of the game (GameState)
		"""
		# Model creation
		self._game_model = game_model
		self._game_state = game_state


	def addPlayer(self, player):
		"""
		Add a player to the game

		:param player:  New player (Player)
		:raises:  RuntimeError if max number of player is already reached
		"""
		self._game_model.addPlayer(player)
		try:
			if self._game_state.next_player is None:
				self._game_state.next_player = self.getNextPlayer()
		except RuntimeError, e:
			# Minimum number of player is not reached yet
			pass

	def getNextPlayer(self, player=None):
		"""
		Return the player who will play after the given player. If player is
		None, first player is returned.

		:param player:  Original player (Player)
		:return:  Next player (Player)

		"""
		return self._game_model.getNextPlayer(player)


	def runOnce(self):
		"""
		Run one turn of the game.

		Wait for the current player to play a valid move
		"""
		gm=self._game_model
		while True:
			played_move = self._game_state.next_player.play(self._game_state)
			try:
				# gm.applyMove(played_move)
				self._game_state = self._game_model.estimateNextState(
					                   self._game_state, played_move)
				break
			except RuntimeError, e:
				print e
				print "This move is not possible"

	def isGameOver(self):
		"""
		Return True if the game is finished
		"""
		return self._game_model.isFinal(self._game_state)

	def getWinner(self):
		"""
		Returns the winning player if there is one
		"""
		if not self.isGameOver():
			return None
		else:
			return self._game_model.getWinner(self._game_state)
