
class GameState(object):
	"""
	Wraps a state of the game

	A game state can vary a lot from a game to another, which is why
	only two functions must be overridden `isFinal` and `isTie`, the
	rest being left to the user's discretion.
	"""

	def isFinal(self):
		"""
		True if the current state finishes the game

		This happens when somebody won or when there is no possible
		move left
		"""
		raise NotImplementedError

	def isTie(self):
		"""
		True if the current state finishes the game without a winner
		"""
		raise NotImplementedError

class GameModel(object):
	"""
	Wraps the game behavior.

	This class should be inherited and both method `getPossibleMoves`
	and `estimateNextState` must be overridden.
	It is also important to define `min_num_of_players` and `max_num_of_players`
	which are class variables.
	"""
	_player_list = []
	min_num_of_players = -1
	max_num_of_players = -1

	@staticmethod
	def getPossibleMoves(state):
		"""
		Return the list of move that can be played from the given state

		@state  :  Game state to evaluate (GameState)
		@return :  List of possible moves (list)
		"""
		raise NotImplementedError()

	@staticmethod
	def estimateNextState(state, move):
		"""
		Estimate what the game state will be after the given move
		is applied to the given state.

		@state  :  Original game state (GameState)
		@move   :  Move to play
		@return :  New state (GameState)

		..warning::
			This function must not change the actual state of the game.
			Its only purpose is to estimate what the game board will be,
			not to actually change it.
		"""
		raise NotImplementedError()

	@classmethod
	def addPlayer(self, player):
		"""
		Add a player to the game

		@player  :  New player (Player)
		@raises  :  RuntimeError if max number of player is already reached
		"""
		if len(self._player_list)>=self.max_num_of_players:
			raise RuntimeError("Maximum number of player is reached")
		self._player_list.append(player)

	@classmethod
	def getNextPlayer(self, player=None):
		"""
		Return the player who will play after the given player. If player is
		None, first player is returned.

		@player  :  Original player (Player)
		@return  :  Next player (Player)

		"""
		if len(self._player_list)<self.min_num_of_players:
			raise RuntimeError("Minimum number of player is not reached")
		if player is None:
			return self._player_list[0]
		next_player_index = (self._player_list.index(player) + 1) %len(self._player_list)
		return self._player_list[next_player_index]
