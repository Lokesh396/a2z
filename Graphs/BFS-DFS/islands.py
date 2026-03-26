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

def numIslands(self, grid: List[List[str]]) -> int:
        """
        Pattern: DFS / Flood Fill
        Difficulty: Medium
        Key Insight: Each DFS from an unvisited '1' sinks the whole island (marks cells '0'); count how many times DFS is triggered = number of islands.
        Related: provinces.py, floodFill.py, enclaves.py
        """
        m = len(grid)
        n = len(grid[0])
        def traverse(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                x = i + dx
                y = j + dy

                traverse(x, y)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    traverse(i, j)
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