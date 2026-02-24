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

def jump(nums: List[int]) -> int:
        jumps = [float('inf') for _ in range(len(nums))]
        jumps[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, i+nums[i]+1):
                if j < len(nums):
                    jumps[j] = min(jumps[j], jumps[i]+1)
        
        return jumps[-1]

def jumpV2(nums: List[int]) -> int:
        
        jumps = 0
        current_jump = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == current_jump:
                jumps += 1
                current_jump = farthest
        
        return jumps

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    jumps = list(map(int, input().split()))
    print('minimum Jumps:', jump(jumps))
    print('minimum Jumps:', jumpV2(jumps))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()