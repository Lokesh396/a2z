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


def selection_sort(n, arr):
    """
        Selection sort works base on
        Select the minimum and keep at the start
        of the array by swaping.
    """
    for i in range(n-1):
        mIndex = i
        for j in range(i+1,n):
            if arr[mIndex] > arr[j]:
                mIndex = j
        arr[i], arr[mIndex] = arr[mIndex], arr[i]
        print(arr, f"step -{i+1}")
    return arr
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr, "unsorted")
    print(selection_sort(n, arr), "sorted")
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()