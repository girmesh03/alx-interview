#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest number
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        while coin <= total:
            total -= coin
            count += 1

    if total != 0:
        return -1

    return count
