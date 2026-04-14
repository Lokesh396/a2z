import sys
import os
from pathlib import Path
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here
    dp = [[[None for i in range(c)] for _ in range(c)] for _ in range(r)]

    def f(i, j1, j2):
        if j1 < 0 or j2 < 0 or j1 > c-1 or j2 > c-1:
            return 0
        if i == r-1:
            if j1 == j2:
                return grid[i][j1]

            return grid[i][j1] + grid[i][j2]
        
        if dp[i][j1][j2] is not None:
            return dp[i][j1][j2]
        maxi = -float('inf')
        for k in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if j1 == j2:
                    value = grid[i][j1] + f(i+1, j1+k, j2+l)
                else:
                    value = grid[i][j1] + grid[i][j2] + f(i+1, j1+k, j2+l)
                maxi = max(maxi,value)
        dp[i][j1][j2] = maxi
        return maxi
        
    return f(0,0,c-1)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()