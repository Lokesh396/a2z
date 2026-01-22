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
    """
    given array of nums and maximum sum possible in a subarray, return the max subarray sum
    and the subarrays count

    Algorithm:
    - Before adding current element to the sum we will check whethter the sum is less than the 
    allowed sum or not, once it increases the threshold we will increments the splits update
    the gmax and csum.

    Args:
        nums: input array 
        mid: the max allowed sum

    Returns: returns the splits and the maximum sum of the subarray

    Time Complexity: O(n)

    Space Complexity: O(1)

    """
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

def splitArray(nums: List[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the
    largest sum of any subarray is minimized.

    Algorithm:
    - the search is between the maximum element and the sum of the elements. 
    - for each mid we will check the splits if splits are greater we move to right else to left and update
    the maximum.

    Args:
        nums: input array
        k: no of splits allowed

    Returns: return the maximum split sum

    Time Complexity: O(n * lg(sum(nums)))

    Space Complexity: O(1)

    Pattern: Binary Search on answers

    Subpattern: is possible min(max)

    """
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
    print('max Split Array',splitArray(arr, s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()