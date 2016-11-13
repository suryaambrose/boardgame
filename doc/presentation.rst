General principles
==================

This package allows you to code, play to and code ai player for several strategy
games.

It is composed by several parts

**State**
  The state describes entirely the current situation of the game. It contains
  all the parameters and information necessary to differentiate a situation from
  another.

:Example:
	The state in chess contains:

	* the current position of every piece (current configuration)
	* the list of all configurations since the last capture or pawn move (since 
	  three occurences of the same configuration leads to a draw by `threefold
	  repetition`)
	* the number of move since the last capture or pawn move (since fifty moves
	  without any capture or pawn move lead to a draw by the `fifty-move rule`)
	* the player whose turn it is to play
	* the possibility for each player to castle
	* the possibilities to make an `en passant` capture.


**Model**
  The model encodes the rules of the game. It determines, from a given state,
  which moves are possible, and which state will result from each of those moves.


**Controller**
  A controller handles the whole game's proceeding (ask the current player to
  play, update the game state using the model, and start over).


**Viewer**
  A viewer is a object meant to show the current state of the game, or at least
  the relevant parts. It is mostly meant for human players.


**Player**
  A player can be a human or a program. If the player is human, he or she will
  rely on a viewer to see which moves are possible. A program does not need a 
  viewer and can directly ask the possible moves to the model.