
SMALL_DESCRIPTION = """
boardgame aims to gather several simple boardgames like TicTacToe or Connect 4
"""

LONG_DESCRIPTION = """
boardgame aims to gather several simple boardgames like TicTacToe or Connect 4

Each game is described by a State and a Model. A State represents the current
state of the game (obviously) but can also provide a value for that state. This
value is helpful for AI playing the game. A Model represents the rules of the
game and is used to describe which moves are possible from a given state, and
what would be their resulting states.

Aside of those two elements is a Viewer, whose purpose is to display the
current state of the game and to handle human actions.

Above all this, a Controller handles the state, the model, the player actions
returned by the viewer or the AI actions to run the game. This Controller is
generic and does not need to be overwritten for each game.
"""

VERSION = "0.1.0"

__doc__ = "\n" + SMALL_DESCRIPTION + LONG_DESCRIPTION
