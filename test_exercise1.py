#!/usr/bin/env python3

""" Module to test exercise1.py """

__author__ = 'Susan Sim (modified by Evan Moir)'
__email__ = "ses@drsusansim.org (evan.moir@utoronto.ca)"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Final Submission"

# imports one per line
import pytest
from exercise1 import grade_to_gpa


def test_letter_grade():
    """
    Letter grade inputs
    """

    # Positive Tests
    assert grade_to_gpa("A+") == 4.0
    assert grade_to_gpa("A") == 4.0
    assert grade_to_gpa("A-") == 3.7
    assert grade_to_gpa("B+") == 3.3
    assert grade_to_gpa("B") == 3.0
    assert grade_to_gpa("B-") == 2.7
    assert grade_to_gpa("FZ") == 0.0

    # Negative Tests
    assert grade_to_gpa("A+") == 0.0
    assert grade_to_gpa("A") == 3.7
    assert grade_to_gpa("A-") == 3.3
    assert grade_to_gpa("B+") == 3.0
    assert grade_to_gpa("B") == 2.7
    assert grade_to_gpa("B-") == 0.0
    assert grade_to_gpa("FZ") == 4.0

    # Invalid string inputs
    with pytest.raises(ValueError):
        grade_to_gpa("q")
    with pytest.raises(ValueError):
        grade_to_gpa("wfucgwiubwt")
    with pytest.raises(ValueError):
        grade_to_gpa("1234567890")


def test_percentage_grade():
    """
    Numeric grade inputs
    """

    # Positive tests
    assert grade_to_gpa(100) == 4.0
    assert grade_to_gpa(95) == 4.0
    assert grade_to_gpa(90) == 4.0
    
    assert grade_to_gpa(89) == 4.0
    assert grade_to_gpa(87) == 4.0
    assert grade_to_gpa(85) == 4.0

    assert grade_to_gpa(84) == 3.7
    assert grade_to_gpa(82) == 3.7
    assert grade_to_gpa(80) == 3.7

    assert grade_to_gpa(79) == 3.3
    assert grade_to_gpa(78) == 3.3
    assert grade_to_gpa(77) == 3.3

    assert grade_to_gpa(76) == 3.0 
    assert grade_to_gpa(74) == 3.0
    assert grade_to_gpa(73) == 3.0

    assert grade_to_gpa(72) == 2.7
    assert grade_to_gpa(71) == 2.7
    assert grade_to_gpa(70) == 2.7

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(0) == 0.0

    # Negative Tests

    assert grade_to_gpa(100) == 0.0
    assert grade_to_gpa(95) == 1.0
    assert grade_to_gpa(90) == 2.7

    assert grade_to_gpa(89) == 3.0
    assert grade_to_gpa(87) == 1.1
    assert grade_to_gpa(85) == 0.0

    assert grade_to_gpa(84) == 4.0
    assert grade_to_gpa(82) == 1.0
    assert grade_to_gpa(80) == 3.3

    assert grade_to_gpa(79) == 2.7
    assert grade_to_gpa(78) == 4.0
    assert grade_to_gpa(77) == 3.7

    assert grade_to_gpa(76) == 4.0
    assert grade_to_gpa(74) == 2.7
    assert grade_to_gpa(73) == 0.0

    assert grade_to_gpa(72) == 4.0
    assert grade_to_gpa(71) == 3.3
    assert grade_to_gpa(70) == 0.0

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(0) == 0.0

    # Integer inputs that are out of valid range (0-100).
    with pytest.raises(ValueError):
        grade_to_gpa(101)
    with pytest.raises(ValueError):
        grade_to_gpa(-1)

    # Float test (wrong type!)
    with pytest.raises(TypeError):
        grade_to_gpa(50.0)

test_letter_grade()
test_percentage_grade()
test_float_intput()
