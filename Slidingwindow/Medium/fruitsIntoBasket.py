import sys
import os
from pathlib import Path
from typing import List
from collections import defaultdict

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def totalFruit(fruits: List[int]) -> int:
    distinct = defaultdict(int)

    r = 0
    l = 0
    gmax = 0
    while r < len(fruits):
        distinct[fruits[r]] += 1
        while len(distinct) > 2 and  l < r:
            distinct[fruits[l]] -= 1
            if distinct[fruits[l]] == 0:
                del distinct[fruits[l]]
            
            l += 1
        
        gmax = max(gmax, r-l+1)
        r += 1
    return gmax

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('total Fruit:', totalFruit(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()