from ..gamecontroller import GameController

from tictactoemodel import TicTacToeModel
from tictactoeviewer import TicTacToeViewer
from tictactoeplayer import TicTacToeHumanPlayer, TicTacToeAiPlayer


class TicTacToeController(GameController):
	def __init__(self, game_config):
		super(TicTacToeController, self).__init__(TicTacToeModel(),
			                                       TicTacToeViewer())
		for i in range(game_config.hum_players):
			self.addPlayer(TicTacToeHumanPlayer(self._game_viewer))
		for i in range(game_config.ai_players):
			self.addPlayer(TicTacToeAiPlayer(self._game_model))

		self._game_viewer.registerPlayers(self._game_model._player_list)
		self._game_viewer.showState(self._game_model._state)