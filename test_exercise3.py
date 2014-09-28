#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
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