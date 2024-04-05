#!/usr/bin/python3
"""Validation for UTF-8 encoding"""


def validUTF8(data):
    """Validates a given data set as UTF-8"""
    num_bytes, maskF, maskC = 0, 1 << 7, 1 << 6

    for n in data:
        mask = maskF
        if num_bytes == 0:
            while mask & n:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes == 4:
                return False
        else:
            if not (n & maskF and not (n & maskC)):
                return False
        num_bytes -= 1
    return num_bytes == 0
