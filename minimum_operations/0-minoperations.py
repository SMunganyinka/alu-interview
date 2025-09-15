#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
to achieve n 'H' characters in a file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    The only operations allowed are 'Copy All' and 'Paste'.
    Starts with a single character 'H'.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations. Returns 0 if n is impossible
             to achieve or n <= 1.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    num_h = n  # Use a mutable copy of n
    divisor = 2

    while num_h > 1:
        # While divisor is a factor of num_h
        while num_h % divisor == 0:
            operations += divisor
            num_h //= divisor
        divisor += 1

    return operations
