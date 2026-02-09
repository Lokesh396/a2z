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
    
def findMaxinCol( matrix,n, col):
    """
    Given an matrix and the column, we need to find the maximum value in that col.

    Algorithm:
    - Iterate through the column and update the index accordingly.

    Args:
        matrix: 2d matrix
        n: length of matrix
        col: column index
    Returns: returns the idx of the col with max element.

    Time Complexity: O(n)

    Space Complexity: O(1)

    """
    mx = matrix[0][col]
    idx = 0
    for i in range(1,n):
        if mx < matrix[i][col]:
            idx = i
            mx = matrix[i][col]

    return idx

def findPeakGrid( matrix: List[List[int]]) -> List[int]:

    """
    Given a matrix, we need to find the peak element such that left, right, top and bottom is less than
    the element.

    Algorithm:
    - we will start from left to right, and we pick the mid and find the maximum row in that column,
    and check whether left and right element is smaller than the picked element.
    - we need to eliminate the search space accordingly.

    Args:
        matrix: input 2d array
    
    Returns: returns the index of the peak element exists.

    Time Complexity:  O(mlgn)

    Space Complexity: O(1)
    """

    low = 0
    n = len(matrix)
    m = len(matrix[0])
    high = m-1

    while low <= high:
        
        mid =(low+high)//2
        row = findMaxinCol(matrix,n, mid)

        left = matrix[row][mid-1] if mid > 0 else -1
        right  = matrix[row][mid+1] if mid < m-1 else -1

        if matrix[row][mid] > left and matrix[row][mid] > right:
            return [row, mid]
        if matrix[row][mid] < right:
            low = mid + 1
        else:
            high = mid -1
    
    return [-1, -1]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    mat = []
    for i in range(n):
        arr=list(map(int, input().split()))
        mat.append(arr)
    
    print('peak Element:', findPeakGrid(mat))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()