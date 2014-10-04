#!/usr/bin/env python3

"""
   Assignment 1, Exercise 3, INF1340 Fall 2014

    Determine the winner of a game of Rock, Paper, Scissors. The function assumes that each player's play will
    given as one of the following strings:

    "Rock"
    "Paper"
    "Scissors"

    :param player1, player2: Strings representing the plays of the
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
"""

__author__ = 'Evan Moir
__email__ = "evan.moir@utoronto.ca"

__copyright__ = "2014 Evan Moir"
__license__ = ""

__status__ = "Submission Ready"

def decide_rps(player1, player2):

    # If both players submit the same value, it's a tie.
    if (player1 == player2):
        return 0
    else:

        # If the result is not a tie, create a data object using nested dictionaries that summarizes the win states for
        # Player 1 for each play as a function of Player 2's play.
        winMatrix = {
            "Rock": {"Scissors": True},
            "Paper": {"Rock": True},
            "Scissors": {"Paper": True}
        }

        # If the value at the index described by the input returns True, Player 1 wins...
        if winMatrix[player1][player2]:
            return 1

        # ... otherwise, Player 2 wins.
        else:
            return 2