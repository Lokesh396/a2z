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
def possible(node,c, colA, mat):

    for idx, child in enumerate(mat[node-1]):
        if child and colA[idx+1] == c:
            return False
    
    return True

def dfs(node, n, m, colA, mat):
    if node == n:
        return True
    
    for i in range(1, m+1):

        if possible(node, i, colA, mat):
            colA[node] = i
            if dfs(node+1,n,m,colA, mat):
                return True
            colA[node] = 0
        
    
    return False


def graphColoring(mat: List[List[int]], m: int) -> str:
    # Write your code here
    colA = [0 for _ in range(len(mat)+1)]

    if dfs(1, len(mat)+1, m, colA, mat):
        return 'YES'

    return 'NO'
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()