import os
import sys
from ..gameviewer import GameViewer

class TicTacToeViewer(GameViewer):
	def __init__(self):
		super(TicTacToeViewer, self).__init__([3,3])

	def showState(self, state):
		os.system("clear")
		sys.stdout.write("x\y|")
		for k in range(0, self.map_width):
			sys.stdout.write("%d "%(k))
		sys.stdout.write("\n")
		for i in range(0, self.map_height):
			sys.stdout.write(" %d "%(i))
			for j in range(0, self.map_width):
				sys.stdout.write("|")
				if state._board[i][j] is not None:
					sys.stdout.write(self.symbol_map[state._board[i][j]])
				else:
					sys.stdout.write(" ")
			sys.stdout.write("|\n")

	def waitForAMove(self):
		while True:
			try:
				played_coordinates = raw_input(
					"Choose your play move (e.g. 0 1 for top center cell):"
					).split(" ")
				x = int(played_coordinates[0])
				y = int(played_coordinates[1])
				break
			except Exception, e:
				print e
		return [x,y]