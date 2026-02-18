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

        while True:
            largest = i
            l = 2 * i +1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            
            if largest == i:
                break

            arr[largest], arr[i] = arr[i], arr[largest]
            i = largest
    
    for i in range(n//2-1, -1, -1):
        sift_down(i)
    
    return arr
def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    print('Min heap to Max Heap:', heapify(arr))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()