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


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()

    out = [intervals[0]]

    for i in range(1, len(intervals)):
        [start, end] = intervals[i]

        [prevs, preve] = out[-1]

        if start <= preve:
            if not end < preve:
                out[-1][1] = end
        else:
            out.append(intervals[i])

    
    return out

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    intervals = []
    for i in range(n):
        interval = list(map(int, input().split()))
        intervals.append(interval)
    print('Merged Intervals', merge(intervals=intervals))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()