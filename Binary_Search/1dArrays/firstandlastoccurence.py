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
def first(arr, n,k):
    low = 0
    high = n -1
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            high = mid -1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return ans

def last(arr, n,k):
    low = 0
    high = n -1
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            low = mid +1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return ans
def occurence(arr: List[int], n: int, x: int) -> int:
    # Your code goes here
    fst = first(arr, n, x)
    if fst == -1: return [-1, -1]
    lst = last(arr, n, x)
    return [fst, lst]
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    target = int(input())
    print('first and last occurence are:', occurence(arr, len(arr), target))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()