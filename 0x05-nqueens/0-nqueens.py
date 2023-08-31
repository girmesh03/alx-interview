#!/usr/bin/python3
"""N queens"""

import sys


def printBoard(board):
    """Prints the board"""
    n = len(board)
    print("[", end="")
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end="")
                if i != n - 1:
                    print(", ", end="")
    print("]")

def isSafe(board, row, col):
    """Checks if a queen can be placed on board at row, col"""
    n = len(board)
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """Solves the N queen problem using Backtracking"""
    n = len(board)
    if col == n:
        printBoard(board)
        return True
    res = False
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ(n):
    """Solves the N queen problem using Backtracking"""
    board = [[0 for j in range(n)] for i in range(n)]
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False
    return True


if __name__ == "__main__":
    """Solves the N queen problem"""
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
    solveNQ(n)
