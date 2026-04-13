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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1, m):
            n = len(triangle[i])
            for j in range(n):
                min_ = float('inf')
                if j != 0:
                    min_= min(min_, triangle[i-1][j-1])
                if j < i:
                    min_= min(min_, triangle[i-1][j])

                triangle[i][j] += min_
        
        return min(triangle[-1])
    
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()