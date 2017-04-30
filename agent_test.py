"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import datetime
import random

from importlib import reload
random.seed(1)


def return_time_dummy():
    return random.randint(1,10000)


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_MinimaxPlayer_legal_move(self):
        self.setUp()
        self.game.apply_move((2, 1))
        self.game.apply_move((3, 3))
        move = game_agent.MinimaxPlayer().get_move(self.game, return_time_dummy)
        legal_moves = self.game.get_legal_moves(self.player1)
        self.assertTrue(move in legal_moves)

    def test_AlphaBetaPlayer_legal_move(self):
        self.setUp()
        self.game.apply_move((2, 1))
        self.game.apply_move((4, 4))
        move = game_agent.AlphaBetaPlayer().get_move(self.game, return_time_dummy)
        legal_moves = self.game.get_legal_moves(self.player1)
        self.assertTrue(move in legal_moves)

    def test_L_shaped_moves(self):
        self.setUp()
        self.game.apply_move((0,0))
        self.game.apply_move((4, 4))
        player1_valid_moves = game_agent.L_shaped_moves(self.game, self.player1)
        player2_valid_moves = game_agent.L_shaped_moves(self.game, self.player2)
        self.assertIsNotNone(player1_valid_moves)
        self.assertIsNotNone(player2_valid_moves)
        self.assertTrue((1, 2) in player1_valid_moves)
        self.assertTrue((3, 2) in player2_valid_moves)


    def test_custom_score(self):
        self.setUp()
        self.game.apply_move((2,1))
        self.game.apply_move((3, 3))
        player1_custom_score = game_agent.custom_score(self.game, self.player1)
        self.assertIsNotNone(player1_custom_score)
        self.assertIsInstance(player1_custom_score, float)

    def test_custom_score_2(self):
        self.setUp()
        self.game.apply_move((2,1))
        self.game.apply_move((3, 3))
        player1_custom_score = game_agent.custom_score_2(self.game, self.player1)
        self.assertIsNotNone(player1_custom_score)
        self.assertIsInstance(player1_custom_score, float)

    def test_custom_score_3(self):
        self.setUp()
        self.game.apply_move((2,1))
        self.game.apply_move((3, 3))
        player1_custom_score = game_agent.custom_score_3(self.game, self.player1)
        self.assertIsNotNone(player1_custom_score)
        self.assertIsInstance(player1_custom_score, float)



if __name__ == '__main__':
    unittest.main()
