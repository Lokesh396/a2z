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

def generate( nums, idx, curr, ans):
    if idx >= len(nums):
        ans.append(curr[::])
        return
    
    generate(nums, idx+1, curr, ans)
    curr.append(nums[idx])
    generate(nums, idx+1, curr, ans)
    curr.pop()
def subsets( nums: List[int]) -> List[List[int]]:
    ans = []
    generate(nums, 0, [], ans)
    return ans

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    nums = list(map(int, input().split()))
    print(f'All subsets for {nums}:',subsets(nums))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()