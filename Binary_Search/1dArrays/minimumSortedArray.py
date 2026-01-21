import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def minimum(nums):
    """
    Given an rotated sorted array we need to return the minimum in the array.

    Algorithm:
    - if the array is rotated and sorted, if we divide the array in two parts before and 
    after mid definitely one part of the array is sorted, so based on that we can check
    in which direction we need to move.

    Args:
        nums: input array

    Returns: returns the minimum element in the array.

    Time Complexity: O(lgn)

    Space Complexity: O(1)
    """
    low, high, ans = 0, len(nums)-1, float('inf')

    while low <= high:

        mid = (low + high) // 2

        if nums[mid] <= nums[high]:
            ans = min(nums[mid], ans)
            high = mid - 1
        else:
            ans = min(nums[low], ans)
            low = mid + 1
    
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Minimum element is at:', minimum(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()