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
def longestOnes(nums: List[int], k: int) -> int:
        

    l, r = 0, 0
    gmax = 0
    while r < len(nums):
        if nums[r] == 0:
            k -= 1
        while l <= r and k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        gmax = max(gmax, r-l+1)
        r += 1
    return gmax

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print('longestOnes:', longestOnes(arr, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()