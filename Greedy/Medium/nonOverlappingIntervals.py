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

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
        print(intervals)
        if not intervals:
            return 0
        intervals.sort()
        out = intervals[0][1]
        merged = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < out:
                out = min(out, intervals[i][1])
                merged += 1
            else:
                out = intervals[i][1]
        return merged

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print('Minimum erasing intervals:', eraseOverlapIntervals(list(map(list, zip(start,end)))))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()