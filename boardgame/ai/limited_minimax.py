import random
import json

class LimitedMiniMax:
	"""
	Implements an LimitedMiniMax game algorithm which is a MiniMax with depth
	limitation.
	"""
	def __init__(self, game, max_depth=4):
		"""
		Create LimitedMiniMax

		@game  :  The model of the game played
		"""
		self._game = game
		self._max_depth = max_depth

	def _estimateGameEvolution(self, state, depth=0):
		"""
		Estimate how the game can evolve from the given state

		This method is recursive

		@state : Current state of the game
		@depth : Number of iterations already done
		"""
		if self._game.isFinal(state):
			if self._game.isTie(state):
				# print "Final state tie"
				return 0
			#TODO: replace %2 by number of players
			elif depth%2 == 1:
				# print "Final state win"
				return float("inf")
			else:
				# print "Final state lose"
				return -float("inf")

		if depth == self._max_depth:
			# print "Stop digging, value is %f"%(state.value * (-1.0 if depth%2 else 1.0))
			return state.value * (-1 if depth%2 else 1)

		max_result = -float("inf")
		min_result = float("inf")

		# Create Tree
		# print "start children evaluation"
		for possible_move in self._game.getPossibleMoves(state):
			possible_next_state = self._game.estimateNextState(state,
			                                                    possible_move)
			# print possible_move
			move_value = self._estimateGameEvolution(possible_next_state,
			                                                depth+1)
			max_result = max(max_result, move_value)
			min_result = min(min_result, move_value)

		# print "end of evaluation, result is %f"%(min_result if depth%2 else max_result)
		return min_result if depth%2 else max_result

	def getBestNextMove(self, state):
		"""
		Determine the best move to do.

		@state  : Current state of the game (GameState)
		@return : The best possible move

		..note::
			If several moves give the same winning probability, one of them is
			chosen randomly.
			The type of the returned move depends on the game model
		"""
		max_result = -float("inf")
		best_move = []
		# Create Tree
		# print "start children evaluation"
		for possible_move in self._game.getPossibleMoves(state):
			possible_next_state = self._game.estimateNextState(state,
			                                                    possible_move)
			# print possible_move
			move_value = self._estimateGameEvolution(possible_next_state, 1)
			if move_value > max_result:
				max_result = move_value
				best_move = [possible_move]
			elif move_value == max_result:
				best_move.append(possible_move)

		# print max_result
		# print best_move
		return random.choice(best_move)