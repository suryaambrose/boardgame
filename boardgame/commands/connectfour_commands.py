from boardgame.connectfour import makeConnectFour

DESCRIPTION = "Starts a ConnectFour game"

def make_command_parser(parser):
	parser.add_argument("--ai-players", default=1, type=int)
	parser.add_argument("--human-players", default=1, type=int)
	parser.set_defaults(game_maker=makeConnectFour)
	return parser