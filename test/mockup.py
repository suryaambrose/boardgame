from boardgame.gamemodel import GameModel, GameState
from boardgame.gameviewer import GameViewer
from boardgame.player import Player


class MockUpGameModel(GameModel):
	"""Fake GameModel for test purposes"""

	@classmethod
	def getPossibleMoves(self, state):
		if state.depth >= 2:
			return range(3)
		elif state.depth == 1:
			return range(2)
		else:
			return []

	@staticmethod
	def estimateNextState(state, move):
		if state.depth >= 2:
			if move == 0:
				s = MockUpNonFinalGameState()
				s.depth = 1
				return s
			elif move == 1:
				return MockUpTieGameState()
			elif move == 2:
				s = MockUpNonFinalGameState()
				s.depth = state.depth - 1
				return s
		elif state.depth == 1:
			if move == 0:
				return MockUpFinalGameState()
			elif move == 1:
				return MockUpTieGameState()

	@staticmethod
	def isFinal(state):
		if isinstance(state, MockUpNonFinalGameState):
			return False
		else:
			return True

	@staticmethod
	def isTie(state):
		if isinstance(state, MockUpTieGameState):
			return True
		else:
			return False

class MockUpFinalGameState(GameState):
	"""Fake final (no tie) GameState for test purposes"""

	# Special property for the mockup
	depth = 0

	# def isFinal(self):
	# 	return True

	# def isTie(self):
	# 	return False

class MockUpTieGameState(GameState):
	"""Fake tie GameState for test purposes"""

	# Special property for the mockup
	depth = 0

	# def isFinal(self):
	# 	return True

	# def isTie(self):
	# 	return True

class MockUpNonFinalGameState(GameState):
	"""Fake non final GameState for test purposes"""

	# Special property for the mockup
	depth = 1

	# def isFinal(self):
	# 	return False

	# def isTie(self):
	# 	return False

class MockUpGameViewer(GameViewer):
	def showState(self, state):
		pass

class MockUpPlayer(Player):
	def play(self, state):
		return 0