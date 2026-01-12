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

def largest (nums):
    """
    Given an array return the length of largest subarray with zero sum.

    Algorithm:
    - we take the prefix sum as zero, we add every element at each index and check whether that sum is 0,
    that means we encountered a zero sum, we will try to assign that to the max sum.
    - if we encountered the current psum in our hashmap that means, after that elements we encountered a
    sub array whose sum is 0.
    - we will add current psum to the hashmap if it is not already present.

    Args:
        nums: input array
    
    Returns: returns the length of the largest subarray with zero sum.

    Time Complexity: O(n)

    Space Complexity: O(n)
    """
    psum = 0
    pmap = dict()
    max_length = 0
    for idx, num in enumerate(nums):
        psum += num
        if psum == 0:
            max_length = max(max_length, idx+1)
        
        if psum in pmap:
            max_length = max(max_length, idx - pmap[psum])
        
        if psum not in pmap:
            pmap[psum] = idx
    
    return max_length
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Largest subarray with zero sum length:', largest(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()