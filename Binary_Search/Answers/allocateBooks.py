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
def isPossible(arr, n, m, mid):
    csum  = arr[0]
    sc = 1
    for i in range(1,n):
        if csum + arr[i] <= mid:
            csum += arr[i]
        else:
            sc += 1
            csum = arr[i]
    return sc

def findPages(arr: list[int], n: int, m: int) -> int:
    if n < m:
        return -1
    # Write your code here
    # Return the minimum number of pages
    low = max(arr)
    high = sum(arr)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        sc = isPossible(arr, n, m, mid)
        if sc > m:
            low = mid + 1
        else:
            high = mid - 1
    
    return low
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    s = int(input())
    print('max Pages',findPages(arr,len(arr), s))
    return 0
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()