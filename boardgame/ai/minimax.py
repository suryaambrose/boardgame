import random
import json

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

		@game  :  The model of the game played
		"""
		self._game = game
		
	def _estimateGameEvolution(self, state, depth=0):
		"""
		Estimate how the game can evolve from the given state

		This method is recursive

		@state : Current state of the game
		@depth : Number of iterations already done
		"""
		if state.isFinal():
			if state.isTie():
				return (0, dict())
			#TODO: replace %2 by number of players
			elif depth%2 == 1:
				return (1, dict())
			else:
				return (-1, dict())


		move_values = dict()
		max_result = -1
		min_result = 1

		# Create Tree
		for possible_move in self._game.getPossibleMoves(state):
			# TODO : get rid of json
			key = json.dumps(possible_move)
			possible_next_state = self._game.estimateNextState(state, possible_move)
			move_values[key] = self._estimateGameEvolution(possible_next_state, depth+1)
			max_result = max(max_result, move_values[key][0])
			min_result = min(min_result, move_values[key][0])

		state_value = min_result if depth%2 else max_result
		return (state_value, move_values)
		
	def getBestNextMove(self, player, state):
		"""
		Determine the best move to do.

		@player : The person who moght play the returned move (Player)
		@state  : Current state of the game (GameState)
		@return : The best possible move

		..note::
			If several moves give the same winning probability, one of them is
			chosen randomly.
			The type of the returned move depends on the game model
		"""
		state_estimation = self._estimateGameEvolution(state)

		max_move_value = -2 # -2 so that even a -1 move can be played if there is no other choice
		best_move = []
		
		for (possible_move, value) in state_estimation[1].iteritems():
			if value[0] > max_move_value:
				max_move_value = value[0]
				best_move = [possible_move]
			elif value[0] == max_move_value:
				best_move.append(possible_move)
		return json.loads(random.choice(best_move))
