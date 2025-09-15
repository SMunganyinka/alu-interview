#!/usr/bin/python3

"""
Return the fewest operations needed to reach
n 'H' characters using Copy All and Paste.

- def minOperations(n): → int
- Returns 0 if n ≤ 1
- Uses prime factorization to compute minimal steps
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
