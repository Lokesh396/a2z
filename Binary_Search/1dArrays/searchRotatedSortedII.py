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

def search(arr: List[int], target: int) -> bool:
    """
    Given an array which sorted and it is rotated by some places, we need to return whehter a given 
    target is present or not in the array the array may contains duplicates.

    Algorithm:
    - we will a normal binary search, but in order to eliminate the search, we will check which 
    half is sorted, based on that we will decide the search space that need to be elimiated.
    - we will just check all the low, mid and high are same and adjust the indexes.

    Args:
        nums: rotated sorted array
        target: target element.

    returns: returns index if elements present else -1
    
    Time Complexity: O(lgn)

    Space Complexity: O(1)
    """
    low, high = 0, len(arr)-1
    ans = 0
    while low <= high:

        mid = (low + high) // 2
        if arr[mid] == target: ans = True
        if(arr[low] == arr[mid] and arr[mid] == arr[high]):
            low += 1
            high -= 1
            continue
        
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return True if ans else False

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print("is Element present:", search(arr,target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()