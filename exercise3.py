#!/usr/bin/env python3

"""
   Assignment 1, Exercise 3, INF1340 Fall 2014

    Determine the winner of a game of Rock, Paper, Scissors between two players.

    :param:
        player1, player2: Strings representing the plays of the two players. The following are valid plays:

        "Rock"
        "Paper"
        "Scissors"

    :return:
        integer: the result of the game.
        - 0 if the result is a tie
        - 1 is the winner is Player 1
        - 2 is the winner is Player 2

    :raises:
        TypeError if either input is not a string.
        ValueError if either input is not a valid move ("Rock", "Paper", "Scissors").
"""

__author__ = 'Evan Moir'
__email__ = "evan.moir@utoronto.ca"

__copyright__ = "2014 Evan Moir"
__license__ = ""

__status__ = "Submission Ready"


def decide_rps(player1, player2):

    # Check that inputs are the correct type.
    if (type(player1) is not str):
        raise TypeError("Player 1's input is not a string!")
    if (type(player2) is not str):
        raise TypeError("Player 2's input is not a string!")

    # Check that inputs are valid plays.
    if ((player1 != "Rock") and (player1 != "Paper") and (player1 != "Scissors")):
        raise ValueError("Player 1's play is not a valid move!")
    if ((player2 != "Rock") and (player2 != "Paper") and (player2 != "Scissors")):
        raise ValueError("Player 2's play is not a valid move!")

    # Once inputs are verified, check the game logic to determine play result:

    # If both players submit the same value, it's a tie.
    if (player1 == player2):
        return 0
    else:
        # If the result is not a tie:
        # Create a data object using nested dictionaries that represents the win states for Player 1,
        # as a function of the inputs.
        # Use Player 1 and Player 2's plays as the keys.

        player1_win_states = {
            "Rock": {"Scissors": True},
            "Paper": {"Rock": True},
            "Scissors": {"Paper": True}
        }

        # If the value at the key index described by the inputs returns True, Player 1 wins.
        if player1_win_states{player1}{player2}:
            return 1

        # If it's not a tie, and Player 1 didn't win, Player 2 must have won.
        else:
            return 2