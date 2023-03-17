#!/usr/bin/env python3
import sys

# check if n is valid
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

# check if the queen in column x conflicts with the queens in the previous columns
def is_valid(board, x, y):
    for i in range(x):
        if board[i] == y or abs(i - x) == abs(board[i] - y):
            return False
    return True

# recursively find all solutions
def n_queens(board, x):
    if x == n:
        print(board)
        return
    for y in range(n):
        if is_valid(board, x, y):
            board.append(y)
            n_queens(board, x + 1)
            board.pop()

# solve the problem
board = []
n_queens(board, 0)

