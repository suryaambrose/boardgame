
class GameState(object):
	"""
	Wraps a state of the game
	"""
	next_player = None

	@property
	def value(self):
		"""
		Defines the estimated value of a state

		This is very useful for AI program, but is not really important for
		human players.
		"""
		raise NotImplementedError

class GameModel(object):
	"""
	Wraps the game behavior.
	"""

	min_num_of_players = 1
	max_num_of_players = 0
	_player_list = []

	@classmethod
	def addPlayer(cls, player):
		"""
		Add a player to the game

		:param player:  New player (Player)
		:raises:  RuntimeError if max number of player is already reached
		"""
		if len(cls._player_list)>=cls.max_num_of_players:
			raise RuntimeError("Maximum number of player is reached")
		cls._player_list.append(player)

	@classmethod
	def getNextPlayer(cls, player=None):
		"""
		Return the player who will play after the given player. If player is
		None, first player is returned.

		:param player:  Original player (Player)
		:return:  Next player (Player)

		"""
		if len(cls._player_list)<cls.min_num_of_players:
			raise RuntimeError("Minimum number of player is not reached")
		if player is None:
			return cls._player_list[0]
		next_player_index = (cls._player_list.index(player) + 1) %len(cls._player_list)
		return cls._player_list[next_player_index]

	@staticmethod
	def getPossibleMoves(state):
		"""
		Return the list of move that can be played from the given state

		:param state:  Game state to evaluate (GameState)
		:return:  List of possible moves (list)
		:raises NotImplementedError: if child does not override this function
		"""
		raise NotImplementedError()

	@staticmethod
	def estimateNextState(state, move):
		"""
		Estimate what the game state will be after the given move
		is applied to the given state.

		:param state:  Current game state (GameState)
		:param move:  Move to play
		:return:  New state (GameState)
		:raises  RuntimeError: if move is not possible
		:raises NotImplementedError: if child does not override this function
		"""
		raise NotImplementedError()

	@staticmethod
	def isFinal(state):
		"""
		True if the given state finishes the game

		This happens when somebody won or when there is no possible
		move left

		:param state:  Current game state (GameState)
		:raises NotImplementedError: if child does not override this function
		"""
		raise NotImplementedError

	@staticmethod
	def getWinner(state):
		"""
		Returns the winning player, None is the game is not over or is a draw

		:param state:  Current game state (GameState)
		:raises NotImplementedError: if child does not override this function
		"""
		raise NotImplementedError

	@staticmethod
	def isTie(state):
		"""
		True if the given state finishes the game without a winner

		:param state:  Game state to evaluate (GameState)
		:raises NotImplementedError: if child does not override this function
		"""
		raise NotImplementedError
