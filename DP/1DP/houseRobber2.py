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

def rob(nums: List[int]) -> int:
    def func(nums):
        n = len(nums)
        if n <= 2:
            return max(nums)
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            temp = curr
            curr = max(nums[i] + prev, curr)
            prev = temp
        return curr
    if len(nums) <= 2:
        return max(nums)
    return max(func(nums[1:]), func(nums[:-1]))
    
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()