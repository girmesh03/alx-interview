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

Eg. without Recursion:

def minOperations(n):
    if n <= 1:
        return 0
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            operations += 2
        else:
            n = n - 1
            operations += 1
    return operations

"""


def minOperations(n):
    """ Calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""

    if n <= 1:
        return 0
    if n % 2 == 0:
        return 2 + minOperations(n // 2)
    else:
        return 1 + minOperations(n - 1)
