#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = 'Evan Moir'
__email__ = "evan.moir@utoronto.ca"

__copyright__ = "2014 Evan Moir"
__license__ = "MIT License"

__status__ = "Final Submission"

# imports one per line
import pytest
from exercise3 import decide_rps


def test_decide_rps():
    """
    Inputs that are the correct format and length. All correct cases covered
    """
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1

    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Paper") == 2

    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Scissors") == 0

    # Some incorrect cases:

    assert decide_rps("Rock", "Rock") == 1
    assert decide_rps("Paper", "Paper") == 2
    assert decide_rps("Rock", "Paper") == 1
    assert decide_rps("Paper", "Scissors") == 0
    assert decide_rps("Paper", "Rock") == 2
    assert decide_rps("Paper", "Paper") == 2

    # One or more input is not a string:

    with pytest.raises(TypeError):
        decide_rps(1, "string!")
    with pytest.raises(TypeError):
        decide_rps("string!", 1)
    with pytest.raises(TypeError):
        decide_rps(80.0, 9)

    # One or more inputs are not valid moves:

    with pytest.raises(ValueError):
        decide_rps("rock", "Scissors")
    with pytest.raises(ValueError):
        decide_rps("Paper", "rock")
    with pytest.raises(ValueError):
        decide_rps("cqaefvcurbcwwr", "cwncuwctwruybtwub")
