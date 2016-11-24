import unittest

from boardgame.ai import *
from boardgame.player import AiPlayer

from mockup import MockUpNonFinalGameState, MockUpGameModel

class MiniMaxTest(unittest.TestCase):
	def setUp(self):
		self.algo = MiniMax(MockUpGameModel)

	def testRun1(self):
		state = MockUpNonFinalGameState()
		res = self.algo.getBestNextMove(state)
		assert(res == 0)

	def testRun2(self):
		state = MockUpNonFinalGameState()
		state.depth = 2
		res = self.algo.getBestNextMove(state)
		assert(res == 1)

	def testRun3(self):
		state = MockUpNonFinalGameState()
		state.depth = 3
		res = self.algo.getBestNextMove(state)
		assert(res in [1,2])

class AiPlayerTest(unittest.TestCase):
	def setUp(self):
		algo = minimax.MiniMax(MockUpGameModel)
		self.player = AiPlayer("Ai_1",algo)

	def testCreate(self):
		assert(True) # Just make sure player creation is ok

	def testPlay(self):
		state = MockUpNonFinalGameState()
		res = self.player.play(state)
		assert(res == 0)
