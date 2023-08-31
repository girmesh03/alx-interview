#!/usr/bin/python3
"""
Module for 0x0C. N Queens.
"""
from sys import argv, exit


def solveNQueens(n):
    """Program that solves the N queens problem"""
    res = []
    queens = [-1] * n
    col_diff = [0] * n
    diag_diff = [0] * (2 * n)
    diag_sum = [0] * (2 * n)

    def dfs(index):
        """Recursively resolves the N queens problem"""
        if index == len(queens):  # n queens have been placed correctly
            res.append(queens[:])
            return  # backtracking
        for i in range(len(queens)):
            if not col_diff[i] and not \
                    diag_diff[index - i] and not diag_sum[index + i]:
                queens[index] = i
                col_diff[i] = 1
                diag_diff[index - i] = 1
                diag_sum[index + i] = 1
                dfs(index + 1)
                col_diff[i] = 0
                diag_diff[index - i] = 0
                diag_sum[index + i] = 0

    dfs(0)
    return [[[row, col] for row, col in enumerate(queens)]
            for queens in res]


if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solveNQueens(n)
        for board in result:
            print(board)
