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

def rotated(arr):
    low, high = 0, len(arr)-1
    ans = float('inf')
    idx = -1
    while low <= high:

        mid = (low + high) // 2
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[mid] <= arr[high]:
            if ans > arr[mid]:
                ans = arr[mid]
                idx = mid
            high = mid - 1
        else:
            if ans > arr[low]:
                ans = arr[low]
                idx = low
            low = mid + 1
    return idx

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('The array is rotated ', rotated(arr), 'times')
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()