from ..gamemodel import GameState, GameModel

class ConnectFourState(GameState):
	def __init__(self, rhs=None):
		super(ConnectFourState, self).__init__()
		if rhs is None:
			self._board = [
					[None, None, None, None, None, None, None],
					[None, None, None, None, None, None, None],
					[None, None, None, None, None, None, None],
					[None, None, None, None, None, None, None],
					[None, None, None, None, None, None, None],
					[None, None, None, None, None, None, None]
					 ]
			self.next_player = None
		else:
			self._board = [
							list(rhs._board[0]),
							list(rhs._board[1]),
							list(rhs._board[2]),
							list(rhs._board[3]),
							list(rhs._board[4]),
							list(rhs._board[5]),
						 ]
			self.next_player = rhs.next_player

	def isFinal(self):
		res = False
		is_tie = True
		for j in range(7):
			for i in range(6):
				if self._board[i][j] is None:
					is_tie = False
					continue

				if i+3<6:
					for k in range(1,4):
						if self._board[i+k][j]!=self._board[i][j]:
							break
					else:
						return True
				if j+3<7:
					for k in range(1,4):
						if self._board[i][j+k]!=self._board[i][j]:
							break
					else:
						return True
				if i+3<6 and j+3<7:
					for k in range(1,4):
						if self._board[i+k][j+k]!=self._board[i][j]:
							break
					else:
						return True
				if i+3<6 and j-3>=0:
					for k in range(1,4):
						if self._board[i+k][j-k]!=self._board[i][j]:
							break
					else:
						return True

		return is_tie

	def isTie(self):
		for j in range(7):
			for i in range(6):
				if self._board[i][j] is None:
					return False

		for i in range(3):
			if self._board[i][0] == self._board[i][1]\
			   and self._board[i][0] == self._board[i][2]:
				return False
		for j in range(3):
			if self._board[0][j] == self._board[1][j]\
			   and self._board[0][j] == self._board[2][j]:
				return False
		if self._board[0][0] == self._board[1][1]\
		   and self._board[0][0] == self._board[2][2]:
			return False

		if self._board[2][0] == self._board[1][1]\
		   and self._board[2][0] == self._board[0][2]:
			return False

		return True

class ConnectFourModel(GameModel):
	def __init__(self):
		super(ConnectFourModel, self).__init__(ConnectFourState(), 2, 2)

	@staticmethod
	def getPossibleMoves(state):
		out = []
		for j in range(7):
			if state._board[0][j] is None:
				out.append(j)
		return out

	def estimateNextState(self, state, move):
		out = ConnectFourState(state)
		if move not in ConnectFourModel.getPossibleMoves(state):
			raise RuntimeError("Given move is not a possible move")
		for i in range(5, -1, -1):
			if out._board[i][move] is None:
				out._board[i][move] = out.next_player
				break
		out.next_player = self.getNextPlayer(out.next_player)
		return out
