import sys
import os
from pathlib import Path
from collections import defaultdict
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def atmostK( nums, k):
        seen = defaultdict(int)
        count, l = 0, 0
        for right in range(len(nums)):
            seen[nums[right]] += 1

            while len(seen) > k:
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l+= 1
            count += (right-l+1)
        return count


def subarraysWithKDistinct( nums: List[int], k: int) -> int:
    return atmostK(nums, k) - atmostK(nums, k-1)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()