import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")
def path(arr, n, i, j, curr, ans, visited):
    if i < 0 or j < 0 or  i > n-1 or j > n-1 or arr[i][j] == 0 or (i, j) in visited:
        return
    if i == n-1 and j == n-1:
        ans.append("".join(curr))
        return
    visited.add((i,j))
    for x,y,d in [(0,-1,'L'), (0,1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]:
        dx = i + x
        dy = j + y
        curr.append(d)
        path(arr, n, dx,dy,curr, ans, visited)
        curr.pop()
    visited.remove((i, j))


def searchMaze(arr, n):
    # Write your code here.
    ans = []
    path(arr, n, 0, 0, [], ans, set())
    ans.sort()
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()