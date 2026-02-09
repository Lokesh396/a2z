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
def upperBound(arr, t, n):
    """
    Given an array and target, return the upper bound of the target.

    Algorithm:
    - Do binary search on the search and eliminate the search space accordingly.

    Args:
        arr: input array
        t: target
        n: length of the array
    
    Returns: returns the upper bound of the target.
    """
    low = 0
    high = n -1
    while low <= high:

        mid = (low+high)//2
        if arr[mid] <= t:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

def countSmallEquals(matrix, m, n, mid):
    """
    Counting number of elements smaller than the given target.
    """
    cnt = 0
    for idx, row in enumerate(matrix):
        less = upperBound(row, mid,n)
        cnt += less
    return cnt

def median(matrix: List[int], m: int, n: int) -> int:
    """
    Given an row wise sorted matrix, return the median of the array

    Algorithm:
    - we will find the search space first bu finding the minimum and maximum element in the matrix.
    - After we will calculate the mid and serach for lessthan equals, if the less than equals or less
    than threshold, we will update low, else the high.

    Args:
        matrix: matrix array
        m: length of the matrix
        n: width of the matrix
    
    Returns: returns the median of the matrix

    Time Complexity: lg(mx) * nlgm

    Space Complexity: O(1)
    """
    # Write your code here.
    low = 1e9
    high = 0

    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][-1])

    threshold = (n*m)//2
    
    while low <= high:

        mid = (low + high)//2

        smallEquls = countSmallEquals(matrix, m,n, mid) 

        if smallEquls <= threshold:
            low = mid + 1
        else:
            high = mid - 1
    
    return low
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    mat = []
    for i in range(n):
        arr=list(map(int, input().split()))
        mat.append(arr)
    
    print('Median:', median(mat, len(mat), len(mat[0])))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()