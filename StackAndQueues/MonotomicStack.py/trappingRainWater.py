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

def trap( height: List[int]) -> int:
        nextGreater  = [-1 for i in range(len(height))]
        prevGreater = [-1 for i in range(len(height))]
        n = len(height)
        nextGreater[-1] = height[-1]
        prevGreater[0] = height[0]
        for i in range(n-2, -1, -1):
           nextGreater[i] = max(nextGreater[i+1],height[i])
        for i in range(1,n):
           prevGreater[i] = max(prevGreater[i-1],height[i])
        
        units = 0
        for i in range(n):
            min_ = min(prevGreater[i], nextGreater[i])
            if min_ != -1:
                units += (min_ - height[i])
        
        return units

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Total water trapped:', trap(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()