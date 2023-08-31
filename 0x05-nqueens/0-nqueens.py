#!/usr/bin/python3
"""N queens"""

import sys


def printBoard(board, n):
    """Prints the board"""
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                res.append([i, j])
    print(res)


if __name__ == "__main__":
    """Solves the N queens problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for j in range(n)] for i in range(n)]

    def isSafe(board, row, col):
        """Checks if a queen can be placed on board at row, col"""
        for j in range(col):
            if board[row][j] == 1:
                return False
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        i = row
        j = col
        while j >= 0 and i < n:
            if board[i][j] == 1:
                return False
            i = i + 1
            j = j - 1
        return True

    def solveNQUtil(board, col):
        """Solves the N queens problem using Backtracking"""
        if col == n:
            printBoard(board, n)
            return True
        res = False
        for i in range(n):
            if isSafe(board, i, col):
                board[i][col] = 1
                res = solveNQUtil(board, col + 1) or res
                board[i][col] = 0
        return res

    solveNQUtil(board, 0)
