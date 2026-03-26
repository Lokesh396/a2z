import sys
import os
from pathlib import Path
from typing import List
from collections import deque

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Pattern: Multi-Source BFS
        Difficulty: Medium
        Key Insight: Start BFS from all 0-cells simultaneously and propagate distance outward — avoids TLE compared to running BFS from each 1-cell individually.
        Related: rottingOranges.py
        """
        rows, cols = len(mat), len(mat[0])
        dis = [[-1] * cols for _ in range(rows)]

        q =deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    dis[i][j] = 0
                    
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        while q:
            x, y, t = q.popleft()

            for dx, dy in directions:
                ni = x + dx
                ny = y + dy

                if  0<= ni < rows and 0 <= ny < cols and dis[ni][ny]==-1:
                    dis[ni][ny] = t + 1
                    q.append((ni, ny, t+1))
        
        return dis
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()