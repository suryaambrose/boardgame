from setuptools import setup, find_packages
from boardgame import VERSION, DESCRIPTION

setup(
    name='boardgame',
    version=VERSION,
    description=DESCRIPTION,
    author='Surya Ambrose',
    author_email='surya.ambrose@gmail.com',
    packages=[
        'boardgame',
        'boardgame.commands',
        'boardgame.ai',
        'boardgame.tictactoe',
        'boardgame.connectfour'
    ],
    requires=[],
    license = "MIT",
    scripts=['bin/boardgame']
)
