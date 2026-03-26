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

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    Pattern: DFS / Flood Fill
    Difficulty: Easy
    Key Insight: DFS from the source pixel recolors all connected same-colored cells; early exit if source already equals the target color avoids infinite loop.
    Related: islands.py, enclaves.py, surroundingRegions.py
    """
    if image[sr][sc] == color:
        return image
    m = len(image)
    n = len(image[0])
    def dfs(i, j, prev):
        if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != prev:
            return
        image[i][j] = color
        for x, y in [[-1,0], [0, -1],[1,0], [0, 1]]:
            dfs(i+x,j+y, prev)
    
    dfs(sr, sc, image[sr][sc])
    return image
    
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()