#!/usr/bin/python3
"""Validation for UTF-8 encoding"""


def validUTF8(data):
    """Validates a given data set as UTF-8"""
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 7) == 0b0:
                num_bytes = 0
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

        return num_bytes == 0