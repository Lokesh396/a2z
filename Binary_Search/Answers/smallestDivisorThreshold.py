import sys
import os
from pathlib import Path
from math import ceil
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def divisorSum(nums,mid):
    total = 0
    
    for num in nums:
        total += ceil(num / mid)
    return total

def smallestDivisor(nums: List[int], threshold: int) -> int:
    

    low = 1
    high = max(nums)
    ans = -1
    while low <= high:

        mid = (low + high) // 2

        total = divisorSum(nums, mid)

        if total <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    threshold = int(input())
    print('Smallest divisor:', smallestDivisor(arr, threshold))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()