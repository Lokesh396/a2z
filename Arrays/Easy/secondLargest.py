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


def second_largest(arr):
    maximum = max(arr)
    smax = -10001

    for num in arr:
        if num != maximum:
            smax = max(smax, num)

    return smax


def optimal_second_largest(arr):
    largest = arr[0]
    slargest = -10001

    for i in range(1, len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] != largest and arr[i] > slargest:
            slargest = arr[i]
    
    return slargest


def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Second Largest Element: ',second_largest(arr=arr))
    print('Second Largest Element: ',optimal_second_largest(arr=arr))

    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()