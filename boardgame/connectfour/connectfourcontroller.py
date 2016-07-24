from ..gamecontroller import GameController

from connectfourmodel import ConnectFourModel
from connectfourviewer import ConnectFourViewer
from connectfourplayer import ConnectFourHumanPlayer, ConnectFourAiPlayer


class ConnectFourController(GameController):
	def __init__(self, game_config):
		super(ConnectFourController, self).__init__(ConnectFourModel(),
			                                       ConnectFourViewer())
		for i in range(game_config.hum_players):
			self.addPlayer(ConnectFourHumanPlayer(self._game_viewer))
		for i in range(game_config.ai_players):
			self.addPlayer(ConnectFourAiPlayer(self._game_model))

		self._game_viewer.registerPlayers(self._game_model._player_list)
		self._game_viewer.showState(self._game_model._state)