import sys
import os
from pathlib import Path
from collections import deque
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def orangesRotting( grid: List[List[int]]) -> int:
    
    q = deque()
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j, 0))
    
    max_time = 0
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    while q:
        i, j, t = q.popleft()
        max_time = max(max_time, t)

        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 2
                q.append((x, y, t+1))
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1
    
    return max_time
        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()