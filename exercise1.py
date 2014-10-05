#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = "Susan Sim (modified by Evan Moir)"
__email__ = "ses@drsusansim.org (evan.moir@utoronto.ca)"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Final Submission"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    # Check if the input is a string (str). If so, run through the letter grade to GPA logic to determine GPA value.
    if type(grade) is str:
        if (letter_grade == "A") or (letter_grade == "A+"):
            gpa = 4.0
        elif letter_grade == "A-":
            gpa = 3.7
        elif letter_grade == "B+":
            gpa = 3.3
        elif letter_grade == "B":
            gpa = 3.0
        elif letter_grade == "B-":
            gpa = 2.7
        elif letter_grade == "FZ":
            gpa = 0.0
        else:
            # Error handling for string input that doesn't correspond to a valid grade.
            raise ValueError("Passed string grade is not a valid letter grade!")

    # Check if the input is an integer (int). If so, run through the numeric grade to GPA logic to determine GPA value.
    elif type(grade) is int:
        if ((letter_grade <= 100) and (letter_grade > 84)):
            gpa = 4.0
        elif letter_grade > 79:
            gpa = 3.7
        elif letter_grade > 76:
            gpa = 3.3
        elif letter_grade > 72:
            gpa = 3.0
        elif letter_grade > 69:
            gpa = 2.7
        elif ((letter_grade < 70) and (letter_grade >= 0)):
            gpa = 0.0
        else:
            # Error handling for integer input that doesn't fall within the range of 0-100.
            raise ValueError("Passed integer grade does not fall between 0 and 100!")

    # Error handling for input that is neither int or string
    else:
        raise TypeError("Invalid type passed as parameter!")

    return gpa

