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

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0

    for i , h in enumerate(heights+[0]):
        
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1

            max_area = max(max_area, int(width) * int(height))
        
        stack.append(i)
    
    return max_area
def maximalRectangle(matrix: List[List[str]]) -> int:
    max_area = 0

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):
            if matrix[i][j] != '0' and i != 0:
                matrix[i][j] = int(matrix[i][j]) + int(matrix[i-1][j])
            matrix[i][j] = int(matrix[i][j])

        area = largestRectangleArea(matrix[i])
        max_area = max(max_area, area)

    return max_area

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    print('maximal rectangle area:', maximalRectangle(matrix=matrix))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()