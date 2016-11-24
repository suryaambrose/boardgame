import random

class RandomChoice(object):
	"""
	Implements a Random game algorithm

	This algorithm is simply playing random moves. It is particularly handy for
	game testing.
	"""
	def __init__(self, game):
		"""
		Create Random

		:param game:  Game model
		"""
		self._game = game

	def getBestNextMove(self, state):
		options = self._game.getPossibleMoves(state)
		return random.choice(options)
