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

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] or obstacleGrid[0][0] :
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = -1
        obstacleGrid[0][0] = 1
        
        for i in range(1,m):
            if not obstacleGrid[i][0] == -1:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
        
        for i in range(1,n):
            if not obstacleGrid[0][i] == -1:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j] == -1:
                    top = obstacleGrid[i-1][j]
                    left = obstacleGrid[i][j-1]
                    if top == -1 and left == -1:
                        obstacleGrid[i][j] = -1
                    else:
                        if top == -1:
                            top = 0
                        elif left == -1:
                            left = 0
                        obstacleGrid[i][j] = top + left
                        
        return obstacleGrid[m-1][n-1] if not obstacleGrid[m-1][n-1] == -1 else 0

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()