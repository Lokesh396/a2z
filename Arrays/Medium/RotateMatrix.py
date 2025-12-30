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
def rotate(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    matrix = []
    m = int(input())
    for i in range(m):
        arr = list(map(int, input().strip().split()))
        matrix.append(arr)
    print('Matrix before rotating', matrix)
    rotate(matrix=matrix)
    print('Matrix after rotating', matrix)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()