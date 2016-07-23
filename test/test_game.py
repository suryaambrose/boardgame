import unittest

from boardgame.gamemodel import GameState, GameModel
from boardgame.player import Player

class GameModelTest(unittest.TestCase):

	def setUp(self):
		GameModel.min_num_of_players = -1
		GameModel.max_num_of_players = -1
		GameModel._player_list = []

	def testRaiseNotImplemented(self):
		state = GameState()
		with self.assertRaises(NotImplementedError):
			GameModel.getPossibleMoves(state)

		with self.assertRaises(NotImplementedError):
			GameModel.estimateNextState(state, None)

	def testPlayerAddition(self):
		player = Player("test")
		GameModel.max_num_of_players = 0
		with self.assertRaises(RuntimeError):
			GameModel.addPlayer(player)

		GameModel.max_num_of_players = 2
		GameModel.addPlayer(player)
		GameModel.addPlayer(player)
		with self.assertRaises(RuntimeError):
			GameModel.addPlayer(player)

	def testGetFirstPlayer(self):
		GameModel.max_num_of_players = 5
		GameModel.min_num_of_players = 2
		player = Player("test")
		GameModel.addPlayer(player)
		with self.assertRaises(RuntimeError):
			GameModel.getNextPlayer()
		GameModel.addPlayer(player)
		GameModel.getNextPlayer()

	def testGetNextPlayer(self):
		GameModel.max_num_of_players = 5
		GameModel.min_num_of_players = 1
		GameModel.addPlayer(Player("one"))
		GameModel.addPlayer(Player("two"))
		GameModel.addPlayer(Player("three"))
		GameModel.addPlayer(Player("four"))
		GameModel.addPlayer(Player("five"))

		p = GameModel.getNextPlayer()
		assert(p.name == "one")
		p = GameModel.getNextPlayer(p)
		assert(p.name == "two")
		p = GameModel.getNextPlayer(p)
		assert(p.name == "three")
		p = GameModel.getNextPlayer(p)
		assert(p.name == "four")
		p = GameModel.getNextPlayer(p)
		assert(p.name == "five")
		p = GameModel.getNextPlayer(p)
		assert(p.name == "one")



class GameStateTest(unittest.TestCase):

	def testRaiseNotImplemented(self):
		state = GameState()
		with self.assertRaises(NotImplementedError):
			state.isFinal()

		with self.assertRaises(NotImplementedError):
			state.isTie()