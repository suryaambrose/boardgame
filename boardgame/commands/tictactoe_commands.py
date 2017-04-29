from boardgame.tictactoe import makeTicTacToe

DESCRIPTION = "Starts a TicTacToe game"

def make_command_parser(parser):
	parser.add_argument("--ai-players", default=1, type=int)
	parser.add_argument("--human-players", default=1, type=int)
	parser.set_defaults(game_maker=makeTicTacToe)
	return parser