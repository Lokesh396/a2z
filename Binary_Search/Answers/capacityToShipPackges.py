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

def ispossible(weights, cap, days):

    dc = 0
    lc = 0
    for weight in weights:
        lc += weight
        if lc >  cap:
            dc += 1
            lc = weight
    return dc+1 <= days

        

def shipWithinDays(weights: List[int], days: int) -> int:
    low  = max(weights)
    high = sum(weights)

    while low <= high:

        mid = (low + high)//2

        if ispossible(weights,mid, days):
            high = mid - 1
        else:
            low = mid + 1
    
    return low


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    h = int(input())
    print('least no. of days required is: ', shipWithinDays(arr, h))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()