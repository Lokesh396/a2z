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
def maxSubArray( nums):
    """
    
    Given an array, return the maximum subarray.

    Algorithm:
    - The algorithm is based on kadane's. we will add every element to our running sum, every time
    it becomes less than zero we turn it back to 0.
    - compare the running sum with the global maximum and store the indexes..

    Args:
        nums: Input array.

    Returns: returns the maximum subarray sum

    Time Complexity: O(n) linear traversal of the array.

    Space Complexity: O(1) no extra space is required.s

    """
    csum = 0
    arrStart , arrEnd = -1 , -1
    start = 0
    gmax = -float('inf')
    for i in range(len(nums)):

        csum += nums[i]

        if csum > gmax:
            gmax = csum
            arrStart = start
            arrEnd = i

        if csum < 0:
            csum = 0
            start = i + 1

    
    return [arrStart, arrEnd]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Maximum Subarray sum locates at : ',maxSubArray(arr) )
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()