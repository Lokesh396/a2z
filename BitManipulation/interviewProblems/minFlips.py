import sys
import os
from pathlib import Path

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def minBitFlips( start: int, goal: int) -> int:
    cnt = 0
    while start or goal:
        lastbit = start & 1
        endlast = goal & 1
        if lastbit != endlast:
            cnt += 1
        
        start = start >> 1
        goal = goal >> 1
    
    return cnt

def minBitFlips1(start: int, goal: int) -> int:
        cnt = 0
        res = start ^ goal
        while res:
            res = res & (res-1)
            cnt += 1
        
        return cnt
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()