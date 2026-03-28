import sys
import os
from pathlib import Path
import heapq
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        if grid[0][0] == 1:
            return -1
        m = len(grid)
        n = len(grid[0])
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1],[0, 1], [1,-1], [1, 0], [1, 1]]
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        while pq:
            d, i, j = heapq.heappop(pq)

            if i == m-1 and j == n-1:
                return d+1
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or  y < 0 or y >= n or grid[x][y] == 1:
                    continue
                heapq.heappush(pq, (d+1, x, y))
                grid[x][y] = 1

        
        return -1
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()