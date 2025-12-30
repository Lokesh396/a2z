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

def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    left, top, right, bottom = 0, 0, n-1, m-1
    ans = []
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
    
        top += 1
        for i in range(top, bottom+1):
            ans.append(matrix[i][right])
        
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1


    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    matrix = []
    m = int(input())
    for i in range(m):
        arr = list(map(int, input().strip().split()))
        matrix.append(arr)
    print('Spiral Matrix: ', spiralOrder(matrix=matrix))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()