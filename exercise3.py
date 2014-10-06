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

    # Once inputs are verified, check the game logic to determine play result. There are 3 possible outcomes:
    #   A tie
    #   Player 1 wins
    #   Player 2 wins

    # If both players submit the same value, it's a tie.
    if player1 == player2:
        return 0
    else:
        # If the result is not a tie:
        # Create a data object using nested dictionaries that represents the win states for Player 1 as a function of
        # both inputs in their listed order (player1, player2). This is essentially re-creating 1/3 of the results table
        # that was created on paper - only those tables cells that represented wins for Player 1.
        player1_win_states = {
            "Rock": {"Scissors": True},
            "Paper": {"Rock": True},
            "Scissors": {"Paper": True}
        }

        # If the value at the key index described by the inputs returns True, Player 1 wins.
        if player1_win_states[player1][player2]:
            return 1

        # If it's not a tie, and Player 1 didn't win, Player 2 must have won.
        else:
            return 2