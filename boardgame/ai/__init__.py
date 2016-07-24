"""
Package containing different game AI algorithms. Those algorithms are used by
the AIPlayer class (which extends `boardgame.player.Player` class) to take part
in a boardgame.

An algorithm must always implement at least the "getBestNextMove" method which
takes a boardgame.gamemodel.GameState in argument.
"""

__all__ = ["minimax"]