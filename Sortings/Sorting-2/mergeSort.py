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


def merge(p,q,r, arr):
    i = p
    j = q+ 1
    temp = []
    while i <= q and j <=r:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while i <= q:
        temp.append(arr[i])
        i += 1
    
    while j <= r:
        temp.append(arr[j])
        j += 1
    arr[p:r+1] = temp[::]


def mergeSort(p,r, arr):
    if p < r:
        q = (p+r) // 2
        print(p,q,r, arr[p:q+1], arr[q+1:r+1], 'divide')
        mergeSort(p,q, arr)
        mergeSort(q+1,r, arr)
        print(p,q,r, arr[p:q+1], arr[q+1:r+1], 'merge')
        merge(p, q,r, arr)

def main():
    # -------------------------
    # WRITE YOUR LOGIC BELOW
    # -------------------------
    n = int(input())
    arr = list(map(int, input().split()))
    p = 0
    r = n-1
    print(arr, 'unsorted')
    mergeSort(p,r, arr)
    print(arr, "sorted")
  
    return 0

if __name__ == "__main__":
    # Note: These prints will go to output.txt if USE_FILE is True
    main()