from setuptools import setup, find_packages
from boardgame import (
    VERSION,
    SMALL_DESCRIPTION,
    LONG_DESCRIPTION
)

setup(
    name='boardgame',
    version=VERSION,
    description=SMALL_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Surya Ambrose',
    author_email='surya.ambrose@gmail.com',
    packages=[
        'boardgame',
        'boardgame.commands',
        'boardgame.ai',
        'boardgame.tictactoe',
        'boardgame.connectfour'
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Games/Entertainment :: Board Games",
    ],
    requires=[],
    license = "MIT",
    scripts=['bin/boardgame']
)
