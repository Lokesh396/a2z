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
    
def atmost(nums, k):
    count = 0
    left = 0
    oddc = 0
    for right in range(len(nums)):
        oddc += nums[right] & 1

        while oddc > k and left <= right:
            if nums[left] & 1:
                oddc -= 1
            
            left += 1
        
        count += (right - left + 1)
    
    return count

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    return self.atmost(nums, k) - self.atmost(nums, k -1)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()