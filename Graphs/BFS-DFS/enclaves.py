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

def numEnclaves( grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            
            grid[i][j] = 0

            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i+1, j)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1,j)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
        
        return cnt
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()