""""
    This is a Regression Test Suite to automatically test all combinations of games and ML frameworks. Each test
    plays two quick games using an untrained neural network (randomly initialized) against a random player.

    In order for the entire test suite to run successfully, all the required libraries must be installed.  They are:
    Pytorch, Keras.

     [ Games ]      Pytorch      Keras
      -----------   -------      -----
    - Othello        [Yes]       [Yes]
    - TicTacToe                  [Yes]
    - TicTacToe3D                [Yes]
    - Connect4                   [Yes]
    - Gobang                     [Yes]
    - Tafl           [Yes]       [Yes]
    - Rts                        [Yes]
    - DotsAndBoxes               [Yes]
"""

import unittest

import Arena
from MCTS import MCTS

from othello.OthelloGame import OthelloGame
from othello.pytorch.NNet import NNetWrapper as OthelloPytorchNNet
from othello.keras.NNet import NNetWrapper as OthelloKerasNNet

from quoridor.QuoridorGame import QuoridorGame
from quoridor.QuoridorPlayers import RandomPlayer
from quoridor.pytorch.NNet import NNetWrapper as QuoridorPytorchNNet


import numpy as np
from utils import *


class TestAllGames(unittest.TestCase):

    @staticmethod
    def execute_game_test(game, neural_net):
        rp = RandomPlayer(game).play

        args = dotdict({'numMCTSSims': 25, 'cpuct': 1.0})
        mcts = MCTS(game, neural_net(game), args)
        n1p = lambda x: np.argmax(mcts.getActionProb(x, temp=0))

        arena = Arena.Arena(n1p, rp, game)
        print(arena.playGames(2, verbose=False))
   
    def test_othello_pytorch(self):
        self.execute_game_test(OthelloGame(6), OthelloPytorchNNet)

    def test_othello_keras(self):
        self.execute_game_test(OthelloGame(6), OthelloKerasNNet)

    def test_quoridor(self):
        self.execute_game_test(QuoridorGame(5), QuoridorPytorchNNet)


if __name__ == '__main__':
    unittest.main()
