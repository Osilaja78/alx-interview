#!/usr/bin/python3
"""0-nqueens.py module"""
import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column"""

    for i in range(row):
        if board[i] == col:
            return False
        # Check if there is a queen in the diagonal
        if abs(row - i) == abs(col - board[i]):
            return False
    return True


def solve_nqueens(N):
    """Solve the nqueens board"""

    def solve(board, row):
        if row == N:
            return [board[:]]
        solutions = []
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solutions += solve(board, row + 1)
                board[row] = -1
        return solutions

    board = [-1] * N

    return solve(board, 0)


def print_solutions(N):
    """Print the solution to output"""

    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    print_solutions(N)
