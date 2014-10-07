#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """

    # Some positive tests and some negative tests
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("121846511984") is True
    assert checksum("121846511980") is False
    assert checksum("121846511984") is False
    assert checksum("121846511980") is True


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
    with pytest.raises(TypeError):
        checksum(786936224306)
    with pytest.raises(TypeError):
        checksum(True)

    with pytest.raises(ValueError):
        checksum("1")
    with pytest.raises(ValueError):
        checksum("1234567890")
    with pytest.raises(ValueError):
        checksum(123)
    with pytest.raises(ValueError):
        checksum("True")
    with pytest.raises(ValueError):
        checksum("upc")
    with pytest.raises(ValueError):
        checksum("100.0")

test_checksum()
test_input()