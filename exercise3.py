#!/usr/bin/env python3

"""
   Assignment 1, Exercise 3, INF1340 Fall 2014

    Determine the winner of a game of Rock, Paper, Scissors between two players.
"""

__author__ = 'Evan Moir'
__email__ = "evan.moir@utoronto.ca"

__copyright__ = "2014 Evan Moir"
__license__ = "MIT License"

__status__ = "Submission Ready"


def decide_rps(player1, player2):
    """
    :param: player1: a string representing the play of the first player. Valid values are:
        "Rock"
        "Paper"
        "Scissors"
    :param: player2: a string representing the play of the second player. Valid values are:
        "Rock"
        "Paper"
        "Scissors"
    :return:
        integer: the result of the game:
            0 if the result is a tie
            1 is the winner is Player 1
            2 is the winner is Player 2
  :raises:
        TypeError if either input is not a string, with error string indicating which input(s) is/are not valid.
        ValueError if either input is not a valid move ("Rock", "Paper", "Scissors").
    """

    # Check that inputs are the correct type. Raise appropriate errors for all three cases of incorrect type.
    if type(player1) is not str:
        if type(player2) is not str:
            raise TypeError("Neither player's input is a string!")
        else:
            raise TypeError("Player 1's input is not a string!")
    if type(player2) is not str:
        raise TypeError("Player 2's input is not a string!")

    # Check that inputs are valid plays.
    valid_plays = ["Rock", "Paper", "Scissors"]
    if player1 not in valid_plays:
        raise ValueError("Player 1's play is not a valid move!")
    if player2 not in valid_plays:
        raise ValueError("Player 2's play is not a valid move!")

    # Once the inputs are verified, create a nested dictionary that emulates the matrix of possible game outcomes.
    # Note that the indexes are valid plays, so that the matrix can be "queried" using the inputs to determine
    # the game outcome.
    outcome_matrix = {
        "Rock": {"Rock": 0, "Paper": 2, "Scissors": 1},
        "Paper": {"Rock": 1, "Paper": 0, "Scissors": 2},
        "Scissors": {"Rock": 2, "Paper": 1, "Scissors": 0}
    }

    # "Query" the outcome matrix using the players' plays to determine the result, and return that.
    return outcome_matrix[player1][player2]