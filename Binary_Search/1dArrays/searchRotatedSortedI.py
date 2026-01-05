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
def search(nums: List[int], target: int) -> int:
        
    low, high = 0, len(nums)-1

    while low <= high:

        mid = (low+high) // 2

        if nums[mid] == target:
            return mid
        
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    arr = list(map(int, input().split()))
    target = int(input())
    print('Element is at:', search(arr, target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()