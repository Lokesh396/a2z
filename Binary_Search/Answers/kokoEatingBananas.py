import sys
import os
from pathlib import Path
from math import ceil
from typing import List

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def min_time( piles, mid):

    totalTime = 0
    for pile in piles:
        totalTime += ceil(pile/mid)
    return totalTime

def minEatingSpeed( piles: List[int], h: int) -> int:
    high = max(piles)
    low = 1

    while low <= high:

        mid = (low + high) // 2
        totalTime = min_time(piles, mid)
        if totalTime <= h:
            high = mid - 1
        else:
            low = mid + 1
    
    return low


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    h = int(input())
    print('Minimum eating speed required is: ', minEatingSpeed(arr, h))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()