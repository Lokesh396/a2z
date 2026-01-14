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

def beautySum(s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            frequency = defaultdict(int)

            for j in range(i, n):
                frequency[s[j]] += 1
                maxf = max(frequency.values())
                minf = min(frequency.values())
                total += (maxf - minf)
        
        return total

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    s = input()
    print('Beauty Sum:', beautySum(s))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()