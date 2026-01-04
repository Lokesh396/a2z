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
def setZeroes(matrix):
    """
    
    Given an 2d array, which contains zeroes, if we find a zero, make the containing row and col
    elements to zero.

    Algorithm:
    - we will store the zero elements in the row zero and col zero, the intersection part will be
    stored in col1.
    - we iterate through the array from row1, col1 and map the zero elements.
    - we will map the zero row first then followed by col zero.

    Args:
        matrix: 2d matrix
    
    Returns: returns the 2d array, by setting zeroes.

    Time Complexity: O(n^2) iterating through the entire matrix.

    Space Complexity: O(1) no extra space required.
    """
    m = len(matrix)
    n = len(matrix[0])
    col1 = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col1 = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    for i in range(1,n):
        if matrix[0][0] == 0:
            matrix[0][i] = 0
    if col1 == 0:
        for i in range(m):
            matrix[i][0] = 0
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    m = int(input())
    matrix = []
    for i in range(m):
        cols = list(map(int, input().split()))
        matrix.append(cols)
    setZeroes(matrix=matrix)
    print('Matrix After Zeroes: ', matrix)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()