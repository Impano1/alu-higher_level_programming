#!/usr/bin/python3
import sys

def n_queens(N):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == N:
            solutions.append(board.copy())
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(board, 0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = n_queens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])
