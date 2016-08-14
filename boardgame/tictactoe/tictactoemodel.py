from ..gamemodel import GameState, GameModel

class TicTacToeState(GameState):
	def __init__(self, rhs=None):
		super(TicTacToeState, self).__init__()
		if rhs is None:
			self._board = [
					[None, None, None],
					[None, None, None],
					[None, None, None]
					 ]
			self.next_player = None
		else:
			self._board = [
							list(rhs._board[0]),
							list(rhs._board[1]),
							list(rhs._board[2]),
						 ]
			self.next_player = rhs.next_player

	def isFinal(self):
		for i in range(3):
			if self._board[i][0] == self._board[i][1]\
			   and self._board[i][0] == self._board[i][2]\
			   and self._board[i][0] is not None:
				return True
		for j in range(3):
			if self._board[0][j] == self._board[1][j]\
			   and self._board[0][j] == self._board[2][j]\
			   and self._board[0][j] is not None:
				return True
		if self._board[0][0] == self._board[1][1]\
		   and self._board[0][0] == self._board[2][2]\
		   and self._board[0][0] is not None:
			return True

		if self._board[2][0] == self._board[1][1]\
		   and self._board[2][0] == self._board[0][2]\
		   and self._board[2][0] is not None:
			return True

		for i in range(3):
			for j in range(3):
				if self._board[i][j] is None:
					return False
		return True

	def isTie(self):
		for i in range(3):
			for j in range(3):
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

	@property
	def value(self):
		max_heuristic = 0
		min_heuristic = 0
		for i in range(3):
			if self._board[i][0] in [None, self.next_player]\
			   and self._board[i][1] in [None, self.next_player]\
			   and self._board[i][2] in [None, self.next_player]:
				max_heuristic += 1
		for i in range(3):
			if self._board[i][0] != self.next_player\
			   and self._board[i][1] != self.next_player\
			   and self._board[i][2] != self.next_player:
				min_heuristic += 1
		for j in range(3):
			if self._board[0][j] in [None, self.next_player]\
			   and self._board[1][j] in [None, self.next_player]\
			   and self._board[2][j] in [None, self.next_player]:
				max_heuristic += 1
		for j in range(3):
			if self._board[0][j] != self.next_player\
			   and self._board[1][j] != self.next_player\
			   and self._board[2][j] != self.next_player:
				min_heuristic += 1

		if self._board[0][0] in [None, self.next_player]\
		   and self._board[1][1] in [None, self.next_player]\
		   and self._board[2][2] in [None, self.next_player]:
			max_heuristic += 1

		if self._board[0][0] != self.next_player\
		   and self._board[1][1] != self.next_player\
		   and self._board[2][2] != self.next_player:
			min_heuristic += 1

		if self._board[2][0] in [None, self.next_player]\
		   and self._board[1][1] in [None, self.next_player]\
		   and self._board[0][2] in [None, self.next_player]:
			max_heuristic += 1

		if self._board[2][0] != self.next_player\
		   and self._board[1][1] != self.next_player\
		   and self._board[0][2] != self.next_player:
			min_heuristic += 1

		return max_heuristic - min_heuristic


class TicTacToeModel(GameModel):
	def __init__(self):
		super(TicTacToeModel, self).__init__(TicTacToeState(), 2, 2)

	@staticmethod
	def getPossibleMoves(state):
		out = []
		for i in range(3):
			for j in range(3):
				if state._board[i][j] is None:
					out.append([i,j])
		return out

	def estimateNextState(self, state, move):
		if move not in TicTacToeModel.getPossibleMoves(state):
			raise RuntimeError("Given move is not a possible move")
		out = TicTacToeState(state)
		out._board[move[0]][move[1]] = out.next_player
		out.next_player = self.getNextPlayer(out.next_player)
		return out
