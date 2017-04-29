# from connectfourcontroller import ConnectFourController as ConnectFour
from ..gamecontroller import GameController

from connectfourmodel import ConnectFourModel, ConnectFourState
from connectfourviewer import ConnectFourViewer
from ..player import HumanPlayer, AiPlayer
from ..ai.limited_minimax import LimitedMiniMax

def makeConnectFour(game_config):
	viewer = ConnectFourViewer()
	game_handler = GameController(ConnectFourModel, ConnectFourState())

	for i in range(game_config.hum_players):
		game_handler.addPlayer(HumanPlayer("Human", viewer))
	for i in range(game_config.ai_players):
		game_handler.addPlayer(AiPlayer("AI",LimitedMiniMax(ConnectFourModel)))

	viewer.registerPlayers(ConnectFourModel._player_list)
	viewer.showState(game_handler._game_state)

	return game_handler

ConnectFour = makeConnectFour