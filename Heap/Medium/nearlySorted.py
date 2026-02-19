import sys
import os
from pathlib import Path
import heapq

# Fast I/O and Recursion Setup
sys.setrecursionlimit(2000)
input = sys.stdin.readline

USE_FILE = True

if USE_FILE:
    BASE_DIR = Path(__file__).resolve().parents[2]
    sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")
    sys.stdout = open(os.path.join(BASE_DIR, "output.txt"), "w")

def nearlySorted(arr, k):
    # Write your code here
    n = len(arr)
    heap = []
    for i in range(k+1):
        heapq.heappush(heap, arr[i])
    sarray = []
    for i in range(k+1,n):
        sarray.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        sarray.append(heapq.heappop(heap))
    
    return sarray

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    arr = list(map(int, input().split()))
    k = int(input())
    print('After sorting:', nearlySorted(arr, k))
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()