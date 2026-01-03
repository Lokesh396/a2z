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
def findMaxConsecutiveOnes(nums):
    """
    
    Given an input array nums return the maximum consecutive zero length.

    Algorithm:
    - we iterate through the array, evey time we encounter a non zero element we will
    increment the count by 1.
    - when we encounter a zero we will the maxlength and make the count as 0.
    - finally we the maximum of maxlenght and the count.

    Args:
        nums: Input array
    
    Returns:
        It return the max consecutive zero length.
    
    Time Complexity: O(n) Single traversal of the array

    Space Complexity: O(1) No extra space is required.
    
    """
    gmax = 0
    lmax = 0

    for num in nums:
        if num != 0:
            lmax += 1
        else:
            gmax = max(lmax, gmax)
            lmax = 0

    return max(gmax, lmax)
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Max Consecutive ones length: ', findMaxConsecutiveOnes(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()