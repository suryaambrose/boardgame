import unittest

from boardgame.gamemodel import GameState, GameModel
from boardgame.player import Player

class GameModelTest(unittest.TestCase):

	def setUp(self):
		self.game_model = GameModel(GameState, 1, 0)

	def testRaiseNotImplemented(self):
		state = GameState()
		with self.assertRaises(NotImplementedError):
			self.game_model.getPossibleMoves(state)

		with self.assertRaises(NotImplementedError):
			self.game_model.estimateNextState(state, None)

	def testPlayerAddition(self):
		player = Player("test")
		self.game_model.max_num_of_players = 0
		with self.assertRaises(RuntimeError):
			self.game_model.addPlayer(player)

		self.game_model.max_num_of_players = 2
		self.game_model.addPlayer(player)
		self.game_model.addPlayer(player)
		with self.assertRaises(RuntimeError):
			self.game_model.addPlayer(player)

	def testGetFirstPlayer(self):
		self.game_model.max_num_of_players = 5
		self.game_model.min_num_of_players = 2
		player = Player("test")
		self.game_model.addPlayer(player)
		with self.assertRaises(RuntimeError):
			self.game_model.getNextPlayer()
		self.game_model.addPlayer(player)
		self.game_model.getNextPlayer()

	def testGetNextPlayer(self):
		self.game_model.max_num_of_players = 5
		self.game_model.min_num_of_players = 1
		self.game_model.addPlayer(Player("one"))
		self.game_model.addPlayer(Player("two"))
		self.game_model.addPlayer(Player("three"))
		self.game_model.addPlayer(Player("four"))
		self.game_model.addPlayer(Player("five"))

		p = self.game_model.getNextPlayer()
		assert(p.name == "one")
		p = self.game_model.getNextPlayer(p)
		assert(p.name == "two")
		p = self.game_model.getNextPlayer(p)
		assert(p.name == "three")
		p = self.game_model.getNextPlayer(p)
		assert(p.name == "four")
		p = self.game_model.getNextPlayer(p)
		assert(p.name == "five")
		p = self.game_model.getNextPlayer(p)
		assert(p.name == "one")

class GameStateTest(unittest.TestCase):

	def testRaiseNotImplemented(self):
		state = GameState()
		with self.assertRaises(NotImplementedError):
			state.isFinal()

		with self.assertRaises(NotImplementedError):
			state.isTie()
