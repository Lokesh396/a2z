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

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    def f(idx, target):
        if target == 0:
            return 1
        
        if idx < 0:
            return 0
        
        nottake = f(idx-1, target)
        take = 0
        if target >= arr[idx]:
            take = f(idx-1, target-arr[idx])
        return take + nottake
    
    return f(n-1, k)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print(findWays(arr, k))

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()