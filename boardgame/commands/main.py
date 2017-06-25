import argparse

from boardgame.gameconfig import GameConfig

SUBCOMMANDS = []
DESCRIPTION = """Play small boardgames like TicTacToe."""

import connectfour_commands
SUBCOMMANDS.append([connectfour_commands, "connectfour"])

import tictactoe_commands
SUBCOMMANDS.append([tictactoe_commands, "tictactoe"])

def gameRunner(args):
	config = GameConfig()
	config.hum_players=args.human_players
	config.ai_players=args.ai_players
	game = args.game_maker(config)
	while(not game.isGameOver()):
		game.runOnce()
	winner = game.getWinner()
	if winner is None:
		print "It's a draw"
	else:
		print "%s wins !"%winner.name

def parser():
	parser = argparse.ArgumentParser(description=DESCRIPTION)
	subparsers = parser.add_subparsers()
	for sc in SUBCOMMANDS:
		sub_parser = subparsers.add_parser(sc[1],
		                                      description=sc[0].DESCRIPTION,
		                                      help=sc[0].DESCRIPTION)
		sc[0].make_command_parser(sub_parser)

	parser.set_defaults(func=gameRunner)
	return parser

main_parser = parser()
