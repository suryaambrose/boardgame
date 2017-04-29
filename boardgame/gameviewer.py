colors = dict(red = 31, green = 32, yellow=33, blue=34)

def colorize(s, color):
	return "\033[%dm%s\033[0m"%(colors[color], s)

class GameInterface(object):

	def registerPlayers(self, players_list):
		"""
		Create a symbol map to represent all players

		:param players_list: list of players
		"""
		raise NotImplementedError

	def showState(self, state):
		"""
		Display the current state of the game

		:param state: Current state game (GameState)
		"""
		raise NotImplementedError

	def waitForAMove(self):
		raise NotImplementedError

class GameViewer(GameInterface):

	symbol_list = [colorize("x", "red"), colorize("o", "yellow")]

	def __init__(self, map_size):
		"""
		Create a game displayer

		:param map_size: size of the map to display ([h,w])
		"""
		self.map_height = map_size[0]
		self.map_width = map_size[1]
		self.symbol_map = dict()

	def registerPlayers(self, players_list):
		"""
		Create a symbol map to represent all players

		:param players_list: list of players
		"""
		for i in range(len(players_list)):
			self.symbol_map[players_list[i]] = self.symbol_list[i]

	def showState(self, state):
		"""
		Display the current state of the game

		:param state: Current state game (GameState)
		"""
		raise NotImplementedError

	def waitForAMove(self):
		"""
		Asks the user to play
		"""
		raise NotImplementedError
