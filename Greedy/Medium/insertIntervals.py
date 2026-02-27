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

def lower_bound(intervals, newInterval):
        low = 0
        high = len(intervals)-1

        while low <= high:
            mid = (low+high)//2
            if intervals[mid][0] >= newInterval[0]:
                high = mid - 1
            else:
                low = mid+1
        return low
def insert( intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    idx = lower_bound(intervals, newInterval)

    intervals.insert(idx, newInterval)

    i = 1
    out = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], intervals[i][1])
        else:
            out.append(intervals[i])
        i += 1
    return out


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print('After Merging:', insert(list(map(list, zip(start,end))), [3,4]))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()