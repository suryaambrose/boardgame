import unittest

from boardgame.gamemodel import GameState, GameModel
from boardgame.gamecontroller import GameController
from boardgame.gameviewer import GameViewer
from boardgame.player import Player
from mockup import *

class GameModelTest(unittest.TestCase):

	def setUp(self):
		self.game_model = GameModel()

	def testRaiseNotImplemented(self):
		state = GameState()
		with self.assertRaises(NotImplementedError):
			self.game_model.getPossibleMoves(state)

		with self.assertRaises(NotImplementedError):
			self.game_model.estimateNextState(state, None)

		with self.assertRaises(NotImplementedError):
			self.game_model.isFinal(state)

		with self.assertRaises(NotImplementedError):
			self.game_model.isTie(state)

class GameStateTest(unittest.TestCase):

	def testRaiseNotImplemented(self):
		state = GameState()

		with self.assertRaises(NotImplementedError):
			state.value

class GameControllerTest(unittest.TestCase):

	def testPlayerAddition(self):
		game_model = GameModel
		game_model.min_num_of_players = 1
		game_model.max_num_of_players = 0
		game_model._player_list = []
		game_controller = GameController(game_model, GameState())

		with self.assertRaises(RuntimeError):
			game_controller.addPlayer(MockUpPlayer("one"))

		game_model.min_num_of_players = 2
		game_model.max_num_of_players = 2

		game_controller.addPlayer(MockUpPlayer("one"))
		assert(game_controller._game_state.next_player is None)
		game_controller.addPlayer(Player("two"))
		assert(game_controller._game_state.next_player is not None)
		assert(game_controller._game_state.next_player.name=="one")

		with self.assertRaises(RuntimeError):
			game_controller.addPlayer(Player("three"))

	def testGetFirstPlayer(self):
		game_model = GameModel
		game_model.min_num_of_players = 1
		game_model.max_num_of_players = 0
		game_model._player_list = []
		game_controller = GameController(game_model, GameState())
		game_model.max_num_of_players = 5
		game_model.min_num_of_players = 2
		game_controller.addPlayer(MockUpPlayer("one"))
		with self.assertRaises(RuntimeError):
			game_controller.getNextPlayer()
		game_controller.addPlayer(MockUpPlayer("two"))
		p = game_controller.getNextPlayer()
		assert(p.name == "one")

	def testGetNextPlayer(self):
		game_model = GameModel
		game_model.min_num_of_players = 1
		game_model.max_num_of_players = 0
		game_model._player_list = []
		game_controller = GameController(game_model, GameState())
		game_model.max_num_of_players = 5
		game_model.min_num_of_players = 1
		game_controller.addPlayer(Player("one"))
		game_controller.addPlayer(Player("two"))
		game_controller.addPlayer(Player("three"))
		game_controller.addPlayer(Player("four"))
		game_controller.addPlayer(Player("five"))

		p = game_controller.getNextPlayer()
		assert(p.name == "one")
		p = game_controller.getNextPlayer(p)
		assert(p.name == "two")
		p = game_controller.getNextPlayer(p)
		assert(p.name == "three")
		p = game_controller.getNextPlayer(p)
		assert(p.name == "four")
		p = game_controller.getNextPlayer(p)
		assert(p.name == "five")
		p = game_controller.getNextPlayer(p)
		assert(p.name == "one")

	def testRun(self):
		game_model = MockUpGameModel
		game_model._player_list = []
		game_model.max_num_of_players = 1
		game_model.min_num_of_players = 1
		# game_viewer = MockUpGameViewer([0, 0])
		game_controller = GameController(game_model, MockUpNonFinalGameState())
		game_controller.addPlayer(MockUpPlayer("one"))
		game_controller.runOnce()
