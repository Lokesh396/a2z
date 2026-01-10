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
def isPossible( nums, mid):
    csum = nums[0]
    splits = 1
    max_s = nums[0]
    for i in range(1, len(nums)):
        if csum + nums[i] <= mid:
            csum += nums[i]
        else:
            max_s = max(max_s, csum)
            splits += 1
            csum = nums[i]
    return [splits, max(max_s, csum)]

def paintersPartition(nums: List[int], k: int) -> int:

    low = max(nums)
    high = sum(nums)
    gmax = 0
    while low <= high:

        mid = (low + high) // 2

        [splits, maxs] = isPossible(nums, mid)
        if splits > k:
            low = mid + 1
        else:
            gmax = maxs
            high = mid - 1
    return gmax
       
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    s = int(input())
    print('max Split Array',paintersPartition(arr, s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()