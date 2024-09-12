#!/usr/bin/python3
"""N queens puzzle"""
import sys
from typing import List


def solveNQueens(n: int) -> List[List[int]]:
    """Solve N queens puzzle"""
    def solve(queens, xy_dif, xy_sum):
        """Solve N queens puzzle"""
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                solve(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    result = []
    solve([], [], [])
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solveNQueens(n)
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)
    print()
