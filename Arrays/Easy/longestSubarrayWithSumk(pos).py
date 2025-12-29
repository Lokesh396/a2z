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


def optimal(arr, k):
    n = len(arr)
    left, right = 0, 0
    maxLen = 0
    csum = arr[0]

    while right < n:

        while csum >k and left <= right:
            csum -= arr[left]
            left += 1
        
        if csum == k:
            maxLen = max(maxLen, right - left + 1)

        right += 1
        if right < n:
            csum += arr[right]

    
    return maxLen

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print('The length of the longest Subarray with sum K: ', optimal(arr=arr, k=k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()