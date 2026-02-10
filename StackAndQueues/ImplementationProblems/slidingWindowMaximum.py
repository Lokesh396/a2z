import sys
import os
from pathlib import Path
from collections import deque
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    queue = deque()
    output = []

    l, r = 0, 0

    while r < len(nums):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        
        queue.append(r)

        if l > queue[0]:
            queue.popleft()
        
        if (r+1) >= k:
            output.append(nums[queue[0]])
            l += 1
        
        r += 1

    return output

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('max Sliding Window:', maxSlidingWindow(arr, 3))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()