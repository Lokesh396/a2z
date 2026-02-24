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

def maximumMeetings(start: List[int], end: List[int]) -> int:
    # write your code here
    meetings = zip(start, end)
    meetings = sorted(meetings, key = lambda x : x[1])

    last_completed = -1
    out = 0
    for start, end in meetings:
        if start > last_completed:
            out += 1
            last_completed = end
    
    return out

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print('Maximum Meetings possible', maximumMeetings(start, end))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()