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
def sortColors(nums):
    """
    Given an array which contains only 0, 1 and 2 elements we need to sort them.

    Algorithm:
    - The algorithm is widely called as `Dutch National flag Algorithm`.
    - the intution here is we divide the array  into four parts, 0 to low-1, 
    low to mid-1, mid+1 to high and high+1 to last
        - from 0 to low-1 we will have zeroes
        - from low to mid-1 we have ones
        - from mid+1 to high we have unsorted elements
        - from high+1 to last we have two.
    - if we encounter a zero at mid, we will swap with low and increment both low and mid
    - if we encounter a one at mid, we wil simply increment the mid
    - if we encoutner a two at mid, we swap with high and decrement the high.

    Returns: Array will be sorted inplace.

    Time Complexity: O(n) single traversal of the entire array.

    Space Complexity: O(1) no extra space is requried.

    """
    low, mid, high = 0, 0, len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

        
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    sortColors(arr)
    print("After Sorting Colors: ", arr)
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()