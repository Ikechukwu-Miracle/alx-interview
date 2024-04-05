#!/usr/bin/python3
"""Minimum operations required to print a certain number of characters."""


def minOperations(n):
    """Returns the required minimum operations"""
    if n <= 1:
        return 0

    for i in range (2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
