#!/usr/bin/python3
"""0-minoperations.py module"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            n //= factor
            operations += factor

        factor += 1

    return operations
