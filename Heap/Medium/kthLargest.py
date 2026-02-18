import sys
import os
from pathlib import Path
from typing import List
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def findKthLargest( nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k - 1:
            heapq.heappop(nums)
            k -= 1
        return -heapq.heappop(nums)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k  = int(input())
    print(f'{k}th largest:', findKthLargest(arr, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()