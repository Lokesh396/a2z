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
def isPossible(stalls,d,cows):
    cpc = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= d:
            cpc += 1
            last = stalls[i]
    
    if cpc >= cows:
        return True
    return False

def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    low = 1
    high = max(stalls)-min(stalls)

    while low <= high:

        mid = (low + high)//2
        if isPossible(stalls,mid, k):
            low = mid + 1
        else:
            high = mid - 1
    
    return high
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    cows = int(input())
    print('max distance between cows:',aggressiveCows(arr, cows))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()