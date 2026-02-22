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

def findContentChildren(g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        l = 0
        r = 0
        cnt = 0
        while l < len(s) and r < len(g):
            if s[l] >= g[r]:
                cnt += 1
                r += 1
            
            l += 1

        return cnt
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = list(map(int, input().split()))
    g = list(map(int, input().split()))
    print("Maximum Content children:", findContentChildren(g, s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()