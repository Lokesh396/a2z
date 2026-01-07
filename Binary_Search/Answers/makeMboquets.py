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
def isPossible(bloomDay, m, k, mid):

    count = 0
    bc = 0 
    for num in bloomDay:
        if mid >= num:
            count += 1
        else:
            count = 0
        
        if count == k:
            bc += 1
            count = 0
    if bc >= m:
        return True
    


def minDays( bloomDay: List[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1 
    
    high = max(bloomDay)
    low = min(bloomDay)
    ans = -1
    while low <= high:

        mid = (low + high) // 2
        possible = isPossible(bloomDay, m, k , mid)

        if possible:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    m = int(input()) # boquet count
    k = int(input()) # adjacent days

    print('Minimum Days required is: ', minDays(arr, m, k))
    return 0
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()