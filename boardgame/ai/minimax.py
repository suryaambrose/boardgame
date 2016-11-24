import random

class MiniMax:
	"""
	Implements a MiniMax game algorithm.

	MiniMax recursively creates a tree of possible moves to determine
	which moves will lead to a win or a loss. The main assumption is
	that both players will always play the best move in their interest.

	As opposed to other tree-based algorithm, MiniMax is not optimized to
	solve problems with many possible moves or with long game sequences.
	Its usage should be reserved for very simple games, like TicTacToe.
	"""
	def __init__(self, game):
		"""
		Create MiniMax

		:param game:  The model of the game played
		"""
		self._game = game
		
	def _estimateGameEvolution(self, state, depth=0):
		"""
		Estimate how the game can evolve from the given state

		This method is recursive

		:param state: Current state of the game
		:param depth: Number of iterations already done
		"""
		if self._game.isFinal(state):
			if self._game.isTie(state):
				return 0
			#TODO: replace %2 by number of players
			elif depth%2 == 1:
				return 1
			else:
				return -1

		max_result = -1
		min_result = 1

		# Create Tree
		for possible_move in self._game.getPossibleMoves(state):
			possible_next_state = self._game.estimateNextState(state,
			                                                    possible_move)
			move_value = self._estimateGameEvolution(possible_next_state,
			                                                depth+1)
			max_result = max(max_result, move_value)
			min_result = min(min_result, move_value)

		return min_result if depth%2 else max_result
		
	def getBestNextMove(self, state):
		"""
		Determine the best move to do.

		:param state: Current state of the game (GameState)
		:return: The best possible move

		.. note::
			If several moves give the same winning probability, one of them is
			chosen randomly.
			The type of the returned move depends on the game model
		"""
		max_result = -2
		best_move = []
		# Create Tree
		for possible_move in self._game.getPossibleMoves(state):
			possible_next_state = self._game.estimateNextState(state,
			                                                    possible_move)
			move_value = self._estimateGameEvolution(possible_next_state, 1)
			if move_value > max_result:
				max_result = move_value
				best_move = [possible_move]
			elif move_value == max_result:
				best_move.append(possible_move)

		return random.choice(best_move)