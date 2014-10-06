#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = "Susan Sim (modified by Evan Moir)"
__email__ = "ses@drsusansim.org (evan.moir@utoronto.ca)"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Final Submission"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input, raise TypeError if not string.
    if type(upc) is not str:
        raise TypeError("Passed UPC is not a valid string!")

    # check length of string, raise ValueError if not 12.
    if len(upc) < 12:
        raise ValueError("Passed UPC is too short!")
    if len(upc) > 12:
        raise ValueError("Passed UPC is too long!")

    # convert string to array
    # hint: use the list function
    upc_list = list(upc)

    # Calculate sum of values at odd indices and multiply by 3. Then add values at even indices.
    index_sum = (3 * (upc_list[0] + upc_list[2] + upc_list[4] + upc_list[6] + upc_list[8] + upc_list[10])) + \
                (upc_list[1] + upc_list[3] + upc_list[5] + upc_list[7] + upc_list[9])

    # Determine modulo 10 value.
    modulo_value = index_sum % 10
    if modulo_value is not 0:
        modulo_value = 10 - modulo_value

    # Return True if they are equal, False otherwise
    if modulo_value == upc_list[11]:
        return True
    else:
        return False

