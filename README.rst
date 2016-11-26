***boardgame*** is a Python package gathering several simple games like
TicTacToe or Connect 4. It is meant to be played by humans or by programs.


This page only describes basic usage of this package. For a more advanced usage,
(e.g. to have a program play a game, or to add a new game) check this page.


How to install it
-----------------

* Download the source
* Run ``python setup.py install``


How to play it
--------------

You can play TicTacToe or ConnectFour using the corresponding subcommands of the
boardgame command

``boardgame tictactoe -h``

You will have to specify the players taking part of the game:

``boardgame tictactoe --human-players 1 --ai-players 1``

This allows you to play against someone.

``boardgame tictactoe --human-players 2``