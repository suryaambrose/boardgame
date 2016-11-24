from ..gamecontroller import GameController

from tictactoemodel import TicTacToeModel, TicTacToeState
from tictactoeviewer import TicTacToeViewer
from tictactoeplayer import TicTacToeHumanPlayer, TicTacToeAiPlayer


def makeTicTacToe(game_config):
	viewer = TicTacToeViewer()
	game_handler = GameController(TicTacToeModel, TicTacToeState())

	for i in range(game_config.hum_players):
		game_handler.addPlayer(TicTacToeHumanPlayer(viewer))
	for i in range(game_config.ai_players):
		game_handler.addPlayer(TicTacToeAiPlayer(TicTacToeModel))

	viewer.registerPlayers(TicTacToeModel._player_list)
	viewer.showState(game_handler._game_state)

	return game_handler

TicTacToe = makeTicTacToe