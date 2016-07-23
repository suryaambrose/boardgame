
class GameState(object):
	"""
	Wraps a state of the game

	A game state can vary a lot from a game to another, which is why
	only two functions must be overridden `isFinal` and `isTie`, the
	rest being left to the user's discretion.
	"""
	next_player = None

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

	def __init__(self, state, players_min_num, players_max_num):
		"""
		Create GameModel

		@state           : Initial state (GameState)
		@players_min_num : Minimum number of player required (int)
		@players_max_num : Maximum number of player required (int)
		"""
		self._state = state
		self._player_list = []
		self.min_num_of_players = players_min_num
		self.max_num_of_players = players_max_num

	@staticmethod
	def getPossibleMoves(state):
		"""
		Return the list of move that can be played from the given state

		@state  :  Game state to evaluate (GameState)
		@return :  List of possible moves (list)
		"""
		raise NotImplementedError()

	def estimateNextState(self, state, move):
		"""
		Estimate what the game state will be after the given move
		is applied to the given state.

		@state  :  Original game state (GameState)
		@move   :  Move to play
		@return :  New state (GameState)
		@raises :  RuntimeError if move is not possible

		..warning::
			This function does not change the actual state of the game.
			Its only purpose is to estimate what the game board would be if the
			move was applied, not to actually change it.
		"""
		raise NotImplementedError()

	def applyMove(self, move):
		"""
		Apply the given move to the current state

		@move   :  Move to play
		@raises :  RuntimeError if move is not possible

		..note::
			This function changes the actual state of the game.
		"""
		self._state = self.estimateNextState(self._state, move)

	def addPlayer(self, player):
		"""
		Add a player to the game

		@player  :  New player (Player)
		@raises  :  RuntimeError if max number of player is already reached
		"""
		if len(self._player_list)>=self.max_num_of_players:
			raise RuntimeError("Maximum number of player is reached")
		self._player_list.append(player)

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
