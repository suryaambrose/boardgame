import os
import sys
from ..gameviewer import GameViewer

class ConnectFourViewer(GameViewer):
	def __init__(self):
		super(ConnectFourViewer, self).__init__([6,7])

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