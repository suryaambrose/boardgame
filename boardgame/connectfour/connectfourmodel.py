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

	@property
	def value(self):
		max_heuristic = 0
		min_heuristic = 0

		for j in range(7):
			for i in range(6):
				if i+3<6:
					h = 0
					for k in range(0,4):
						if self._board[i+k][j] == self.next_player:
							h+=1
						elif self._board[i+k][j] is None:
							continue
						else:
							break
					else:
						max_heuristic += h

					h = 0
					for k in range(0,4):
						if self._board[i+k][j] != self.next_player and self._board[i+k][j] is not None:
							h+=1
						elif self._board[i+k][j] is None:
							continue
						else:
							break
					else:
						min_heuristic += h
				if j+3<7:
					h = 0
					for k in range(0,4):
						if self._board[i][j+k] == self.next_player:
							h+=1
						elif self._board[i][j+k] is None:
							continue
						else:
							break
					else:
						max_heuristic += h

					h = 0
					for k in range(0,4):
						if self._board[i][j+k] != self.next_player and self._board[i][j+k] is not None:
							h+=1
						elif self._board[i][j+k] is None:
							continue
						else:
							break
					else:
						min_heuristic += h

				if i+3<6 and j+3<7:
					h = 0
					for k in range(0,4):
						if self._board[i+k][j+k] == self.next_player:
							h+=1
						elif self._board[i+k][j+k] is None:
							continue
						else:
							break
					else:
						max_heuristic += h

					h = 0
					for k in range(0,4):
						if self._board[i+k][j+k] != self.next_player and self._board[i+k][j+k] is not None:
							h+=1
						elif self._board[i+k][j+k] is None:
							continue
						else:
							break
					else:
						min_heuristic += h

				if i+3<6 and j-3>=0:
					h = 0
					for k in range(0,4):
						if self._board[i+k][j-k] == self.next_player:
							h+=1
						elif self._board[i+k][j-k] is None:
							continue
						else:
							break
					else:
						max_heuristic += h

					h = 0
					for k in range(0,4):
						if self._board[i+k][j-k] != self.next_player and self._board[i+k][j-k] is not None:
							h+=1
						elif self._board[i+k][j-k] is None:
							continue
						else:
							break
					else:
						min_heuristic += h

		return max_heuristic - min_heuristic

class ConnectFourModel(GameModel):

	min_num_of_players = 2
	max_num_of_players = 2

	def __init__(self):
		super(ConnectFourModel, self).__init__(ConnectFourState(), 2, 2)

	@staticmethod
	def getPossibleMoves(state):
		out = []
		for j in range(7):
			if state._board[0][j] is None:
				out.append(j)
		return out

	@staticmethod
	def estimateNextState(state, move):
		out = ConnectFourState(state)
		if move not in ConnectFourModel.getPossibleMoves(state):
			raise RuntimeError("Given move is not a possible move")
		for i in range(5, -1, -1):
			if out._board[i][move] is None:
				out._board[i][move] = out.next_player
				break
		out.next_player = ConnectFourModel.getNextPlayer(out.next_player)
		return out

	@staticmethod
	def isFinal(state):
		res = False
		is_tie = True
		for j in range(7):
			for i in range(6):
				if state._board[i][j] is None:
					is_tie = False
					continue

				if i+3<6:
					for k in range(1,4):
						if state._board[i+k][j]!=state._board[i][j]:
							break
					else:
						return True
				if j+3<7:
					for k in range(1,4):
						if state._board[i][j+k]!=state._board[i][j]:
							break
					else:
						return True
				if i+3<6 and j+3<7:
					for k in range(1,4):
						if state._board[i+k][j+k]!=state._board[i][j]:
							break
					else:
						return True
				if i+3<6 and j-3>=0:
					for k in range(1,4):
						if state._board[i+k][j-k]!=state._board[i][j]:
							break
					else:
						return True

		return is_tie

	@staticmethod
	def getWinner(state):
		for j in range(7):
			for i in range(6):
				if state._board[i][j] is None:
					continue

				if i+3<6:
					for k in range(1,4):
						if state._board[i+k][j]!=state._board[i][j]:
							break
					else:
						return state._board[i][j]
				if j+3<7:
					for k in range(1,4):
						if state._board[i][j+k]!=state._board[i][j]:
							break
					else:
						return state._board[i][j]
				if i+3<6 and j+3<7:
					for k in range(1,4):
						if state._board[i+k][j+k]!=state._board[i][j]:
							break
					else:
						return state._board[i][j]
				if i+3<6 and j-3>=0:
					for k in range(1,4):
						if state._board[i+k][j-k]!=state._board[i][j]:
							break
					else:
						return state._board[i][j]

		return None

	@staticmethod
	def isTie(state):
		for j in range(7):
			for i in range(6):
				if state._board[i][j] is None:
					return False

		for i in range(3):
			if state._board[i][0] == state._board[i][1]\
			   and state._board[i][0] == state._board[i][2]:
				return False
		for j in range(3):
			if state._board[0][j] == state._board[1][j]\
			   and state._board[0][j] == state._board[2][j]:
				return False
		if state._board[0][0] == state._board[1][1]\
		   and state._board[0][0] == state._board[2][2]:
			return False

		if state._board[2][0] == state._board[1][1]\
		   and state._board[2][0] == state._board[0][2]:
			return False

		return True
