

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
def heapify(arr):
    n = len(arr)

    def sift_down(i):
        smallest = i 

        while True:
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] < arr[smallest]:
                smallest = l
            
            if r < n and arr[r] < arr[smallest]:
                smallest = r
            
            if smallest == i:
                break

            arr[smallest], arr[i] = arr[i], arr[smallest]
            i = smallest
        
    for i in range(n//2-1, -1, -1):
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] < arr[i]:
            print(i, l, "left")
            return False
        
        if r < n and arr[r] < arr[i]:
            print(i, r, "right")
            return False
    return True
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Arr satisfies min heap property:', heapify(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()