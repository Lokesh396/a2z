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

def searchMatrixBetter( matrix: List[List[int]], target: int) -> bool:
    """
    Given a matrix which is sorted row an column wise, search if a target exists or not if exists
    return True else False

    Algorithm:
    - Given the matrix is sorted row wise we can check each row whether the target is in range or not,
    if the target is in the range of a particaulr we can don binary search on that row.

    Args:
        matrix: 2d matrix which is our search space
        target: elements that needs to find

    Returns: returns true if element exists else false

    Time Complexity: O(n+lgm)

    Space Complexity: O(1)
    """
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

def searchMatrix( matrix: List[List[int]], target: int) -> bool:
    """
    Given matrix and target return if the return if that target exists in the matrix or not

    Algorithm:
    - we stand at the top most right corner, now the column is sorted and we are at the maximum of
    that row.
    - we will check whether the target is greater than the corner position, if that is greater means we
    can definitely say we cant find that element in that row, if it is smaller we will move left.

    Args:
        matrix: 2d matrix which is our search space
        target: elements that needs to find

    Returns: returns true if element exists else false

    Time Complexity: O(n+m)

    Space Complexity: O(1)

    """
    n = len(matrix)

    m = len(matrix[0])
    row, col = 0, m-1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    
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
    print('Target Found:', searchMatrixBetter(mat, target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()