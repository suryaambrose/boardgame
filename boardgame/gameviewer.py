
class GameViewer(object):

	symbol_list = ["x","o"]

	def __init__(self, map_size):
		"""
		Create a game displayer

		@map_size      : size of the map to display ([h,w])
		"""
		self.map_height = map_size[0]
		self.map_width = map_size[1]
		self.symbol_map = dict()

	def registerPlayers(self, players_list):
		"""
		Create a symbol map to represent all players

		@players_list  : list of players
		"""
		for i in range(len(players_list)):
			self.symbol_map[players_list[i]] = self.symbol_list[i]

	def showState(self, state):
		"""
		Display the current state of the game

		@state : Current state game (GameState)
		"""
		raise NotImplementedError()