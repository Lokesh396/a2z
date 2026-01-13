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

def searchMatrix( matrix: List[List[int]], target: int) -> bool:

    n = len(matrix)

    for i in range(n):
        if matrix[i][0] <= target and target <= matrix[i][-1]:

            low = 0
            high = len(matrix[0]) - 1
            while low <= high:

                mid = (low + high) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
    
    return False

def searchMatrixOptimized(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = n * m - 1
    while low <= high:

        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    mat = []
    for i in range(n):
        arr=list(map(int, input().split()))
        mat.append(arr)
    target = int(input())
    
    print('Target Found:', searchMatrix(mat, target=target))
    print('Target Found:', searchMatrixOptimized(mat, target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()