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


def maxProduct(arr):
    prefix = 1
    suffix = 1
    maxi, n = -float('inf'), len(arr)
    for i in range(n):
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1
        prefix *= arr[i]
        suffix *= arr[n-i-1]
        maxi = max(maxi, max(prefix, suffix))
    
    return maxi

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Max Product:', maxProduct(arr=arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()