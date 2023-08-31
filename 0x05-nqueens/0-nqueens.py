#!/usr/bin/python3
"""N Queens"""
import sys

def print_board(board):
    """Print allocated positions of the queens"""
    b = [[i, board[i]] for i in range(len(board))]
    print(b)

def is_position_safe(board, row, col):
    """Checks if the position is safe for the queen"""
    for prev_row in range(row):
        if board[prev_row] == col or \
           abs(board[prev_row] - col) == abs(prev_row - row):
            return False
    return True

def safe_positions(board, row, n):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board)
    else:
        for col in range(n):
            if is_position_safe(board, row, col):
                board[row] = col
                safe_positions(board, row + 1, n)

def create_board(size):
    """Generates the board"""
    return [0] * size

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

board = create_board(n)
safe_positions(board, 0, n)
