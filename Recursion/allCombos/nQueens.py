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

def isvalid(matrix, n, x,y):
    for i in range(n):
        if matrix[i][y] == 'Q':
            return False
    tempx = x
    tempy = y
    while tempx > 0 and tempy > 0:
        tempx -= 1
        tempy -= 1
        if matrix[tempx][tempy] == 'Q':
            return False
    tempx = x
    tempy = y
    while tempx > 0 and tempy < n-1:
        tempx -= 1
        tempy += 1
        if matrix[tempx][tempy] == 'Q':
            return False
    return True
def generate(n, matrix, idx,ans):
    if idx == n:
        out = []
        for row in matrix:
            out.append("".join(row))
        ans.append(out)
        return
    
    for idy in range(n):
        if isvalid(matrix,n,idx,idy):
            matrix[idx][idy] ='Q'
            generate(n, matrix,idx+1,ans)
            matrix[idx][idy] = '.'
        

def solveNQueens( n: int) -> List[List[str]]:
    ans = []
    matrix = [['.' for _ in range(n)] for i in range(n)]
    generate(n, matrix, 0, ans)
    return ans
    

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    print('N queens:', solveNQueens(n))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()