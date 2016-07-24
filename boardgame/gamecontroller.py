
class GameController(object):
	"""
	Handles the game, the different player turns and the display.

	This class should be inherited, but only the constructor needs to be
	overwritten
	"""

	def __init__(self, game_model, game_viewer=None):
		"""
		Create GameController

		@game_model  : Model handling the game behavior (GameModel)
		@game_viewer : Class handling the game rendering (Map)
		"""
		# Model creation
		self._game_model = game_model

		# View creation
		self._game_viewer = game_viewer

	def addPlayer(self, player):
		"""
		Add a player to the model

		@player : New player to add
		"""
		gm=self._game_model
		gm.addPlayer(player)
		try:
			if gm._state.next_player is None:
				gm._state.next_player = gm.getNextPlayer()
		except RuntimeError, e:
			# Minimum number of player is not reached yet
			pass

	def runOnce(self):
		"""
		Run one turn of the game.

		Wait for the current player to play a valid move
		"""
		gm=self._game_model
		while True:
			played_move = gm._state.next_player.play(gm._state)
			try:
				gm.applyMove(played_move)
				break
			except RuntimeError:
				print "This move is not possible"
		if self._game_viewer is not None:
			self._game_viewer.showState(gm._state)

	def isGameOver(self):
		"""
		Return True if the game is finished
		"""
		return self._game_model._state.isFinal()

