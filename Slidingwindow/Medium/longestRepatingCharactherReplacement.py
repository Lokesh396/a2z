import sys
import os
from pathlib import Path
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def characterReplacement( s: str, k: int) -> int:
    distinct = defaultdict(int)

    r = 0
    l = 0
    gmax = 0
    while r < len(s):
        distinct[s[r]] += 1

        if max(distinct.values()) + k < (r-l+1) :
            distinct[s[l]] -= 1
            if distinct[s[l]] == 0:
                del distinct[s[l]]
            
            l += 1
        gmax = max(gmax, r-l+1)
        r += 1
    return gmax

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    k = int(input())
    print('longest repeating characther replacement:', characterReplacement(s,k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()