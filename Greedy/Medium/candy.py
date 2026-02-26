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


def candy(ratings: List[int]) -> int:
    

    peak = 1
    total = 1
    left = 1
    n = len(ratings)-1
    prev = 1
    while left <= n:

        while left <= n and ratings[left-1] < ratings[left]:
            total += prev + 1
            prev = prev +1
            peak = prev
            left += 1
        prev = 1
        while left <= n and ratings[left-1] > ratings[left]:
            total += prev
            prev = prev +1
            left += 1
            if prev > peak:
                total += 1
        while left <= n and ratings[left-1] == ratings[left]:
            
            total += 1
            left += 1
        peak = 1
        prev = 1
    return total

def candyOptimal(ratings: List[int]) -> int:
    left = [1 for i in range(len(ratings))]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1
    curr = 1
    total = left[-1]
    right = 1
    for i in range(len(ratings)-2, -1,-1):
        if ratings[i] > ratings[i+1]:
            curr = right + 1
        else:
            curr = 1
    
        right = curr
        
        total += max(left[i], curr)
    
    return total

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('candy:', candyOptimal(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()