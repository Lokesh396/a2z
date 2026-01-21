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

def findPeakElement( nums: List[int]) -> int:
    """
    
    Given array nums, we need to find a peak element, peak element is an element
    where it is greater than both left and right neighbour. For the first and last
    element check only the valid neighbour.

    Algorithm:
    - we will start by looking at the middle, if that is the peak element we return it
    - we got two scenarios, if the array is rotated and sorted it will change at a 
    single point.
    - we will check whether the previous element is smaller to the current mid, if it is
    then we are in an increasing curve there is a high chance of having peak on the right.
    - we go the left and check.

    Args:
        nums: input array

    Returns: returns peak (peak definitely exists according to the problem statetment)

    Time Complexity: O(lgn)

    Space Complexity: O(1)
    """
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]: # as index 0 has no previous element we are simplyfying the logic
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1
    
    low, high = 1, n-2

    while low <= high:
        mid = (low + high) // 2

        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        if nums[mid-1] < nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Peak Element:', findPeakElement(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()