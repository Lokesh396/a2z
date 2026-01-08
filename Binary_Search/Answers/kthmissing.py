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

def findKthPositive(arr: List[int], k: int) -> int:
    low = 0
    high = len(arr) -1

    while low <= high:

        mid = (low+high) // 2
        
        missing = arr[mid] - (mid+1)

        if missing <= k:
            low = mid + 1
        else:
            high = mid -1
    return low + k


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    h = int(input())
    print('Kth missing positive is: ', findKthPositive(arr, h))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()