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

def singleNonDuplicate(nums: List[int]) -> int:
    """

    Given an array of nums where every element repeat twice except one,
    return the element which dont repeat twice.

    Algorithm:
    - if we are at a even index, we need to check whether the next element is same or not, if all
    the elements prior is pairs that means our single element is to the right else to the left.

    Args:
        nums: input array
    
    Returns: returns the element that appears only once.

    Time Complexity: O(lgn)

    Space Complexity: O(1)

    """
    n = len(nums)

    if n == 1:
        return nums[0]
    
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]
    
    low, high = 1, n-2

    while low <= high:

        mid = (low + high) // 2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        if (mid & 1 and nums[mid] == nums[mid-1]) or (mid & 1 == 0 and nums[mid] == nums[mid+1]):
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('single elemnt is:', singleNonDuplicate(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()