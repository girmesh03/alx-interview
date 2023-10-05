#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve2 = sieve[:]
    for i in range(1, n + 1):
        sieve2[i] = sieve2[i - 1] + (sieve[i])
    player = 0
    for n in nums:
        player += sieve2[n] % 2 == 1
    if player * 2 == len(nums):
        return None
    if player * 2 > len(nums):
        return "Maria"
    return "Ben"
