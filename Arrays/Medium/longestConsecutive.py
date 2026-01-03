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
def longestConsecutive(nums):
    """
    Given an array of elements return the length of the maximum consecutive sequence.

    Algorithm:
    - we convert the list to set, every time we see a element will check whether it is the start of the
    sequence or the already part of the sequence.
    - we will return the maximum length of the sequence.

    Args:
        nums: Input array
    
    Returns: returns the length of max consecutive sequence.

    Time Complexity: O(n) at most two traversals.

    Space Complexity: O(n) we use set data structure.
    
    """
    if len(nums) == 0:
        return 0        
    nums = set(nums)
    max_l = 1
    for num in nums:
        
        if num-1 not in nums:
            count = 1
            temp = num
            while temp + 1 in nums:
                count += 1
                temp += 1
            
            max_l = max(max_l, count)
    
    return max_l

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().strip().split()))
    print('Max Sequence length: ',longestConsecutive(arr) )
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()