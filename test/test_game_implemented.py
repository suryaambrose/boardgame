import unittest
from boardgame.tictactoe import TicTacToe
from boardgame.connectfour import ConnectFour

from boardgame.gameconfig import GameConfig

class GameImplementedTest(object):

	def testStateNotRaising(self):
		self.state.isFinal()
		self.state.isTie()

	def testModelNotRaising(self):
		m = self.model.getPossibleMoves(self.state)
		self.model.estimateNextState(self.state, m[0])

	def testFullGame(self):
		while(not self.game.isGameOver()):
			self.game.runOnce()

class TicTacToeTest(GameImplementedTest, unittest.TestCase):

	def setUp(self):
		config = GameConfig()
		config.hum_players=1
		config.ai_players=1
		self.game = TicTacToe(config)
		self.model = self.game._game_model
		self.state = self.model._state

class ConnectFourTest(GameImplementedTest, unittest.TestCase):

	def setUp(self):
		config = GameConfig()
		config.hum_players=1
		config.ai_players=1
		self.game = ConnectFour(config)
		self.model = self.game._game_model
		self.state = self.model._state
