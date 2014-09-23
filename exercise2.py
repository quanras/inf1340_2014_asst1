#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string
    if type(upc) is not str:
        raise TypeError("Passed UPC is not a valid string!")

    # check length of string
    # raise ValueError if not 12
    if len(upc) < 12:
        raise ValueError("Passed UPC is too short!")
    if len(upc) > 12:
        raise ValueError("Passed UPC is too long!")

    # convert string to array
    # hint: use the list function
    upcList = list(upc)   # NEED TO CHECK IF THESE ARE INTS

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # Calculate sum of values at odd indices and multiply by 3.
    oddValues = 3 * (upcList[0] + upcList[2] + upcList[4] + upcList[6] + upcList[8] + upcList[10])

    # Calculate sum of values at even indices
    evenValues = upcList[1] + upcList[3] + upcList[5] + upcList[7] + upcList[9]

    # Sum values calculated from odd and even indices
    allValues = oddValues + evenValues

    # Determine modulo 10
    moduloValue = allValues % 10

    # return True if they are equal, False otherwise

    return False

