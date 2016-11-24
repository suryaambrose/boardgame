"""
Package containing different game AI algorithms. Those algorithms are used by
the AiPlayer class (which extends `boardgame.player.Player` class) to take part
in a boardgame.

An algorithm must always implement at least the "getBestNextMove" method which
takes a boardgame.gamemodel.GameState in argument.
"""

from limited_minimax import LimitedMiniMax
from minimax import MiniMax
from randomchoice import RandomChoice