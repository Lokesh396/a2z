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
def lengthOfLongestSubstring( s: str) -> int:
    l = 0
    r = 0
    gmax = 0
    lookup = dict()

    while r < len(s):

        if s[r] in lookup:
            l = max(l, lookup[s[r]]+1)

        gmax = max(gmax, r-l+1)
        lookup[s[r]] = r
        r += 1
    return gmax
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('length of longest Substring:', lengthOfLongestSubstring(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()