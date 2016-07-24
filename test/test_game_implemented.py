import unittest
from boardgame.tictactoe import TicTacToe

from boardgame.gameconfig import GameConfig

class GameImplementedTest(object):

	def testStateNotRaising(self):
		self.state.isFinal()
		self.state.isTie()

	def testModelNotRaising(self):
		m = self.model.getPossibleMoves(self.state)
		self.model.estimateNextState(self.state, m[0])

class TicTacToeTest(GameImplementedTest, unittest.TestCase):

	def setUp(self):
		config = GameConfig()
		config.hum_players=1
		config.ai_players=1
		self.controller = TicTacToe(config)
		self.model = self.controller._game_model
		self.state = self.model._state

	def testFullGameAi(self):
		config = GameConfig()
		config.hum_players=0
		config.ai_players=2
		self.game = TicTacToe(config)

		while(not self.game.isGameOver()):
			self.game.runOnce()

	def testFullGameHuman(self):
		config = GameConfig()
		config.hum_players=2
		config.ai_players=0
		self.game = TicTacToe(config)

		while(not self.game.isGameOver()):
			self.game.runOnce()
