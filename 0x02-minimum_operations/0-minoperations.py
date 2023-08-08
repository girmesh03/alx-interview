#!/usr/bin/python3

"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result in
exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH =>
Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """ Calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""

    if n <= 1:
        return 0

    operations = n  # Initialize with a worst-case value

    # Try all possible divisors up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # We can generate n by copying i times and
            # then pasting n // i times
            operations = min(operations, minOperations(i) + n // i)
            # We can generate n by copying n // i times
            # and then pasting i times
            operations = min(operations, minOperations(n // i) + i)

    return operations
