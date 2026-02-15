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
def kDistinctChars(k, s:str):
    # Write your code here
    # Return an integer value
    max_l = 0
    l = 0
    charmap = defaultdict(int)
    for r in range(len(s)):
        charmap[s[r]] += 1

        while len(charmap) > k:
            charmap[s[l]] -= 1
            if charmap[s[l]] == 0:
                del charmap[s[l]]
            l+= 1
        
        if len(charmap) <= k:
            max_l = max(max_l, r-l+1)
    
    return max_l




def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    k = int(input())
    print(" Longest substring with k different chars:",kDistinctChars(k, s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()