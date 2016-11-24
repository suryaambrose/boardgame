# from connectfourcontroller import ConnectFourController as ConnectFour
from ..gamecontroller import GameController

from connectfourmodel import ConnectFourModel, ConnectFourState
from connectfourviewer import ConnectFourViewer
from connectfourplayer import ConnectFourHumanPlayer, ConnectFourAiPlayer

def makeConnectFour(game_config):
	viewer = ConnectFourViewer()
	game_handler = GameController(ConnectFourModel, ConnectFourState())

	for i in range(game_config.hum_players):
		game_handler.addPlayer(ConnectFourHumanPlayer(viewer))
	for i in range(game_config.ai_players):
		game_handler.addPlayer(ConnectFourAiPlayer(ConnectFourModel))

	viewer.registerPlayers(ConnectFourModel._player_list)
	viewer.showState(game_handler._game_state)

	return game_handler

ConnectFour = makeConnectFour